#!/usr/bin/env python3
"""
PANDORA — SOVEREIGN GEX ENGINE (L1b)
Self-contained Gamma Exposure calculator. Free options data. No paid API.

Methodology (SpotGamma formula, publicly documented + Pandora extensions):
  GEX per strike = Gamma × OI × 100 × Spot² × 0.01
  Net GEX = Σ(Call_GEX) − Σ(Put_GEX)
  HVL (Gamma Flip) = strike where cumulative Net GEX crosses zero

  Gamma computed via Black-Scholes-Merton when not provided by data source:
    d1 = [ln(S/K) + (r + σ²/2)T] / (σ√T)
    Γ  = φ(d1) / (S × σ × √T)    [φ = standard normal PDF]

Sign convention:
  Dealers LONG calls  → positive gamma → positive GEX (call side)
  Dealers SHORT puts  → negative gamma → negative GEX (put side)
  Above HVL → Positive gamma regime → price mean-reverts to HVL (low vol)
  Below HVL → Negative gamma regime → price trends, volatility amplified

Pandora improvements over commercial providers:
  1. Transparent formula — no black box, fully documented
  2. Forex proxy via currency ETFs (FXE/FXB/FXY/GLD) — providers are US-only
  3. Zero-DTE separation with weight vs full chain + directional lean
  4. Multi-expiry aggregation with configurable window
  5. STIS integration — feeds directly into pmib.py L1b coherence score
  6. Historical logging to quant/ for walk-forward validation
  7. Pine Script level output for TradingView — auto-generated
  8. Vanna/Charm directional estimate from VIX regime

Usage:
  python3 gex_engine.py                     # SPY (S&P 500)
  python3 gex_engine.py --symbol QQQ        # Nasdaq proxy
  python3 gex_engine.py --symbol GLD        # Gold / XAU proxy
  python3 gex_engine.py --symbol FXE        # EUR/USD proxy (currency ETF)
  python3 gex_engine.py --symbol FXY        # USD/JPY proxy (currency ETF)
  python3 gex_engine.py --days 7            # 0DTE + weekly window only
  python3 gex_engine.py --all               # Scan all default symbols
  python3 gex_engine.py --json              # Machine-readable output
  python3 gex_engine.py --save              # Log today's reading to quant/
  python3 gex_engine.py --pine              # Generate Pine Script levels file
"""

import sys
import json
import argparse
import math
import os
from datetime import date, datetime, timedelta

try:
    import yfinance as yf
    import numpy as np
    import pandas as pd
except ImportError as e:
    print(f"\n  ERROR: Missing dependency — {e}")
    print("  Install with: pip3 install yfinance pandas numpy\n")
    sys.exit(1)


# ── Symbol Registry ────────────────────────────────────────────────────────────

SYMBOLS = {
    # US Indices — direct options
    'SPY': {'label': 'S&P 500 (ETF)',   'category': 'index',  'forex_proxy': None},
    'QQQ': {'label': 'Nasdaq 100 (ETF)','category': 'index',  'forex_proxy': None},
    'IWM': {'label': 'Russell 2K (ETF)','category': 'index',  'forex_proxy': None},
    # Commodities
    'GLD': {'label': 'Gold / XAU',      'category': 'metal',  'forex_proxy': 'XAU/USD'},
    'SLV': {'label': 'Silver / XAG',    'category': 'metal',  'forex_proxy': 'XAG/USD'},
    'USO': {'label': 'Oil / WTI',       'category': 'energy', 'forex_proxy': 'WTI'},
    # Forex proxies via currency ETFs (Pandora advantage — providers lack this)
    'FXE': {'label': 'EUR/USD',         'category': 'forex',  'forex_proxy': 'EUR/USD'},
    'FXB': {'label': 'GBP/USD',         'category': 'forex',  'forex_proxy': 'GBP/USD'},
    'FXY': {'label': 'USD/JPY (inv.)',  'category': 'forex',  'forex_proxy': 'USD/JPY (inverse)'},
    'FXA': {'label': 'AUD/USD',         'category': 'forex',  'forex_proxy': 'AUD/USD'},
    'UUP': {'label': 'DXY / USD Index', 'category': 'forex',  'forex_proxy': 'DXY'},
    # Rates / credit context
    'TLT': {'label': '20Y Treasuries',  'category': 'rates',  'forex_proxy': None},
    'HYG': {'label': 'High Yield',      'category': 'credit', 'forex_proxy': None},
}

DEFAULT_SCAN = ['SPY', 'QQQ', 'GLD', 'FXE', 'FXY', 'UUP']

# Risk-free rate — approximate 3-month T-bill; update quarterly
RISK_FREE_RATE = 0.0525


# ── Black-Scholes Greeks ───────────────────────────────────────────────────────

def _norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_gamma(S: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Black-Scholes Gamma (identical for calls and puts).
    S = spot, K = strike, T = years to expiry, r = risk-free rate, sigma = IV
    """
    if T <= 0.0 or sigma <= 0.0 or S <= 0.0 or K <= 0.0:
        return 0.0
    try:
        d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
        return _norm_pdf(d1) / (S * sigma * math.sqrt(T))
    except (ValueError, ZeroDivisionError):
        return 0.0


def bs_delta(S: float, K: float, T: float, r: float, sigma: float,
             option_type: str = 'call') -> float:
    """Black-Scholes Delta."""
    if T <= 0.0 or sigma <= 0.0 or S <= 0.0 or K <= 0.0:
        return 0.0
    try:
        d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
        return _norm_cdf(d1) if option_type == 'call' else _norm_cdf(d1) - 1.0
    except (ValueError, ZeroDivisionError):
        return 0.0


# ── Data Fetching ──────────────────────────────────────────────────────────────

def fetch_spot(symbol: str) -> float:
    """Current spot price via yfinance."""
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period='2d', interval='1d')
        if not hist.empty:
            return float(hist['Close'].iloc[-1])
        return float(ticker.fast_info.last_price)
    except Exception:
        return 0.0


def fetch_vix() -> float:
    """Current VIX level."""
    try:
        hist = yf.Ticker('^VIX').history(period='2d', interval='1d')
        return float(hist['Close'].iloc[-1]) if not hist.empty else 0.0
    except Exception:
        return 0.0


def fetch_option_chain(symbol: str, days: int = 45) -> pd.DataFrame:
    """
    Fetch all option chains within the expiry window via yfinance.
    Returns combined DataFrame with per-contract rows.
    yfinance provides: strike, openInterest, impliedVolatility, volume
    Gamma is NOT provided — computed via Black-Scholes in compute_gex().
    """
    ticker = yf.Ticker(symbol)

    try:
        expiry_dates = ticker.options
    except Exception:
        return pd.DataFrame()

    if not expiry_dates:
        return pd.DataFrame()

    today = date.today()
    cutoff = today + timedelta(days=days)
    rows = []

    for expiry_str in expiry_dates:
        try:
            expiry_dt = date.fromisoformat(expiry_str)
        except ValueError:
            continue

        if expiry_dt > cutoff:
            continue

        dte = (expiry_dt - today).days
        T = max(dte / 365.0, 1.0 / 365.0)  # floor at 1-day to avoid divide-by-zero

        try:
            chain = ticker.option_chain(expiry_str)
        except Exception:
            continue

        for opt_type, df in (('call', chain.calls), ('put', chain.puts)):
            for _, row in df.iterrows():
                strike = float(row.get('strike', 0) or 0)
                if strike <= 0:
                    continue
                raw_oi  = row.get('openInterest', 0)
                raw_iv  = row.get('impliedVolatility', 0)
                raw_vol = row.get('volume', 0)
                # Guard against NaN values from yfinance
                oi  = int(raw_oi)  if (raw_oi  is not None and raw_oi  == raw_oi)  else 0
                iv  = float(raw_iv)  if (raw_iv  is not None and raw_iv  == raw_iv)  else 0.0
                vol = int(raw_vol) if (raw_vol is not None and raw_vol == raw_vol) else 0
                rows.append({
                    'strike':      strike,
                    'expiry':      expiry_str,
                    'dte':         dte,
                    'option_type': opt_type,
                    'oi':          oi,
                    'volume':      vol,
                    'iv':          iv,
                    'T':           T,
                })

    return pd.DataFrame(rows) if rows else pd.DataFrame()


# ── GEX Computation ────────────────────────────────────────────────────────────

def compute_gex(chain_df: pd.DataFrame, spot: float) -> pd.DataFrame:
    """
    Compute Net GEX per strike across all expiries.

    Formula:
      GEX  = Gamma × OI × 100 × Spot² × 0.01
      Sign: calls = +1 (dealers long calls = long gamma)
            puts  = -1 (dealers short puts = short gamma)
      Net GEX per strike = sum(call_GEX) + sum(put_GEX)
      Cumulative GEX = running sum from lowest to highest strike
      HVL = strike where cumulative GEX crosses zero
    """
    if chain_df.empty or spot <= 0:
        return pd.DataFrame()

    chain = chain_df.copy()

    # Compute Black-Scholes gamma for every contract
    chain['gamma'] = [
        bs_gamma(spot, row.strike, row.T, RISK_FREE_RATE, row.iv)
        for row in chain.itertuples(index=False)
    ]

    # GEX with sign
    sign = chain['option_type'].map({'call': 1.0, 'put': -1.0})
    chain['gex'] = chain['gamma'] * chain['oi'] * 100.0 * (spot ** 2) * 0.01 * sign

    # Aggregate per strike — separate calls and puts
    calls = chain[chain['option_type'] == 'call'].groupby('strike').agg(
        call_gex=('gex', 'sum'),
        call_oi=('oi', 'sum'),
        call_vol=('volume', 'sum'),
    )
    puts = chain[chain['option_type'] == 'put'].groupby('strike').agg(
        put_gex=('gex', 'sum'),
        put_oi=('oi', 'sum'),
        put_vol=('volume', 'sum'),
    )

    gex_df = calls.join(puts, how='outer').fillna(0.0).reset_index()
    gex_df['net_gex'] = gex_df['call_gex'] + gex_df['put_gex']
    gex_df = gex_df.sort_values('strike').reset_index(drop=True)
    gex_df['cum_gex'] = gex_df['net_gex'].cumsum()

    return gex_df


# ── Key Level Detection ────────────────────────────────────────────────────────

def detect_key_levels(gex_df: pd.DataFrame, spot: float) -> dict:
    """
    Extract all key GEX levels from the strike GEX table.

    HVL (Gamma Flip)       — cumulative GEX zero crossing
    Call Wall              — highest positive GEX strike above spot (ceiling)
    Put Wall               — largest negative GEX strike below spot (floor)
    Max Gamma              — highest absolute GEX strike (strongest magnet)
    Volatility Trigger     — nearest strike to spot (ATM reference)
    """
    if gex_df.empty:
        return {}

    strikes = gex_df['strike'].values
    cum_gex = gex_df['cum_gex'].values
    net_gex = gex_df['net_gex'].values

    # HVL — find zero crossing of cumulative GEX
    hvl = None
    hvl_note = ''
    for i in range(len(gex_df) - 1):
        if cum_gex[i] >= 0 > cum_gex[i + 1]:
            hvl = float(strikes[i + 1])
            hvl_note = 'cum GEX crosses negative'
            break
        elif cum_gex[i] < 0 <= cum_gex[i + 1]:
            hvl = float(strikes[i])
            hvl_note = 'cum GEX crosses positive'
            break

    if hvl is None:
        # No clean crossover — use strike with minimum absolute cumulative GEX
        min_idx = int(np.argmin(np.abs(cum_gex)))
        hvl = float(strikes[min_idx])
        hvl_note = 'approximate — no clean zero cross'

    gamma_regime = 'POSITIVE (mean-reverting)' if spot > hvl else 'NEGATIVE (trending)'

    # Call Wall — highest positive net GEX strike above spot
    above = gex_df[gex_df['strike'] >= spot]
    call_wall = None
    if not above.empty and above['net_gex'].max() > 0:
        call_wall = float(above.loc[above['net_gex'].idxmax(), 'strike'])

    # Put Wall — largest negative net GEX strike below spot
    below = gex_df[gex_df['strike'] <= spot]
    put_wall = None
    if not below.empty and below['net_gex'].min() < 0:
        put_wall = float(below.loc[below['net_gex'].idxmin(), 'strike'])

    # Max Gamma — strike with highest absolute GEX
    max_gex_idx = int(np.argmax(np.abs(net_gex)))
    max_gamma = float(strikes[max_gex_idx])

    # Volatility Trigger — nearest strike to spot
    vt_idx = int(np.argmin(np.abs(strikes - spot)))
    vt = float(strikes[vt_idx])

    # Net GEX near spot (±0.5%)
    near_mask = (gex_df['strike'] >= spot * 0.995) & (gex_df['strike'] <= spot * 1.005)
    net_gex_at_spot = float(gex_df.loc[near_mask, 'net_gex'].sum())

    return {
        'spot':             round(spot, 4),
        'hvl':              round(hvl, 4),
        'hvl_note':         hvl_note,
        'gamma_regime':     gamma_regime,
        'call_wall':        round(call_wall, 4) if call_wall is not None else None,
        'put_wall':         round(put_wall,  4) if put_wall  is not None else None,
        'max_gamma':        round(max_gamma, 4),
        'volatility_trigger': round(vt, 4),
        'total_net_gex':    round(float(gex_df['net_gex'].sum()), 0),
        'net_gex_at_spot':  round(net_gex_at_spot, 0),
    }


# ── Zero-DTE Analysis ──────────────────────────────────────────────────────────

def analyze_zero_dte(chain_df: pd.DataFrame, spot: float) -> dict:
    """
    Separate 0DTE analysis — Pandora improvement.
    Providers show full chain; we isolate same-day expiry weight and directional lean.
    Zero-DTE has grown to ~45% of SPX volume since 2022 — it warps gamma levels.
    """
    if chain_df.empty:
        return {'available': False}

    zdte = chain_df[chain_df['dte'] <= 1]
    if zdte.empty:
        return {'available': False, 'note': 'No 0DTE expiry today'}

    total_oi   = int(zdte['oi'].sum())
    total_vol  = int(zdte['volume'].sum())
    full_oi    = int(chain_df['oi'].sum())

    zero_dte_weight_pct = round(total_oi / full_oi * 100 if full_oi > 0 else 0.0, 1)

    # Highest OI strike (magnet)
    oi_by_strike = zdte.groupby('strike')['oi'].sum()
    magnet = float(oi_by_strike.idxmax()) if not oi_by_strike.empty else spot

    # Call vs put OI (directional lean)
    call_oi = int(zdte[zdte['option_type'] == 'call']['oi'].sum())
    put_oi  = int(zdte[zdte['option_type'] == 'put']['oi'].sum())
    pc_ratio = round(put_oi / call_oi, 2) if call_oi > 0 else 0.0

    if pc_ratio < 0.7:
        interp = 'CALL HEAVY — upward 0DTE pressure'
    elif pc_ratio > 1.3:
        interp = 'PUT HEAVY — downward 0DTE pressure'
    else:
        interp = 'BALANCED — no strong 0DTE directional lean'

    return {
        'available':             True,
        'total_oi':              total_oi,
        'total_volume':          total_vol,
        'zero_dte_weight_pct':   zero_dte_weight_pct,
        'magnet_strike':         round(magnet, 4),
        'call_oi':               call_oi,
        'put_oi':                put_oi,
        'put_call_ratio':        pc_ratio,
        'interpretation':        interp,
    }


# ── Vanna / Charm Estimation ───────────────────────────────────────────────────

def estimate_vanna_charm(chain_df: pd.DataFrame, spot: float, vix: float) -> dict:
    """
    Vanna and Charm directional bias estimates.

    Vanna: sensitivity of delta to IV changes.
      VIX falling → IV declining → long Vanna → delta drift UP → bullish
      VIX rising  → IV expanding → short Vanna → delta drift DOWN → bearish

    Charm: delta decay with time (strongest in final 2h, especially on 0DTE).
      Call heavy ATM → charm pulls delta toward 0 → spot supported (dealers buy)
      Put heavy ATM  → charm pulls delta toward 0 → spot pressured (dealers sell)

    Approximation — exact Greeks require full order book. These are regime signals.
    """
    if vix > 0:
        if vix >= 30:
            vanna_regime = 'EXTREME VIX — Vanna strong headwind (dealer selling)'
            vanna_bias = -2
        elif vix >= 25:
            vanna_regime = f'HIGH VIX ({vix:.1f}) — Vanna headwind (bearish drift)'
            vanna_bias = -1
        elif vix >= 20:
            vanna_regime = f'ELEVATED VIX ({vix:.1f}) — Vanna neutral to headwind'
            vanna_bias = 0
        elif vix <= 12:
            vanna_regime = f'LOW VIX ({vix:.1f}) — Vanna tailwind (IV crush bullish)'
            vanna_bias = 2
        elif vix <= 15:
            vanna_regime = f'LOW VIX ({vix:.1f}) — Vanna tailwind (mild bullish drift)'
            vanna_bias = 1
        else:
            vanna_regime = f'NORMAL VIX ({vix:.1f}) — Vanna neutral'
            vanna_bias = 0
    else:
        vanna_regime = 'VIX unavailable'
        vanna_bias = 0

    # Charm — ATM call/put OI imbalance
    if not chain_df.empty:
        atm = chain_df[
            (chain_df['strike'] >= spot * 0.985) &
            (chain_df['strike'] <= spot * 1.015)
        ]
        atm_call_oi = int(atm[atm['option_type'] == 'call']['oi'].sum())
        atm_put_oi  = int(atm[atm['option_type'] == 'put']['oi'].sum())
        charm_ratio = atm_call_oi / atm_put_oi if atm_put_oi > 0 else 1.0
        if charm_ratio > 1.3:
            charm_dir = 'CALL HEAVY ATM — afternoon charm supports spot'
        elif charm_ratio < 0.7:
            charm_dir = 'PUT HEAVY ATM — afternoon charm weighs on spot'
        else:
            charm_dir = 'BALANCED ATM — neutral charm effect'
    else:
        charm_dir = 'Insufficient ATM data'

    return {
        'vix':           round(vix, 1) if vix else None,
        'vanna_regime':  vanna_regime,
        'vanna_bias':    vanna_bias,
        'charm_direction': charm_dir,
    }


# ── Historical Logging ─────────────────────────────────────────────────────────

def save_gex_log(symbol: str, levels: dict, zero_dte: dict, vanna_charm: dict) -> str:
    """Save today's GEX reading to D.S.E/trading/quant/ for walk-forward validation."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    quant_dir = os.path.normpath(
        os.path.join(script_dir, '..', '..', 'D.S.E', 'trading', 'quant')
    )
    os.makedirs(quant_dir, exist_ok=True)

    today = date.today().isoformat()
    filename = os.path.join(quant_dir, f'{today}_gex-session-map_{symbol.lower()}.md')

    vc = vanna_charm
    zdoc = zero_dte

    content = f"""# GEX SESSION MAP — {symbol} — {today}
**D.S.E/trading/quant/ | Sovereign GEX Engine L1b**

## Key Levels
| Level | Strike |
|---|---|
| Spot | {levels.get('spot', 'N/A')} |
| HVL (Gamma Flip) | {levels.get('hvl', 'N/A')} |
| Call Wall | {levels.get('call_wall', 'N/A')} |
| Put Wall | {levels.get('put_wall', 'N/A')} |
| Max Gamma | {levels.get('max_gamma', 'N/A')} |
| Volatility Trigger (ATM) | {levels.get('volatility_trigger', 'N/A')} |
| Net GEX (total) | {levels.get('total_net_gex', 'N/A'):,} |

## Regime
**Gamma Regime:** {levels.get('gamma_regime', 'N/A')}
**HVL Note:** {levels.get('hvl_note', 'N/A')}
**VIX:** {vc.get('vix', 'N/A')}
**Vanna:** {vc.get('vanna_regime', 'N/A')}
**Charm:** {vc.get('charm_direction', 'N/A')}

## Zero-DTE
**Available:** {zdoc.get('available', False)}
**Chain Weight:** {zdoc.get('zero_dte_weight_pct', 'N/A')}%
**Magnet Strike:** {zdoc.get('magnet_strike', 'N/A')}
**P/C Ratio:** {zdoc.get('put_call_ratio', 'N/A')}
**Signal:** {zdoc.get('interpretation', 'N/A')}

---
*Saved by gex_engine.py | STIS L1b | {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    with open(filename, 'w') as f:
        f.write(content)

    return filename


# ── Pine Script Level Output ───────────────────────────────────────────────────

def generate_pine_levels(symbol: str, levels: dict) -> str:
    """
    Generate Pine Script v6 overlay with computed GEX levels as hlines.
    Paste into TradingView Pine Script editor — works on any chart.
    """
    spot    = levels.get('spot', 0)
    hvl     = levels.get('hvl', 0) or 0
    cw      = levels.get('call_wall', 0) or 0
    pw      = levels.get('put_wall', 0) or 0
    mg      = levels.get('max_gamma', 0) or 0
    vt      = levels.get('volatility_trigger', 0) or 0
    regime  = levels.get('gamma_regime', '')
    today   = date.today().isoformat()

    return f"""// PANDORA — GEX LEVELS — {symbol} — {today}
// Sovereign GEX Engine L1b | Auto-generated — paste into TradingView
// Gamma Regime: {regime}
// Spot at generation: {spot}

//@version=6
indicator("GEX Levels [{symbol}] {today}", overlay=true, max_lines_count=20)

// ── Computed GEX Key Levels ────────────────────────────────────────────────
var float hvl        = {hvl}     // High Volatility Level (Gamma Flip)
var float call_wall  = {cw}   // Call Wall (ceiling — dealers buy above)
var float put_wall   = {pw}    // Put Wall  (floor  — dealers sell below)
var float max_gamma  = {mg}  // Max Gamma (strongest price magnet)
var float vol_trigger = {vt}  // Volatility Trigger (ATM reference)

// ── Level Lines ────────────────────────────────────────────────────────────
hline(hvl,         "HVL — Gamma Flip",    color.new(color.yellow, 0), linewidth=2, linestyle=hline.style_dashed)
hline(call_wall,   "Call Wall",           color.new(color.green,  0), linewidth=2, linestyle=hline.style_solid)
hline(put_wall,    "Put Wall",            color.new(color.red,    0), linewidth=2, linestyle=hline.style_solid)
hline(max_gamma,   "Max Gamma",           color.new(color.purple, 0), linewidth=1, linestyle=hline.style_dotted)
hline(vol_trigger, "Vol Trigger (ATM)",   color.new(color.white,  30), linewidth=1, linestyle=hline.style_dotted)

// ── Gamma Regime Background ────────────────────────────────────────────────
positive_gamma = close > hvl
bgcolor(positive_gamma ? color.new(color.green, 94) : color.new(color.red, 94), title="Gamma Regime")

// ── Labels (right edge) ────────────────────────────────────────────────────
if barstate.islast
    label.new(bar_index + 2, hvl,         "HVL "  + str.tostring(hvl,  "#.##"), style=label.style_label_left, color=color.yellow, textcolor=color.black, size=size.small)
    label.new(bar_index + 2, call_wall,   "CW "   + str.tostring(call_wall,  "#.##"), style=label.style_label_left, color=color.green,  textcolor=color.white, size=size.small)
    label.new(bar_index + 2, put_wall,    "PW "   + str.tostring(put_wall,   "#.##"), style=label.style_label_left, color=color.red,    textcolor=color.white, size=size.small)
    label.new(bar_index + 2, max_gamma,   "MG "   + str.tostring(max_gamma,  "#.##"), style=label.style_label_left, color=color.purple, textcolor=color.white, size=size.small)
    label.new(bar_index + 2, vol_trigger, "VT "   + str.tostring(vol_trigger,"#.##"), style=label.style_label_left, color=color.gray,   textcolor=color.white, size=size.small)
"""


# ── Terminal Output ────────────────────────────────────────────────────────────

def _fmt_gex(n: float) -> str:
    if abs(n) >= 1e9:
        return f'{n / 1e9:+.2f}B'
    if abs(n) >= 1e6:
        return f'{n / 1e6:+.2f}M'
    if abs(n) >= 1e3:
        return f'{n / 1e3:+.1f}K'
    return f'{n:+.0f}'


def print_gex_report(symbol: str, levels: dict, zero_dte: dict, vanna_charm: dict):
    meta = SYMBOLS.get(symbol, {'label': symbol, 'forex_proxy': None})
    label = meta['label']
    fx_note = f" → {meta['forex_proxy']}" if meta['forex_proxy'] else ''
    spot = levels.get('spot', 0)
    hvl = levels.get('hvl')

    W = 68
    pad = ' ' * (W - 2)

    def row(text):
        return f'║  {text:<{W - 4}s}║'

    def divider():
        return '╠' + '═' * (W - 2) + '╣'

    print()
    print('╔' + '═' * (W - 2) + '╗')
    print(row(f'PANDORA — SOVEREIGN GEX ENGINE  L1b'))
    print(row(f'{symbol} — {label}{fx_note}'))
    print(row(f'{date.today().isoformat()}   Spot: {spot:.4f}'))
    print(divider())

    # Gamma Regime
    regime = levels.get('gamma_regime', 'N/A')
    flag = '▲ POSITIVE — mean-reverting (pin risk, low vol)' if 'POSITIVE' in regime \
        else '▼ NEGATIVE — trending (vol amplified, dealers chase)'
    total_gex = levels.get('total_net_gex', 0)
    print(row(f'GAMMA REGIME: {flag}'))
    print(row(f'Net GEX: {_fmt_gex(total_gex):>10s}   |   Net at Spot: {_fmt_gex(levels.get("net_gex_at_spot", 0)):>10s}'))
    print(divider())

    # Key Levels
    hvl_str = f'{hvl:.2f}' if hvl is not None else 'N/A'
    rel = '+gamma' if spot > (hvl or 0) else '-gamma'
    print(row('KEY LEVELS:'))
    print(row(f'  HVL (Gamma Flip): {hvl_str:>10s}   Spot {spot:.2f} is {"ABOVE" if rel=="+gamma" else "BELOW"} HVL ({rel})'))
    cw = levels.get('call_wall')
    pw = levels.get('put_wall')
    mg = levels.get('max_gamma')
    vt = levels.get('volatility_trigger')
    print(row(f'  Call Wall:        {str(cw) if cw else "N/A":>10s}   (ceiling — dealers buy above)'))
    print(row(f'  Put Wall:         {str(pw) if pw else "N/A":>10s}   (floor   — dealers sell below)'))
    print(row(f'  Max Gamma:        {str(mg) if mg else "N/A":>10s}   (strongest price magnet)'))
    print(row(f'  Vol Trigger:      {str(vt) if vt else "N/A":>10s}   (ATM reference)'))
    print(divider())

    # Vanna / Charm
    vc = vanna_charm
    print(row('GREEKS CONTEXT:'))
    print(row(f'  Vanna: {vc.get("vanna_regime", "N/A")[:56]}'))
    print(row(f'  Charm: {vc.get("charm_direction", "N/A")[:56]}'))
    print(divider())

    # Zero DTE
    print(row('ZERO-DTE:'))
    if zero_dte.get('available'):
        wt = zero_dte.get('zero_dte_weight_pct', 0)
        mag = zero_dte.get('magnet_strike', 0)
        pc = zero_dte.get('put_call_ratio', 0)
        interp = zero_dte.get('interpretation', '')
        print(row(f'  Weight: {wt:.1f}% of chain OI   |   Magnet: {mag:.4f}   P/C: {pc:.2f}'))
        print(row(f'  {interp[:58]}'))
    else:
        print(row(f'  {zero_dte.get("note", "No 0DTE data available today")}'))

    print('╚' + '═' * (W - 2) + '╝')
    print()


# ── PMIB Integration Hook ──────────────────────────────────────────────────────

def get_gex_brief(symbol: str = 'SPY', days: int = 45) -> dict:
    """
    Single-call function for pmib.py L1b integration.
    Returns structured dict for coherence scoring + brief display.
    Call signature matches pmib.py import pattern.
    """
    spot = fetch_spot(symbol)
    if spot <= 0:
        return {'available': False, 'error': f'Cannot fetch spot for {symbol}'}

    vix = fetch_vix()
    chain_df = fetch_option_chain(symbol, days=days)

    if chain_df.empty:
        return {'available': False, 'error': f'No options chain for {symbol}'}

    gex_df = compute_gex(chain_df, spot)
    if gex_df.empty:
        return {'available': False, 'error': 'GEX computation failed'}

    levels     = detect_key_levels(gex_df, spot)
    zero_dte   = analyze_zero_dte(chain_df, spot)
    vc         = estimate_vanna_charm(chain_df, spot, vix)

    gamma_signal = 1 if 'POSITIVE' in levels.get('gamma_regime', '') else -1
    vanna_signal = vc.get('vanna_bias', 0)

    return {
        'available':          True,
        'symbol':             symbol,
        'spot':               levels.get('spot'),
        'hvl':                levels.get('hvl'),
        'gamma_regime':       levels.get('gamma_regime'),
        'call_wall':          levels.get('call_wall'),
        'put_wall':           levels.get('put_wall'),
        'total_net_gex':      levels.get('total_net_gex'),
        'vix':                vc.get('vix'),
        'vanna_regime':       vc.get('vanna_regime'),
        'charm_direction':    vc.get('charm_direction'),
        'zero_dte_available': zero_dte.get('available'),
        'zero_dte_weight':    zero_dte.get('zero_dte_weight_pct'),
        'zero_dte_magnet':    zero_dte.get('magnet_strike'),
        'zero_dte_pc_ratio':  zero_dte.get('put_call_ratio'),
        'gamma_signal':       gamma_signal,
        'vanna_signal':       vanna_signal,
        '_levels':            levels,
        '_zero_dte':          zero_dte,
        '_vanna_charm':       vc,
    }


# ── Main ───────────────────────────────────────────────────────────────────────

def run_analysis(symbol: str, days: int = 45, save: bool = False,
                 pine: bool = False, json_out: bool = False) -> dict:
    """Full GEX analysis pipeline for one symbol."""
    if not json_out:
        print(f'  Fetching spot + options chain for {symbol}...')

    spot = fetch_spot(symbol)
    if spot <= 0:
        err = {'error': f'Cannot fetch spot price for {symbol}'}
        if not json_out:
            print(f'  ERROR: {err["error"]}')
        return err

    vix      = fetch_vix()
    chain_df = fetch_option_chain(symbol, days=days)

    if chain_df.empty:
        err = {'error': f'No options data for {symbol}. Symbol may not have listed options.'}
        if not json_out:
            print(f'  ERROR: {err["error"]}')
            print(f'  Tip: Forex ETFs (FXE, FXB, FXY) may have lower options liquidity.')
        return err

    gex_df   = compute_gex(chain_df, spot)
    if gex_df.empty:
        err = {'error': 'GEX computation returned empty result'}
        if not json_out:
            print(f'  ERROR: {err["error"]}')
        return err

    levels     = detect_key_levels(gex_df, spot)
    zero_dte   = analyze_zero_dte(chain_df, spot)
    vc         = estimate_vanna_charm(chain_df, spot, vix)

    result = {
        'symbol':            symbol,
        'date':              date.today().isoformat(),
        'levels':            levels,
        'zero_dte':          zero_dte,
        'vanna_charm':       vc,
        'strikes_analyzed':  len(gex_df),
        'expiries_included': int(chain_df['expiry'].nunique()),
    }

    if not json_out:
        print_gex_report(symbol, levels, zero_dte, vc)

    if save:
        log_path = save_gex_log(symbol, levels, zero_dte, vc)
        if not json_out:
            print(f'  Saved → {log_path}')
            print()

    if pine:
        pine_code = generate_pine_levels(symbol, levels)
        if json_out:
            result['pine_script'] = pine_code
        else:
            print('── Pine Script (paste into TradingView) ──────────────────────────')
            print(pine_code)
            print('──────────────────────────────────────────────────────────────────')
            print()

    return result


def main():
    parser = argparse.ArgumentParser(description='Pandora Sovereign GEX Engine')
    parser.add_argument('--symbol', default='SPY',
                        help='Symbol to analyze (default: SPY). '
                             'Forex proxies: FXE (EUR), FXB (GBP), FXY (JPY), UUP (DXY)')
    parser.add_argument('--days',   type=int, default=45,
                        help='Max DTE for option chain inclusion (default: 45)')
    parser.add_argument('--all',    action='store_true',
                        help=f'Scan default symbols: {DEFAULT_SCAN}')
    parser.add_argument('--save',   action='store_true',
                        help='Save GEX reading to D.S.E/trading/quant/')
    parser.add_argument('--pine',   action='store_true',
                        help='Output Pine Script levels snippet (single symbol only)')
    parser.add_argument('--json',   action='store_true',
                        help='Machine-readable JSON output')
    args = parser.parse_args()

    symbols = DEFAULT_SCAN if args.all else [args.symbol.upper()]
    results = []

    for sym in symbols:
        result = run_analysis(
            symbol=sym,
            days=args.days,
            save=args.save,
            pine=args.pine and len(symbols) == 1,
            json_out=args.json,
        )
        results.append(result)

    if args.json:
        out = results[0] if len(results) == 1 else results
        print(json.dumps(out, indent=2, default=str))


if __name__ == '__main__':
    main()

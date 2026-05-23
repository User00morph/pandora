#!/usr/bin/env python3
"""
PANDORA — IEC CYCLE SCANNER
STIS Layer 1: Mechanical — Institutional Expansion Cycle phase detection.

Nathan Banks' 5-phase IEC model:
  Phase 1: ACCUMULATION  — Range-bound, ATR contracting, Bollinger squeeze
  Phase 2: MANIPULATION  — False breakout / stop hunt opposite intended direction
  Phase 3: EXPANSION     — Real directional move, ADX rising, ATR expanding
  Phase 4: RETRACEMENT   — Pullback 38-62% of Phase 3 move, lower volatility
  Phase 5: REVERSAL      — Structure break opposing Phase 3, new cycle begins

Usage:
  python3 iec_scanner.py                    # Scan all 10 default instruments
  python3 iec_scanner.py --symbol EURUSD=X  # Deep scan single symbol
  python3 iec_scanner.py --timeframe 1wk    # Weekly timeframe
  python3 iec_scanner.py --json             # Machine-readable output
"""

import sys
import json
import argparse
from datetime import date

try:
    import yfinance as yf
    import numpy as np
    import pandas as pd
except ImportError as e:
    print(f"\n  ERROR: Missing dependency — {e}")
    print("  Install with: pip3 install yfinance pandas numpy\n")
    sys.exit(1)


INSTRUMENTS = {
    'EURUSD': 'EURUSD=X',
    'GBPUSD': 'GBPUSD=X',
    'USDJPY': 'JPY=X',
    'GOLD':   'GC=F',
    'OIL':    'CL=F',
    'SPX':    '^GSPC',
    'NDX':    '^NDX',
    'DXY':    'DX-Y.NYB',
    'BTCUSD': 'BTC-USD',
    'ETHUSD': 'ETH-USD',
}

TIMEFRAME_MAP = {
    '1d':  {'period': '6mo',  'interval': '1d'},
    '1wk': {'period': '2y',   'interval': '1wk'},
    '1h':  {'period': '60d',  'interval': '1h'},
    '4h':  {'period': '60d',  'interval': '4h'},
    '15m': {'period': '5d',   'interval': '15m'},
}


# ── Technical Indicators (no TA-Lib) ─────────────────────────────────────────

def calc_atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high, low, close = df['High'], df['Low'], df['Close']
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low  - prev_close).abs(),
    ], axis=1).max(axis=1)
    return tr.rolling(period).mean()


def calc_adx(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    high, low, close = df['High'], df['Low'], df['Close']
    prev_high = high.shift(1)
    prev_low  = low.shift(1)

    dm_plus  = (high - prev_high).clip(lower=0)
    dm_minus = (prev_low - low).clip(lower=0)
    # Where both are positive, keep only the larger
    both_pos = (dm_plus > 0) & (dm_minus > 0)
    dm_plus  = dm_plus.where(~both_pos | (dm_plus >= dm_minus), 0)
    dm_minus = dm_minus.where(~both_pos | (dm_minus > dm_plus), 0)

    atr = calc_atr(df, period)
    di_plus  = 100 * dm_plus.rolling(period).mean()  / atr.replace(0, np.nan)
    di_minus = 100 * dm_minus.rolling(period).mean() / atr.replace(0, np.nan)

    dx = 100 * (di_plus - di_minus).abs() / (di_plus + di_minus).replace(0, np.nan)
    adx = dx.rolling(period).mean()

    return pd.DataFrame({'adx': adx, 'di_plus': di_plus, 'di_minus': di_minus})


def calc_bollinger(df: pd.DataFrame, period: int = 20, std: float = 2.0) -> pd.DataFrame:
    mid   = df['Close'].rolling(period).mean()
    sigma = df['Close'].rolling(period).std()
    upper = mid + std * sigma
    lower = mid - std * sigma
    bw    = (upper - lower) / mid  # bandwidth — squeeze = low bandwidth
    return pd.DataFrame({'bb_upper': upper, 'bb_lower': lower, 'bb_mid': mid, 'bb_bw': bw})


def calc_fibonacci_levels(swing_high: float, swing_low: float) -> dict:
    rng = swing_high - swing_low
    return {
        'fib_236': swing_high - 0.236 * rng,
        'fib_382': swing_high - 0.382 * rng,
        'fib_500': swing_high - 0.500 * rng,
        'fib_618': swing_high - 0.618 * rng,
        'fib_786': swing_high - 0.786 * rng,
    }


# ── Phase Detection Heuristics ────────────────────────────────────────────────

def score_phases(df: pd.DataFrame) -> dict:
    """
    Returns a dict with confidence scores (0-100) for each IEC phase.
    Uses the last 3 candles as 'current state', rest as context.
    """
    if len(df) < 30:
        return {f'phase_{i}': 0 for i in range(1, 6)}

    adx_df = calc_adx(df)
    bb_df  = calc_bollinger(df)
    atr    = calc_atr(df)

    # Current values (last complete bar)
    cur_close  = df['Close'].iloc[-1]
    cur_adx    = adx_df['adx'].iloc[-1]
    cur_di_p   = adx_df['di_plus'].iloc[-1]
    cur_di_m   = adx_df['di_minus'].iloc[-1]
    cur_bw     = bb_df['bb_bw'].iloc[-1]
    cur_atr    = atr.iloc[-1]
    cur_bb_u   = bb_df['bb_upper'].iloc[-1]
    cur_bb_l   = bb_df['bb_lower'].iloc[-1]

    # Historical context (20-bar window)
    recent_atr = atr.iloc[-20:]
    recent_bw  = bb_df['bb_bw'].iloc[-20:]
    recent_adx = adx_df['adx'].iloc[-20:]

    atr_trend   = (cur_atr - recent_atr.iloc[0]) / recent_atr.iloc[0] if recent_atr.iloc[0] else 0
    bw_pctile   = (recent_bw < cur_bw).mean()    # 0=squeeze, 1=expansion
    adx_pctile  = (recent_adx < cur_adx).mean()

    # Swing high/low over 20 bars for Fibonacci
    swing_hi = df['High'].iloc[-20:].max()
    swing_lo = df['Low'].iloc[-20:].min()
    swing_range = swing_hi - swing_lo
    fibs = calc_fibonacci_levels(swing_hi, swing_lo) if swing_range > 0 else {}

    # Recent price vs structure
    prev_highs = df['High'].iloc[-10:-1]
    prev_lows  = df['Low'].iloc[-10:-1]
    above_range = cur_close > prev_highs.max() if len(prev_highs) else False
    below_range = cur_close < prev_lows.min()  if len(prev_lows)  else False
    inside_range = not above_range and not below_range

    # --- Phase 1: ACCUMULATION ---
    # Low ADX, ATR contracting or flat, BB squeeze, price inside range
    p1 = 0
    if cur_adx < 25:             p1 += 30
    if atr_trend < 0.05:         p1 += 20   # ATR not growing
    if bw_pctile < 0.30:         p1 += 25   # BB squeeze (low bandwidth pctile)
    if inside_range:             p1 += 25

    # --- Phase 2: MANIPULATION ---
    # Brief break outside range that reverses back inside within 1-2 bars
    # Look for wick beyond range with close back inside
    last_bar   = df.iloc[-1]
    prev_bar   = df.iloc[-2]
    wicked_up  = last_bar['High'] > prev_highs.max() and last_bar['Close'] < prev_highs.max()
    wicked_dn  = last_bar['Low']  < prev_lows.min()  and last_bar['Close'] > prev_lows.min()
    wick_trap  = wicked_up or wicked_dn
    p2 = 0
    if wick_trap:                p2 += 50
    if cur_adx < 30:             p2 += 20   # Still relatively low ADX during manipulation
    if inside_range:             p2 += 30   # Close back inside

    # --- Phase 3: EXPANSION ---
    # High ADX, ATR expanding, price breaking outside range with conviction
    p3 = 0
    if cur_adx > 25:             p3 += 25
    if cur_adx > 35:             p3 += 15
    if atr_trend > 0.05:         p3 += 20   # ATR growing
    if bw_pctile > 0.60:         p3 += 15   # BB expanding
    if above_range or below_range: p3 += 25

    # --- Phase 4: RETRACEMENT ---
    # Price pulling back into Phase 3 move, within fib zone, ATR contracting
    p4 = 0
    if fibs:
        in_fib_zone = fibs['fib_618'] <= cur_close <= fibs['fib_236']
        if in_fib_zone:          p4 += 40
    if atr_trend < 0:            p4 += 20   # ATR contracting after expansion
    if cur_adx < adx_pctile * 50: p4 += 20  # ADX retreating from peak
    if inside_range:             p4 += 20

    # --- Phase 5: REVERSAL ---
    # Strong move opposing previous trend, ADX high but DI flip
    di_flip = (cur_di_p > cur_di_m) != (adx_df['di_plus'].iloc[-5] > adx_df['di_minus'].iloc[-5])
    p5 = 0
    if di_flip:                  p5 += 40
    if cur_adx > 30 and di_flip: p5 += 20
    if above_range or below_range: p5 += 20
    if atr_trend > 0.10:         p5 += 20

    scores = {'phase_1': p1, 'phase_2': p2, 'phase_3': p3, 'phase_4': p4, 'phase_5': p5}

    # Determine direction for expansion phases
    direction = 'BULLISH' if cur_di_p > cur_di_m else 'BEARISH'

    return {
        'scores': scores,
        'direction': direction,
        'adx': round(cur_adx, 1) if not np.isnan(cur_adx) else 0,
        'atr_trend': round(atr_trend * 100, 1),
        'bb_bandwidth_pct': round(bw_pctile * 100, 0),
        'current_close': round(cur_close, 4),
    }


def classify_phase(scores: dict) -> tuple:
    """Returns (phase_number, confidence_score)."""
    best = max(scores.items(), key=lambda x: x[1])
    return int(best[0].split('_')[1]), best[1]


PHASE_LABELS = {
    1: 'ACCUMULATION',
    2: 'MANIPULATION',
    3: 'EXPANSION    ',
    4: 'RETRACEMENT  ',
    5: 'REVERSAL     ',
}

PHASE_ACTIONS = {
    1: 'WAIT — range-bound, no signal',
    2: 'CAUTION — potential trap, wait for close back inside',
    3: 'TRADE — follow momentum, enter on pullback to Phase 4',
    4: 'ENTRY ZONE — Phase 3 continuation setup',
    5: 'FLIP BIAS — new cycle beginning, reassess direction',
}


def fetch_data(ticker: str, timeframe: str = '1d'):
    tf = TIMEFRAME_MAP.get(timeframe, TIMEFRAME_MAP['1d'])
    try:
        data = yf.download(ticker, period=tf['period'], interval=tf['interval'],
                           progress=False, auto_adjust=True)
        if data.empty or len(data) < 30:
            return None
        # Flatten MultiIndex columns if present
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
        return data
    except Exception:
        return None


def scan_all(timeframe: str = '1d') -> list:
    results = []
    for name, ticker in INSTRUMENTS.items():
        df = fetch_data(ticker, timeframe)
        if df is None:
            results.append({'name': name, 'ticker': ticker, 'error': 'fetch_failed'})
            continue
        analysis = score_phases(df)
        phase, conf = classify_phase(analysis['scores'])
        results.append({
            'name':      name,
            'ticker':    ticker,
            'phase':     phase,
            'label':     PHASE_LABELS[phase],
            'confidence': conf,
            'direction': analysis['direction'],
            'adx':       analysis['adx'],
            'atr_trend': analysis['atr_trend'],
            'action':    PHASE_ACTIONS[phase],
            'close':     analysis['current_close'],
        })
    return results


def confidence_bar(score: int, width: int = 10) -> str:
    filled = int(min(score, 100) / 10)
    return '█' * filled + '░' * (width - filled)


def print_scan_report(results: list, timeframe: str):
    print()
    print('═' * 72)
    print('  PANDORA — IEC CYCLE SCANNER')
    print(f'  {date.today().isoformat()}   Timeframe: {timeframe}')
    print('═' * 72)
    print(f'  {"Symbol":8s}  {"Phase":14s}  {"Conf":6s}  {"Dir":8s}  {"ADX":5s}  Action')
    print(f'  {"─"*8}  {"─"*14}  {"─"*6}  {"─"*8}  {"─"*5}  {"─"*28}')

    for r in results:
        if 'error' in r:
            print(f'  {r["name"]:8s}  {"ERROR":14s}  {"N/A":6s}  {"N/A":8s}  {"N/A":5s}  {r["error"]}')
            continue

        phase = r['phase']
        phase_arrow = '▲' if r['direction'] == 'BULLISH' else '▼' if r['direction'] == 'BEARISH' else ' '
        phase_str   = f'Phase {phase} {phase_arrow} {PHASE_LABELS[phase].strip()}'
        conf_bar    = confidence_bar(r['confidence'])
        action_short = PHASE_ACTIONS[phase].split(' — ')[0]

        print(f'  {r["name"]:8s}  {phase_str:14s}  {conf_bar}  {r["direction"]:8s}  {r["adx"]:5.1f}  {action_short}')

    print()
    print('  LEGEND:')
    for p, label in PHASE_LABELS.items():
        print(f'    Phase {p} {label.strip():14s}  {PHASE_ACTIONS[p]}')
    print()
    print('═' * 72)


def print_deep_scan(name: str, ticker: str, df: pd.DataFrame, timeframe: str):
    analysis = score_phases(df)
    scores   = analysis['scores']
    phase, conf = classify_phase(scores)

    print()
    print('═' * 60)
    print(f'  DEEP SCAN: {name} ({ticker})')
    print(f'  {date.today().isoformat()}  |  Timeframe: {timeframe}  |  Close: {analysis["current_close"]}')
    print('═' * 60)
    print(f'  ADX: {analysis["adx"]}  |  ATR Trend: {analysis["atr_trend"]:+.1f}%  |  '
          f'BB BW Percentile: {analysis["bb_bandwidth_pct"]:.0f}%')
    print()
    print('  PHASE SCORES:')
    for p in range(1, 6):
        s = scores[f'phase_{p}']
        bar = confidence_bar(s)
        marker = ' ◄ CURRENT' if p == phase else ''
        print(f'    Phase {p} {PHASE_LABELS[p].strip():14s}  [{bar}] {s:3d}{marker}')

    print()
    print(f'  RESULT:  Phase {phase} — {PHASE_LABELS[phase].strip()}  (confidence: {conf})')
    print(f'  DIR:     {analysis["direction"]}')
    print(f'  ACTION:  {PHASE_ACTIONS[phase]}')
    print()
    print('═' * 60)


def main():
    parser = argparse.ArgumentParser(description='Pandora IEC Cycle Scanner')
    parser.add_argument('--symbol',    help='Single symbol deep scan (e.g. EURUSD=X)')
    parser.add_argument('--name',      default='', help='Display name for --symbol')
    parser.add_argument('--timeframe', default='1d',
                        choices=list(TIMEFRAME_MAP.keys()), help='Timeframe (default: 1d)')
    parser.add_argument('--json',      action='store_true', help='JSON output')
    args = parser.parse_args()

    if args.symbol:
        print(f'  Fetching {args.symbol}...')
        df = fetch_data(args.symbol, args.timeframe)
        if df is None:
            print(f'  ERROR: Could not fetch data for {args.symbol}')
            sys.exit(1)
        name = args.name or args.symbol
        if args.json:
            analysis = score_phases(df)
            phase, conf = classify_phase(analysis['scores'])
            print(json.dumps({
                'symbol': args.symbol, 'name': name,
                'phase': phase, 'label': PHASE_LABELS[phase].strip(),
                'confidence': conf, 'direction': analysis['direction'],
                'action': PHASE_ACTIONS[phase],
                'scores': analysis['scores'],
                'indicators': {k: v for k, v in analysis.items() if k != 'scores'},
            }, indent=2))
        else:
            print_deep_scan(name, args.symbol, df, args.timeframe)
    else:
        print(f'\n  Scanning {len(INSTRUMENTS)} instruments ({args.timeframe})...')
        results = scan_all(args.timeframe)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print_scan_report(results, args.timeframe)


if __name__ == '__main__':
    main()

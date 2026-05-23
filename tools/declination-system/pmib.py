#!/usr/bin/env python3
"""
PANDORA — PRE-MARKET INTELLIGENCE BRIEF (P.M.I.B)
Single-command daily briefing combining all STIS layers.

Layers integrated:
  L1a Mechanical IEC → IEC phase scanner (iec_scanner.py)
  L1b GEX / Options  → Sovereign GEX Engine (gex_engine.py) — gamma regime
  L2 Collective      → Schumann Proxy (NOAA SWPC Kp + Solar Wind)
  L3 Pattern         → Aspect Scanner (applying planetary aspects + triggers)
  L4 Esoteric/Astro  → Declination System (DS forecast + turning points)
  L5 Observer        → Coherence score (aggregated signal alignment)

Usage:
  python3 pmib.py                     # Today's brief, New York
  python3 pmib.py --location london   # London session
  python3 pmib.py --orb 1.5           # Tighter aspect filter
  python3 pmib.py --no-gex            # Skip GEX layer (faster, no options data)
  python3 pmib.py --gex-symbol QQQ    # Use QQQ instead of SPY for GEX
  python3 pmib.py --json              # Machine-readable output
"""

import ephem
import math
import json
import argparse
from datetime import date, datetime, timedelta, timezone

# Import from sibling modules
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from schumann_resonance import get_current_kp, get_solar_wind, interpret_kp, interpret_wind
from declination_system  import get_declinations, compute_ds, generate_series, find_turning_points
from aspect_scanner      import find_aspects, build_trigger_schedule, LOCATIONS, find_t_squares

# L1b — Sovereign GEX Engine (optional — requires yfinance + options data)
_GEX_ENGINE_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', 'gex-engine')
)
sys.path.insert(0, _GEX_ENGINE_PATH)
try:
    from gex_engine import get_gex_brief
    _GEX_AVAILABLE = True
except ImportError:
    _GEX_AVAILABLE = False


RAD_TO_DEG = 180.0 / math.pi


def get_ds_brief(today: date) -> dict:
    """Current DS reading and next turning point."""
    start = today
    end   = today + timedelta(days=90)

    series = generate_series(start, end, step_days=1)
    turns  = find_turning_points(series, window=7)

    today_ds = series[0]['ds']
    # 90-day min/max for percentile
    vals = [p['ds'] for p in series]
    ds_min, ds_max = min(vals), max(vals)
    ds_range = ds_max - ds_min
    pct = (today_ds - ds_min) / ds_range * 100 if ds_range else 50

    today_str = today.isoformat()
    upcoming = [t for t in turns if t['date'] >= today_str][:2]

    if pct >= 70:
        bias = 'TOP ZONE — Bearish bias'
    elif pct <= 30:
        bias = 'BOTTOM ZONE — Bullish bias'
    else:
        bias = 'NEUTRAL ZONE — No strong bias'

    return {
        'ds': today_ds,
        'pct_of_range': round(pct, 1),
        'bias': bias,
        'upcoming_turns': upcoming,
        'ds_min': ds_min,
        'ds_max': ds_max,
    }


def get_aspect_brief(today: date, location: str, orb: float) -> dict:
    """Key aspects and trigger schedule for today."""
    loc = LOCATIONS[location]
    obs = ephem.Observer()
    obs.lat       = loc['lat']
    obs.lon       = loc['lon']
    obs.elevation = 10
    obs.date      = ephem.Date(f"{today.isoformat().replace('-', '/')} 13:30:00")

    aspects  = find_aspects(obs, orb=orb)
    triggers = build_trigger_schedule(aspects, obs, loc['tz_offset'], loc['label'])
    t_squares = find_t_squares(aspects)

    applying = [a for a in aspects if a['applying']]
    top_aspects = sorted(applying, key=lambda x: x['orb'])[:3]

    # High-quality triggers (applying + orb < 1°)
    hot_triggers = [t for t in triggers if t['applying'] and t['orb'] < 1.0]

    return {
        'applying_count': len(applying),
        'top_aspects': top_aspects,
        'hot_triggers': hot_triggers,
        'all_triggers': triggers,
        't_squares': t_squares,
        'location_label': loc['label'],
    }


def compute_coherence(kp, ds_pct: float, applying_count: int,
                      hot_trigger_count: int, t_square_count: int,
                      gamma_signal: int = 0, vanna_signal: int = 0) -> dict:
    """
    L5 Observer coherence score — how well do all layers align?
    gamma_signal: +1 = positive gamma (supportive), -1 = negative gamma (amplifying)
    vanna_signal: +2/+1/0/-1/-2 from VIX regime
    Returns score 0–100 and interpretation.
    """
    score = 50  # baseline

    # Kp contribution (lower = better for trading)
    if kp is not None:
        if kp <= 1:
            score += 15
        elif kp <= 2:
            score += 10
        elif kp <= 3:
            score += 0
        elif kp <= 5:
            score -= 10
        else:
            score -= 25

    # DS extreme zones add signal clarity
    if ds_pct >= 75 or ds_pct <= 25:
        score += 10
    elif ds_pct >= 60 or ds_pct <= 40:
        score += 5

    # Applying aspects add signal energy
    score += min(applying_count * 5, 20)

    # Hot triggers (tight applying) are high-value setups
    score += hot_trigger_count * 8

    # T-squares are highest probability
    score += t_square_count * 10

    # L1b GEX — gamma and Vanna alignment
    # Positive gamma = controlled environment (score bonus — cleaner setups)
    # Negative gamma = trending volatile (neutral — opportunities exist but wider stops)
    if gamma_signal == 1:
        score += 5
    # Vanna tailwind confirms directional bias; headwind reduces conviction
    score += max(-10, min(10, vanna_signal * 5))

    score = max(0, min(100, score))

    if score >= 80:
        grade = 'A — PRIME DAY'
        note  = 'All layers aligned. Prioritize high-confidence entries.'
    elif score >= 65:
        grade = 'B — SOLID DAY'
        note  = 'Good signal environment. Execute standard plan.'
    elif score >= 45:
        grade = 'C — AVERAGE DAY'
        note  = 'Moderate signals. Be selective. Wait for Grade A setups.'
    else:
        grade = 'D — QUIET/NOISY DAY'
        note  = 'Weak alignment. Reduce size or stay patient. No forcing.'

    return {'score': score, 'grade': grade, 'note': note}


def print_gex_section(gex: dict):
    """Print L1b GEX layer section for the P.M.I.B."""
    W = 66

    def row(text):
        return f'║  {text:<{W - 4}s}║'

    if not gex.get('available'):
        err = gex.get('error', 'GEX data unavailable')
        print(row(f'L1b GEX: {err[:56]}'))
        print('╠' + '═' * (W - 2) + '╣')
        return

    sym     = gex.get('symbol', 'SPY')
    spot    = gex.get('spot', 0)
    hvl     = gex.get('hvl')
    regime  = gex.get('gamma_regime', 'N/A')
    cw      = gex.get('call_wall')
    pw      = gex.get('put_wall')
    vix     = gex.get('vix')
    vanna   = gex.get('vanna_regime', 'N/A')
    zw      = gex.get('zero_dte_weight')
    zmag    = gex.get('zero_dte_magnet')
    zpc     = gex.get('zero_dte_pc_ratio')

    hvl_str  = f'{hvl:.2f}' if hvl is not None else 'N/A'
    rel      = 'ABOVE HVL' if spot > (hvl or 0) else 'BELOW HVL'
    regime_s = '▲ POSITIVE' if 'POSITIVE' in regime else '▼ NEGATIVE'
    vix_s    = f'VIX {vix:.1f}' if vix else 'VIX N/A'

    print(row(f'L1b GEX [{sym}]   Spot {spot:.2f}   {vix_s}'))
    print(row(f'  Regime: {regime_s} gamma   Spot {rel}   HVL: {hvl_str}'))
    if cw or pw:
        cw_s = f'CW {cw:.2f}' if cw else ''
        pw_s = f'PW {pw:.2f}' if pw else ''
        print(row(f'  {cw_s}   {pw_s}'))
    print(row(f'  {vanna[:58]}'))
    if zw is not None:
        zpc_s = f'P/C {zpc:.2f}' if zpc else ''
        print(row(f'  0DTE weight: {zw:.1f}%   Magnet: {zmag:.2f}   {zpc_s}'))
    print('╠' + '═' * (W - 2) + '╣')


def print_brief(today: date, ds_brief: dict, aspect_brief: dict,
                kp_data: dict, wind: dict, coherence: dict, location: str,
                gex: dict = None):
    kp     = kp_data.get('kp')
    kp_int = interpret_kp(kp)
    wind_int = interpret_wind(wind)

    print()
    print('╔' + '═' * 66 + '╗')
    print('║  PANDORA — PRE-MARKET INTELLIGENCE BRIEF (P.M.I.B)' + ' ' * 14 + '║')
    print(f'║  {today.strftime("%A %d %B %Y"):64s}║')
    print(f'║  Location: {aspect_brief["location_label"]:54s}║')
    print('╠' + '═' * 66 + '╣')

    # Coherence
    score = coherence['score']
    bar_filled = int(score / 10)
    bar = '█' * bar_filled + '░' * (10 - bar_filled)
    print(f'║  L5 COHERENCE: [{bar}] {score:3d}/100  Grade {coherence["grade"]:30s}║')
    print(f'║  {coherence["note"]:64s}║')
    print('╠' + '═' * 66 + '╣')

    # L1b GEX
    if gex is not None:
        print_gex_section(gex)

    # L2 Schumann
    kp_val = f'{kp:.1f}' if kp is not None else 'N/A'
    speed  = wind.get('speed')
    bz     = wind.get('bz')
    bz_str = f'  Bz {bz:+.1f}nT' if bz is not None else ''
    sw_str = f'{speed:.0f}km/s{bz_str}' if speed is not None else 'N/A'
    kp_color = kp_int['color']
    l2_inner = f'  L2 SCHUMANN: Kp={kp_val} {kp_int["level"]:10s}  Wind: {sw_str}'
    print(f'║{l2_inner:<66s}║  {kp_color}')
    print(f'║  → {kp_int["action"]:62s}║')
    if wind_int['alert']:
        print(f'║  {"⚠ SOLAR WIND ELEVATED — monitor Kp in next 30-60 min":<64s}║')
    print('╠' + '═' * 66 + '╣')

    # L4 Declination System
    ds = ds_brief['ds']
    pct = ds_brief['pct_of_range']
    bias = ds_brief['bias']
    bar_d = int(pct / 10)
    ds_bar = '█' * bar_d + '░' * (10 - bar_d)
    print(f'║  L4 DECLINATION SYSTEM: DS={ds:+.2f}  [{ds_bar}] {pct:.0f}%' + ' ' * 14 + '║')
    print(f'║  → {bias:62s}║')
    if ds_brief['upcoming_turns']:
        t = ds_brief['upcoming_turns'][0]
        days = (date.fromisoformat(t['date']) - today).days
        print(f'║  → Next turn: {t["date"]} ({days}d)  {t["type"]}  DS={t["ds"]:+.2f}' + ' ' * 20 + '║')
    print('╠' + '═' * 66 + '╣')

    # L3 Aspects
    applying_count = aspect_brief['applying_count']
    t_sq_count = len(aspect_brief['t_squares'])
    print(f'║  L3 ASPECTS: {applying_count} applying  |  {t_sq_count} T-square(s)' + ' ' * 35 + '║')

    if aspect_brief['top_aspects']:
        for a in aspect_brief['top_aspects']:
            pair = f'{a["planet1"]}/{a["planet2"]}'
            line = f'     ◆ {pair:18s}  {a["aspect"]:12s}  {a["orb"]:.2f}°  APPLYING'
            print(f'║  {line:64s}║')
    else:
        print(f'║  {"  No applying aspects within orb today.":64s}║')

    if aspect_brief['t_squares']:
        for ts in aspect_brief['t_squares']:
            line = f'  T-SQ: {ts["p1"]} – {ts["p2"]} – {ts["p3"]}  (empty corner {ts["empty_corner"]:.0f}° RA)'
            print(f'║  {line:64s}║')

    print('╠' + '═' * 66 + '╣')

    # Trigger schedule
    hot = aspect_brief['hot_triggers']
    all_t = aspect_brief['all_triggers']
    print(f'║  TRIGGER SCHEDULE — {len(all_t)} events  ({len(hot)} HIGH priority)' + ' ' * 27 + '║')

    shown = 0
    for t in all_t[:8]:
        quality = '◆◆' if t['applying'] and t['orb'] < 0.5 else \
                  '◆ ' if t['applying'] and t['orb'] < 1.5 else '  '
        line = f'  {t["local_time"]}  {t["trigger"]:4s}  {t["planet"]:9s} / {t["partners"]:9s}  {quality} {t["orb"]:.2f}°'
        print(f'║  {line:64s}║')
        shown += 1
    if len(all_t) > 8:
        print(f'║  {"  ... " + str(len(all_t) - 8) + " more triggers (run aspect_scanner.py for full list)":64s}║')

    print('╚' + '═' * 66 + '╝')
    print()


def main():
    parser = argparse.ArgumentParser(description='Pandora Pre-Market Intelligence Brief')
    parser.add_argument('--date',       help='Date YYYY-MM-DD (default: today)')
    parser.add_argument('--tomorrow',   action='store_true', help='Run brief for tomorrow')
    parser.add_argument('--location',   default='new_york',
                        choices=list(LOCATIONS.keys()), help='Trading location')
    parser.add_argument('--orb',        type=float, default=2.0, help='Aspect orb (default: 2.0)')
    parser.add_argument('--brief',      action='store_true', help='Single-line summary output')
    parser.add_argument('--json',       action='store_true', help='JSON output')
    parser.add_argument('--no-gex',     action='store_true',
                        help='Skip GEX layer (faster — no options data fetch)')
    parser.add_argument('--gex-symbol', default='SPY',
                        help='Symbol for GEX analysis (default: SPY)')
    args = parser.parse_args()

    if args.date:
        today = date.fromisoformat(args.date)
    elif args.tomorrow:
        today = date.today() + timedelta(days=1)
    else:
        today = date.today()

    print(f'\n  Building P.M.I.B for {today}...')

    # L1b GEX (fetch first — can run while other layers load)
    gex = None
    if _GEX_AVAILABLE and not args.no_gex:
        print(f'  L1b: Fetching GEX for {args.gex_symbol}...')
        try:
            gex = get_gex_brief(symbol=args.gex_symbol)
        except Exception as e:
            gex = {'available': False, 'error': str(e)}
    elif not _GEX_AVAILABLE:
        gex = {'available': False, 'error': 'gex_engine not found — check tools/gex-engine/'}

    # Fetch remaining layers
    kp_data   = get_current_kp()
    wind      = get_solar_wind()
    ds_brief  = get_ds_brief(today)
    asp_brief = get_aspect_brief(today, args.location, args.orb)

    kp = kp_data.get('kp')
    gamma_signal = gex.get('gamma_signal', 0) if gex else 0
    vanna_signal = gex.get('vanna_signal', 0) if gex else 0
    coherence = compute_coherence(
        kp                = kp,
        ds_pct            = ds_brief['pct_of_range'],
        applying_count    = asp_brief['applying_count'],
        hot_trigger_count = len(asp_brief['hot_triggers']),
        t_square_count    = len(asp_brief['t_squares']),
        gamma_signal      = gamma_signal,
        vanna_signal      = vanna_signal,
    )

    if args.brief:
        kp_val   = f'{kp:.1f}' if kp is not None else 'N/A'
        kp_level = interpret_kp(kp)['level']
        ds       = ds_brief['ds']
        pct      = ds_brief['pct_of_range']
        ds_zone  = 'TOP' if pct >= 70 else 'BTM' if pct <= 30 else 'MID'
        applying = asp_brief['applying_count']
        grade_letter = coherence['grade'].split(' ')[0]
        score    = coherence['score']
        gex_str  = ''
        if gex and gex.get('available'):
            gr = '▲' if gex.get('gamma_signal', 0) > 0 else '▼'
            gex_str = f' | GEX {gr} HVL:{gex.get("hvl","?")} VIX:{gex.get("vix","?")}'
        print(f"PMIB {today.isoformat()} | Kp={kp_val} {kp_level} | DS={ds:+.2f} {ds_zone} ({pct:.0f}%) | Aspects: {applying} applying{gex_str} | Grade {grade_letter} ({score}/100)")
        return

    if args.json:
        output = {
            'date':       today.isoformat(),
            'location':   args.location,
            'coherence':  coherence,
            'l1b_gex':    gex,
            'l2_schumann': {'kp': kp_data, 'wind': wind, 'interpretation': interpret_kp(kp)},
            'l4_declination': ds_brief,
            'l3_aspects': {
                'applying_count': asp_brief['applying_count'],
                'top_aspects':    asp_brief['top_aspects'],
                'hot_triggers':   asp_brief['hot_triggers'],
                't_squares':      asp_brief['t_squares'],
            },
        }
        print(json.dumps(output, indent=2, default=str))
        return

    print_brief(today, ds_brief, asp_brief, kp_data, wind, coherence, args.location, gex=gex)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
PANDORA — SCHUMANN RESONANCE PROXY
STIS Layer 2: Collective Consciousness / Electromagnetic Mood State

Direct SR monitoring stations require SSL workarounds.
This module uses NOAA SWPC real-time data as the best available proxy:
  - Kp Index (planetary geomagnetic activity) — 1-minute resolution
  - Solar Wind Speed + Proton Density (DSCOVR satellite) — 1-minute resolution

Interpretation (Earik Beann / STIS L2 framework):
  Kp 0–2   → QUIET   — Calm collective field. Trending behavior likely.
  Kp 3–4   → UNSETTLED — Elevated noise. Reduce size, tighter stops.
  Kp 5+    → STORM   — Geomagnetic storm. Expect reversals, erratic moves.
             HIGH SR activity = heightened collective emotion → volatility
             LOW SR activity  = calm collective field → trend continuation

Usage:
  python3 schumann_resonance.py              # Live reading
  python3 schumann_resonance.py --watch      # Refresh every 60s
  python3 schumann_resonance.py --history    # Last 24h Kp chart
  python3 schumann_resonance.py --json       # Machine-readable output
"""

import json
import math
import argparse
import time
import urllib.request
from datetime import datetime, timezone

# NOAA SWPC endpoints (confirmed live)
KP_URL    = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
WIND_URL  = "https://services.swpc.noaa.gov/json/rtsw/rtsw_wind_1m.json"
KP_3H_URL = "https://services.swpc.noaa.gov/json/geospace/geospace_3_hour_kp.json"


def fetch_json(url: str, timeout: int = 15):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'PandoraOS-STIS/1.0 (educational use)',
        'Accept': 'application/json',
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"  [FETCH ERROR] {url}: {e}")
        return None


def get_current_kp() -> dict:
    """Fetch the most recent 1-minute Kp reading."""
    data = fetch_json(KP_URL)
    if not data:
        return {'kp': None, 'time_utc': None, 'error': 'fetch_failed'}

    # Data is a list; most recent entry last
    recent = data[-1] if data else {}
    kp = recent.get('kp_index') or recent.get('kp') or recent.get('Kp')
    time_tag = recent.get('time_tag') or recent.get('observed_time')
    try:
        kp_float = float(str(kp).rstrip('PpGg')) if kp is not None else None
    except (ValueError, TypeError):
        kp_float = None
    return {'kp': kp_float, 'time_utc': time_tag, 'raw': recent}


def get_solar_wind() -> dict:
    """Fetch the most recent solar wind reading from DSCOVR."""
    data = fetch_json(WIND_URL)
    if not data:
        return {'speed': None, 'density': None, 'error': 'fetch_failed'}

    recent = data[-1] if data else {}
    speed   = recent.get('proton_speed')   or recent.get('speed')
    density = recent.get('proton_density') or recent.get('density')
    bt      = recent.get('bt')   # total magnetic field strength
    bz      = recent.get('bz')   # z-component (negative bz = geo-effective)
    time_tag = recent.get('time_tag')
    return {
        'speed':   float(speed)   if speed   is not None else None,
        'density': float(density) if density is not None else None,
        'bt':      float(bt)      if bt      is not None else None,
        'bz':      float(bz)      if bz      is not None else None,
        'time_utc': time_tag,
        'raw': recent,
    }


def get_kp_history_3h() -> list:
    """Fetch 3-hour Kp readings for the last ~72 hours."""
    data = fetch_json(KP_3H_URL)
    if not data:
        return []
    return data


def interpret_kp(kp: float) -> dict:
    """Map Kp value to STIS L2 trading state."""
    if kp is None:
        return {'level': 'UNKNOWN', 'color': '⬜', 'action': 'No data — proceed with caution'}

    if kp <= 2:
        return {
            'level':  'QUIET',
            'color':  '🟢',
            'stis':   'L2: Calm collective field',
            'action': 'Full size allowed. Trend-following setups favored.',
            'note':   'Collective nervous system is settled. Follow the plan.',
        }
    elif kp <= 4:
        return {
            'level':  'UNSETTLED',
            'color':  '🟡',
            'stis':   'L2: Elevated electromagnetic noise',
            'action': 'Reduce position size 20-30%. Tighten stops. No counter-trend.',
            'note':   'Collective field disturbed. Expect increased false moves.',
        }
    elif kp <= 6:
        return {
            'level':  'STORM',
            'color':  '🔴',
            'stis':   'L2: Geomagnetic storm — heightened collective emotion',
            'action': 'Minimum size or stand aside. Watch for sharp reversals.',
            'note':   'High SR proxy. Crowd psychology unstable. Reactive environment.',
        }
    else:
        return {
            'level':  'SEVERE STORM',
            'color':  '🟣',
            'stis':   'L2: Severe geomagnetic event',
            'action': 'DO NOT TRADE. Stand completely aside.',
            'note':   'Extreme collective disturbance. All setups invalidated.',
        }


def interpret_wind(wind: dict) -> dict:
    """Interpret solar wind data for STIS L2 context."""
    speed   = wind.get('speed')
    density = wind.get('density')
    bz      = wind.get('bz')

    notes = []
    alert = False

    if speed is not None:
        if speed > 600:
            notes.append(f'FAST solar wind ({speed:.0f} km/s) — storm driver incoming')
            alert = True
        elif speed > 450:
            notes.append(f'Elevated solar wind ({speed:.0f} km/s) — watch Kp trend')
        else:
            notes.append(f'Normal solar wind ({speed:.0f} km/s)')

    if density is not None:
        if density > 20:
            notes.append(f'High proton density ({density:.1f}/cm³) — compressed magnetosphere')
            alert = True
        else:
            notes.append(f'Proton density {density:.1f}/cm³')

    if bz is not None:
        if bz < -10:
            notes.append(f'Bz strongly negative ({bz:.1f} nT) — energy injection to magnetosphere')
            alert = True
        elif bz < -5:
            notes.append(f'Bz negative ({bz:.1f} nT) — mild geo-effectiveness')
        else:
            notes.append(f'Bz {bz:.1f} nT (neutral/positive)')

    return {'notes': notes, 'alert': alert}


def kp_bar(kp: float, width: int = 20) -> str:
    if kp is None:
        return '░' * width
    pct = min(kp / 9.0, 1.0)
    filled = int(pct * width)
    if kp <= 2:
        char = '█'
    elif kp <= 4:
        char = '▓'
    elif kp <= 6:
        char = '▒'
    else:
        char = '░'
    return char * filled + '·' * (width - filled)


def print_report(kp_data: dict, wind: dict, interp: dict, wind_interp: dict):
    now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    kp = kp_data.get('kp')
    kp_time = kp_data.get('time_utc', 'unknown')

    print()
    print('═' * 68)
    print('  PANDORA — SCHUMANN RESONANCE PROXY  (NOAA SWPC)')
    print(f'  Fetched: {now_utc}')
    print('═' * 68)

    print(f'\n  GEOMAGNETIC FIELD (Kp Index)')
    if kp is not None:
        bar = kp_bar(kp)
        print(f'  Kp = {kp:.1f}  [{bar}]  (0 = quiet → 9 = extreme storm)')
        print(f'  Reading time: {kp_time}')
    else:
        print('  Kp = N/A  (fetch failed)')

    print()
    print(f'  {interp["color"]}  STATUS: {interp["level"]}')
    print(f'  {interp.get("stis", "")}')
    print(f'  TRADING ACTION: {interp["action"]}')
    if 'note' in interp:
        print(f'  NOTE: {interp["note"]}')

    print(f'\n  SOLAR WIND (DSCOVR satellite)')
    speed   = wind.get('speed')
    density = wind.get('density')
    bz      = wind.get('bz')
    if speed is not None:
        print(f'  Speed:   {speed:.0f} km/s')
    if density is not None:
        print(f'  Density: {density:.1f} protons/cm³')
    if bz is not None:
        print(f'  Bz:      {bz:+.1f} nT  {"← GEO-EFFECTIVE" if bz < -5 else ""}')
    if wind_interp['notes']:
        print()
        for note in wind_interp['notes']:
            print(f'  → {note}')
    if wind_interp['alert']:
        print(f'  ⚠ SOLAR WIND ALERT — Kp escalation likely within 30–60 min')

    print(f'\n  STIS L2 INTEGRATION:')
    print(f'  Layer 2 (Collective Consciousness) state = {interp["level"]}')
    print(f'  This modifies L1 (Mechanical) signal execution:')
    print(f'    QUIET     → Execute signals at full confidence')
    print(f'    UNSETTLED → Downgrade signal confidence, reduce size')
    print(f'    STORM     → Override L1 signals, minimize exposure')
    print(f'    SEVERE    → Full stand-aside, all L1 signals void')

    print()
    print('  INTERPRETATION GUIDE:')
    print('  Kp 0-2  🟢 Quiet    — Trend-following, full size')
    print('  Kp 3-4  🟡 Unsettled — Reduce size 20-30%, tighter stops')
    print('  Kp 5-6  🔴 Storm    — Minimum size, expect reversals')
    print('  Kp 7+   🟣 Severe   — Stand aside, do not trade')
    print()
    print('═' * 68)


def print_history(history: list):
    if not history:
        print('  No 3-hour Kp history available.')
        return

    print()
    print('  KP INDEX — LAST 72 HOURS (3-hour resolution)')
    print(f'  {"Time":22s}  {"Kp":>5s}  {"Bar":22s}  Level')
    print(f'  {"─"*22}  {"─"*5}  {"─"*22}  {"─"*12}')

    # Show last 24 entries (~72 hours at 3h resolution)
    for entry in history[-24:]:
        t = entry.get('time_tag') or entry.get('observed_time', '')
        kp_val = entry.get('kp_index') or entry.get('Kp') or entry.get('kp')
        if kp_val is None:
            continue
        kp_f = float(kp_val)
        bar = kp_bar(kp_f, width=12)
        interp = interpret_kp(kp_f)
        print(f'  {str(t):22s}  {kp_f:>5.1f}  [{bar}]  {interp["level"]}')


def main():
    parser = argparse.ArgumentParser(description='Pandora Schumann Resonance Proxy')
    parser.add_argument('--watch',   action='store_true', help='Refresh every 60 seconds')
    parser.add_argument('--history', action='store_true', help='Show 72h Kp history')
    parser.add_argument('--json',    action='store_true', help='Machine-readable JSON output')
    parser.add_argument('--interval', type=int, default=60, help='Watch interval in seconds')
    args = parser.parse_args()

    def run_once():
        print('  Fetching NOAA SWPC data...')
        kp_data   = get_current_kp()
        wind      = get_solar_wind()
        interp    = interpret_kp(kp_data.get('kp'))
        wind_interp = interpret_wind(wind)

        if args.json:
            output = {
                'timestamp_utc': datetime.now(timezone.utc).isoformat(),
                'kp': kp_data,
                'solar_wind': wind,
                'interpretation': interp,
                'wind_interpretation': wind_interp,
                'stis_l2_state': interp['level'],
                'trading_action': interp['action'],
            }
            print(json.dumps(output, indent=2))
            return

        print_report(kp_data, wind, interp, wind_interp)

        if args.history:
            history = get_kp_history_3h()
            print_history(history)

    if args.watch:
        print(f'  Watching NOAA SWPC (refresh every {args.interval}s). Ctrl+C to stop.')
        try:
            while True:
                run_once()
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print('\n  Watch stopped.')
    else:
        run_once()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
PANDORA — DECLINATION SYSTEM
Earik Beann's planetary declination forecast for market turning points.

Formula: DS = (6 × Mercury) + (5 × Venus) + (4 × Earth) + (3 × Mars)
            + (2 × Jupiter) + (1 × Saturn)
where each value is the planet's declination in degrees (N = positive, S = negative)

Usage:
  python3 declination_system.py                     # Next 6 months from today
  python3 declination_system.py --start 2026-01-01 --end 2026-12-31
  python3 declination_system.py --months 12 --chart  # Generate PNG chart
  python3 declination_system.py --today              # Just today's reading
"""

import ephem
import math
import argparse
import json
from datetime import date, timedelta, datetime


# ── Weights (Earik Beann formula) ─────────────────────────────────────────────
WEIGHTS = {
    'mercury': 6,
    'venus':   5,
    'earth':   4,  # Earth's declination = Sun's declination (geocentric)
    'mars':    3,
    'jupiter': 2,
    'saturn':  1,
}

RAD_TO_DEG = 180.0 / math.pi


def get_declinations(dt: date) -> dict:
    """Return declination in degrees for each planet on the given date."""
    d = ephem.Date(dt.strftime('%Y/%m/%d'))
    return {
        'mercury': float(ephem.Mercury(d).dec) * RAD_TO_DEG,
        'venus':   float(ephem.Venus(d).dec)   * RAD_TO_DEG,
        'earth':   float(ephem.Sun(d).dec)     * RAD_TO_DEG,
        'mars':    float(ephem.Mars(d).dec)    * RAD_TO_DEG,
        'jupiter': float(ephem.Jupiter(d).dec) * RAD_TO_DEG,
        'saturn':  float(ephem.Saturn(d).dec)  * RAD_TO_DEG,
    }


def compute_ds(decls: dict) -> float:
    """Compute the Declination System composite value."""
    return sum(WEIGHTS[planet] * decls[planet] for planet in WEIGHTS)


def generate_series(start: date, end: date, step_days: int = 1) -> list:
    """Generate DS values for a date range. Returns list of (date, ds, decls)."""
    series = []
    current = start
    while current <= end:
        decls = get_declinations(current)
        ds = compute_ds(decls)
        series.append({
            'date': current.isoformat(),
            'ds': round(ds, 4),
            'decls': {k: round(v, 4) for k, v in decls.items()},
        })
        current += timedelta(days=step_days)
    return series


def find_turning_points(series: list, window: int = 5) -> list:
    """
    Find local maxima and minima in the DS curve.
    window: number of points each side to compare against.
    Returns list of turning point dicts with date, ds, type ('TOP' or 'BOTTOM').
    """
    turns = []
    vals = [p['ds'] for p in series]
    for i in range(window, len(vals) - window):
        segment = vals[i - window: i + window + 1]
        center = vals[i]
        if center == max(segment):
            turns.append({
                'date': series[i]['date'],
                'ds': series[i]['ds'],
                'type': 'TOP',
            })
        elif center == min(segment):
            turns.append({
                'date': series[i]['date'],
                'ds': series[i]['ds'],
                'type': 'BOTTOM',
            })
    return turns


def print_report(series: list, turns: list):
    """Print a clean text report."""
    if not series:
        return

    dates = [p['date'] for p in series]
    vals  = [p['ds']   for p in series]
    ds_min, ds_max = min(vals), max(vals)
    ds_range = ds_max - ds_min

    print()
    print('═' * 60)
    print('  PANDORA — DECLINATION SYSTEM')
    print(f'  Range: {dates[0]}  →  {dates[-1]}')
    print('═' * 60)

    # Current reading
    today_entry = series[0]
    today_ds = today_entry['ds']
    pct = (today_ds - ds_min) / ds_range * 100 if ds_range else 50
    bar_len = int(pct / 5)
    bar = '█' * bar_len + '░' * (20 - bar_len)
    print(f'\n  TODAY  {today_entry["date"]}')
    print(f'  DS = {today_ds:+.2f}  [{bar}] {pct:.0f}% of range')
    print(f'  Range: {ds_min:.2f} (low) → {ds_max:.2f} (high)')

    # Individual planet readings today
    d = today_entry['decls']
    print(f'\n  PLANET DECLINATIONS (today):')
    for planet, weight in WEIGHTS.items():
        dec = d[planet]
        direction = 'N' if dec >= 0 else 'S'
        print(f'    {planet.capitalize():8s}  {weight}×  {abs(dec):6.2f}°{direction}  '
              f'contrib: {weight * dec:+7.2f}')

    # Turning points
    print(f'\n  TURNING POINTS ({len(turns)} found):')
    print(f'  {"Date":12s}  {"Type":8s}  {"DS Value":>10s}  Signal')
    print(f'  {"─"*12}  {"─"*8}  {"─"*10}  {"─"*20}')
    for t in turns:
        pct_t = (t['ds'] - ds_min) / ds_range * 100 if ds_range else 50
        signal = '◆ STRONG TOP' if t['type'] == 'TOP' and pct_t > 70 else \
                 '◆ STRONG BOT' if t['type'] == 'BOTTOM' and pct_t < 30 else \
                 '  moderate'
        print(f'  {t["date"]:12s}  {t["type"]:8s}  {t["ds"]:+10.2f}  {signal}')

    # Next 3 turning points from today
    today_str = date.today().isoformat()
    upcoming = [t for t in turns if t['date'] >= today_str][:3]
    if upcoming:
        print(f'\n  NEXT TURNING POINTS:')
        for t in upcoming:
            days_away = (date.fromisoformat(t['date']) - date.today()).days
            print(f'    {t["date"]}  ({days_away:+d} days)  {t["type"]}  DS={t["ds"]:+.2f}')

    print()
    print('  READING GUIDE:')
    print('  HIGH DS → market likely forming a TOP (sell zone)')
    print('  LOW DS  → market likely forming a BOTTOM (buy zone)')
    print('  Watch for INVERSION: if market moves opposite → stay inverted')
    print('  until the next turning point, then re-assess.')
    print()
    print('═' * 60)


def generate_chart(series: list, turns: list, output_path: str):
    """Generate a matplotlib chart of the DS curve with turning points."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates

        dates_dt = [datetime.fromisoformat(p['date']) for p in series]
        vals     = [p['ds'] for p in series]

        fig, ax = plt.subplots(figsize=(16, 6))
        fig.patch.set_facecolor('#0d0d0d')
        ax.set_facecolor('#0d0d0d')

        # DS curve
        ax.plot(dates_dt, vals, color='#c8a96e', linewidth=1.5, label='Declination System')

        # Fill: positive = bullish tint, negative relative = bearish tint
        mid = (max(vals) + min(vals)) / 2
        ax.fill_between(dates_dt, vals, mid,
                        where=[v > mid for v in vals],
                        alpha=0.15, color='#00ff88', label='Elevated (top zone)')
        ax.fill_between(dates_dt, vals, mid,
                        where=[v < mid for v in vals],
                        alpha=0.15, color='#ff4444', label='Depressed (bottom zone)')

        # Midline
        ax.axhline(mid, color='#555555', linewidth=0.8, linestyle='--')

        # Turning points
        for t in turns:
            dt = datetime.fromisoformat(t['date'])
            color = '#ff4444' if t['type'] == 'TOP' else '#00ff88'
            marker = 'v' if t['type'] == 'TOP' else '^'
            ax.scatter([dt], [t['ds']], color=color, s=60, zorder=5, marker=marker)

        # Today marker
        today = datetime.combine(date.today(), datetime.min.time())
        if dates_dt[0] <= today <= dates_dt[-1]:
            ax.axvline(today, color='#ffffff', linewidth=1, linestyle=':', alpha=0.6)
            ax.text(today, max(vals), ' TODAY', color='#ffffff', fontsize=8, va='top')

        # Styling
        ax.set_title('PANDORA — DECLINATION SYSTEM\nEarik Beann Formula  ·  DS = 6×Mer + 5×Ven + 4×Ear + 3×Mar + 2×Jup + 1×Sat',
                     color='#c8a96e', fontsize=11, pad=12)
        ax.set_xlabel('Date', color='#888888')
        ax.set_ylabel('DS Composite Value', color='#888888')
        ax.tick_params(colors='#888888')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=30, ha='right')
        for spine in ax.spines.values():
            spine.set_edgecolor('#333333')
        ax.legend(loc='upper right', facecolor='#1a1a1a', edgecolor='#333333',
                  labelcolor='#888888', fontsize=8)
        ax.grid(True, color='#222222', linewidth=0.5)

        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='#0d0d0d')
        plt.close()
        print(f'  Chart saved: {output_path}')
    except Exception as e:
        print(f'  Chart error: {e}')


def today_snapshot():
    """Quick single-day reading."""
    today = date.today()
    decls = get_declinations(today)
    ds = compute_ds(decls)
    print(f'\nDECLINATION SYSTEM — {today.isoformat()}')
    print(f'DS = {ds:+.4f}')
    for planet, weight in WEIGHTS.items():
        dec = decls[planet]
        direction = 'N' if dec >= 0 else 'S'
        contrib = weight * dec
        print(f'  {planet.capitalize():8s}  {weight}×  {abs(dec):6.3f}°{direction}  →  {contrib:+.3f}')
    print()


def main():
    parser = argparse.ArgumentParser(description='Pandora Declination System')
    parser.add_argument('--start', help='Start date YYYY-MM-DD (default: today)')
    parser.add_argument('--end',   help='End date YYYY-MM-DD')
    parser.add_argument('--months', type=int, default=6, help='Months to forecast (default: 6)')
    parser.add_argument('--step',   type=int, default=1, help='Day step (default: 1)')
    parser.add_argument('--window', type=int, default=7, help='Turning point window (default: 7)')
    parser.add_argument('--chart',  action='store_true', help='Generate PNG chart')
    parser.add_argument('--today',  action='store_true', help='Single-day snapshot')
    parser.add_argument('--json',   action='store_true', help='Output raw JSON data')
    parser.add_argument('--output', default='/tmp/declination_chart.png', help='Chart output path')
    args = parser.parse_args()

    if args.today:
        today_snapshot()
        return

    start = date.fromisoformat(args.start) if args.start else date.today()
    if args.end:
        end = date.fromisoformat(args.end)
    else:
        # Default: args.months forward
        from dateutil.relativedelta import relativedelta
        try:
            end = start + relativedelta(months=args.months)
        except ImportError:
            end = start + timedelta(days=args.months * 30)

    print(f'\n  Calculating DS from {start} to {end}...')
    series = generate_series(start, end, step_days=args.step)
    turns  = find_turning_points(series, window=args.window)

    if args.json:
        print(json.dumps({'series': series, 'turning_points': turns}, indent=2))
        return

    print_report(series, turns)

    if args.chart:
        generate_chart(series, turns, args.output)

    # Always save JSON alongside
    json_path = args.output.replace('.png', '.json') if args.output.endswith('.png') \
                else args.output + '.json'
    with open(json_path, 'w') as f:
        json.dump({'series': series, 'turning_points': turns,
                   'generated': date.today().isoformat(),
                   'formula': 'DS = 6×Mercury + 5×Venus + 4×Earth + 3×Mars + 2×Jupiter + 1×Saturn'}, f, indent=2)
    print(f'  Data saved: {json_path}')


if __name__ == '__main__':
    main()

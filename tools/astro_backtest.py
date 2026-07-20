#!/usr/bin/env python3
"""
PANDORA — L4 ASTRO VALIDATION HARNESS (PRD v6 build #9)
"As above, so below" — tested, not assumed.

Question: do Declination System (Earik Beann) turning points cluster near
real market turning points more than chance would produce?

Method (decoded 4-step validation, applied to L4):
  1. Compute DS series over a historical window (ephem — works for any date)
  2. Find DS turning points (peaks/troughs of the weighted declination wave)
  3. Find market turning points (swing highs/lows on daily closes)
  4. Score: % of market turns with a DS turn within ±N days
  5. Permutation baseline: 1000 draws of equally many random dates —
     does the real DS beat the random distribution? (p-value)

Usage:
  python3 astro_backtest.py --symbol SPY --years 10
  python3 astro_backtest.py --symbol GLD --years 15 --tolerance 4
"""

import argparse
import random
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'declination-system'))
import declination_system as ds


def price_turning_points(closes, dates, window=10):
    """Swing highs/lows: strict local extrema over ±window trading days."""
    turns = []
    for i in range(window, len(closes) - window):
        seg = closes[i - window: i + window + 1]
        if closes[i] == max(seg):
            turns.append((dates[i], 'HIGH'))
        elif closes[i] == min(seg):
            turns.append((dates[i], 'LOW'))
    return turns


def hit_rate(price_turns, event_dates, tol):
    """% of price turns with an event within ±tol calendar days."""
    if not price_turns:
        return 0.0
    hits = 0
    ev = sorted(event_dates)
    for pd_, _ in price_turns:
        # nearest event distance
        best = min(abs((pd_ - e).days) for e in ev)
        if best <= tol:
            hits += 1
    return hits / len(price_turns)


def main():
    p = argparse.ArgumentParser(description='L4 Astro Validation Harness')
    p.add_argument('--symbol', default='SPY')
    p.add_argument('--years', type=int, default=10)
    p.add_argument('--tolerance', type=int, default=5, help='±calendar days for a hit')
    p.add_argument('--price-window', type=int, default=10, help='swing window (trading days)')
    p.add_argument('--ds-window', type=int, default=7, help='DS turning point window (days)')
    p.add_argument('--permutations', type=int, default=1000)
    p.add_argument('--extremes', type=float, default=None,
                   help='Test only DS turns in the top/bottom X fraction of the DS range (e.g. 0.2) — the book\'s actual claim')
    a = p.parse_args()

    end = date.today()
    start = end - timedelta(days=int(a.years * 365.25))
    print(f'  L4 ASTRO VALIDATION — {a.symbol} | {start} → {end} | hit = DS turn within ±{a.tolerance}d')
    print('  ─' * 38)

    # 1-2. DS series + turns
    print('  computing declination series (ephem)...')
    series = ds.generate_series(start, end, step_days=1)
    ds_turns = ds.find_turning_points(series, window=a.ds_window)
    ds_dates = [t['date'] if isinstance(t, dict) else t[0] for t in ds_turns]
    ds_dates = [d if isinstance(d, date) else date.fromisoformat(str(d)[:10]) for d in ds_dates]
    if a.extremes:
        vals = [pt['ds'] for pt in series]
        lo, hi = min(vals), max(vals)
        span = hi - lo
        keep = []
        for t in ds_turns:
            frac = (t['ds'] - lo) / span
            if frac >= 1 - a.extremes or frac <= a.extremes:
                keep.append(date.fromisoformat(str(t['date'])[:10]))
        ds_dates = keep
        print(f'  EXTREMES filter ({a.extremes:.0%} tails of DS range): {len(ds_dates)} turns kept')
    print(f'  DS turning points: {len(ds_dates)} '
          f'(avg one per {round((end-start).days/max(len(ds_dates),1))} days)')

    # 3. market turns
    import yfinance as yf
    h = yf.Ticker(a.symbol).history(start=str(start), end=str(end), interval='1d')
    if h.empty:
        print('  ✗ no price data'); return
    closes = h['Close'].tolist()
    dates = [d.date() for d in h.index]
    pturns = price_turning_points(closes, dates, window=a.price_window)
    print(f'  {a.symbol} swing turns (±{a.price_window} trading days): {len(pturns)}')

    # 4. real hit rate
    real = hit_rate(pturns, ds_dates, a.tolerance)

    # 5. permutation baseline: same NUMBER of events, random calendar dates
    total_days = (end - start).days
    n_events = len(ds_dates)
    rng = random.Random(42)
    baseline = []
    for _ in range(a.permutations):
        fake = [start + timedelta(days=rng.randrange(total_days)) for _ in range(n_events)]
        baseline.append(hit_rate(pturns, fake, a.tolerance))
    bmean = sum(baseline) / len(baseline)
    beat = sum(1 for b in baseline if b >= real)
    pval = beat / len(baseline)

    print('  ─' * 38)
    print(f'  REAL DS hit rate:      {real:6.1%}')
    print(f'  Random baseline mean:  {bmean:6.1%}  ({a.permutations} permutations)')
    print(f'  p-value (random ≥ real): {pval:.3f}')
    print('  ─' * 38)
    if pval <= 0.05 and real > bmean:
        print('  ✓ SIGNAL — DS turns cluster near market turns beyond chance.')
        print('    Next: walk-forward split + per-instrument weighting refinement.')
    elif real > bmean:
        print('  ~ WEAK — above chance but not significant. More data / refine weights,')
        print('    or narrow the claim (DS extremes only, specific instruments).')
    else:
        print('  ✗ NO EDGE at these parameters — DS turns do not beat random dates.')
        print('    Doctrine remains L4 context; directional authority stays suspended (PRD v6 §9).')
    print(f'\n  Ledger line: {a.symbol} | {a.years}y | tol ±{a.tolerance}d | real {real:.1%} vs base {bmean:.1%} | p={pval:.3f}')


if __name__ == '__main__':
    main()

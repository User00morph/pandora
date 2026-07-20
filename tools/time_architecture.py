#!/usr/bin/env python3
"""
PANDORA — STIS TIME ARCHITECTURE MODULE
The engineered-calendar edge (PRD v6 §7). Market time is a construct;
its boundaries force real capital to move at scheduled appointments.
This module answers: "which engineered flows are active TODAY?"

Usage:
  python3 time_architecture.py            — today's flows
  python3 time_architecture.py --date 2026-09-18
  python3 time_architecture.py --week     — next 7 days
Importable: get_flows(date) -> list[(tag, label, detail)]
"""

import argparse
from datetime import date, datetime, timedelta

# FOMC 2026 scheduled meeting dates (decision = day 2, 14:00 ET).
# Verify annually against federalreserve.gov/monetarypolicy/fomccalendars.htm
FOMC_2026 = [
    date(2026, 1, 28), date(2026, 3, 18), date(2026, 4, 29),
    date(2026, 6, 17), date(2026, 7, 29), date(2026, 9, 16),
    date(2026, 10, 28), date(2026, 12, 9),
]

QUAD_MONTHS = {3, 6, 9, 12}


def _nth_weekday(year, month, weekday, n):
    """n-th weekday (0=Mon..4=Fri) of a month."""
    d = date(year, month, 1)
    offset = (weekday - d.weekday()) % 7
    return d + timedelta(days=offset + 7 * (n - 1))


def _last_weekday(year, month, weekday):
    if month == 12:
        d = date(year, 12, 31)
    else:
        d = date(year, month + 1, 1) - timedelta(days=1)
    offset = (d.weekday() - weekday) % 7
    return d - timedelta(days=offset)


def _trading_days_back(d, n):
    """n trading days (weekdays) before d — holiday-approximate."""
    cur = d
    while n > 0:
        cur -= timedelta(days=1)
        if cur.weekday() < 5:
            n -= 1
    return cur


def _last_trading_day_of_month(year, month):
    if month == 12:
        d = date(year, 12, 31)
    else:
        d = date(year, month + 1, 1) - timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def _first_n_trading_days(year, month, n):
    days, d = [], date(year, month, 1)
    while len(days) < n:
        if d.weekday() < 5:
            days.append(d)
        d += timedelta(days=1)
    return days


def get_flows(d=None):
    """Return list of (tag, label, detail) for engineered flows active on date d."""
    d = d or date.today()
    flows = []

    if d.weekday() >= 5:
        flows.append(('CLOSED', 'Weekend', 'Equity/futures closed. Crypto is 24/7 — weekend liquidity thin, moves exaggerated, wicks unreliable.'))
        return flows

    y, m = d.year, d.month
    opex = _nth_weekday(y, m, 4, 3)                      # 3rd Friday
    opex_week = opex - timedelta(days=opex.weekday())     # that week's Monday

    # --- OPEX / quad witching ---
    if d == opex:
        tag = 'QUAD WITCHING' if m in QUAD_MONTHS else 'OPEX'
        flows.append((tag, 'Monthly options expiration TODAY',
                      'Gamma map collapses at close. Expect pin to max-gamma into 16:00, then Monday directional reset.'))
    elif opex_week <= d < opex:
        flows.append(('OPEX WEEK', f'Monthly OPEX this Friday ({opex})',
                      'Pinning pressure builds toward major gamma strikes into Friday.'))

    # --- Futures roll (week before quarterly expiry) ---
    if m in QUAD_MONTHS:
        roll_start = opex - timedelta(days=opex.weekday() + 7)
        if roll_start <= d < opex_week:
            flows.append(('FUTURES ROLL', 'Quarterly futures roll week',
                          'Volume migrating contracts — suspend volume-based reads (VP/footprint distorted).'))

    # --- Month-end rebalance / turn-of-month ---
    ltd = _last_trading_day_of_month(y, m)
    if d in (_trading_days_back(ltd, 1), ltd):
        q = ' + QUARTER-END window-dressing' if m in QUAD_MONTHS else ''
        flows.append(('MONTH-END', f'Month-end rebalance window{q}',
                      'Pension/target-date mechanical flows: after a strong equity month expect supply, after a weak one expect demand.'))
    # window = last trading day of any month + first 3 trading days of the next
    tom = [ltd] + _first_n_trading_days(y, m, 3)
    if d in tom:
        flows.append(('TURN-OF-MONTH', 'Turn-of-month inflow window',
                      'Payroll/401k passive inflows — documented long-bias tailwind (last + first 3 trading days).'))

    # --- FOMC ---
    for f in FOMC_2026:
        if d == f:
            flows.append(('FOMC', 'FOMC decision TODAY (14:00 ET)',
                          'No new positions before the print. The reaction is the sacred-vs-reactive test — trade the second move, not the first.'))
        elif d == _trading_days_back(f, 1):
            flows.append(('FOMC-1', f'FOMC decision tomorrow ({f})',
                          'Pre-FOMC drift window (historical upward bias). No fresh risk inside 24h of the print.'))

    # --- Weekly cadence ---
    if d.weekday() == 4:
        flows.append(('FRI EXPIRY', 'Weekly options expiry',
                      'Weekly gamma collapses at close → Monday repositioning. Feeds the Monday Gold Box (IEC).'))
    if d.weekday() == 0:
        flows.append(('MONDAY', 'Weekly reset / Monday Gold Box',
                      'Post-expiry repositioning day. IEC weekly range forming — Gold Box rules apply.'))
    if d == _nth_weekday(y, m, 4, 1):
        flows.append(('NFP', 'Non-Farm Payrolls (08:30 ET)',
                      'Reactive (non-sacred) force — trade the reaction, do not mistake it for regime change. Reduced size per risk skill.'))

    # --- Crypto calendar ---
    cme_btc = _last_weekday(y, m, 4)
    if d == cme_btc:
        flows.append(('CRYPTO EXPIRY', 'CME BTC futures + Deribit monthly options expiry (last Friday)',
                      'Monthly crypto max-pain window — expect pinning into expiry, release after.'))
    elif 0 <= (cme_btc - d).days <= 4 and d.weekday() <= cme_btc.weekday():
        flows.append(('CRYPTO EXPIRY WK', f'Crypto monthly expiry this Friday ({cme_btc})',
                      'Deribit/CME positioning builds — watch max-pain gravitation on BTC/ETH.'))

    # --- Session anatomy (always) ---
    flows.append(('SESSION', 'Anatomy: 9:30–10:00 auction sets range · 12:00–13:30 lunch void (levels lie) · 14:00+ 0DTE pinning in positive gamma · 15:50–16:00 MOC imbalances',
                  'Event time > clock time: a bar at 9:35 and a bar at 12:30 are not the same object.'))

    return flows


def render(d=None):
    d = d or date.today()
    lines = [f'  ⏱  TIME ARCHITECTURE — engineered flows for {d} ({d.strftime("%A")})']
    for tag, label, detail in get_flows(d):
        lines.append(f'    [{tag}] {label}')
        lines.append(f'        {detail}')
    return '\n'.join(lines)


def main():
    p = argparse.ArgumentParser(description='STIS Time Architecture — engineered flow calendar')
    p.add_argument('--date', help='YYYY-MM-DD (default today)')
    p.add_argument('--week', action='store_true', help='Show next 7 days')
    a = p.parse_args()
    d = datetime.strptime(a.date, '%Y-%m-%d').date() if a.date else date.today()
    if a.week:
        for i in range(7):
            print(render(d + timedelta(days=i)))
            print()
    else:
        print(render(d))


if __name__ == '__main__':
    main()

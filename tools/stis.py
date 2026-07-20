#!/usr/bin/env python3
"""
PANDORA — STIS UNIFIED LAUNCHER (v2 — PRD v6 build #1)
Single entry point for the Sovereign Trading Intelligence System tool stack.

Commands:
  pulse     — THE 5-MINUTE DAILY PULSE (PRD v6 §12): TTL staleness check →
              Time Architecture flows → crypto pulse → GEX all symbols (saved)
              → PMIB brief → Forge streak update. Run this every market day.
  brief     — Alias for pulse (upgraded per PRD v6 build queue #1)
  report    — Full Pre-Market Intelligence Brief (P.M.I.B)
  flows     — Time Architecture engineered-flow calendar (today)
  crypto    — Crypto pulse only (BTC/ETH regime read)
  ttl       — Intelligence freshness check only
  streak    — Show Forge gate streak status
  gex       — GEX engine (pass-through, e.g. --symbol SPY --save)
  ds        — Declination System reading (today)
  aspects   — Aspect scanner (today)
  kp        — Schumann Resonance proxy (live Kp / solar wind)
  iec       — IEC Cycle Scanner (all 10 instruments)
  all       — Legacy sequential run (ds + aspects + kp + iec)

Usage:
  python3 stis.py pulse
  python3 stis.py pulse --fast        (skip GEX save — offline/weekend mode)
  python3 stis.py flows --week
"""

import sys
import subprocess
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT     = Path(__file__).parent
PANDORA  = ROOT.parent
DS_DIR   = ROOT / 'declination-system'
IEC_DIR  = ROOT / 'iec-scanner'
GEX_DIR  = ROOT / 'gex-engine'
QUANT    = PANDORA / 'D.S.E' / 'trading' / 'quant'
RESEARCH = PANDORA / 'D.S.E' / 'trading' / 'research'
TRADING  = PANDORA / 'D.S.E' / 'trading'
STREAK   = QUANT / 'pulse_streak.log'

sys.path.insert(0, str(ROOT))

TOOLS = {
    'report':  [sys.executable, str(DS_DIR / 'pmib.py')],
    'ds':      [sys.executable, str(DS_DIR / 'declination_system.py'), '--today'],
    'aspects': [sys.executable, str(DS_DIR / 'aspect_scanner.py')],
    'kp':      [sys.executable, str(DS_DIR / 'schumann_resonance.py')],
    'iec':     [sys.executable, str(IEC_DIR / 'iec_scanner.py')],
    'gex':     [sys.executable, str(GEX_DIR / 'gex_engine.py')],
}

ALL_ORDER = ['ds', 'aspects', 'kp', 'iec']

# ── TTL TABLE (PRD v6 §10) — (glob under Pandora root, ttl days, label) ──
TTL_RULES = [
    ('D.S.E/trading/quant/*_gex-session-map_spy.md', 1,  'GEX session map (SPY)'),
    ('D.S.E/trading/research/*_current-field.md',    14, 'Macro current-field summary'),
    ('D.S.E/trading/context_trading.md',             30, 'context_trading.md (pairs table / cycle phase)'),
    ('D.S.E/trading/logs/pmib/*_pmib_*.md',          1,  'PMIB session file'),
]


def _env():
    """Subprocess env with proper SSL certs (macOS python lacks system CAs)."""
    import os
    env = os.environ.copy()
    try:
        import certifi
        env.setdefault('SSL_CERT_FILE', certifi.where())
        env.setdefault('REQUESTS_CA_BUNDLE', certifi.where())
    except ImportError:
        pass
    return env


def run(cmd: list, extra_args: list = None):
    sys.stdout.flush()
    subprocess.run(cmd + (extra_args or []), env=_env())


# ─────────────────────────── TTL CHECK ───────────────────────────

def ttl_check(verbose=True):
    if verbose:
        print('  🕰  INTELLIGENCE FRESHNESS (PRD v6 §10)')
    stale = 0
    today = date.today()
    for pattern, ttl, label in TTL_RULES:
        files = sorted(PANDORA.glob(pattern))
        if not files:
            print(f'    ✗ MISSING  {label} — no file matches {pattern}')
            stale += 1
            continue
        newest = max(files, key=lambda f: f.stat().st_mtime)
        age = (today - date.fromtimestamp(newest.stat().st_mtime)).days
        # trading-day grace: Mon reads Fri's dailies as fresh
        eff_ttl = ttl + 2 if (ttl == 1 and today.weekday() == 0) else ttl
        if age > eff_ttl:
            print(f'    ✗ STALE    {label} — {age}d old (TTL {ttl}d): {newest.name}')
            stale += 1
        elif verbose:
            print(f'    ✓ fresh    {label} ({age}d old)')
    if stale:
        print(f'    ⚠  {stale} artifact(s) expired — refresh before trusting any read that touches them.')
    else:
        print('    ✓ all tracked intelligence fresh')
    return stale


# ─────────────────────────── CRYPTO PULSE ───────────────────────────

CRYPTO_SYMBOLS = [('BTC-USD', 'BTC'), ('ETH-USD', 'ETH')]

def crypto_pulse():
    print('  ₿  CRYPTO PULSE (Stream B / 24-7 field)')
    try:
        import yfinance as yf
    except ImportError:
        print('    ✗ yfinance not available')
        return
    for ticker, name in CRYPTO_SYMBOLS:
        try:
            h = yf.Ticker(ticker).history(period='1y', interval='1d')
            if h.empty:
                print(f'    ✗ {name}: no data')
                continue
            close = h['Close']
            px = close.iloc[-1]
            chg = (px / close.iloc[-2] - 1) * 100 if len(close) > 1 else 0.0
            ma50 = close.rolling(50).mean().iloc[-1]
            ma200 = close.rolling(200).mean().iloc[-1]
            above50, above200 = px > ma50, px > ma200
            regime = ('BULL (above 50d + 200d)' if above50 and above200 else
                      'BEAR (below 50d + 200d)' if not above50 and not above200 else
                      'TRANSITION (between MAs)')
            hi52 = close.max()
            from_hi = (px / hi52 - 1) * 100
            print(f'    {name}: ${px:,.0f}  {chg:+.1f}%d  |  {regime}  |  {from_hi:+.1f}% vs 52w high'
                  + ('  ← ATH ZONE (Playbook B territory)' if from_hi > -3 else ''))
        except Exception as e:
            print(f'    ✗ {name}: {e}')
    print('    Law: BTC is the base; alt deployment stays D.R.D-gated (use case + team + tokenomics + PROBABLE+).')


# ─────────────────────────── FORGE STREAK ───────────────────────────

def _log_pulse_today():
    QUANT.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    lines = STREAK.read_text().splitlines() if STREAK.exists() else []
    if today not in lines:
        lines.append(today)
        STREAK.write_text('\n'.join(lines) + '\n')


def _streak_count():
    if not STREAK.exists():
        return 0, 0
    days = {l.strip() for l in STREAK.read_text().splitlines() if l.strip()}
    streak, d = 0, date.today()
    # walk backward over market days (weekdays)
    while True:
        if d.weekday() >= 5:
            d -= timedelta(days=1)
            continue
        if d.isoformat() in days:
            streak += 1
            d -= timedelta(days=1)
        else:
            break
    return streak, len(days)


def show_streak(after_log=False):
    streak, total = _streak_count()
    bar = '█' * min(streak, 20) + '░' * max(0, 20 - streak)
    print(f'  🔥 FORGE GATE — consecutive market-day pulse streak: {streak}/20  [{bar}]  (total pulses: {total})')
    if streak >= 20:
        print('     ✓ FORGE GATE CONDITION MET — pair with live expectancy ledger to pass Phase 1.5.')
    elif after_log:
        print('     The streak IS the system. Same time tomorrow.')


# ─────────────────────────── PULSE ───────────────────────────

def pulse(extra):
    fast = '--fast' in extra
    today = date.today()
    print('─' * 78)
    print(f'  STIS PULSE — {today} ({today.strftime("%A")})  |  PRD v6 §12  |  mode: {"FAST" if fast else "FULL"}')
    print('─' * 78)

    # 1. Freshness
    ttl_check(verbose=False)
    print()

    # 2. Time Architecture
    try:
        import time_architecture
        print(time_architecture.render(today))
    except Exception as e:
        print(f'  ✗ time architecture failed: {e}')
    print()

    # 3. Crypto
    crypto_pulse()
    print()

    # 4. GEX all symbols (saved to quant/) — skip in fast mode / weekends
    if not fast and today.weekday() < 5:
        print('  📊 GEX ENGINE — all symbols, saving session maps to quant/')
        run(TOOLS['gex'], ['--all', '--save'])
    else:
        print('  📊 GEX skipped (fast mode / weekend) — run `stis.py gex --all --save` when market data is live.')
    print()

    # 5. PMIB one-liner
    print('  🧭 PMIB BRIEF')
    run(TOOLS['report'], ['--brief'] + [a for a in extra if a != '--fast'])
    print()

    # 6. Streak
    _log_pulse_today()
    show_streak(after_log=True)
    print('─' * 78)
    print('  Observer check: is the Observer present? If not — no charts today. The pulse still counted.')
    print('─' * 78)


# ─────────────────────────── MAIN ───────────────────────────

HELP = """
  STIS — Sovereign Trading Intelligence System (PRD v6)
  ─────────────────────────────────────────────────────
  pulse     THE DAILY 5-MINUTE PULSE — run every market day (Forge gate)
            --fast  skip GEX fetch (offline/weekend)
  brief     alias for pulse
  report    Full P.M.I.B (all layers)
  flows     Time Architecture calendar (--week for 7 days, --date YYYY-MM-DD)
  crypto    BTC/ETH regime pulse only
  ttl       Intelligence freshness check only
  streak    Forge gate streak status
  gex       GEX engine pass-through (--symbol SPY --save / --all --save / --pine)
  ds        Declination System — today
  aspects   Aspect Scanner — intraday triggers
  kp        Schumann Proxy — live Kp + solar wind
  iec       IEC Cycle Scanner — 10 instruments
  all       Legacy: ds + aspects + kp + iec sequentially
"""


def main():
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help', 'help'):
        print(HELP)
        return

    command, extra = args[0], args[1:]

    if command in ('pulse', 'brief'):
        pulse(extra)
    elif command == 'flows':
        import time_architecture
        d = date.today()
        if '--date' in extra:
            d = datetime.strptime(extra[extra.index('--date') + 1], '%Y-%m-%d').date()
        if '--week' in extra:
            for i in range(7):
                print(time_architecture.render(d + timedelta(days=i)))
                print()
        else:
            print(time_architecture.render(d))
    elif command == 'crypto':
        crypto_pulse()
    elif command == 'ttl':
        ttl_check(verbose=True)
    elif command == 'streak':
        show_streak()
    elif command == 'all':
        for name in ALL_ORDER:
            filtered = [a for a in extra if not (a == '--timeframe' and name != 'iec')]
            run(TOOLS[name], filtered)
    elif command in TOOLS:
        run(TOOLS[command], extra)
    else:
        print(f'  Unknown command: {command}')
        print(f'  Available: pulse, brief, flows, crypto, ttl, streak, {", ".join(TOOLS.keys())}, all')
        sys.exit(1)


if __name__ == '__main__':
    main()

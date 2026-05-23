#!/usr/bin/env python3
"""
PANDORA — STIS UNIFIED LAUNCHER
Single entry point for the Sovereign Trading Intelligence System tool stack.

Commands:
  brief     — One-line status summary (Kp / DS / Aspects / Grade)
  report    — Full Pre-Market Intelligence Brief (P.M.I.B)
  ds        — Declination System reading (today)
  aspects   — Aspect scanner (today)
  kp        — Schumann Resonance proxy (live Kp / solar wind)
  iec       — IEC Cycle Scanner (all 10 instruments)
  all       — Run everything sequentially

Usage:
  python3 stis.py brief
  python3 stis.py report --location london
  python3 stis.py iec --timeframe 1wk
  python3 stis.py all
"""

import sys
import subprocess
from pathlib import Path

ROOT     = Path(__file__).parent
DS_DIR   = ROOT / 'declination-system'
IEC_DIR  = ROOT / 'iec-scanner'

TOOLS = {
    'brief':   [sys.executable, str(DS_DIR / 'pmib.py'), '--brief'],
    'report':  [sys.executable, str(DS_DIR / 'pmib.py')],
    'ds':      [sys.executable, str(DS_DIR / 'declination_system.py'), '--today'],
    'aspects': [sys.executable, str(DS_DIR / 'aspect_scanner.py')],
    'kp':      [sys.executable, str(DS_DIR / 'schumann_resonance.py')],
    'iec':     [sys.executable, str(IEC_DIR / 'iec_scanner.py')],
}

ALL_ORDER = ['brief', 'ds', 'aspects', 'kp', 'iec']

HELP = """
  STIS — Sovereign Trading Intelligence System
  ─────────────────────────────────────────────
  brief     One-line status: Kp / DS / Aspects / Grade
  report    Full P.M.I.B (all layers, ~15 seconds)
  ds        Declination System — today's reading
  aspects   Aspect Scanner — intraday triggers
  kp        Schumann Proxy — live Kp + solar wind
  iec       IEC Cycle Scanner — 10 instruments
  all       Run ds + aspects + kp + iec sequentially

  Pass-through flags (append after command):
    --location [new_york|london|chicago|tokyo]
    --orb 1.5          (aspect orb in degrees)
    --timeframe 1wk    (iec only: 1d|1wk|1h)
    --json             (machine-readable output)

  Examples:
    python3 stis.py brief
    python3 stis.py report --location london
    python3 stis.py iec --timeframe 1wk --json
    python3 stis.py all
"""


def run(cmd: list, extra_args: list):
    subprocess.run(cmd + extra_args)


def main():
    args = sys.argv[1:]
    if not args or args[0] in ('-h', '--help', 'help'):
        print(HELP)
        return

    command   = args[0]
    extra     = args[1:]

    if command == 'all':
        for name in ALL_ORDER:
            cmd = TOOLS[name]
            # Don't pass timeframe to non-iec tools
            filtered = [a for a in extra if not (a == '--timeframe' and name != 'iec')]
            run(cmd, filtered)
        return

    if command not in TOOLS:
        print(f'  Unknown command: {command}')
        print(f'  Available: {", ".join(TOOLS.keys())}, all')
        sys.exit(1)

    run(TOOLS[command], extra)


if __name__ == '__main__':
    main()

# WF STAGE 2 — DAILY SESSION
## D.TRD — Trading | Pre-market through trade log

**Trigger:** Any live or practice trading session, once Stage 1 (setup) is complete.

## STAGE CONTRACT

1. Load `skills/skill_support-resistance-reading.md` — the active strategy logic.
2. Read the current chart/data provided for the symbol(s) in scope.
3. Identify key support/resistance levels per the strategy (prior swing highs/lows, value area high/low, POC, liquidity pools).
4. Determine market structure context (trending vs. ranging; testing support vs. resistance).
5. If a setup meets the strategy's entry criteria: state the trade plan (entry, stop, target, size) sized against `_config/trd_config_tiki-profile.md` risk rules.
6. **Confirm with Tiki before executing or recommending execution of any live trade.**
7. Log the outcome (taken or passed, and why) in `logs/trd_log_trades_[YYYY-MM].md` — every session produces a log entry, even a no-trade day.

**Exit condition:** Trade logged (or explicitly logged as no-trade), ref card Current State updated if anything changed.

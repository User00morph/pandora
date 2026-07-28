# WF STAGE 2 — DAILY SESSION
## D.TRD — Trading | Pre-market through trade log

**Trigger:** Any live or practice trading session, once Stage 1 (setup) is complete.

## OPERATING CADENCE (source: Tiki's own weekly routine, `FXIFY Trading/FXIFY-200K-Gold-GJ-MASTER-PLAN.md`)

**Sunday (prep, 30–45 min) — run once, before the trading week:**
1. Pull the week's high-impact USD/GBP/JPY calendar events (Fed, BoE, BoJ, NFP, CPI, UoM) — flag day + time for each.
2. Mark the week's range edges (one support zone, one resistance zone) on Gold's 1H/4H and on GBP/JPY. These are the only trade areas for the week.
3. Note any BoJ/MoF/intervention risk on the calendar for GJ.
4. Check the FXIFY dashboard: last closing balance → today's 3% daily room and current drawdown room.
5. Write one bias line per pair (bull/bear/range) as a hypothesis to test, not an order.

**Monday–Friday (each session, run this Stage 2 contract):**
1. Load `skills/skill_support-resistance-reading.md` — the active strategy logic.
2. Read the current chart/data provided for the symbol(s) in scope. Confirm no high-impact event in the next 2 hours.
3. Identify key support/resistance levels per the strategy (prior swing highs/lows, value area high/low, POC, liquidity pools) and set alerts at the week's edges — not standing orders. Let price come to the level.
4. Determine market structure context (trending vs. ranging; testing support vs. resistance).
5. When price reaches an edge: run the full Nawaf/KimG checklist in `frameworks/trd_framework_support-resistance-system_v1.md` §2 out loud before treating anything as A+.
6. If a setup meets every criterion: state the trade plan (entry, stop, target, size) sized against `_config/trd_config_tiki-profile.md` risk rules.
7. **Confirm with Tiki before executing or recommending execution of any live trade.**
8. After resolution: a win permits one more A+ if it sets up, then done. A loss closes the platform for the session — no exceptions.
9. Log the outcome (taken or passed, and why) in `logs/trd_log_trades_[YYYY-MM].md` — every session produces a log entry, even a no-trade day. Grade the day against the three KPI boxes in the framework's §6 (≤2 trades, never two open, no re-entry after a stop).

**Friday (weekly review, ~20 min) — run once, after the week's last session:**
1. Log the week's trades and EOD balance to `FXIFY Trading/FXIFY-Risk-Tracker.md`.
2. Score the week on the KPI boxes, not P&L — target 5 green days out of 5.
3. Note where the itch to break a rule showed up and what triggered it.
4. Reset — new week, clean slate, back to Sunday prep.

**Exit condition:** Trade logged (or explicitly logged as no-trade), ref card Current State updated if anything changed.

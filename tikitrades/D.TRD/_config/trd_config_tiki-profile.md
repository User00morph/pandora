# Tiki Trading Profile
## Fill in before any live trade — no live trade happens with blank fields below

**Source:** Extracted from `FXIFY Trading/` (Master Plan, Risk Tracker, Trade Journal, Weekly Plans) — this is Tiki's own verified trading history, not an assumption. Two fields below are flagged and still need her direct confirmation.

- **Capital allocated to trading:** FXIFY prop-firm evaluations, two accounts:
  - **200K One-Phase — Account #1849940 — LIVE, currently trading.** Initial balance $200,000. High-Water Mark $201,178.33. Balance as of 2026-07-24: $194,746.06.
  - **100K — purchased, not yet started.** No rows logged.
  - Prop-firm rules apply, not personal-account rules: **daily loss limit 3% of previous day's closing balance**, **max drawdown 6% trailing below HWM** ($12,000 on the 200K). Breach = account lost, not just a bad day.
- **Broker / platform:** FXIFY (prop firm) via **DXtrade**.
- **Asset class:** Forex/commodity CFDs — **exactly two instruments, on purpose: XAU/USD (Gold) and GBP/JPY.** Not a general forex system — correlated-risk pair, sized and ruled specifically for these two.
- **Timeframe / hours available to trade:** **CONFIRMED — London + NY session overlap.** Highest-volume window for both instruments; covers the majority of the A+ setups described in the framework. Sessions outside this window are not this profile's trading hours — do not surface Asia-only setups as actionable.
- **Risk per trade (max % of capital on one position):**
  - **CONFIRMED — standard size: Gold 0.33 lots (~$33/point), GBP/JPY 2.00 lots (~$12.34/pip).** This is a $ risk of roughly **0.25–0.51% per trade** depending on stop distance (15–30pt gold, 40–80pip GJ) — verified against 10 days of actual fills, and confirmed as the real rule going forward (2026-07-26).
  - The "Risk % per Trade: 2.0%" figure previously listed in `FXIFY-Risk-Tracker.md`'s config table was stale/wrong — corrected there to match this (see that file).
  - **Hard cap, not a target:** gold stop > 30pt → cut size or skip. GJ stop > 80pip → cut size or skip. Never scale size up "to make it back."
- **Experience level:** Not a clean beginner/intermediate/experienced label in the source files — evidenced instead:
  - **Mechanically competent:** correctly executing $200K funded evaluation, understands lot sizing, partials, breakeven stops, R-multiples.
  - **Documented behavioral leak, recurring across at least 3 sessions (Jul 15/16/17):** revenge re-entries seconds after a stop, and averaging into a position via two simultaneous same-direction trades. Per the account's own 10-day stats: 42 trades, 35.7% win rate, **profit factor 0.66 as executed** (loses ~34¢ per $1 risked) — despite the underlying setup logic testing out fine on the A+ days (e.g., Jul 23: +$3,147, one trade, textbook).
  - **Working label: intermediate execution, undisciplined under losses.** The strategy refinement below is written to protect against that specific failure mode, not to teach basic chart reading.
- **Non-negotiables / things to avoid:** (proven costly, in her own trade history — not generic risk-management advice)
  1. **One open position at a time. Ever.** Never two on the same instrument, never gold + GJ together (correlated).
  2. **Max 2 trades per day.** Two losses = flat, laptop closed, no matter how good the next setup looks.
  3. **After ANY loss, done for the session.** No re-entry. (This single rule turns a −$432 day into the whole day, per the Jul 17 post-mortem.)
  4. **Every position gets a stop attached at entry. No exceptions.** The single worst loss in the record (Jul 16, −$932) was 71% caused by one naked position with no stop.
  5. **Limit orders only fill the plan.** If price passes the level before the order is in, the trade no longer exists — no market chases.
  6. **No position into event risk or live intervention chatter**, especially GJ (BoJ/MoF spikes can gap past a stop).
  7. **Daily journal entry against these rules before the platform closes** — grade the behavior, not the P&L.

*Last updated: 2026-07-26 — filled from FXIFY Trading source files; both previously-flagged items (hours, risk-per-trade) confirmed directly by Tiki same day. Profile complete.*

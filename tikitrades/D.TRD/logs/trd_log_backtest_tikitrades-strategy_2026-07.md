# TikiTrades Strategy — Backtest Log

Source script: `indicators/trd_script_tikitrades-strategy_v1.pine`
Symbol: OANDA:XAUUSD · Platform: TradingView Strategy Tester · Basic plan (chart-loaded-bars only, no Deep Backtesting)

## 4H — 2023-01-02 to 2026-07-28 (full available history)

| Metric | Value |
|---|---|
| Total trades | 25 |
| Win rate | 40.00% (10 winners / 15 losers) |
| Profit factor | 1.461 |
| Avg win | +2.96% |
| Avg loss | −1.23% |
| Avg PnL/trade | $479.93 (0.66%) |
| Max drawdown | 7.20% of initial capital |
| Current drawdown | 6.00% |

**Read:** Profit factor and win-rate shape (low hit-rate, asymmetric win size) closely track KimG's own documented session stats in `fxify-200k-gold-gj-trading-plan.md` (~33% win rate, PF 1.27, avg win ≈1.9× avg loss). The mechanical grading system is reproducing the same edge shape the discretionary version was built from — a meaningful sanity check, not proof of forward performance.

## 15m and 5m — inconclusive (data ceiling, not a strategy flaw)

TradingView's Basic plan only backtests over bars already loaded on the chart; "Deep Backtesting" (arbitrary date range on any resolution) requires Premium. OANDA's intraday feed on this plan retains:
- 15m: ~3 months (testing period capped at "Apr 30, 2026 — Jul 28, 2026")
- 5m: ~1 month (capped at "Jun 28, 2026 — Jul 28, 2026")

Zero A/B-grade signals landed in either window — with sample sizes this small that's not a meaningful negative result either way. Do not conclude the strategy fails on faster timeframes from this; it's simply unmeasured. Re-run once more calendar time has accumulated, or upgrade to Premium for a proper 15m/5m historical sample.

## Bug found and fixed during this test

Initial version guarded entries with `stopBuy < close` / `stopSell > close` (skip trade if stop landed on the wrong side) — this caused a runtime "invalid qty" crash on bar 3133 the first run. Fix: removed the guard, switched qty calc to `riskPerTrade / math.abs(...)` so a stale/wrong-side swing-point stop can't produce a crashing negative quantity. Confirmed clean compile and real trades registering after the fix (see 4H results above).

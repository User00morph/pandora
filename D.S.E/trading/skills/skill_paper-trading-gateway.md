# SKILL — PAPER TRADING GATEWAY
**The Formal Protocol for Graduating a Strategy to Live Capital**
**Load when:** A backtested strategy has passed walk-forward validation and is being considered for live deployment.
**Department:** D.S.E trading workspace | STIS Strategy Lifecycle | Capital deployment gate

---

## WHAT THIS IS

The formal gate between paper trading and real capital. No strategy touches live money until it passes this protocol. The risk management agent (or Morph directly) controls this gate with single veto authority.

---

## THE GRADUATION CRITERIA

A strategy must meet ALL of the following in the paper trading period before any capital is deployed:

```
METRIC                          MINIMUM THRESHOLD
─────────────────────────────────────────────────
Sharpe Ratio                    ≥ 1.0
Win Rate                        ≥ 40% (or positive expectancy confirmed)
Maximum Drawdown                ≤ 20% of paper account
Number of trades (paper)        ≥ 30 (minimum statistical sample)
Paper trading duration          ≥ 4 weeks (must include varied conditions)
Expectancy per trade            Positive (calculated, not estimated)
Performance vs. backtest        Live performance within 30% of backtest
```

If ANY metric fails → strategy returns to paper trading. Not negotiable.

---

## THE GRADUATED DEPLOYMENT SEQUENCE

```
STAGE 1 — PAPER TRADING
  All criteria pass → advance to Stage 2

STAGE 2 — MICRO LIVE (5% of intended capital)
  Run 4 weeks → metrics sustained → advance to Stage 3

STAGE 3 — PARTIAL LIVE (25% of intended capital)
  Run 4 weeks → metrics sustained → advance to Stage 4

STAGE 4 — FULL DEPLOYMENT (100% of intended capital)
  Ongoing monitoring → retire if edge decays
```

Each stage requires sustained performance before advancing. Failures at any stage → return to paper trading, not to the previous stage.

---

## THE RECOVERY RATE METRIC

Before promoting any strategy from paper trading to live, calculate the **recovery rate**: how many days does the strategy historically take to recover from its maximum drawdown?

```
RECOVERY RATE = Days to recover from max drawdown (historical average)
  Fast recovery (< 90 days):   Acceptable
  Moderate recovery (90-180):  Acceptable with monitoring
  Slow recovery (180-365+):    Requires conviction — understand WHY before deploying

EXAMPLE from the 27-bot portfolio:
  Some bots had 4+ months of consecutive losses BEFORE new highs
  Traders who exited during that period missed the recovery entirely
  The recovery rate told them upfront: "this is a slow-recovery strategy"
```

**The recovery rate must be disclosed to yourself before deploying any strategy.** If the historical recovery is 6 months and you cannot psychologically hold for 6 months → do not deploy this strategy regardless of expected returns.

---

## THE "SCENT TEST"

The minimum viability signal: if a strategy can make even a consistent cent in paper trading with healthy metrics — it is a candidate. The bar is consistency, not magnitude. Magnitude comes from capital sizing. The strategy's job is to prove the edge exists. Capital is Morph's job to provide.

---

## EDGE DECAY MONITORING (live deployment)

After going live, check these monthly:

```
□ Rolling 30-trade expectancy trending toward zero?
□ Win rate declining below backtest floor?
□ Drawdown approaching the maximum threshold?
□ Market regime has shifted (regime-change-detection.md)?
```

Any red flag → reduce size. Two red flags → suspend strategy. Three → retire.

---

## RULES

- No live capital before all graduation criteria are met — no exceptions
- The risk management agent or Morph must explicitly approve each stage advancement
- Paper trading with small live capital ($100 test) is not a substitute for proper paper trading
- A strategy that fails the graduation criteria is not a failed strategy — it needs more development

*D.S.E trading workspace | STIS Strategy Lifecycle | Source: Travis Woo Zero Human Trading Firm video*

# SKILL — STRATEGY LIFECYCLE MANAGEMENT
**Every Strategy as a Tracked Initiative with Explicit Stage Gates**
**Load when:** Managing the trading strategy portfolio, reviewing the backtest queue, conducting strategy audits.
**Department:** D.S.E + D.I.I | STIS Strategy Portfolio

---

## WHAT THIS IS

Every strategy is an initiative with a formal lifecycle. Nothing is informal. Everything is tracked — what was tried, what passed, what failed, why, and what was learned. "You want to make sure your entire system is tracking from the outset."

---

## THE LIFECYCLE STAGES

```
IDEA GENERATED
  Source identified, hypothesis documented, added to queue
        ↓
BACKTEST QUEUE
  Waiting for backtest agent to process
        ↓
BACKTEST IN PROGRESS
  Walk-forward validation running
        ↓
BACKTEST COMPLETE
  Pass → advance to Red Team
  Fail → archive with failure analysis
        ↓
RED TEAM REVIEW
  Adversarial stress test
  Pass → advance to Paper Trading
  Fail → return to development or archive
        ↓
PAPER TRADING
  Live paper trade for 4+ weeks
  Pass gateway criteria → advance to live
  Fail → return to development
        ↓
LIVE — MICRO (5% capital)
  Monitor 4 weeks → advance to partial
        ↓
LIVE — PARTIAL (25% capital)
  Monitor 4 weeks → advance to full
        ↓
LIVE — FULL DEPLOYMENT
  Ongoing edge monitoring
        ↓
RETIRED
  Edge decayed, market changed, or better strategy found
```

---

## THE MASTER STRATEGY LOG FORMAT

Every strategy gets an entry:

```
ID:              STR-[number]
Name:            [descriptive name]
Source:          [where the idea originated]
Hypothesis:      [what edge is being tested, in one sentence]
Asset class:     [what it was designed for]
Status:          [current stage]
Backtest:        Sharpe [X] | Win rate [X%] | Max DD [X%] | Expectancy [X]R
Walk-forward:    [pass/fail/in progress] | Date: [YYYY-MM-DD]
Paper result:    [if applicable] | Duration: [N weeks]
Live result:     [if applicable] | Capital: [stage]
Notes:           [any important observations]
Retired:         [reason, if applicable]
```

---

## EDGE DECAY DETECTION

Monthly check for all live strategies:

```
□ Rolling 30-trade expectancy trending toward zero?
□ Win rate declining below the backtest floor?
□ Drawdown in the last 30 trades exceeding historical average?
□ Market regime has shifted (run regime-change-detection.md)?
□ Strategy was only designed for a regime that no longer exists?
```

Two red flags → reduce to micro size.
Three red flags → suspend and re-evaluate.
Four red flags → retire.

---

## THE RECOVERY RATE FIELD

Every strategy in the master log must include its **recovery rate** — the historical average number of days to recover from the maximum drawdown.

```
MASTER STRATEGY LOG — ADDITIONAL FIELD:
  Recovery rate:   [N days from max drawdown to new high]
  
WHAT THIS TELLS YOU:
  Recovery < 60 days:  Fast — likely a higher-frequency strategy with small edge
  Recovery 60-180:     Medium — typical for swing strategies
  Recovery 180-365:    Slow — requires strong conviction and patience
  Recovery > 365:      Very slow — only viable with genuine long-term edge

BEFORE DEPLOYING: Ask "Can I psychologically hold through [N] days of drawdown?"
                  If NO → do not deploy regardless of expected return
```

This one field prevents the most common systematic trading failure: deploying a strategy, experiencing its normal drawdown, quitting during the drawdown, and missing the recovery. The recovery rate sets the expectation in advance.

---

## THE REALISTIC FUNNEL

Based on real systematic trading operations:
- 100 ideas generated → ~30 pass backtest → ~10 pass red team → ~5 pass paper trading → 1-3 viable live strategies

**This ratio is correct and healthy.** A 3% live success rate from raw ideas is not failure — it is the cost of finding genuine edges.

---

## RULES

- Every strategy has a lifecycle record from day 1 — nothing is informal
- Retired strategies are kept in the archive (failures contain valuable information)
- The lifecycle is sequential — no stage can be skipped, regardless of time pressure

*D.S.E + D.I.I | STIS Strategy Portfolio | Source: Travis Woo Zero Human Trading Firm video*

# SKILL — PERIOD RETURN DISTRIBUTION ANALYSIS
**Reading System Performance Across All Timeframe Granularities**
**Load when:** Evaluating a system's performance, setting investor expectations, or deciding whether to continue a system during a losing period.
**Department:** D.S.E trading workspace | STIS System Evaluation | Performance analysis

---

## WHAT THIS IS

Most traders evaluate systems at the wrong timeframe — judging a multi-year trend-following system by daily P&L. This skill provides the correct multi-timeframe performance picture and the benchmarks for each level.

---

## THE PERFORMANCE LADDER

| Timeframe | Healthy benchmark | What it means |
|---|---|---|
| Winning days | 48-52% | Normal. Losing almost half your days is expected. |
| Winning weeks | 54-56% | Slightly better than chance. Compounding begins. |
| Winning months | 56-58% | The trend-following edge starts showing. |
| Winning quarters | 56-60% | Stable outperformance. |
| Winning years | 70-77% | Strong systematic edge. |
| Winning decades | 100% | The ultimate robustness proof. |

Note: win percentages don't add up to 100% because the system doesn't trade every single period.

---

## THE PARADOX

A system losing 52% of days can have a 77% winning year rate. How?

**The average winning year (+47%) >> the average losing year (-12%)**

Over a distribution of days, the few big winning sequences dwarf the many small losing days. The system feels like it's failing daily but succeeds annually. This is mathematically correct and expected.

---

## THE PSYCHOLOGICAL CALIBRATION

Set your evaluation timeframe BEFORE deploying capital:

```
"I will evaluate this system on YEARLY performance.
 I will NOT react to daily, weekly, or monthly results.
 A losing month in a winning year is NORMAL.
 A losing year in a winning decade is NORMAL."
```

Write this into the trade log on deployment day. Return to it whenever a losing streak triggers doubt.

---

## THE DECADE FRAME

100% winning decades = the system has NEVER lost money over any 10-year period in its historical test.

Use this when facing a losing year: "I am inside a decade. The decade has a 100% win rate. This losing year is one data point inside a 10-year sequence that has always been positive."

---

## THE MTP LIVE DATA (7-asset portfolio, 1965-present)

```
Winning days:     ~34%  (losing days: ~29% | rest = flat/no trade)
Winning weeks:    majority > 50%
Winning months:   46% (avg winning month: +8%, avg losing: -5%)
Winning quarters: majority
Winning years:    73-77%
Winning decades:  100% (avg decade: 10× or ~900% return)
```

The day-level numbers look alarming. The decade-level numbers look extraordinary. **These describe the SAME system.** The correct evaluation timeframe is YEARS, not days.

---

## THE 10× DECADE PROOF

At standard sizing (around 500 equity risk): 100k → 1M in 10 years → 10M in 20 years.
At aggressive sizing (higher leverage): 100k → 5M in 10 years → 250M in 20 years.

Both require holding through max drawdowns of 45-78%. The difference between these two outcomes is entirely determined by the leverage calibration.

---

## APPLYING TO THE STIS SYSTEM

After any backtest run, extract and record:
```
□ % winning days
□ % winning weeks
□ % winning months
□ % winning quarters
□ % winning years (must be ≥ 70%)
□ % winning decades (must be 100%)
□ Average winning year magnitude
□ Average losing year magnitude
□ Ratio of avg win year to avg loss year (must be > 2:1)
```

*D.S.E/trading/skills | STIS System Evaluation | Source: Travis Woo MTP Backtesting video*

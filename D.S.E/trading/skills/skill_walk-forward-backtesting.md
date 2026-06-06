# SKILL — WALK-FORWARD BACKTESTING
**The Only Valid Backtesting Methodology for Adaptive Systems**
**Load when:** Validating any trading strategy before deploying capital.
**Department:** D.S.E trading workspace | STIS System Validation

---

## WHAT THIS IS

Walk-forward backtesting is the standard that separates a genuine edge from overfitting. Standard backtesting is invalid for adaptive systems. This protocol eliminates the most common backtesting failure mode: future data contamination.

---

## THE PROBLEM WITH STANDARD BACKTESTING

Standard backtest: apply strategy to all historical data → optimize → test.

**The flaw:** The strategy has already seen 2020 by the time you test 2020. It already "knows" the future outcome. A strategy trained on 2015-2025 data has 2020 embedded in its parameters. Testing it on 2020 is not an out-of-sample test — it is a circular test.

"The strategy has learnt from all the data applied to the past and it just doesn't work."

---

## THE WALK-FORWARD PROTOCOL

```
For each day D in history (starting from minimum lookback period):

  1. Gather ALL data from inception → day D-1 only
  2. Calculate the strategy parameters using only that data
  3. Generate the signal for day D
  4. Record the signal and actual outcome
  5. Advance to day D+1
  6. Repeat — NEVER look forward

Result: A signal history where every prediction used only past information
```

**The discipline:** No future data EVER enters a calculation. If the strategy uses a 20-day moving average for day 100, it uses days 80-99 — not days 101-119.

---

## THE LAG RULE (for all rolling features)

Any feature computed from rolling/historical data must use LAGGED values:

```
CORRECT:   Rolling average of returns t-1, t-2, ..., t-N
WRONG:     Rolling average including the current period t

Current period return is unknown at prediction time.
Using it = data leakage = invalid backtest.
```

---

## THE VALIDATION STANDARD

A strategy passes walk-forward validation when:

```
□ Walk-forward in-sample performance ≈ out-of-sample performance
  (large divergence = overfitting)
□ Strategy validated on 3+ uncorrelated asset classes
□ Strategy validated across 50+ years of data (if available)
□ 100+ trade sample in the walk-forward period
□ Performance holds in at least one major bear market period
```

---

## THE DECADE-LEVEL STANDARD (highest robustness bar)

Walk-forward validation across rolling 10-year blocks produces a decade-level performance record. The gold standard:

```
100% of tested decades = positive → structural edge, not regime-specific
Any decade = negative → edge may be regime-dependent → add regime filter
```

The MTP system achieved 100% winning decades across 60+ years of data on 7 asset classes. This is the benchmark to reach before considering any strategy fully validated.

---

## RULES

- NEVER shuffle time-series data when splitting train/test
- The walk-forward is computationally heavy — use AI automation (Claude Code)
- A strategy that passes standard backtesting but fails walk-forward has no edge
- Walk-forward is the prerequisite before paper trading; paper trading is the prerequisite before live
- The decade-level pass rate is the final robustness check — aim for 100% winning decades

*D.S.E/trading/skills | STIS System Validation | Source: Travis Woo Quant Strategy video + Regime Changes video + MTP Backtesting video*

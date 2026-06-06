# SKILL — OPTIMIZATION METRIC SELECTION
**Choosing the Right Objective for System Optimization**
**Load when:** Setting up any backtest optimization run or evaluating which metric to target.
**Department:** D.S.E trading workspace | STIS System Design | Optimization layer

---

## WHAT THIS IS

The optimization metric determines what the backtest algorithm is trying to maximize. Different metrics produce different systems — choosing the wrong one optimizes for the wrong objective. This decision happens before running a single trial.

---

## THE THREE METRICS

### SHARPE RATIO
**What it maximizes:** Return divided by total volatility (up and down).
**What it penalizes:** ANY variance — including upside variance.
**Best for:** Regular withdrawals, institutional mandates, anyone who needs a predictable smooth equity curve.
**Drawback:** Penalizes winning streaks. Will produce a "smoother" system that may miss big wins.

### SORTINO RATIO
**What it maximizes:** Return divided by DOWNSIDE volatility only.
**What it penalizes:** Only drawdowns and losing periods — not upside variance.
**Better than Sharpe for:** Trend-following systems where upside can be large and lumpy.
**Drawback:** Still doesn't directly optimize for the maximum return possible.

### KALMAR RATIO
**What it maximizes:** Total return divided by maximum drawdown.
**What it penalizes:** Only the worst drawdown event.
**Best for:** Investors who will hold through volatility and want maximum wealth creation.
**Travis's choice and the sovereign default:** "I just want to make the most possible money. I don't care about the path. Kalmar."

---

## THE DECISION FRAMEWORK

```
QUESTION: Will I need to withdraw from this account regularly?
  YES → Use Sharpe or Sortino (smooth equity curve protects withdrawals)
  NO  → Use Kalmar (maximize total wealth, accept lumpiness)

QUESTION: Will I panic during volatile upswings?
  YES → Use Sharpe (smoother ride reduces emotional interference)
  NO  → Use Kalmar (don't sacrifice returns for unnecessary smoothness)

QUESTION: Is this for institutional/external capital?
  YES → Use Sharpe (investors expect smooth Sharpe reporting)
  NO  → Use Kalmar (personal account, own rules)
```

---

## SOVEREIGN DEFAULT

For the STIS system: **Kalmar is the correct optimizer.** The Observer holds through drawdowns by design. There are no regular withdrawals during the growth phase. The objective is maximum long-run wealth creation. Sharpe smoothness is an unnecessary cost.

---

## RULES

- Set the optimization metric BEFORE running any trials — changing it mid-optimization invalidates the comparison
- The same system optimized for Sharpe vs. Kalmar will produce different parameter sets — they are not interchangeable
- When reporting performance to others, translate to Sharpe — most investors understand it. When optimizing for yourself — Kalmar.

*D.S.E/trading/skills | STIS System Design | Source: Travis Woo MTP Backtesting video*

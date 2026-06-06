# SKILL — PORTFOLIO CONCENTRATION MANAGEMENT
**Preventing Single-Asset Dominance in a Multi-Asset System**
**Load when:** Reviewing portfolio weights, running portfolio optimization, evaluating annual performance attribution.
**Department:** D.S.E trading workspace | STIS Portfolio Management | Risk distribution

---

## WHAT THIS IS

When one asset carries 80%+ of portfolio returns in a backtest, the system's apparent performance is an illusion — it's concentrated exposure dressed up as diversification. This skill identifies and corrects concentration before it causes a surprise losing year.

---

## THE FINDING

From MTP backtesting: the same system parameters, when run on the standard universe (S&P, Nasdaq, Gold, Silver, Bitcoin, Nikkei, European), produced dramatically different results depending on which asset dominated in a given test period:

- Test A: Gold carried 70%+ of the portfolio returns → "great performance"
- Test B: Bitcoin carried 80%+ → "even better performance"
- Test C: Portfolio balanced → lower average return BUT 77% winning years vs. ~65%

The balanced portfolio traded absolute return for consistency. **More winning years = more trust in the system = better adherence during losing periods.**

---

## THE DETECTION METHOD

After every backtest run, look at the equity contribution chart:

```
CHECK: Which asset contributed the most to total returns?
  If one asset > 50% of total portfolio gains → CONCENTRATION FLAG
  If one asset > 70% → SEVERE CONCENTRATION — rebalance weights
  If no single asset > 40% → HEALTHY DISTRIBUTION
```

---

## THE REBALANCING PROTOCOL

When a concentration flag is detected:

1. Reduce the overweighted asset's allocation by 20-30%
2. Redistribute weight to underperforming assets in the universe
3. Re-run optimization with new relative weights
4. Check: did the % winning years improve? Did max drawdown improve?
5. Accept the rebalanced weights if both improved, even if average return dropped slightly

---

## THE TRADEOFF TABLE

| Portfolio approach | Avg return | Winning years | What it means |
|---|---|---|---|
| Concentrated (best asset dominates) | Higher | ~65-70% | More volatile, harder to hold through bad periods |
| Balanced (no asset > 40%) | Moderate | ~75-80% | More consistent, easier to maintain conviction |

For a systematic investor who needs to STAY in the system through losing years: **winning years matter more than average returns.**

---

## THE ANNUAL ATTRIBUTION REVIEW

Every year, run a performance attribution analysis:
- Which asset contributed the most this year?
- Which asset detracted the most?
- Is the current real portfolio drifting toward concentration?
- If one position has grown disproportionately due to pyramiding → consider trimming to restore balance

---

## THE DRAWDOWN REDUCTION PROOF

From live backtesting data (MTP system, SPX only vs. SPX + Gold):

```
SPX ONLY:
  Max drawdown: -78%
  Average year: 35%
  Winning years: ~65%

SPX + GOLD (added one uncorrelated asset):
  Max drawdown: -45%  ← 33 percentage points LESS
  Average year: 30%   ← only 5 points less
  Winning years: 68%  ← improved

LESSON: Adding one uncorrelated asset reduced max drawdown by 33pp
        while reducing average returns by only 5pp.
        The risk-adjusted improvement is dramatic.
```

Every additional uncorrelated asset added to the portfolio reduces the correlation-driven drawdown while barely affecting expected returns. This is why the 7-asset STIS portfolio is structurally superior to a single-asset system.

---

## RULES

- No single asset should be expected to carry more than 50% of portfolio returns
- Concentration feels great until the concentrated asset has a bad year — then it wipes out years of "diversification"
- Rebalance portfolio weights annually in the optimization run, not based on recent performance
- When adding any new asset: verify it is genuinely uncorrelated to existing holdings — correlated assets add exposure, not diversification

*D.S.E/trading/skills | STIS Portfolio Management | Source: Travis Woo MTP Backtesting videos*

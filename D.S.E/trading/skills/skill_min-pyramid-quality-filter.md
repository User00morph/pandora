# SKILL — MIN PYRAMID QUALITY FILTER
**Using Breakout Sequence Requirements as an Asset Quality Gate**
**Load when:** Designing or adjusting strategy parameters for a broad asset universe.
**Department:** D.S.E trading workspace | STIS System Design | Signal quality

---

## WHAT THIS IS

The min pyramid parameter is a hidden quality filter. By requiring N consecutive breakouts before entering, the system automatically filters out low-quality assets that produce only occasional random breakouts — while still catching genuine trending assets that produce sustained multi-breakout sequences.

---

## THE LOGIC

```
ANY asset (even declining ones) can occasionally make a breakout
ONLY genuinely trending assets consistently make a SECOND breakout
ONLY the strongest trending assets make a THIRD breakout

Therefore:
  Min pyramid = 1 → take every breakout (including random noise)
  Min pyramid = 2 → skip the first, enter on the second (quality filter)
  Min pyramid = 3 → skip first two, enter on third (ultra-strict filter)
```

---

## THE TRADEOFF

| Min pyramid setting | Trade frequency | False signal rate | Best for |
|---|---|---|---|
| 1 (take all) | Highest | Highest | Highest-quality asset universe only |
| 2 (skip first) | Moderate | Reduced | Mixed-quality universe |
| 3 (skip first two) | Lowest | Lowest | Broad universe with weak assets |

---

## WHEN TO ACTIVATE

**Min pyramid = 1 (default):**
- Universe is pre-filtered to only the strongest assets
- All assets in the universe have demonstrated sustained trending behavior
- Example: STIS core universe (S&P 500, Gold, Bitcoin, Nikkei, Silver, NASDAQ, European)

**Min pyramid = 2:**
- Universe includes some assets with weaker trend characteristics
- Backtesting shows a lot of single-trade losses that don't develop into multi-leg winners
- Want to improve win rate at the cost of trade frequency

**Min pyramid = 3:**
- Universe is very broad (hundreds of assets)
- Many low-quality assets included for scanning purposes
- Filtering down to only the most sustained trend followers

---

## THE MTP FINDING

Walk-forward optimization showed: in some decades a min pyramid of 1 was optimal, in others 3 was optimal. The median across all decades: 2. This suggests that a min pyramid of 2 is the structurally robust choice for a diversified asset universe across all market regimes.

---

## RULES

- Min pyramid is a system parameter — set it at design time, not adjusted based on current market conditions
- Raising min pyramid during a losing streak is a form of curve-fitting — don't do it
- If the walk-forward shows different optimal values in different decades → pick the median

*D.S.E/trading/skills | STIS System Design | Source: Travis Woo MTP Backtesting video*

# SKILL — ASSET START DATE PROTOCOL
**When to Begin a Backtest Based on Market Structure History**
**Load when:** Setting up any new backtest, choosing the historical range for a new asset.
**Department:** D.S.E trading workspace | STIS System Validation | Data integrity

---

## WHAT THIS IS

Starting a backtest at the wrong date contaminates the data — including periods when the asset was not a free-market instrument. Using pre-liberalization data produces false results because the price mechanics were fundamentally different.

---

## THE RULE

Only include historical periods where the asset traded as a **free market instrument** with genuine supply-demand price discovery.

---

## ASSET START DATE REFERENCE

| Asset | Recommended start | Reason |
|---|---|---|
| Gold | 1968-1971 | Fixed to dollar at $35/oz until Nixon shock. Before 1971 = no free price movement. |
| S&P 500 | 1871 (available) | Free market throughout. Use all available data. |
| Silver | 1971 | Same as gold — Bretton Woods fix removed 1971. |
| NASDAQ | ~1971-1973 | Formed 1971. Sufficient data by mid-1970s. |
| Japanese Nikkei | ~1950 (available) | Post-WWII reconstruction period creates early distortions. 1965+ is cleaner. |
| Bitcoin | 2011-2012 | 2009-2010 had near-zero liquidity. Meaningful price discovery begins ~2011. |
| Euro (EUR/USD) | 1999 | Euro launched January 1, 1999. Before that — synthetic data only. |
| Portfolio (mixed) | 1965 | Travis's choice: gold becomes meaningful by 1965, and this captures all major regimes |

---

## THE GENERAL PRINCIPLE

```
1. Identify when the asset became freely tradeable
2. Identify when meaningful liquidity existed (early data may be illiquid)
3. Identify any artificial price controls or pegs in the asset's history
4. Set the start date AFTER all of the above are resolved
```

---

## WHAT HAPPENS IF YOU START TOO EARLY

- Gold 1930-1965 data: price barely moves (fixed) → system shows perfect low-volatility performance → completely false
- Bitcoin 2009-2010 data: prices spike from pennies to dollars → massive outlier returns that will never repeat → overstates performance
- Any asset before meaningful liquidity: bid-ask spreads were enormous → backtested profits would be eaten alive by real execution costs

---

## THE PORTFOLIO BACKTEST DEFAULT

For a multi-asset portfolio including gold and silver: **start in 1965.**

This captures:
- All post-WWII market regimes
- The inflationary 1970s (critical stress test)
- All major crashes and recoveries
- Enough of each asset's free-market history to be meaningful

---

## RULES

- Document the chosen start date and the reason in the strategy log
- If unsure, err toward starting LATER — cleaner data beats more data
- Never include data where the price mechanism was fundamentally different from today

*D.S.E/trading/skills | STIS System Validation | Source: Travis Woo MTP Backtesting video*

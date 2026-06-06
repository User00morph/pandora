# SKILL — COMPOUNDING MODE SELECTION
**Fixed Units vs. Percentage of Equity — When to Use Each**
**Load when:** Setting up a live account, choosing backtest settings, or reviewing performance accounting.
**Department:** D.S.E trading workspace | STIS Position Sizing | Compounding mechanics

---

## WHAT THIS IS

Two fundamentally different ways to size positions — fixed units and percentage of equity — produce completely different account growth curves. The choice determines whether the account grows linearly or exponentially. Confusing the two in a backtest produces misleading performance data.

---

## THE TWO MODES

### FIXED UNITS (Constant Contract Count)
```
Definition:    Always trade the same number of contracts regardless of account size
Growth curve:  LINEAR — adding the same dollar P&L each period
Example:       Always trade 1 MES contract
               Account grows from $25k → $30k → $35k (adding ~$5k/period)
               NOT compounding
```

**Best for:** Understanding the raw edge of the strategy (how many dollars per contract per period). Comparing strategy versions. Understanding slippage and cost at a given position size.

**Misleads on:** Long-term performance projections. Makes the system look weaker than it actually is over time.

### PERCENTAGE OF EQUITY (Proportional Sizing)
```
Definition:    Risk a fixed % of current account on every trade
Growth curve:  EXPONENTIAL — each period's gains reinvested
Example:       Always risk 2% of account
               Account grows from $25k → $30k → $36k → $43.2k (compounding)
```

**Best for:** Long-term wealth projection. Understanding what happens to real account value over years/decades.

**Misleads on:** Early-stage performance when account is small (the compounding advantage is minimal until the account reaches a meaningful size).

---

## THE KEY CONFUSION TO AVOID

A backtest showing "from 2015 to 2025, account grew to $1M" may be running percentage-of-equity mode. The LIVE account using fixed units may only show $250k growth in the same period. Neither is wrong — they're different questions being answered.

**Always specify in every backtest report:** which compounding mode was used.

---

## PRACTICAL IMPLEMENTATION

For LIVE trading:
- **Growth phase** (account under $100k): percentage of equity — every dollar of profit immediately increases the next position's size
- **Withdrawal phase** (regularly withdrawing): fixed units or percentage of smaller "trading capital" separated from "withdrawal reserve"

For BACKTESTING:
- Run both modes on every system — compare the two curves
- Fixed units tells you the edge quality
- Percentage of equity tells you the wealth creation potential

---

## THE COMPOUNDING THRESHOLD

The account size at which compounding becomes visually meaningful:

```
$10k account: 1% = $100/trade — feels trivial
$50k account: 1% = $500/trade — starting to matter
$100k account: 1% = $1,000/trade — meaningful
$500k account: 1% = $5,000/trade — highly impactful

The compounding effect is always there mathematically,
but it becomes psychologically motivating above ~$100k.
```

*D.S.E/trading/skills | STIS Position Sizing | Source: Travis Woo MTP Backtesting video*

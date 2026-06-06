# SKILL — ATR STOP ARCHITECTURE
**Building Stops Proportional to Market Volatility**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Any time a stop loss level needs to be calculated for a new or existing position
DEPARTMENT: D.S.E | STIS Risk Management | Stop placement
LOADS:      None required — this is a calculation skill
PRODUCES:   Stop loss price level + dollar risk per contract
CROSS-REF:  skill_daily-risk-budget.md (uses stop distance to calculate position size)
            skill_stop-advancement-signal.md (uses same ATR method when advancing)
            skill_position-management-protocol.md (uses this output for stage management)
            skill_conservative-stop-philosophy.md (why wide stops work)
```

---

## WHAT THIS IS

ATR-based stops are proportional to what the market is actually doing — not to a fixed dollar amount or arbitrary pip distance. When volatility is high, the stop widens automatically. When volatility is low, it tightens. This prevents being stopped out by normal market noise while still limiting catastrophic losses.

---

## INPUT

```
REQUIRED:
  - Current price (entry price)
  - ATR look-back period (default: 10 days)
  - ATR multiplier (default: 5)
  - Direction of trade (long or short)

OPTIONAL:
  - Nearest structural level (for sanity check — stop should not be inside a structure)
  - Session ATR (intraday) vs. daily ATR (swing)
```

---

## THE CALCULATION

```
STEP 1 — CALCULATE ATR
  ATR = Average of True Ranges over last N days (default N = 10)
  True Range = MAX of:
    (High - Low)
    (|High - Previous Close|)
    (|Low - Previous Close|)
  
  ATR = sum of True Ranges for N periods / N
  
  Example: 10-day ATR on EUR/USD = 0.0045 (45 pips)

STEP 2 — APPLY MULTIPLIER
  Stop distance = ATR × multiplier
  Default multiplier = 5
  
  Example: 0.0045 × 5 = 0.0225 (225 pips)

STEP 3 — PLACE THE STOP
  LONG trade:  stop = entry price - stop distance
  SHORT trade: stop = entry price + stop distance
  
  Example LONG: entry 1.0850 - 0.0225 = 1.0625

STEP 4 — SANITY CHECK
  Is the stop below (long) or above (short) a meaningful structural level?
  YES → stop is clean, use as calculated
  NO  → the structure is too close; either:
        (a) adjust to just beyond the structural level, or
        (b) skip this trade (risk too large for the structure)
```

---

## THE MULTIPLIER CALIBRATION TABLE

| Multiplier | Stop type | Use when |
|---|---|---|
| 3× | Tight | Low volatility regime, mean-reverting environment |
| 5× | Standard | Default for all instruments |
| 7× | Wide | High volatility regime, trending environment |
| 10× | Very wide | Systematic long-term trend positions |

---

## POSITION SIZE FROM STOP DISTANCE

```
POSITION SIZE FORMULA:
  Max dollar risk = daily budget × risk fraction
  Dollar risk per contract = stop distance (pips) × dollar per pip
  Contracts = max dollar risk ÷ dollar risk per contract

EXAMPLE:
  Daily budget remaining: $200
  Risk fraction: 50% = $100
  Stop distance: 225 pips
  Dollar per pip (EUR/USD mini): $1.00
  Dollar per contract: 225 × $1.00 = $225
  
  Contracts = $100 ÷ $225 = 0.44 → round DOWN to 0 contracts
  → Trade too large for current budget at this stop distance
  → Either wait for larger budget or find a setup with tighter stop
```

---

## RULES

- Never manually tighten a stop below the ATR calculation — this guarantees getting stopped out by noise
- When ATR expands (volatility spike) → position size reduces automatically — this is correct behavior
- The stop distance is calculated ONCE at entry — not recalculated daily (until a stop advancement trigger fires)
- If the ATR-calculated stop requires more capital than the daily budget allows → skip the trade

*D.S.E/trading/skills | STIS Risk Management | ATR Stop Calculation*

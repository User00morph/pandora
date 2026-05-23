# SKILL — RISK MANAGEMENT
**Layer 1 Skill | D.S.E/trading/skills/**
**Skill File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: dse_framework_risk-management.md, STIS PRD v3 §13**
**Run: BEFORE every trade entry — non-negotiable**

---

## PURPOSE

This skill provides the step-by-step calculation and verification protocol for every trade before entry. The position sizing formula is the only acceptable basis for size. No other method is valid. If the formula cannot be calculated, the trade cannot be entered.

The skill executes in 3 minutes once internalized. There is no valid reason to skip it.

---

## THE POSITION SIZING CALCULATOR

### Formula

```
POSITION SIZE (lots) = (Account Equity × Risk%) ÷ (Stop Distance in pips × Pip Value per lot)
```

### Variables to establish before every trade:

```
ACCOUNT EQUITY: $_______________
  → Current account value. NOT the starting balance. The CURRENT value.
  → Update before every session. Do not use yesterday's number.

RISK PERCENTAGE: ___% (default: 1%. Maximum: 2%. Never more.)
  → CONVERGENCE ADJUSTMENT:
     Dual-layer convergence score 8-10: 1.5-2% risk
     Dual-layer convergence score 6-7: 0.75-1% risk
     High-impact event week (NFP/FOMC): maximum 0.5% risk
     Mercury retrograde or eclipse within 6 weeks: maximum 0.75% risk

STOP DISTANCE: _____ pips
  → The distance between entry and stop level, in pips
  → Must be a STRUCTURAL stop (see placement section below)
  → NEVER calculated as a round number of pips — calculated from the level where the hypothesis is invalidated

PIP VALUE:
  → USD pairs (EUR/USD, GBP/USD, AUD/USD, NZD/USD): $10 per pip per standard lot
  → JPY pairs (USD/JPY, EUR/JPY): $9.18 per pip per standard lot at current rate (recalculate when rate shifts significantly)
  → XAU/USD (Gold): $1 per pip per standard lot (where 1 pip = $0.01 in gold price)
     Note: Gold is often traded in smaller lot sizes — confirm with broker
  → Confirm pip value with broker platform before trading any new instrument
```

### Worked Examples:

**Example 1 — EUR/USD long:**
```
Account equity: $10,000
Risk: 1% → $100 risk
Entry: 1.0850
Stop: 1.0820 → 30 pips distance
Pip value: $10 per pip per lot

Position size = $100 ÷ (30 × $10) = $100 ÷ $300 = 0.33 lots (3 mini lots or 33 micro lots)
```

**Example 2 — Gold (XAU/USD) long:**
```
Account equity: $10,000
Risk: 1.5% (convergence score: 9) → $150 risk
Entry: $4,380
Stop: $4,330 → 50 pip / $50 distance
Pip value: $1 per pip per 0.01 lot (verify with broker)
Broker standard: 1 lot gold = 100 oz. Each $1 move = $100 per lot.

Position size = $150 ÷ ($50 × $100) = $150 ÷ $5,000 = 0.03 lots
```

**Example 3 — USD/JPY short:**
```
Account equity: $10,000
Risk: 0.75% (FOMC week, reduced size) → $75 risk
Entry: 155.30
Stop: 155.80 → 50 pip distance
Pip value: $9.18 per pip per lot at ~155

Position size = $75 ÷ (50 × $9.18) = $75 ÷ $459 = 0.163 lots ≈ 0.16 lots
```

---

## STOP PLACEMENT PROTOCOL

### Valid Stop Methods (from `dse_framework_risk-management.md`)

**METHOD 1 — STRUCTURAL STOP (primary method)**
```
The stop is placed BEYOND the level where the hypothesis is invalidated.

For a LONG at an OB zone:
  Stop = below the BOTTOM of the OB zone (not at the midpoint — BELOW it)
  + 3-5 pip buffer to account for spread and minor manipulation
  
For a SHORT at a Breaker zone:
  Stop = above the TOP of the Breaker zone + 3-5 pip buffer
  
For a LONG after a liquidity sweep:
  Stop = below the lowest wick of the sweep candle (not the body — the actual wick)
  
For any trade with a defined CHoCH as the invalidation:
  Stop = beyond the CHoCH level (if price closes beyond the CHoCH, the structure is broken)
```

**METHOD 2 — OB/FVG EXTREMITY STOP**
```
When entering at an OB or FVG zone:
  Stop = below the FULL OB zone (not just the entry point within the zone)
  The entire OB is the valid zone — if price exits the entire zone, the setup is invalid
  
This is often a wider stop — compensate by using a smaller position size to maintain 1% risk
DO NOT tighten the stop to maintain position size. Tighten position size to accommodate the stop.
```

**METHOD 3 — ATR STOP (for ranging markets)**
```
Stop = 1.5 × ATR(14) beyond the entry level
ATR(14) = the 14-period Average True Range — available on any charting platform
This method is for range-bound sessions where structural levels are less clean
Not the primary method — use structural stops whenever possible
```

### Stop Placement Violations (NEVER do these)
```
✗ NEVER place a stop at a round number "because it's a clean level"
  → Round numbers are targets, not stops — they are where the Cardinal Cross will sweep
  
✗ NEVER move a stop AWAY from the entry to "give it more room"
  → If the stop must be moved to be structurally valid, recalculate position size. Do not move stop.
  
✗ NEVER set a stop based on "how much I'm comfortable losing"
  → The stop is set by structure. The position size is adjusted to make the structural stop equal to 1% risk.
  
✗ NEVER move a stop to break-even before price has reached 1:1 reward
  → Moving to break-even too early = letting the market knock you out of valid trades at no profit
  → Move to break-even only after price reaches 1:1 reward (and only if market conditions support)
```

---

## TARGET DETERMINATION PROTOCOL

### Valid Target Identification

```
TARGET HIERARCHY (use in order — first valid target = initial take profit):

1. The next unfilled FVG in the trade direction (the nearest imbalance above/below)
2. The nearest liquidity pool (equal highs/lows, previous day high/low)
3. The previous week's high or low
4. A significant round number (but only if structural — not just proximity)
5. An OB zone on a higher timeframe

MINIMUM TARGET: 2:1 risk-reward ratio required
  → If the nearest valid target is less than 2:1, the setup does not meet minimum requirements
  → Either wait for a better entry (closer to the OB) or skip the trade

PREFERRED TARGET: 3:1 or higher
```

### Partial Profit Protocol

For trades with 3:1+ potential:
```
50% of position: close at 2:1 (the first target level)
25% of position: close at 3:1 (the second target level)  
25% of position: trail stop behind structure, let run to 4-5:1 or until stopped out

After the 50% partial:
→ Move stop to break-even on the remaining 50%
→ Now the trade is "risk-free" on the remaining portion
→ The trailing stop follows the most recent swing low (for longs) or swing high (for shorts)
   — specifically: trail behind the MOST RECENT 4H or 1H swing low/high
   — not behind every minor candle low/high (too tight) — the swing structure
```

---

## DAILY AND ACCOUNT-LEVEL RISK CONTROLS

### Daily Loss Limit
```
MAXIMUM DAILY LOSS: 3% of account equity

If this limit is reached:
→ STOP TRADING for the day
→ This is non-negotiable. No exceptions.
→ Log: "Daily loss limit reached. Session complete."
→ Run the post-trade Observer Calibration Protocol
→ The next session begins from the same stable foundation

EXAMPLES:
$10,000 account: Daily loss limit = $300
$20,000 account: Daily loss limit = $600
$5,000 account: Daily loss limit = $150
```

### Drawdown Thresholds
```
5% drawdown (account down 5% from peak):
→ REVIEW: Is the Ray read correct? Is the cycle phase assessment right?
→ Reduce position sizes to 50% of standard until a profitable week restores confidence

10% drawdown (account down 10% from peak):
→ PAUSE: Stop trading. Take 3-5 days off from the market.
→ Complete a full Esoteric Reading and re-assess the macro cycle
→ Return with 25% of standard position size

20% drawdown (account down 20% from peak):
→ FULL AUDIT: A fundamental error in the framework or its application is occurring
→ 2-week minimum pause from all trading
→ Review every trade against the framework criteria
→ Identify the systematic error before returning
→ Return only if the error is identified and corrected — at 10% of standard position size
```

---

## PRE-TRADE RISK CHECKLIST

Run before EVERY trade entry. No exceptions.

```
□ 1. ACCOUNT EQUITY confirmed: $_______________
□ 2. RISK PERCENTAGE determined (standard/adjusted): ___%
□ 3. RISK AMOUNT calculated: $_______________
□ 4. STOP LEVEL identified (structural): _______________ 
     Reasoning: [why this is the structural invalidation level]
□ 5. STOP DISTANCE calculated: _____ pips
□ 6. PIP VALUE confirmed for this instrument: $_____/pip/lot
□ 7. POSITION SIZE calculated: _____ lots
□ 8. R:R ratio confirmed: ___:1 (must be ≥ 2:1 to proceed)
□ 9. TARGET LEVELS identified: 
     T1 (50% close): _______________ at ___:1
     T2 (25% close): _______________ at ___:1
     T3 (trail remainder): structure-following stop
□ 10. DAILY LOSS CHECK: Would this trade, if lost, exceed the daily limit? [ ] No → proceed | [ ] Yes → STOP

ALL 10 CHECKED? 
→ Yes: proceed to entry
→ No: DO NOT enter until all 10 are answered
```

---

## THE R-MULTIPLE TRACKER

Track every trade in R-multiples (how many R were won or lost):

```
TRADE DATE: _______________
PAIR: _______________
DIRECTION: LONG / SHORT
ENTRY: _______________
STOP: _______________ | Stop distance: _____ pips | Risk: $_____ (___% of account)
TARGET 1: _______________ | T1 R: ___:1
TARGET 2: _______________ | T2 R: ___:1

OUTCOME:
T1 hit: [ ] Yes at _____ | [ ] No
T2 hit: [ ] Yes at _____ | [ ] No
T3 trail exit: _____ at ___:1

FINAL R: _____ R (positive = win, negative = loss)
DOLLAR P&L: $_______________
```

**Running statistics (update every 10 trades):**
```
Total trades: _____ | Wins: _____ | Losses: _____
Win rate: ___%
Average win (R): _____ | Average loss (R): _____
Expectancy per trade: (Win rate × Avg win) - (Loss rate × Avg loss) = _____ R
```

Expectancy target: ≥ 0.5R per trade (meaning the system is profitable in expectancy)

---

## CROSS-REFERENCES
- `dse_framework_risk-management.md` — the framework this skill operationalizes
- `skill_dual-layer-chart-reading.md` — convergence score determines the risk % input
- `skill_trade-execution.md` (pending) — how to physically enter the trade after sizing is complete
- `logs/dse_log_trading_YYYY-MM.md` — where trade records and R-multiples are logged

---

*skill_risk-management.md | D.S.E/trading/skills/ | STIS Layer 1 Operational Skill*
*Status: v1.0 — active | Non-negotiable. No trade is entered without completing this skill.*

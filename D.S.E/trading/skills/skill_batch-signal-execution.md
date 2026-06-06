# SKILL — BATCH SIGNAL EXECUTION
**When Multiple Assets Signal on the Same Day**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Two or more systematic signals have fired on the same trading day
DEPARTMENT: D.S.E | STIS Execution Layer | Batch operations
LOADS:      skill_daily-risk-budget.md (portfolio risk check)
            skill_uncorrelated-position-sizing.md (correlation check)
            skill_atr-stop-architecture.md (stop calculation per signal)
PRODUCES:   Execution queue with position sizes + stops + total portfolio risk
CROSS-REF:  skill_5-minute-trading-ritual.md (the ritual that catches batch signals)
            skill_pre-trade-checklist.md (per-signal quality gate)
```

---

## WHAT THIS IS

When the systematic approach is working correctly, multiple signals can fire on the same day — different assets independently meeting the new-high criteria. This is not an anomaly; it often indicates a broad macro move. This protocol handles batch execution efficiently and safely.

---

## INPUT

```
REQUIRED:
  - List of all signals that fired today (instrument + direction + entry price)
  - Current portfolio positions and their current risk
  - Today's remaining daily risk budget
  - Correlation assessment: are these assets related?

OPTIONAL:
  - Macro context (risk-on/risk-off) to confirm batch direction makes sense
```

---

## THE BATCH EXECUTION PROTOCOL

### STEP 1 — ASSESS THE BATCH

```
List all signals:
  Signal 1: [instrument] [long/short] at [price]
  Signal 2: [instrument] [long/short] at [price]
  Signal N: [instrument] [long/short] at [price]

Are they all in the same direction?
  ALL LONG:   broad risk-on move — execute all, verify macro alignment
  ALL SHORT:  broad risk-off move — execute all, verify macro alignment
  MIXED:      uncorrelated signals — execute all, more diversified
```

---

### STEP 2 — CALCULATE TOTAL PORTFOLIO RISK

```
For each signal:
  Stop distance = ATR × 5
  Dollar risk = stop distance × dollar per pip × contracts
  
Sum all dollar risks = Total new risk being added today

Check: existing open positions' total risk + new total risk ≤ 30% of account
  PASS: proceed with all signals
  FAIL: reduce contracts on each signal proportionally until under 30%
```

---

### STEP 3 — CORRELATION CHECK

```
For each pair of signals: are they correlated assets?

CORRELATED PAIRS (count as doubled risk):
  S&P 500 + NASDAQ (correlation > 0.85)
  EUR/USD + GBP/USD (correlation > 0.80)
  Bitcoin + Ethereum (correlation > 0.75)

UNCORRELATED PAIRS (full separate allocation):
  S&P 500 + Gold
  Bitcoin + Nikkei
  EUR/USD + Gold

If two correlated signals fire:
  → Combined risk = both positions risk × 1.5 (not × 1.0)
  → Reduce one position size proportionally
```

---

### STEP 4 — EXECUTE IN ORDER

```
Execution sequence (most important first):
  1. Instruments with strongest Markov signal (highest directional differential)
  2. Instruments with strongest GEX alignment
  3. Instruments at most significant level confluence

Execution action (per instrument):
  □ Place market order at signal price
  □ Immediately place stop loss at ATR-calculated level
  □ Note the entry in the trade log
  □ Move to next instrument
  
Target time: < 2 minutes per instrument
Total batch: < 10 minutes for 4-5 signals
```

---

## OUTPUT FORMAT

```
BATCH EXECUTION — [DATE]
SIGNALS FIRED: [N]

EXECUTION QUEUE:
  [Instrument 1]: [direction] | Entry: [price] | Stop: [price] | Risk: $[X] | Contracts: [N]
  [Instrument 2]: [direction] | Entry: [price] | Stop: [price] | Risk: $[X] | Contracts: [N]
  [Instrument N]: [direction] | Entry: [price] | Stop: [price] | Risk: $[X] | Contracts: [N]

PORTFOLIO CHECK:
  Existing open risk:  $[X]
  New signals risk:    $[X]
  Total risk:          $[X] ([X%] of account)
  Within 30% limit:    [YES / NO — adjusted if needed]

CORRELATION NOTES: [any adjustments made]
ALL ORDERS PLACED:  [YES / timestamp]
```

---

## RULES

- Execute ALL valid signals — never curate based on which "feels" right
- If total risk would exceed 30% of account → reduce proportionally across all, not just some
- Correlated assets require combined risk assessment
- The batch takes under 10 minutes — if it's taking longer, something is wrong

*D.S.E/trading/skills | STIS Execution Layer | Batch Signal Operations*

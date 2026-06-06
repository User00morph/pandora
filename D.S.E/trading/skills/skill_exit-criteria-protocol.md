# SKILL — EXIT CRITERIA PROTOCOL
**Pre-Defining All Exit Conditions Before a Position Reaches Emotional Significance**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  At trade entry — define exits BEFORE the position grows large
DEPARTMENT: D.S.E | STIS Execution Layer | Exit architecture
LOADS:      skill_atr-stop-architecture.md (for stop calculation)
PRODUCES:   Complete exit plan: stop level, target levels, thesis invalidation events,
            funding/carry thresholds, and time-based review triggers
CROSS-REF:  skill_position-management-protocol.md (manages the position after entry)
            skill_stop-advancement-signal.md (when to move the stop)
            skill_euphoria-exit-protocol.md (the only discretionary override)
```

---

## WHAT THIS IS

Exit criteria must be defined on entry day — not when the position is large and emotions are high. A $2.7M position where exits are still being "figured out" is a recipe for panic-driven decisions. This protocol forces all exit decisions into a calm, pre-market environment.

---

## INPUT

```
REQUIRED:
  - Entry price and direction
  - The edge thesis (WHY this position exists)
  - Current GEX level stack and Markov signal
  - Stop distance calculation (ATR method)
  
OPTIONAL:
  - Funding rate (for crypto perpetual positions)
  - Open interest / market cap ratio (for leverage flush risk assessment)
```

---

## THE FIVE EXIT TRIGGERS (define ALL before entry)

### TRIGGER 1 — STOP LOSS HIT (always defined)
```
The non-negotiable exit. Systematic. Automatic.

Stop price: [calculated via ATR method]
Dollar risk: [stop distance × dollar per point × contracts]
Action: Position closes automatically → log the -1.0 R → move on
```

---

### TRIGGER 2 — FUNDAMENTAL INVALIDATION (immediate exit)
```
Define: what specific fact(s) would make this trade thesis wrong?

Examples:
  - "Exit immediately if M2 growth turns negative for 2 consecutive months"
  - "Exit if daily transfer volume on TRX drops below $15B for 3 days"
  - "Exit if GEX regime flips from positive to negative gamma while in a fade trade"

Write it out: "I will exit immediately if: [specific condition]"
This exit is executed without waiting for a stop to be hit.
```

---

### TRIGGER 3 — SIGNAL-BASED EXIT (systematic)
```
The stop has advanced to protect profit. Define where it sits:

Current stop price: [X] — this is the floor on profit
When this stop is hit: position closes → take the realized profit → re-evaluate

Note: never widen this stop. It only moves up (for longs) or down (for shorts).
```

---

### TRIGGER 4 — CARRY COST THRESHOLD (for funded positions)
```
For perpetual futures and margin positions:

Current funding rate: [X%/day or annualized]
Daily carry cost: position size × daily rate
Monthly carry cost: [calculated]

"If funding rate exceeds [X% annualized], the carry cost makes this position
 economically untenable regardless of direction. Exit at that level."

This prevents "hoping it comes back" when carrying costs are bleeding the account.
```

---

### TRIGGER 5 — EUPHORIA OVERRIDE (rare, discretionary)
```
See skill_euphoria-exit-protocol.md for full conditions.
Summary: Only valid when BOTH of these are true:
  □ Position has moved 10-20× initial stop distance
  □ All-time high territory + mass public awareness (everyone talking about it)

If these conditions arise: partial exit only, not full close.
```

---

## THE EXIT CRITERIA LOG ENTRY (fill out at entry)

```
POSITION:          [instrument] | [long/short] | [N contracts]
ENTRY:             [price] | [date]

EXIT PLAN:
  Stop loss:       [price] | Dollar risk: $[X]
  Fundamental inv: [specific condition that invalidates thesis]
  Carry threshold: [funding rate level that triggers exit] (if applicable)
  Euphoria watch:  [current 10× distance target = price X.XXXX]
  
THESIS STATEMENT: "I am in this position because [specific reason].
                   This trade is over when [specific condition changes]."
```

---

## RULES

- All 5 triggers must be reviewed and relevant ones filled in BEFORE the position is opened
- A trade without a defined fundamental invalidation is a directional bet, not a thesis trade
- The exit criteria log lives in the position journal — review it every 2 weeks for open positions
- Triggers 1-4 are non-discretionary — they execute when the condition fires, regardless of current direction

*D.S.E/trading/skills | STIS Execution Layer | Exit Architecture*

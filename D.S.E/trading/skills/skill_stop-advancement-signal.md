# SKILL — STOP ADVANCEMENT SIGNAL
**When and How to Advance Stop Losses on Winning Positions**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  A position is in profit and price has just made a new structural high
            OR a new systematic buy signal has fired on an existing position
DEPARTMENT: D.S.E | STIS Execution Layer | Position management
LOADS:      skill_pyramiding-protocol.md (if also adding contracts)
            skill_atr-stop-architecture.md (for recalculating stop distance)
PRODUCES:   New stop level for all existing contracts + optional new contract add decision
CROSS-REF:  skill_asymmetric-return-design.md (why we don't use take profits)
            skill_position-management-protocol.md (full management framework)
            skill_pyramiding-protocol.md (the add-contract process)
```

---

## WHAT THIS IS

The stop advancement signal is the ONLY mechanism for moving a stop in a winning position. Stops move in ONE direction only — toward the entry price (to protect profit). They move ONLY when price makes a new structural high. Never on time, never on feeling, never to "lock in more profit."

---

## INPUT

```
REQUIRED:
  - Current position: entry price, number of contracts, current stop level
  - Signal trigger: what new structural high or system signal fired?
  - ATR value at the new high (for recalculating stop distance)
  - Account equity (for verifying new position sizing if adding)

OPTIONAL:
  - GEX level at or near the new high (for stop placement reference)
  - Markov signal strength (for confidence in adding)
```

---

## THE PROTOCOL

### STEP 1 — CONFIRM THE TRIGGER

A stop advancement is ONLY valid when ONE of these fires:
```
TRIGGER A: Systematic signal fires a new buy at a new structural high
           (MTP/STIS indicator: price made new N-day high → system signals)
           
TRIGGER B: Price has closed above a significant structural high
           (new weekly high, new monthly high, price above major resistance)
           
TRIGGER C: Price has moved 3× the initial stop distance from entry
           (the trade is significantly in profit, stop has lagged behind)
```

If NONE of these fired → do NOT advance the stop. Let it sit.

---

### STEP 2 — CALCULATE THE NEW STOP LEVEL

```
METHOD A (ATR-based, preferred):
  New stop = Current price - (ATR × multiplier)
  Where: ATR = 5-10 day average true range
         Multiplier = your system's ATR multiple (typically 5)
  
  Example: Price = 1.0950, ATR = 0.0030, Multiplier = 5
  New stop = 1.0950 - (0.0030 × 5) = 1.0950 - 0.0150 = 1.0800

METHOD B (Structural, alternative):
  New stop = just below the most recent structural low
           = below the last significant swing low before the new high
```

---

### STEP 3 — ADVANCE ALL CONTRACTS TOGETHER

When advancing: ALL open contracts in this position advance to the SAME new stop level simultaneously. Not some contracts. Not the newest contract. ALL of them.

```
BEFORE: 5 contracts, stop at 1.0700
AFTER:  5 contracts, stop at 1.0800 (new structural stop)
```

The pyramid positions lock in profit together. The entire position is now protected at the new level.

---

### STEP 4 — DECIDE ON NEW CONTRACT ADD

If TRIGGER A fired (systematic new buy signal) AND the account has sufficient margin:
→ Add a new contract at the new signal price (see `skill_pyramiding-protocol.md`)

If TRIGGER B or C fired (structural advancement only):
→ No new contract — this is a stop move only

---

## OUTPUT FORMAT

```
STOP ADVANCEMENT — [DATE] [INSTRUMENT]
TRIGGER:          [A/B/C — describe]
OLD STOP:         [price]
NEW STOP:         [price]
ALL CONTRACTS:    [N contracts] → new stop [price]
PROFIT LOCKED:    [entry avg] → new stop = [+X pips locked]
NEW CONTRACT ADD: [YES — at [price] / NO]
```

---

## RULES

- Stops ONLY move toward entry (never away from it)
- ALL contracts in the position advance together
- The stop advancement is NOT discretionary — it follows the trigger, not the feeling
- If the new stop calculation puts the stop below the current price → the trigger was premature, do not advance
- Never advance a stop "to take some profit" — that is what partial closes are for

*D.S.E/trading/skills | STIS Execution Layer | Stop Management*

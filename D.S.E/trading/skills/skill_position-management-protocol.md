# SKILL — POSITION MANAGEMENT PROTOCOL
**Active Position Management from Entry to Exit**
**Load when:** A position is open and requires management decisions.
**Department:** D.S.E trading workspace | STIS Execution Layer | Position management

---

## WHAT THIS IS

What you do AFTER entering is as important as the entry. Most losses come not from bad entries but from bad management — moved stops too early, exited too soon, held past the thesis invalidation. This protocol eliminates discretionary management errors.

---

## THE MANAGEMENT STAGES

### STAGE 1 — IMMEDIATELY AFTER ENTRY (first 5 minutes)
```
□ Stop loss placed in the platform (not just noted — placed)
□ First target (2R) identified on chart
□ Second target identified on chart
□ Alert set for: stop level, first target level, thesis invalidation level
□ Position size confirmed matches the pre-trade calculation
□ Close the chart — do not watch it tick by tick
```

---

### STAGE 2 — AT 50% OF FIRST TARGET
```
If price has moved 50% of the way to first target (1R in your favor):
  Option A: Do nothing — let the stop work
  Option B: Move stop to break-even (removes all dollar risk)
  
Sovereign default: Option B when GEX or Markov signal has WEAKENED
                   Option A when GEX and Markov signal remain STRONG
```

---

### STAGE 3 — FIRST TARGET HIT (2R)
```
□ Close 50% of the position (take the guaranteed win)
□ Move stop on remaining 50% to entry price (locked at break-even at worst)
□ Let second half run toward second target
□ Do not move stop again until a new structural high forms (pyramiding rule)
```

---

### STAGE 4 — THESIS INVALIDATION CHECK
These events override all other management rules — EXIT IMMEDIATELY:

```
INVALIDATION EVENTS:
  → GEX regime flips against the trade (price crosses HVL)
  → Markov signal reverses strongly (crosses -30% in opposite direction)
  → MSS (Market Structure Shift) label fires against the trade
  → Unexpected news event creates a gap against the trade
  → Stop loss is hit (exit = automatic, no discretion)
```

---

### STAGE 5 — SECOND TARGET ZONE
```
When price approaches the second target:
  □ Check: is GEX regime still intact?
  □ Check: is Markov signal still aligned?
  □ Check: is session still within the kill zone or productive period?
  
  If all YES → let price reach the level
  If any NO → close remaining position at market
```

---

## THE STOP-WIDENING PROHIBITION

**Never widen a stop after entry.** If the stop is hit, the thesis was wrong. Moving the stop is not risk management — it is hope trading. Every manually widened stop that becomes a larger loss was a teachable moment ignored.

The only valid stop movement direction: **toward the entry price** (to protect profit).

---

## THE POSITION JOURNAL ENTRY

After each position is closed:

```
ENTRY: [price] | STOP: [price] | TARGET 1: [price] | TARGET 2: [price]
EXIT: [price] | REASON: [T1 hit / T2 hit / Stop hit / Thesis invalidated]
R-MULTIPLE: [+X.XX R or -1.0 R]
MANAGEMENT GRADE: A (followed protocol) / B (minor deviation) / C (broke rules)
WHAT I LEARNED: [one sentence]
```

*D.S.E/trading/skills | STIS Execution Layer | Position Management*

# SKILL — Trade Management
**Everything that happens after entry: two-hour clock, ADR ceiling, exits, stop management**
**Load when:** A trade is open or an entry has been executed.

---

## WHAT THIS IS

Entry skill without exit skill = a ship with no rudder. Most accounts are damaged not by bad entries but by poor management of positions that start well — held too long through exhaustion, exited too early in fear, or never moved to breakeven. This skill governs everything after the trigger fires.

**Rule:** The entry decision and the management decision are separate. Do not confuse them.

---

## THE TWO-HOUR CLOCK

> "If a trade has not moved significantly within 2 hours of entry — exit. Mechanical override of attachment."

**What this means:**
- From the moment of entry, start a 2-hour timer
- If price has NOT moved at least 1:1 toward the TP target within 2 hours → close the trade
- This is a MECHANICAL rule — not a judgment call
- "Significantly" = at least 50% of the distance to the first TP target

**Why it exists:**
- An entry that doesn't move is an entry that was made at the wrong time or in the wrong phase
- Holding a stagnant position while the Two-Hour Clock runs is the definition of capital inefficiency
- The attachment to "it might still work" is a program signal (Justification — see Observer Gate)
- Most institutional moves complete in 2 hours from the expansion candle. If yours hasn't moved, it's likely not an institutional expansion.

**Two-Hour Clock Exception:** Strong news event within the 2-hour window that explains the stagnation → extend by 30 minutes max. Only once. This is not permission to hold indefinitely.

---

## ADR PROTOCOL — THE DAILY RANGE BUDGET

**ADR = Average Daily Range** — the average number of pips this instrument moves per day, measured over the last 14 days.

**The Rule:** If 80% or more of the ADR has already been consumed for the day → NO new entries.

```
ADR consumed = (Today's High - Today's Low) / ADR %

If ADR consumed ≥ 80% → No new entries. The range budget is spent.
If ADR consumed = 100% → Reverse watch mode — the range ceiling may be the Three-Hit level.
```

**Why:** Institutions operate within a daily range budget. Once that budget is approximately consumed, further movement requires the next session's mandate. Entering when ADR is nearly consumed means entering at exhaustion with no runway left.

**ADR as TP ceiling:**
- The ADR tells you the maximum likely target for any single-day trade
- Do not set a TP target beyond the ADR ceiling (except for multi-day swing setups)
- When price is within 20 pips of the ADR ceiling → begin managing the position (partial exit / tighten stop)

**Three Pushes into ADR Ceiling = exhaustion complete:**
- If price has made 3 pushes toward the ADR ceiling, each with declining momentum → close fully

---

## STOP MANAGEMENT

### Initial Stop Placement
- Stop must be placed BEYOND the swept level (above the wick for shorts, below the wick for longs)
- Stop is placed at a structural point — never at an arbitrary dollar amount
- Typical placement: 5-10 pips beyond the manipulation wick extreme

### Move to Breakeven
**When:** When price reaches a 1:1 risk-reward (has moved the same distance toward TP as the stop distance)
**How:** Move stop to entry price + 2-3 pips (not exactly entry — allow for spread)
**Why:** This makes the trade "free" — worst case is break-even, not a loss

**Rule:** Never move stop to breakeven too early (within the first 15-30 minutes). Allow the trade to breathe. Premature breakeven stop placement is fear management, not trade management.

### Trail the Stop (during expansion)
**When:** Price is in Phase 3 Expansion, moving cleanly in the direction
**How:** Trail stop to the low of the most recent swing (for longs) or high of the most recent swing (for shorts)
**Method:** After each new swing forms in the direction of the trade — move stop to just beyond that swing's opposite extreme
**When to STOP trailing:** When price shows a Three-Hit pattern at a key level, or ADR ceiling is near → lock in gains, switch to fixed stop

---

## EXIT PROTOCOL

### Primary TP: First Liquidity Pool
- The first significant equal highs/lows, PDH/PDL, or session extreme in the trade direction = Primary TP
- Set as a limit order at entry
- This should be at minimum 1:3 R:R from entry

### Partial Exit Protocol (for larger positions)
```
At 1:1 R:R   → Close 25% of position. Move stop to breakeven.
At 1:2 R:R   → Close another 25%. Trail stop to 1:1 level.
At TP target → Close remaining 50%. Or trail if expansion is strong.
```

**Why partial exits work:** Locks in profit mechanically. Removes the "take profit vs. let it run" dilemma. Remaining position runs for free after breakeven stop is in place.

### Scaling Out Rules
- Only scale out IF the position is at least 3x the minimum trade size
- Do not scale out if the initial position was already at minimum risk
- One TP target = one exit. Do not create multiple micro-exits that fragment the reward.

---

## THE FOUR EXIT SCENARIOS

### Scenario 1: Clean expansion to TP
Price moves directly from entry to TP without significant retracement.
**Action:** Let limit order execute at TP. No discretionary override.

### Scenario 2: Two-Hour Clock expires without TP
Price has not reached 1:1 after 2 hours.
**Action:** Close full position. Log as "stagnant — wrong timing." No exceptions.

### Scenario 3: ADR ceiling approach without TP
Price approaches 80% ADR without reaching TP.
**Action:** If TP is within 20 pips of ADR ceiling — let it run. If TP is beyond ADR ceiling — close at ADR ceiling.

### Scenario 4: Structure break against position
A BOS forms on the 15M or 1H AGAINST the trade direction.
**Action:** Close immediately. Structural break = the read was wrong. Do not hold hoping it recovers.

---

## WHAT NOT TO DO (program management)

These actions all look like "trade management" but are actually program signals:

| Action | What it is | What it sounds like |
|--------|-----------|---------------------|
| Moving TP further when price is near target | Greed program | "It's so close, it can go more" |
| Moving stop further when price is near it | Denial program | "Just give it a bit more room" |
| Closing early in profit (before 1:1) | Fear program | "I'll just take what I have" |
| Adding to a losing position | Revenge program | "If I average down it'll come back" |
| Re-entering immediately after being stopped out | Reactive program | "That was the real entry, this time for sure" |

**Rule:** If you are considering ANY action not covered by this skill's protocol — check the Observer Gate first.

---

## SESSION MANAGEMENT RULES

| Day | Management Rule |
|-----|----------------|
| Monday | No entries. Nothing to manage. |
| Tuesday | Maximum position size allowed. Manage aggressively after 1:1. |
| Wednesday-Thursday | Manage existing positions. New entries in expansion only. |
| Friday (Thursday EOD) | Close all positions by Thursday close. Friday = trap day. |

---

## TRADE LOG FORMAT

Every managed trade gets logged:

```
ENTRY: [Symbol] | [Direction] | [Entry price] | [Stop] | [TP] | [R:R] | [Size]
MANAGEMENT ACTIONS:
  [Time] → [Action taken] — [Reason]
  [Time] → [Action taken] — [Reason]
EXIT: [Price] | [Reason] | [Result: +Xpips / -Xpips] | [R multiple: +X.Xr]
LESSON: [One line — what this trade added to the framework]
```

Filed in: `~/Desktop/Pandora/D.S.E/trading/logs/YYYY-MM-DD_trade-log.md`

---

*D.S.E/trading/skills | Trade Management | Pandora OS*
*Entry is the beginning. Management is the discipline. Exit is the result. All three must be sovereign.*

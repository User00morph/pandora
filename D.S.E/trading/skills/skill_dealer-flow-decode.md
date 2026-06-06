# SKILL — DEALER FLOW DECODE
**Live Tape Reading Through the Dealer Mechanical Lens**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  During any live session when reading real-time price movement.
            Load alongside skill_gex-regime-read.md and skill_four-forces-dominance-read.md.
DEPARTMENT: D.S.E | STIS Layer 1b | Live session execution
LOADS:      skill_options-flow-foundation.md (foundational theory — load first)
            skill_gex-regime-read.md (GEX levels must be known)
PRODUCES:   Dealer action classification + tape read label + continuation/exhaustion signal
CROSS-REF:  skill_options-flow-foundation.md (the why behind every pattern)
            skill_four-forces-dominance-read.md (pre-session dominant force)
            skill_gamma-regime-mechanics.md (regime behavior)
            skill_delta-volume-decode.md (order flow confirmation)
            skill_grade-a-filter.md (dealer read as Grade A criteria)
```

---

## WHAT THIS IS

The live application of dealer mechanics to the tape in real time. While `skill_options-flow-foundation.md` explains WHY dealers create price movement, this skill tells you HOW to read that movement as it happens — identifying dealer hedging bursts, exhaustion, regime flips, and level behavior through the lens of mechanical necessity, not narrative.

Every real-time tape move is a dealer response. This skill teaches you to read whose hand is being forced, how far it needs to go, and when it is done.

---

## THE CORE PRINCIPLE

Dealers do not trade direction. They trade delta neutrality. Every price move you see on tape is a dealer either:

```
A — Hedging fresh exposure from new options trades
B — Re-hedging because price moved and their delta drifted
C — Unwinding a hedge because a position expired or was closed
```

Type A = sharp, directional, often triggers at levels
Type B = continuous, proportional to gamma — faster near GEX levels
Type C = reversal-like, price drifts back, often misread as "rejection"

---

## THE FOUR DEALER TAPE PATTERNS

### Pattern 1 — DEALER BURST
**What it looks like:** Fast, one-sided move through a level. High volume. Minimal wick.
**What it is:** Fresh options flow forcing immediate hedging. Someone bought a large directional position.
**Action:** Do not fade. Dealer hedging has mechanical continuation. Wait for the burst to exhaust before looking for re-entry.

```
TELL: Move begins suddenly, not from an obvious structural level
      Volume spike on the move
      Price does not return to the origin bar's close within 2-3 bars
```

---

### Pattern 2 — DEALER GRIND
**What it looks like:** Slow, grinding directional move. Consistent pressure. Small candles in one direction.
**What it is:** Continuous re-hedging as price drifts and delta exposure compounds (high gamma environment).
**Action:** Trade with the grind. Add when the grind resumes after a pause. Do not counter-trade.

```
TELL: Move is slow and relentless, not fast
      No sharp reversals — small corrective moves quickly reclaimed
      Occurs when price is near a GEX level (high gamma zone)
      Matches positive or negative gamma regime from GEX read
```

---

### Pattern 3 — DEALER EXHAUSTION
**What it looks like:** Rapid move followed by slowing velocity, widening spreads, volume decline.
**What it is:** Dealer hedging is complete. The mechanical forcing function is finished.
**Action:** Exhaustion is not a reversal signal by itself. Wait for structural confirmation before counter-trading.

```
TELL: Volume declining on the last push
      Price making new highs/lows but candles getting smaller
      Delta volume diverging (price up, delta not confirming)
      At or past a known GEX level
```

---

### Pattern 4 — DEALER FLIP
**What it looks like:** Sharp reversal after a clean directional move. Looks like a "stop hunt" in standard TA.
**What it is:** Dealer exposure has inverted. The dominant options flow shifted direction (hedgers became the other side).
**Action:** Treat as a regime signal. If the flip is confirmed by delta and volume, follow the new direction.

```
TELL: Sharp reversal that exceeds the prior corrective range
      Volume spike on the reversal bar
      Prior GEX level is reclaimed
      Occurs at a strong GEX wall (Put Wall or Call Wall)
```

---

## GEX LEVEL BEHAVIOR DECODER

Dealer hedging intensity increases exponentially near GEX levels. These are the behaviors at each level type:

| Level | Dealer Behavior | Tape Read |
|---|---|---|
| Max Gamma / HVL | Both sides hedging. Pinning force. | Chop. Mean-reverting bounces. No follow-through. |
| Call Wall | Dealer selling on approach. | Resistance. Sharp rejections. Multiple tests. |
| Put Wall | Dealer buying on approach. | Support. Bounces feel mechanical. Hard to break. |
| Volatility Trigger | Regime change zone. | Above = trending. Below = mean-reverting. Behavior changes at crossing. |
| GEX Zero Line | No dealer bias. Organic price. | Breakouts follow through. No pinning. |

**Rule:** The closer price is to a GEX level, the more dealer-mechanical the tape behavior. The further from all levels, the more the tape reflects actual directional sentiment.

---

## THE LIVE TAPE READING SEQUENCE

Run in order during any active session:

### STEP 1 — LOCATE PRICE RELATIVE TO GEX
```
Where is price vs. HVL?
  → Above HVL = trending regime (dealer grind expected in trend direction)
  → Below HVL = mean-reverting (expect dealer bursts to be faded)

Nearest GEX level?
  → Within 0.3% = high dealer mechanic influence
  → More than 0.5% from any level = lower dealer influence, more organic
```

### STEP 2 — CLASSIFY THE CURRENT MOVE
```
Is this a burst, grind, exhaustion, or flip?
Apply the four pattern definitions above.
```

### STEP 3 — CONFIRM WITH DELTA
```
Does delta volume confirm or diverge from the tape direction?
  → Confirms = mechanical move has buyer/seller support
  → Diverges = move is dealer-only, exhaustion likely imminent
```

### STEP 4 — LABEL THE TAPE
```
Produce one label before any trade decision:
TAPE: [BURST / GRIND / EXHAUSTION / FLIP / UNCLEAR]
DEALER DIRECTION: [long / short / neutral / pinning]
CONTINUATION PROBABILITY: [high / medium / low]
```

---

## OUTPUT FORMAT

```
─────────────────────────────────────────────
DEALER TAPE READ
─────────────────────────────────────────────
CURRENT PATTERN:     [Burst / Grind / Exhaustion / Flip / Unclear]
DEALER DIRECTION:    [Forced long / Forced short / Neutral / Pinning]
NEAREST GEX LEVEL:   [level name + distance]
DELTA CONFIRMATION:  [Confirmed / Diverging / Neutral]
CONTINUATION:        [High / Medium / Low]
ACTION BIAS:         [Follow / Fade / Wait / Observe]
─────────────────────────────────────────────
```

---

## DECISION RULES

```
IF Burst + delta confirms → follow, do not fade
IF Grind + near GEX level → add to position in grind direction
IF Exhaustion + delta diverging → tighten stop, wait for structural confirm before reversing
IF Flip + reclaims GEX level + volume spike → treat as regime change, follow new direction
IF at HVL / Max Gamma → reduce size, expect mean-reversion, do not chase
IF unclear → no action. Wait for one of the four patterns to become readable.
```

---

## RULES

- Always know GEX level locations before attempting to read the tape — the levels give context to every move
- Never label a move "stop hunt" until dealer mechanical explanation has been eliminated
- Exhaustion is not a trade signal — it is a warning that continuation is weakening
- A Dealer Flip at a strong GEX wall carries more weight than a flip in open space
- "Unclear" is a valid tape read — it means the dealer hand is not visible, reduce confidence accordingly

---

*D.S.E/trading/skills | STIS Layer 1b | Live Dealer Tape Reading | Source: Options Flow Foundation + GEX Engine*

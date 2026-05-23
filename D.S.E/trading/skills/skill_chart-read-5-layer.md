# SKILL — Chart Read: 5-Layer STIS Analysis
**Full-spectrum instrument read through all 5 layers**
**Load when:** Analyzing any instrument for a potential setup or morning brief entry.

---

## WHAT THIS IS

A chart read is not pattern recognition. A chart read is a field assessment — reading the exhaust (price) back to the engine (institutional architecture + collective consciousness + macro context + cyclic position + observer state). This skill structures that assessment so no layer is skipped.

**Doctrine:** "The chart is the exhaust, not the engine. The Sovereign reads the engine."

---

## 5-LAYER READ SEQUENCE

### LAYER 5 FIRST — Observer Gate
*Before reading the instrument, read yourself.*
Load `skill_observer-gate.md` and run the 5-question check.
- If BLOCKED → stop. Do not read the chart. Log "Observer Gate Blocked."
- If CLEAR → continue.

---

### LAYER 3 — Macro Context (Jiang)
*What is the global game doing? Is this instrument's direction aligned with the macro tide?*

1. **DXY position:** Which direction is the dollar trending? Any recent break of structure?
2. **Price hierarchy:** Which tier is dominant? (Resources/Manufacturing/Knowledge/Finance — see pandora_frameworks.json)
3. **Game reset signals:** Any BIS coordination events, petrodollar stress, BRICS news active?
4. **Instrument macro alignment:** Is this pair's directional bias WITH or AGAINST DXY flow?

**Output:** "Macro: [aligned / misaligned / neutral] — reason"

---

### LAYER 4 — Cyclic Position (Bailey)
*Where is this instrument in the Crisis→Polarization→Sweep cycle?*

| Bailey Phase | IEC Equivalent | What It Looks Like |
|---|---|---|
| Crisis | Accumulation | Range-bound, confusing, contradictory signals |
| Polarization | Impulse Trap | Strong move with retail conviction — likely a trap |
| Sweep | Expansion | Clean directional delivery — institutional execution |

1. Identify the current Bailey phase on the HTF (Daily or Weekly)
2. Is there a Three-Hit structure completing? (3 touches = reversal probability high)
3. What is the Six-Month candle saying? (First week = Power of 3 at 6M scale)

**Output:** "Cyclic phase: [Crisis/Polarization/Sweep] — [one-line read]"

---

### LAYER 2 — Collective Consciousness (Saaja)
*Where is the retail crowd? Their position is the liquidity target.*

1. **COT retail %:** Check current Commitments of Traders retail positioning
   - >65% retail long → institutional sweep target = SHORT bias
   - <35% retail long → potential long support
   - 50-65% → neutral, look to other layers for bias
2. **Narrative check:** What is the dominant news narrative for this pair?
   - Dominant bullish narrative = retail long crowding = SHORT
   - Dominant bearish narrative = retail short crowding = LONG
3. **Forgetting cycle:** Has this pair had a recent false break (impulse trap) that retail is now "over"?

**Output:** "COT: [X]% retail long | Narrative: [dominant sentiment] | Crowd position: [against / with]"

---

### LAYER 1 — Mechanical Read (Nathan/Kim/Todd)

**A. Market Structure (Kim)**
1. HTF bias: Is price above or below the last clean market structure point?
2. Is there a confirmed BOS (Break of Structure) or CHoCH (Change of Character) on HTF?
3. Top-down cascade: Does the HTF bias confirm the ITF entry direction?
4. What is the nearest significant order block?

**B. IEC Phase (Nathan Banks)**
Load `skill_iec-phase-detection.md` — identify current phase.

**C. Session Architecture (Nathan Banks)**
Load `skill_session-architecture.md` — what did Asia do? What is London's role right now?

**D. Key Levels**
- Pull pine_lines for horizontal institutional levels
- Pull pine_labels for named levels (PDH, PDL, Settlement, ASN O/U, session highs/lows)
- Pull pine_boxes for supply/demand zones

**E. EMA Stack**
- 5 EMAs: 8, 21, 50, 100, 200
- Bullish aligned: 8>21>50>100>200 and price above all
- Bearish aligned: 8<21<50<100<200 and price below all
- Compressing: EMAs converging = range / indecision

**F. Grade A Filter**
Load `skill_grade-a-filter.md` — does this setup pass all 7 criteria?

---

## SYNTHESIS — THE CONVERGENCE READ

```
L5 (Observer):     [CLEAR / BLOCKED]
L4 (Cyclic):       [Crisis / Polarization / Sweep] → [Accumulation / Trap / Expansion]
L3 (Macro):        [Aligned / Misaligned / Neutral] with instrument direction
L2 (Crowd):        [Retail crowded LONG / SHORT / Neutral] → institutional target = [opposite]
L1 (Mechanical):   [IEC Phase] | [Session position] | [Structure] | [Grade A: YES/NO]

CONVERGENCE:
All 5 layers agree → Grade A+ → Execute
L1 + L3 agree, L5 clear → Grade A → Execute
L1 only → Do not execute (incomplete read)
L5 blocked → No trade regardless
```

---

## OUTPUT FORMAT

```
SYMBOL: [pair] | TIMEFRAME: [active TF] | DATE/TIME: [timestamp]

L5 OBSERVER: [CLEAR / BLOCKED — reason if blocked]
L4 CYCLIC: [phase] — [one line]
L3 MACRO: [alignment] — DXY [trend], [relevant macro note]
L2 CROWD: COT [X]% retail long | Narrative [sentiment] | Target = [direction]
L1 MECHANICAL:
  Structure: [BOS/CHoCH/Range] on [HTF]
  IEC Phase: [phase name]
  Session: [Asia result, London/NY position]
  EMA Stack: [alignment]
  Key Levels: [list top 3-5]
  Grade A: [YES/NO/FORMING — criteria met: X/7]

BIAS: [LONG / SHORT / NEUTRAL / WAIT]
SETUP: [describe if Grade A] | INVALIDATION: [price level that cancels the read]
```

---

*D.S.E/trading/skills | 5-Layer Chart Read | Pandora OS*
*This skill is the analytical core of STIS. Run it for every instrument assessed — never skip layers.*

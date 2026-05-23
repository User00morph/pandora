# SKILL — CHART PATTERN RECOGNITION
**Layer 2 Skill | D.S.E/trading/skills/**
**Skill File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: dse_archive_pattern-library.md, dse_framework_order-flow-mechanics.md**
**Run: At every chart analysis session, during Step 2 of the dual-layer chart reading**

---

## PURPOSE

This skill provides the rapid identification protocol for the 8 core patterns in the STIS pattern library. It also provides the framework for identifying NEW patterns and logging them correctly. Chart pattern recognition is not the starting point — it is applied WITHIN a valid structural context (the dual-layer chart reading must establish the context first).

**Pattern recognition without structure = setup identification in a vacuum.**
**Structure without pattern recognition = knowing WHERE but not WHEN.**

---

## THE PATTERN IDENTIFICATION SEQUENCE

When analyzing any chart at the 1H or 15M entry timeframe:

```
STEP 1: Is there a valid structural context?
□ Daily bias established (from dual-layer reading)
□ 4H OB zone identified
□ Price is in the correct location (discount for longs, premium for shorts)
If NO: Stop here. No pattern identification needed — no valid trade location.

STEP 2: Which of the 8 core patterns might be forming?
(See Section 1 below — rapid pattern check)

STEP 3: Does the pattern have all its confirming signals?
(See Section 2 — confirming signal checklist per pattern)

STEP 4: Is the entry trigger present?
(Cross-reference to skill_candlestick-reading.md for the specific trigger candle)

STEP 5: Log the observation in the pattern library
(Whether traded or not — both observations compound the library)
```

---

## SECTION 1 — THE 8 PATTERN RAPID-CHECK

For each active pair, quickly scan which patterns are visible:

### PATTERN 1 — LIQUIDITY SWEEP + REVERSAL
**Visual signature:** A sharp move BELOW key support (or ABOVE key resistance) followed by immediate recovery.

```
Quick check:
□ Is there an obvious key level visible (previous lows / equal lows / round number)?
□ Has price broken below that level with a long wick candle?
□ Has price recovered back above the level in the same or next candle?
→ YES to all three: POTENTIAL P1 — check confirming signals
```

**Time to identify:** 10 seconds.
**Most common timeframe:** 15M to 1H.
**Most common context:** At the low of a 4H OB zone (the stop hunt before the continuation).

---

### PATTERN 2 — ORDER BLOCK RETURN
**Visual signature:** A strong impulse candle (the BOS) that leaves an OB behind, followed by a pullback to that OB zone.

```
Quick check:
□ Is there a recent strong BOS candle (large body, clear direction)?
□ Has price pulled back toward where that BOS candle originated?
□ Is the pullback candle structure smaller than the BOS candle (lower conviction)?
→ YES: POTENTIAL P2 — check confirming signals
```

**Time to identify:** 15 seconds.
**Most common timeframe:** 1H to 4H.
**Most common context:** The most common pattern in trending markets — the "bread and butter" of the Sweep phase.

---

### PATTERN 3 — FAIR VALUE GAP FILL + REJECTION
**Visual signature:** A three-candle structure where Candle 2 is a large impulse that leaves a gap between Candle 1's high and Candle 3's low (for bullish FVG).

```
Quick check:
□ Can you find a three-candle series where Candle 2 moved so fast it left a gap?
□ Is the gap between C1 high and C3 low still unfilled (price hasn't returned yet)?
□ Is price now approaching that gap zone?
→ YES: POTENTIAL P3 — check confirming signals
```

**Time to identify:** 20 seconds.
**Most common timeframe:** 15M to 1H.
**Key rule:** Mark the MIDPOINT of the FVG (C1 high + C3 low ÷ 2) — the highest probability reaction is at the midpoint, not the edges.

---

### PATTERN 4 — ASIAN RANGE SWEEP + LONDON CONTINUATION
**Visual signature:** Price ranges within a tight band during Asian session, then breaks one side at London open before reversing and continuing the opposite direction.

```
Quick check:
□ Is it currently 2:00 AM - 5:00 AM EST? (London open kill zone)
□ Has Asian session established a clear High and Low?
□ Has price just swept BELOW the Asian Low (if bullish bias) or ABOVE the Asian High (if bearish)?
□ Is the sweep being immediately rejected (recovery candle forming)?
→ YES: POTENTIAL P4 — check confirming signals
```

**Time to identify:** 30 seconds (requires knowing the Asian range before London opens).
**Session-specific:** ONLY valid during the London kill zone window.

---

### PATTERN 5 — DOUBLE TOP / DOUBLE BOTTOM TRAP
**Visual signature:** Price reaches a high/low, pulls back, reaches the same level again — forming two equal peaks or valleys.

```
Quick check:
□ Are there two candles/areas where price reached approximately the same level?
□ Has the second touch of that level been rejected with a wick?
□ Is the SECOND touch being swept (slightly above/below the FIRST touch)?
→ YES to the sweep signal: POTENTIAL P5 — check confirming signals
```

**Time to identify:** 15 seconds.
**Key insight:** The Sovereign enters AFTER the sweep of equal high 2 (not at the neckline break). The sweep IS the setup — not a precursor to it.

---

### PATTERN 6 — BREAKER BLOCK (FAILED OB)
**Visual signature:** A zone that was previously an Order Block (support) has been broken through (price closed below it), and price is now returning to that broken zone (now resistance).

```
Quick check:
□ Was there a prior bullish OB zone that price has since closed BELOW?
□ Is price now rallying back toward that broken zone?
□ Is the rally approaching the Breaker zone from below?
→ YES: POTENTIAL P6 — check confirming signals
```

**Time to identify:** 20 seconds (requires knowing where prior OB zones were).
**Key rule:** The close is decisive. A zone is only a Breaker if price CLOSED beyond it (not just wicked).

---

### PATTERN 7 — COMPRESSION + EXPANSION
**Visual signature:** Progressively smaller candles followed by a decisive large candle.

```
Quick check:
□ Are there 3 or more consecutive candles that are each smaller than the prior?
□ Has an inside bar (completely within the prior candle's range) formed?
□ Are you waiting for the expansion candle to close?
→ YES: POTENTIAL P7 — wait for the expansion candle, do NOT anticipate
```

**Time to identify:** 10 seconds.
**Key warning:** The inside bar during the compression is the SETUP SIGNAL — do not enter until the EXPANSION candle closes and confirms direction. The false expansion (breaks out then reverses) is the most common trap in this pattern.

---

### PATTERN 8 — VOLUME CLIMAX REVERSAL
**Visual signature:** The largest single candle in an extended trend, occurring on the highest volume of that trend, followed by a smaller recovery candle.

```
Quick check:
□ Is there a sustained trend (5+ candles in one direction)?
□ Is the most recent candle SIGNIFICANTLY larger than prior candles in that trend?
□ Is volume on this candle SIGNIFICANTLY higher than the prior candles?
□ Is a recovery candle forming (opposite direction, smaller)?
→ YES: POTENTIAL P8 — check confirming signals
```

**Time to identify:** 20 seconds.
**Primary timeframe:** Daily or Weekly. Lower timeframe climax candles are less reliable.

---

## SECTION 2 — CONFIRMING SIGNAL CHECKLISTS

### For PATTERN 1 (Liquidity Sweep + Reversal)
```
□ Daily bias is aligned with the reversal direction (sweep = into discount for longs)
□ The sweep occurred in the discount zone (below 50% of the last swing for longs)
□ COT shows Commercial Hedgers positioned against the sweep direction
□ Lunar cycle: waxing (if bullish reversal)
□ No major economic event within 4 hours
□ Recovery candle has a bullish close (not just a shadow recovery)
SCORE: ___/6 | Threshold: 4+ to qualify as high-probability
```

### For PATTERN 2 (Order Block Return)
```
□ The OB zone aligns with a higher timeframe structural level
□ Pullback volume is LOWER than the impulse that created the OB
□ A rejection candle (pin bar or engulfing) forms within the OB zone
□ An FVG above (for longs) remains unfilled — the magnet is in place
□ Structure is still making HH+HL (uptrend intact — this is just a pullback, not a CHoCH)
□ The OB has NOT been tested more than twice (third test often breaks)
SCORE: ___/6 | Threshold: 4+ to qualify
```

### For PATTERN 3 (FVG Fill + Rejection)
```
□ The FVG was created by a strong impulse candle (not a small move — a genuine imbalance)
□ The pullback into the FVG is on lower volume than the impulse
□ Price enters the FVG and a rejection candle forms at or near the 50% midpoint
□ The impulse that created the FVG was in the direction of the daily bias
□ No conflicting OB or structure level within the FVG zone
SCORE: ___/5 | Threshold: 3+ to qualify
```

### For PATTERN 4 (Asian Range Sweep + London Continuation)
```
□ Daily bias is established (the expected continuation direction is known)
□ London kill zone is active (2-5 AM EST)
□ The sweep occurred in the expected manipulation direction (sweeps AGAINST the daily bias, then reverses WITH the bias)
□ A bullish/bearish FVG or OB is nearby (the institutional anchor zone for the real move)
□ The rejection candle closed back within the Asian range (the sweep was rejected)
SCORE: ___/5 | Threshold: 4+ to qualify (this pattern demands high confirmation)
```

### For PATTERN 5 (Double Top/Bottom Trap)
```
□ The second touch swept the first touch level (not just reached it — swept it briefly)
□ A rejection candle formed at the sweep of the equal high/low
□ The rejection candle was a shooting star (for double top) or hammer (for double bottom)
□ COT is at an extreme positioning consistent with a reversal
□ Volume on the second touch is LOWER than the first (declining momentum = exhaustion)
SCORE: ___/5 | Threshold: 4+ to qualify
```

### For PATTERN 6 (Breaker Block)
```
□ The original OB zone was definitively broken (price CLOSED beyond it — not just wicked)
□ The break of the OB was with strong momentum (large body candle)
□ Price is now returning to the Breaker zone from the other side
□ The daily bias is now against the original OB direction (the trend has reversed)
□ A rejection candle forms at the Breaker zone
SCORE: ___/5 | Threshold: 4+ to qualify
```

### For PATTERN 7 (Compression + Expansion)
```
□ Minimum 3 progressively smaller candles (5+ = stronger signal)
□ At least one inside bar present in the compression
□ The expansion candle is decisive (large body, closes at or near its extreme)
□ The expansion candle's direction is aligned with the higher timeframe bias
□ The expansion is NOT immediately fully retraced (a false expansion retraces completely)
SCORE: ___/5 | Threshold: 4+ to qualify
```

### For PATTERN 8 (Volume Climax Reversal)
```
□ The trend preceding the climax candle is sustained (minimum 5-7 candles in one direction)
□ The climax candle body is 2x+ larger than average prior candles in the trend
□ The climax candle volume is 2x+ the average volume of prior trend candles
□ A recovery candle follows (closes opposite to the trend, smaller than the climax)
□ The climax occurred at a key structural level (previous high/low, round number, long-term OB)
□ COT shows Commercial Hedgers at an extreme position against the trend direction
SCORE: ___/6 | Threshold: 5+ to qualify (this is a reversal pattern — higher threshold required)
```

---

## SECTION 3 — PATTERN LOG ENTRY FORMAT

After every session (whether a trade was taken or not), log significant patterns observed:

```
## Pattern Observation — [YYYY-MM-DD] — [Pair] — [Timeframe]

**Pattern type:** [P1-P8 or "New pattern — [describe]"]
**Context:** [Which dual-layer reading session this occurred in]
**Structure location:** [At 4H OB / At Daily structure level / At key liquidity pool]
**Daily bias:** [Long/Short/Neutral — was the pattern aligned?]
**Confirming signals present:** ___/[total] → [threshold met / not met]
**Trade taken:** [Yes / No — if No, why?]
**Entry:** _________ | **Stop:** _________ | **Target:** _________
**Outcome (if traded):** [Win / Loss / Break-even] | [R multiple: ___R]
**Pattern quality assessment:** [What worked / What was missing]
**Pattern library update:** [What this adds to the understanding of this pattern]
```

---

## SECTION 4 — IDENTIFYING NEW PATTERNS

The 8 core patterns are not exhaustive. When price produces a consistent behavior NOT in the existing library, document it:

```
NEW PATTERN OBSERVATION:

**Date / Pair / Timeframe:**
**Structure description:** [Draw or describe in text]
**Consciousness read:** [What Mutable/Fixed/Cardinal Cross behavior is creating this pattern?]
**Ray signature:** [Which Ray is this pattern associated with?]
**Conditions required:** [What structural, data, and esoteric conditions produced this?]
**First observation outcome:** [What happened after?]
**Second observation (required before adding to library):** [Date / outcome]
→ If two observations produce similar outcomes: ADD TO PATTERN LIBRARY as Pattern 9+
→ If outcomes diverge: continue observing before codifying
```

---

## CROSS-REFERENCES
- `dse_archive_pattern-library.md` — the pattern reference file this skill applies
- `dse_framework_order-flow-mechanics.md` — the order flow mechanics underlying each pattern
- `skill_candlestick-reading.md` — the trigger candle identification within each pattern
- `skill_dual-layer-chart-reading.md` — Phase 2E where this skill is applied

---

*skill_chart-pattern-recognition.md | D.S.E/trading/skills/ | STIS Layer 2 Operational Skill*
*Status: v1.0 — active | Applied at every chart analysis session during setup identification.*

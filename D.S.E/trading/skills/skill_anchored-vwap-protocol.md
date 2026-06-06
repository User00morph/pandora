# SKILL — ANCHORED VWAP PROTOCOL
**Volume-Weighted Average Price from Key Event Points**
**Load when:** Analyzing price relative to a significant historical event.
**Department:** D.S.E trading workspace | STIS Layer 2 | Price context

---

## WHAT THIS IS

Standard VWAP resets daily. Anchored VWAP calculates the volume-weighted average price from ANY user-defined starting point — an earnings release, a major news event, a swing high/low, a regime change. It shows where the average market participant is positioned relative to that event.

---

## KEY ANCHOR POINTS FOR THE STIS

```
SWING-LEVEL ANCHORS:
  Last major swing low        → AVWAP = institutional cost basis for the bull move
  Last major swing high       → AVWAP = overhead supply level
  Last significant gap        → AVWAP = gap fill reference

TEMPORAL ANCHORS:
  Start of current IEC phase  → AVWAP = phase average entry
  Major news event date       → AVWAP = post-event market consensus
  Session open                → AVWAP = today's VWAP (same as standard)
  Week open                   → Weekly AVWAP = the week's institutional average

GEX-SPECIFIC ANCHORS:
  Last GEX level break        → AVWAP from break point = breakout consensus price
  Last major gamma squeeze    → AVWAP from squeeze = post-squeeze fair value
```

---

## HOW TO READ AVWAP

```
PRICE ABOVE AVWAP:
  Buyers who entered at or after the anchor date are in profit
  The AVWAP is now support (they defend their position)
  Long bias reinforced

PRICE BELOW AVWAP:
  Buyers who entered at or after the anchor date are in loss
  Sellers have control since that event
  Short bias reinforced

PRICE TESTING AVWAP:
  Decision point — will buyers defend or sellers overwhelm?
  Watch volume at this level — high volume test = stronger reaction
```

---

## THE STIS APPLICATION

Multi-anchor AVWAP creates a level stack:
1. **Session AVWAP** (today) — intraday bias
2. **Weekly AVWAP** (Monday open) — medium-term bias
3. **IEC phase AVWAP** (from phase start) — structural bias

When price is above ALL three → maximum long conviction.
When price is below ALL three → maximum short conviction.
Mixed signals → reduce size or wait for alignment.

---

## PINE SCRIPT IMPLEMENTATION

```pine
// Anchored VWAP from user-selected bar
var float avwap_numerator = 0.0
var float avwap_denominator = 0.0

if bar_index == anchor_bar
    avwap_numerator := 0.0
    avwap_denominator := 0.0

avwap_numerator += hlc3 * volume
avwap_denominator += volume
avwap = avwap_numerator / avwap_denominator

plot(avwap, "AVWAP", color.yellow, 2)
```

*D.S.E/trading/skills | STIS Layer 2 | Anchored VWAP Protocol*

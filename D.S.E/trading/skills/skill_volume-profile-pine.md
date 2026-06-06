# SKILL — VOLUME PROFILE PINE SCRIPT
**Free Volume Profile Implementation for STIS Chart Analysis**
**Load when:** Building or reviewing the volume profile module in the STIS chart.
**Department:** D.S.E + D.I.I | STIS Layer 2 | Volume analysis infrastructure

---

## WHAT THIS IS

A Pine Script volume profile that replicates the core functionality of paid volume profile tools — horizontal histogram showing volume distribution by price level, POC highlighting, value area shading — for free.

---

## THE CORE COMPONENTS

```
VISIBLE RANGE VOLUME PROFILE (VRVP):
  - Looks back over the last N bars (default: 200)
  - Divides the price range into 50 rows
  - Counts volume at each price row
  - Renders as horizontal bars on the right side of the chart
  - Highlights POC (highest volume row) in gold/amber

VALUE AREA SHADING:
  - Starting from POC, expands outward row by row
  - Adds rows until 70% of total volume is captured
  - Shades the VAH→VAL zone in a distinct color (muted green)

VOLUME GAP DETECTION:
  - Identifies rows with zero or near-zero volume
  - Marks these as purple lines extending across the chart
  - These are the inefficiency/vacuum zones
```

---

## THE IMPLEMENTATION ARCHITECTURE

```pine
// VRVP — Visible Range Volume Profile
var float[] vol_by_price = array.new_float(50, 0.0)
var float price_low = 0.0
var float price_high = 0.0

// Find range of last N bars
N = 200
price_high := ta.highest(high, N)
price_low  := ta.lowest(low, N)
row_size   = (price_high - price_low) / 50

// Assign volume to rows
for i = 0 to 49
    row_low  = price_low + i * row_size
    row_high = row_low + row_size
    if close >= row_low and close < row_high
        array.set(vol_by_price, i, array.get(vol_by_price, i) + volume)

// Find POC
max_vol = array.max(vol_by_price)
poc_idx = array.indexof(vol_by_price, max_vol)
poc_price = price_low + poc_idx * row_size
```

---

## READING THE PROFILE IN THE STIS

```
THICK BARS (high volume):
  → Strong two-sided acceptance at this price
  → Expect price to revisit and respect these levels
  → Use as support/resistance targets

THIN BARS OR GAPS (low/zero volume):
  → Price moved through quickly — inefficiency
  → When price returns: either rips through or reverses hard
  → Use as target projection zones (vacuum behavior)

WIDE VALUE AREA (VAH-VAL span is large):
  → Wide price acceptance range
  → No single dominant level — choppy environment

NARROW VALUE AREA:
  → Strong consensus around specific price range
  → This is where institutions did their business
  → High-conviction support/resistance zone
```

---

## INTEGRATION WITH GEX LEVELS

When a GEX level coincides with the POC or VAH/VAL boundary → power cluster. The institutional options positioning (GEX) and the institutional transaction history (volume profile) are pointing to the same price → maximum level significance.

*D.S.E + D.I.I | STIS Layer 2 | Volume Profile Implementation*

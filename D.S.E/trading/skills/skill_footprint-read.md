# SKILL — Volume Footprint Read
**Institutional Intent at the Bar Level | Order Flow X-Ray**
**Load when:** Analyzing chart setups, confirming entry zones, evaluating Grade A criteria 3-5.
**Pine Scripts:** `volume_footprint_v1.pine` (delta pane) + `volume_footprint_overlay_v1.pine` (chart overlay)
**Department:** D.S.E trading workspace | STIS Layer 1 (Order Flow sublayer)

---

## WHAT THIS IS

The volume footprint is order flow made visible at the individual candle level. Where standard indicators tell you THAT price moved, the footprint tells you WHO moved it and HOW MUCH conviction was behind it. It is the X-ray beneath the candlestick.

**Five metrics and what each reveals:**

| Metric | What It Measures | What It Tells You |
|--------|-----------------|-------------------|
| **Volume Delta** | Buy vol - sell vol per bar | NET institutional intent — buyers or sellers were more aggressive THIS bar |
| **Cumulative Delta** | Running session total of delta | Who is winning the SESSION — directional dominance |
| **POC** | Price with highest volume in window | Institutional ANCHOR — where the most business was done; price will return here |
| **VAH / VAL** | 70% volume distribution bounds | VALUE AREA — inside = fair value (range). Outside = premium/discount (return expected) |
| **Imbalance / Cluster** | Bid/ask asymmetry >3:1 ratio | ABSORPTION — institutions are aggressively taking one side. 3+ consecutive = cluster |

---

## HOW TO READ EACH METRIC

### VOLUME DELTA (delta histogram pane)

```
POSITIVE DELTA (green bar, tall):
  Buyers were MORE aggressive than sellers
  Heavy buying came in on this candle
  Bullish pressure — confirms up moves, questions down moves

NEGATIVE DELTA (red bar, tall):
  Sellers were MORE aggressive than buyers
  Heavy selling came in on this candle
  Bearish pressure — confirms down moves, questions up moves

SMALL DELTA (short bar, any color):
  Balanced — neither side dominated
  Indecision, consolidation, or a mechanically forced move (Vanna/Charm)
  Low conviction — do not extrapolate direction

DELTA % (number in table):
  Delta as % of total bar volume
  >60%: strong conviction — one side clearly dominated
  <20%: weak — mixed, no clear aggressor
```

### CUMULATIVE SESSION DELTA

```
RISING CUM DELTA:
  Buyers have been more aggressive ALL SESSION
  Background directional pressure is LONG
  Even if price is ranging, the eventual break should favor longs

FALLING CUM DELTA:
  Sellers have been more aggressive ALL SESSION
  Background pressure is SHORT
  Range break should favor shorts

FLAT / OSCILLATING CUM DELTA:
  Session is balanced — no directional dominance
  Expect continued range behavior until delta divergence emerges

DIVERGENCE SIGNAL:
  Price makes new high BUT cum delta is falling = distribution
  Buyers are not following price up — smart money selling into rally
  Reversal likely

  Price makes new low BUT cum delta is rising = accumulation
  Sellers not following price down — smart money buying the dip
  Reversal likely
```

### POC (Point of Control)

```
POC = the price level where the most volume occurred in the window

Price ABOVE POC:
  Market currently in premium territory relative to value
  Gravity toward POC when move exhausts

Price BELOW POC:
  Market in discount territory
  Gravity toward POC on any recovery

Price AT POC:
  At equilibrium — battle zone
  Either direction is valid from here
  Wait for delta evidence before committing

POC as RE-ENTRY ZONE:
  If price breaks out from POC and returns to test it = classic re-entry
  Buy the test of POC after a bullish breakout (POC becomes support)
  Sell the test of POC after a bearish breakdown (POC becomes resistance)
```

### VAH / VAL (Value Area)

```
VALUE AREA = price range containing 70% of session volume
VAH = value area high | VAL = value area low

INSIDE VALUE AREA (between VAH and VAL):
  "Fair value" zone — institutions are comfortable here
  Expect range behavior, mean-reversion tendencies
  Less directional conviction — reduce size on breakouts

OUTSIDE VALUE AREA (above VAH or below VAL):
  PREMIUM (above VAH) or DISCOUNT (below VAL)
  Price is AWAY from where most business was done
  Institutions tend to push price BACK to value (unless new range is forming)
  Use for fade setups — high probability returns to VAH or VAL

KEY ENTRY RULE:
  Best setups are when price RETURNS to value area edge:
  → Drop to VAL from inside = buy
  → Rally to VAH from inside = sell
  → Break above VAH + retest = buy
  → Break below VAL + retest = sell
```

### IMBALANCE AND CLUSTER SIGNALS

```
SINGLE IMBALANCE (diamond marker on histogram):
  One bar where buyers/sellers dominated by 3:1 ratio
  Institutional absorption — someone was aggressively filling a large order
  Note the level. Price often returns to imbalance zones.

IMBALANCE CLUSTER (◆ CLUSTER label on chart):
  3+ consecutive imbalanced bars in same direction
  STRONGEST signal in the footprint toolkit
  Institutional conviction — not a one-bar anomaly, sustained absorption
  High probability: the cluster marks an institutional level that will be defended

CLUSTER + GEX CONFLUENCE:
  When a cluster occurs AT a GEX level (HVL, GEX 1-3):
  = THE HIGHEST PROBABILITY REACTION ZONE IN THE STIS STACK
  Two independent systems (options mechanics + actual order flow) confirming same level
  This is the Grade A+ setup condition
```

---

## READING SEQUENCE (per chart)

```
STEP 1 — CUMULATIVE DELTA TREND
  Is cum delta rising, falling, or oscillating?
  This tells you who has been winning the session.

STEP 2 — VALUE AREA POSITION
  Where is current price relative to VAH, VAL, POC?
  Inside = fair value range behavior
  Outside = premium/discount → expect return

STEP 3 — MOST RECENT BAR DELTA
  Is the current bar's delta confirming or diverging from price?
  Divergence = reversal signal. Confirmation = continuation signal.

STEP 4 — IMBALANCE CHECK
  Are there recent imbalance markers or a live cluster signal?
  If cluster: note the price level — this is an institutional zone.

STEP 5 — CONFLUENCE WITH GEX
  Does any imbalance cluster coincide with a GEX level from skill_gex-regime-read.md?
  If YES → Grade A+ filter condition met (criterion 8: footprint + GEX confluence)
```

---

## INTEGRATION WITH GRADE A FILTER

The footprint adds two new Grade A criteria (use alongside skill_grade-a-filter.md):

**Criterion 8 — FOOTPRINT CONFIRMATION**
- PASS: Delta confirms entry direction (green delta on long setup, red on short)
- PASS: Cum delta is aligned with entry direction
- FAIL: Delta diverging from price (price making new high but delta declining)
- FAIL: Cum delta opposing entry direction

**Criterion 9 — FOOTPRINT + GEX CONFLUENCE (Grade A+ only)**
- PASS: An imbalance cluster exists at or within 5 ticks of a GEX level
- PASS: Price is at POC or VAH/VAL and delta confirms direction
- FAIL: Neither condition — footprint not adding confluence

---

## SETUP ARCHETYPES

**1. POC Return Setup**
Price moves away from POC, then returns → enter as price touches POC with confirming delta
Target: other side of value area (VAH or VAL)

**2. Value Area Break + Retest**
Price breaks above VAH (or below VAL) → pulls back to retest the broken level → enter with delta confirmation
Target: next GEX level beyond the VA

**3. Cluster Absorption + Reversal**
Bear cluster forms at a GEX put support level → cum delta begins rising despite price still falling → enter long
Target: POC or VAH

**4. Delta Divergence**
Price makes new high → delta declining (distribution) → enter short as first red delta bar confirms
Target: VAL or POC

---

## RULES

- Volume delta is an ESTIMATE (estimated from price position within the bar, not tick data). It is directional, not precise.
- A single bar's delta means nothing. The TREND of delta over multiple bars is the signal.
- Imbalance clusters are the strongest signal. Single imbalances are context, not entries.
- Always pair footprint reads with GEX regime (skill_gex-regime-read.md) — the force field determines whether the footprint signal has momentum or will be faded.
- The footprint confirms setup quality. It does not generate the trade idea.

---

*D.S.E/trading/skills | STIS Order Flow Sublayer | Pandora OS*
*Pine Scripts: volume_footprint_v1.pine + volume_footprint_overlay_v1.pine*

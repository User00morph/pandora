# SKILL — VOLUME GAP ZONES
**Price Levels Where Zero Volume Traded — Market Inefficiency Zones**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Analyzing volume profile for key levels, or when price is approaching
            a zone where prior volume was near zero
DEPARTMENT: D.S.E | STIS Layer 2 | Market structure analysis
LOADS:      skill_volume-profile-pine.md (the visualization tool)
            skill_value-area-protocol.md (context for adjacent levels)
PRODUCES:   List of active volume gap zones + expected behavior at each
CROSS-REF:  skill_gex-level-hierarchy.md ("no GEX above" = same vacuum concept)
            skill_session-poc-entry-model.md (gap zones as targets in entry model)
            skill_delta-volume-decode.md (delta behavior in gap zones)
```

---

## WHAT THIS IS

Volume gap zones are price levels where little or no two-sided trading occurred — price moved through so quickly that the market didn't accept that level. When price returns to a volume gap, one of two things happens: it fills through rapidly (vacuum behavior) or it reverses sharply (rejection). Understanding which behavior to expect is the edge.

---

## IDENTIFYING VOLUME GAP ZONES

```
On the volume profile horizontal histogram:
  High volume rows:     thick bars → accepted levels, strong S/R
  Low volume rows:      thin bars → weak acceptance, likely to pass through
  Zero volume rows:     gap in histogram → no acceptance at all → vacuum zone

Visual appearance on chart:
  Visible as blank/thin areas between volume clusters
  Pine Script implementation: purple horizontal lines through gap zones
  Width of gap: wider = stronger vacuum effect
```

---

## THE TWO BEHAVIORS

### BEHAVIOR A — VACUUM (rips through)

```
SETUP:
  Price approaches gap zone from outside
  Gap zone has zero or near-zero volume
  No other significant levels (GEX, POC, key levels) inside the gap

WHAT HAPPENS:
  Price moves through the gap zone with minimal resistance
  Speed accelerates inside the gap — no buyers or sellers to slow it
  Price exits the gap and finds the next high-volume cluster

TRADE APPLICATION:
  → Do NOT fade inside a vacuum zone
  → Use gap zones as TARGET PROJECTIONS: once price enters a gap,
     the next high-volume cluster is the likely destination
  → Do NOT place stops inside gap zones (will get blown through)
```

---

### BEHAVIOR B — REVERSAL (fills and rejects)

```
SETUP:
  Price approaches gap zone
  A significant GEX level, POC, or key level sits AT or just beyond the gap
  The macro regime is mean-reverting (positive gamma)

WHAT HAPPENS:
  Price enters the gap, moves toward the key level beyond it
  At the key level: institutions who traded there defend it strongly
  Price reverses back through the gap

TRADE APPLICATION:
  → The entry is at the first GEX/POC level BEYOND the gap
  → Stop is placed on the other side of that level
  → Target is back through the gap to the origin cluster
```

---

## THE VACUUM + "NO GEX ABOVE" COMBINATION

The strongest vacuum signal:
```
Volume gap zone + no GEX exposure above the gap = maximum vacuum

This means:
  No two-sided trading history at these prices (volume gap)
  No dealer hedging pressure at these prices (no GEX)
  = Pure vacuum — price will run until the next cluster

This is the same signal Travis Woo described: "No GEX above = it's basically
all-time high movement. There is nothing to the left."
```

---

## STOP PLACEMENT RULE

**Never place a stop inside a volume gap zone.** Gap zones are vacuum areas — price moves through them without pausing. A stop inside a gap zone will be executed at a worse price than expected (slippage through the zone).

Place stops:
- Beyond the gap zone entirely (for trend trades through the gap)
- Just inside the gap at the origin cluster edge (for reversal trades)

---

## OUTPUT FORMAT

```
VOLUME GAP ANALYSIS — [INSTRUMENT] [DATE]
IDENTIFIED GAPS:
  Gap 1: [price range] | Width: [N pips] | Expected behavior: [vacuum/reversal]
         Adjacent levels: [above: X, below: Y]
  Gap 2: [price range] | Width: [N pips] | Expected behavior: [vacuum/reversal]

CURRENT PRICE vs. GAPS:
  Above gap [X]: [yes/no — distance: N pips]
  Below gap [X]: [yes/no — distance: N pips]
  
TRADE IMPLICATIONS:
  If price enters gap [X]: [expected behavior + target]
```

*D.S.E/trading/skills | STIS Layer 2 | Volume Gap Analysis*

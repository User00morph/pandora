# SKILL — DELTA VOLUME DECODE
**Reading Buyer vs. Seller Control at Every Price Level**
**Load when:** Analyzing order flow, confirming breakouts, reading session pressure.
**Department:** D.S.E trading workspace | STIS Layer 2 | Order flow confirmation

---

## WHAT THIS IS

Delta volume separates raw volume (how much traded) from directional pressure (WHO was in control). Green = buyers dominated at this level. Red = sellers dominated. Width = magnitude. This is the order flow approximation layer — not perfect tick data, but captures the directional pressure signature.

---

## THE THREE READS

### Read 1 — Aligned Delta (healthy move)
Price rising + delta positive (green) = buyers in control, move is confirmed.
Price falling + delta negative (red) = sellers in control, move is confirmed.
**Action:** Trust the move. Follow the direction.

### Read 2 — Diverging Delta (weakness signal)
Price rising + delta declining (turning red) = buying pressure fading while price still advances.
Price falling + delta rising (turning green) = selling pressure fading while price still drops.
**Action:** Reduce confidence. Potential reversal developing. Tighten stops.

### Read 3 — Extreme One-Sided Delta at Breakout
Breakout through a level + delta massively skewed in the breakout direction = **institutional fingerprint.**
Institutions needed to absorb a large amount of one-sided pressure to push through that level.
**Action:** High-conviction continuation signal. Add to position or enter with full size.

---

## SESSION-LEVEL DELTA AGGREGATION

Sum the delta across the full session to determine which side dominated:

```
BULL SESSION:  Total buyers > total sellers → institutions were net long
BEAR SESSION:  Total sellers > total buyers → institutions were net short
NEUTRAL:       Roughly balanced → two-sided acceptance, no clear direction

Use this for:
  - Setting next session's directional lean
  - Identifying when a session's POC had buyer vs. seller control
  - Confirming or contradicting the Markov state read
```

---

## VOLUME GAP ZONES

Price levels where zero volume traded = market inefficiencies.

**Two behaviors when price returns:**
1. **Rips through** (vacuum) → no market memory at this level, price accepted gap and continued
2. **Reverses hard** (fills the gap) → market rejects the gap, returns to two-sided acceptance

Gap zones are NOT fades — they are high-velocity zones. Use them for target projection on momentum moves, not for counter-trend entries.

---

## THE GRADE-A FILTER APPLICATION

Delta confirmation upgrades any setup:

| Setup without delta | Setup with delta confirmation |
|---|---|
| Breakout of level | Breakout + delta skewed in direction |
| POC support test | POC support + delta positive on bounce |
| GEX level approach | GEX level + delta aligned with direction |

Delta confirmation = +1 grade (C→B, B→A, A→A+).

---

## RULES

- Delta is confirmation, not narrative — build the trade from structure, use delta to confirm
- Diverging delta is an early warning, not a reversal signal — wait for structural confirmation
- Gap zones without delta analysis are incomplete — check delta at the gap before projecting

*D.S.E trading workspace | STIS Layer 2 | Order Flow | Source: Travis Woo Volume Profile video*

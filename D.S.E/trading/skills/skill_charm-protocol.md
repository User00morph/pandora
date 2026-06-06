# SKILL — CHARM PROTOCOL
**Time-Based Drift and the Afternoon Gravity Window**
**Load when:** Planning afternoon sessions or reading end-of-day price behavior.
**Department:** D.S.E trading workspace | STIS Layer 1b | Afternoon session

---

## WHAT THIS IS

Charm is the force created by time decay. As the trading day progresses, options near the current price lose delta (time decay). Dealers slowly remove their hedges — creating a slow directional drift toward the nearest key gamma level by the close.

---

## THE WINDOW MAP

```
MARKET OPEN → 90 MINUTES IN:
  Charm ≈ zero
  Pure gamma + vanna operating
  CLEANEST window for mechanical edge
  Trade here — mechanics are most readable

90 MINUTES → CLOSE:
  Charm activates and grows
  Slow directional drift toward nearest gamma level
  The drift may look random — it is Charm pulling price home

CLOSE OF DAY:
  NQ tends to sit near or at the nearest key gamma level
  Either the HVL or the zero DTE put support / call resistance
```

---

## MORNING PREP INTELLIGENCE

Look at where NQ closed yesterday. Match that close to your gamma level stack.

**Read:** Yesterday's close was at or near [level] → Charm pulled price there during the afternoon → this tells you which level had the most gravitational pull → that level remains relevant today as the anchor.

---

## THE AFTERNOON TARGET PROTOCOL

When holding positions into the afternoon:

1. Identify the nearest key gamma level from your current price
2. That level is the afternoon gravity target
3. Charm is pulling price toward it regardless of intraday noise
4. Use this as your second or final target for the session

```
AFTERNOON TARGET = nearest GEX level (HVL or zero DTE wall)
```

---

## RULES

- Morning traders (first 90 min): Charm is irrelevant — focus on gamma and vanna
- Afternoon traders: Charm defines the directional bias and target
- End-of-day analysis: always check where price closed relative to gamma levels — that close was Charm-driven
- Never fight an afternoon drift toward a major gamma level

*D.S.E/trading/skills | STIS Layer 1b | Charm Drift Protocol | Source: Travis Woo Options Flow video*

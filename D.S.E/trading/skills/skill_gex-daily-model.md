# SKILL — GEX DAILY MODEL
**Travis Woo's Intraday Application Workflow**
**Load when:** Pre-market prep and live session execution using GEX levels.
**Department:** D.S.E trading workspace | STIS Layer 1b | Daily execution

---

## WHAT THIS IS

The specific daily workflow for applying GEX levels from pre-market markup to live entry. Not regime classification (that's `skill_gex-regime-read.md`) — this is the session-by-session execution protocol.

---

## PHASE 1 — PRE-MARKET PREP (before session opens)

1. Pull **previous day's** GEX data (not today's live data — prior session is more stable)
2. Mark up ALL levels before market opens:
   - All-expiry: call resistance, HVL, put support, gamma wall
   - Zero DTE parallel stack: same 4 levels, tighter
   - GEX 1-10 across the level map
3. Establish daily range: `put support → call resistance`
4. Identify regime: above or below HVL
5. Note isolated vs. stacked levels:
   - Isolated level (nothing above) = potential vacuum/initiation zone
   - Stacked levels = reinforced ceiling/floor

---

## PHASE 2 — SESSION OBSERVATION (market open)

**Do not rush. Observe first.**

- Note where price OPENS relative to the level stack → opening price tells the first story
- Wait for structure to develop — do not enter on the first candle
- Watch for an INITIATION signal

**Initiation signal:** Price BREAKS through a GEX level (break with conviction, not just a touch)

---

## PHASE 3 — THE ENTRY SEQUENCE

```
STEP 1 — INITIATION
  Price breaks a GEX level with momentum
  (Not enough to enter here — the next level may be in the way)

STEP 2 — VALUE BUILD
  After initiation, price consolidates at the new level
  Builds acceptance (value) at the new price

STEP 3 — RETURN TO LEVEL
  Price pulls back to the GEX level just broken
  That level now acts as the opposite (broken resistance → support)
  THIS IS THE ENTRY TRIGGER

STEP 4 — CONFLUENCE CHECK
  GEX level aligns with: order flow zone + volume profile level (VAH/VAL)
  Double or triple confluence = Grade A+ setup
```

---

## PHASE 4 — TARGET FRAMEWORK

```
NARRATIVE:      Built from main GEX levels (all-expiry + zero DTE gamma wall)
FIRST TARGET:   2R
SECOND TARGET:  Next GEX level in direction (put support or call resistance)
STOP LOSS:      Below/above the originating GEX level
```

---

## THE TWO-WORLD FUSION

Every entry combines:
- **Options world:** GEX levels (call resistance, put support, GEX 1-10)
- **Futures world:** Volume profile (VAH/VAL), order flow zones, value area

When both worlds point to the same level → maximum conviction.

---

## RULES

- "For me, it's not enough to take a trade right from here because we have this level in the way" — always know what's between entry and target before entering
- GEX levels are TARGETS and CONFIRMATION — never the trade narrative alone
- Most people slap GEX levels on a chart as S/R and wonder why it stops working — the WHY matters more than the WHERE

*D.S.E/trading/skills | STIS Layer 1b | GEX Daily Model | Source: Travis Woo GEX Daily Model video*

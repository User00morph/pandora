# SKILL — GAMMA REGIME MECHANICS
**The Deep Engine Behind Positive and Negative Gamma**
**Load when:** Need to understand WHY the current gamma regime produces the behavior it does.
**Department:** D.S.E trading workspace | STIS Layer 1b deep mechanics

---

## WHAT THIS IS

The mechanical explanation of HOW each gamma regime produces its market behavior. Not just classification (that's `skill_gex-regime-read.md`) — the step-by-step dealer loop that creates the effect.

---

## POSITIVE GAMMA — THE RUBBER BAND LOOP

NQ is in positive gamma **70-80% of the time.**

**The loop:**
```
NQ moves UP
  → Dealer Delta increases (they're long calls now more in-the-money)
  → They must SELL NQ to re-hedge
  → Selling pressure pushes NQ back DOWN
  → Dealer Delta decreases
  → They must BUY NQ to re-hedge
  → Buying pressure pushes NQ back UP
  → Loop repeats
```

**Result:** Price gets PINNED. Rubber band effect. Dealers constantly fight every move.

**Chart signatures:**
- Tight ranges
- Failed breakouts
- Absorption at highs and lows
- Slow drift with wicks
- "Chop" that seems random but is mechanical

**Trading approach:** Fade extensions. Take profits quickly. Never chase breakouts. If trading continuation — wait for overwhelming confirmation.

---

## NEGATIVE GAMMA — THE AMPLIFICATION LOOP

**The loop:**
```
NQ moves UP
  → Dealers are short calls (negative Delta exposure worsens)
  → They must BUY MORE NQ to re-hedge
  → Buying ADDS to the upward move
  → NQ moves further UP
  → Dealers must buy even more
  → Self-reinforcing acceleration

NQ moves DOWN
  → Dealers must SELL MORE NQ
  → Selling ADDS to the downward move
  → 400-500pt NQ drops in hours
```

**Result:** Dealers are SPONSORING the move. They are part of it.

**Chart signatures:**
- Strong sustained trends
- No meaningful pullbacks
- Moves that look "too fast"
- 400-500pt NQ drops in hours with no catalyst
- Breakouts that don't reverse

**Trading approach:** DO NOT FADE. You are fighting a mechanical force. Wait for additional confirmation from order flow and AMT before entering. Follow the trend — momentum is mechanically enforced.

---

## THE STAT

NQ in positive gamma: **70-80% of trading days.**
NQ in negative gamma: **20-30% of trading days** — but these are the big move days.

---

## INTEGRATION

| Gamma regime | What it means for execution |
|---|---|
| Positive | Grade A filter criterion 1 (HTF bias) can be softer — range trades valid |
| Negative | Bias must be unambiguous. Trend only. No fades under any circumstances |
| Transitioning (price near HVL) | Highest uncertainty — reduce size or wait for confirmation |

*D.S.E/trading/skills | STIS Layer 1b | Source: Travis Woo Options Flow video*

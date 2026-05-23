# SKILL — Markov State Read
**Hedge Fund Transition Matrix | Statistical Position Sizing**
**Load when:** Calibrating position size, assessing probability edge, determining holding time.
**Pine Script:** `tools/pine-scripts/markov_state_matrix.pine`
**Source:** Hedge fund method via "Rowan" | decoded in `drd_decode_quant-options-ai-trading-stack_v1.md`
**Department:** D.S.E trading workspace | STIS Layer 1c

---

## WHAT THIS IS

The Markov State Matrix is the statistical probability backbone of the STIS. It answers one question: given the current market state, what is the mathematical probability that the state persists or transitions tomorrow?

This is not prediction. It is probability. The same logic that makes "the trend is your friend" true — quantified into a number.

**Core principle:** The market's next move depends only on its CURRENT state — not on the history of how it got there. Only today has full weight. (Markov property)

---

## THE THREE STATES

```
BULL STATE:     20-day cumulative return ≥ +5%
SIDEWAYS STATE: 20-day cumulative return between -5% and +5%  
BEAR STATE:     20-day cumulative return ≤ -5%
```

These are not arbitrary labels. They represent whether the institutional money is net accumulating (bull), distributing (bear), or cycling internally (sideways).

---

## READING THE INDICATOR

Open `markov_state_matrix.pine` in TradingView (separate pane). The table shows:

```
MATRIX TABLE (top right):
  Rows = today's state (Bear / Side / Bull)
  Columns = tomorrow's state (Bear / Side / Bull)
  Each cell = historical % probability of that transition

  Currently active row = highlighted (the "now" state)

CURRENT STATE (bottom bar, first cell):
  "NOW: BULL" / "NOW: SIDEWAYS" / "NOW: BEAR"
  CUM% = the 20-day cumulative return that produced this state

SIGNAL (bottom bar, middle):
  "SIG: +0.45" → strong long bias
  "SIG: -0.28" → moderate short bias
  "SIG: +0.04" → near zero — no edge

BIAS (bottom bar):
  "LONG" / "SHORT" / "NEUTRAL"

STICKINESS (bottom bar, last cell):
  "STICK: 72%" → 72% probability current state continues tomorrow
```

---

## SIGNAL INTERPRETATION

The signal = P(bull tomorrow) - P(bear tomorrow), given the current state.

```
SIGNAL > +0.30:   STRONG LONG BIAS
  Statistical edge is clear. Full size eligible if other criteria met.
  Hold trades longer — high probability state persists.

SIGNAL +0.10 to +0.30:  MODERATE LONG BIAS
  Edge exists but not strong. 75-80% standard size.
  Take profits at GEX levels, don't hold for extended targets.

SIGNAL -0.05 to +0.10:  NEUTRAL / DEAD ZONE
  No meaningful statistical edge.
  Do not trade on Markov signal alone.
  Reduce size to 50% minimum regardless of other criteria.
  Wait for signal to strengthen before full-size trades.

SIGNAL -0.10 to -0.30:  MODERATE SHORT BIAS
  Statistical edge toward shorts. Same sizing rules as moderate long.

SIGNAL < -0.30:   STRONG SHORT BIAS
  Full short bias. Full size eligible on short setups.
```

---

## STICKINESS SCORE

Stickiness = diagonal probability = P(current state → same state tomorrow)

```
STICKINESS > 70%:
  Current state is very likely to persist.
  Trend-following approach is statistically sound.
  Higher holding time justified.
  Hold trades through pullbacks.

STICKINESS 50-70%:
  Moderate persistence. State could flip.
  Take partial profits at GEX levels.
  Do not hold through significant adverse moves.

STICKINESS < 50%:
  State instability. Transition is more likely than persistence.
  CAUTION: regime change may be underway.
  Reduce size. Widen mental stops. Watch for IEC phase transition signals.
  Log this as a potential regime change event.
```

---

## POSITION SIZING BY SIGNAL

The Markov signal directly modifies your base risk per trade:

```
BASE RISK: whatever your standard risk% is (e.g., 1% of account)

MULTIPLIER TABLE:
  Signal > +0.50:   1.25× base risk (max 1.5× — sovereign capital protection)
  Signal +0.30-0.50: 1.0× base risk (standard)
  Signal +0.10-0.30: 0.75× base risk
  Signal ±0.10:      0.50× base risk (caution zone)
  Signal -0.10 to -0.30: 0.75× base risk (short side)
  Signal < -0.30:    1.0× base risk (standard short)

STICKINESS MODIFIER (applied AFTER signal modifier):
  Stickiness > 70%: +0.10× (hold time extended, slightly larger ok)
  Stickiness 50-70%: no change
  Stickiness < 50%: -0.25× (instability — reduce regardless of signal)

COMBINED EXAMPLE:
  Signal = +0.38 (moderate long) × 1.0
  Stickiness = 65% → no change
  Final multiplier: 1.0 → standard size trade

  Signal = +0.52 (strong long) × 1.25
  Stickiness = 78% → +0.10
  Final multiplier: 1.35× → slightly above standard (respect sovereign capital limits)
```

---

## MATRIX SQUARING (MULTI-DAY FORECAST)

The transition matrix can be squared for N-day forecasts:
- 2-day forecast: matrix × matrix
- 3-day: matrix × matrix × matrix
- Signal degrades past day 3 — not actionable beyond that

**Practical application:**
The Pine Script does not display multi-day forecasts (would require complex Pine Math). Use it conceptually: if the 1-day signal is strong AND stickiness is high, the 2-day signal is approximately signal × signal (e.g., 0.80 × 0.80 = 64% — still strong, but decaying). Hold time for a strong/sticky state: up to 3 trading sessions max.

---

## INTEGRATION WITH OTHER STIS LAYERS

```
MARKOV + IEC:
  Markov Bull + IEC Phase 3 (Expansion) = MAXIMUM conviction long scenario
  Markov Bear + IEC Phase 5 (Reversal) = MAXIMUM conviction short scenario
  Markov Sideways + IEC Phase 1 (Accumulation) = NO TRADE — no edge at any layer

MARKOV + GAMMA:
  Markov Bull + Positive Gamma (mean-reverting) = Long bias but slow, choppy
    → Smaller targets, quicker exits, GEX level fades
  Markov Bull + Negative Gamma (trending) = Long bias with amplification
    → Standard targets, can hold through momentum, trail stops

MARKOV SIGNAL FOR P.M.I.B:
  Morning brief adds: "Markov: [STATE] | Signal: [X.XX] | Stick: [X]%"
  This sets the statistical bias frame for the entire session BEFORE chart analysis
```

---

## REGIME TRANSITION SIGNALS

Watch for these in the indicator:

```
STATE TRANSITION JUST OCCURRED:
  20-day return has just crossed ±5% threshold
  The stickiness is LOWER at the start of a new state (fewer transitions in history)
  New states are less reliable — reduce size until the state has been active 3+ days

STATE INSTABILITY:
  Stickiness drops below 50%
  Signal magnitude is declining (was strong, now weakening)
  Action: halve position size, tighten targets

APPROACHING STATIONARY DISTRIBUTION:
  After 7+ days in any state, N-day forecast convergence makes the signal less useful
  Signal still valid for 1-day reads, but multi-day holds lose statistical backing
```

---

*D.S.E/trading/skills | STIS Layer 1c — Quant/Markov | Pandora OS*
*Pine Script: tools/pine-scripts/markov_state_matrix.pine*
*Source: drd_decode_quant-options-ai-trading-stack_v1.md | Hedge Fund Method*

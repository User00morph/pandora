# SKILL — MARKOV STATE MACHINE
**The Hedge Fund Probability Framework for Regime Classification**
**Load when:** Running regime analysis on any asset, building or evaluating a systematic strategy.
**Department:** D.S.E trading workspace | STIS Quant Layer

---

## WHAT THIS IS

The complete Markov regime framework used by hedge fund quants. Not chart patterns, not indicators — mathematical state classification and transition probabilities. This is how quants replaced "it feels bullish" with "there is a 72% probability of bull state tomorrow."

---

## THE THREE STATES

| State | Definition |
|---|---|
| **BULL** | 20-day cumulative return ≥ +5% |
| **BEAR** | 20-day cumulative return ≤ -5% |
| **SIDEWAYS** | Everything between -5% and +5% |

**Note on the thresholds:** The 5% boundary is the standard starting point, but it is inherently subjective — a human chose it. This is why the Hidden Markov Model (see `skill_hidden-markov-model.md`) exists as a validation layer — it discovers states from the data itself without any threshold assumption. The ±5% boundaries should be treated as an initial approximation, confirmed by HMM agreement before trading on the signal.

**"This sounds elementary, but wait until you see how they use this information."** — The simplicity of the three-state system is intentional. Complexity is in the transition matrix. The state definition is the foundation.

**Labeling protocol:** Run the algorithm over the ENTIRE asset history. Every day from day 20 forward gets labeled with its state. The result is a complete state history for the asset.

---

## THE TRANSITION MATRIX (3×3 Grid)

Count every historical state transition and convert to percentages:

```
             TOMORROW
             Bull    Bear    Sideways
TODAY Bull  [  %  ] [  %  ] [  %  ]    ← must sum to 100%
      Bear  [  %  ] [  %  ] [  %  ]    ← must sum to 100%
      Sidew [  %  ] [  %  ] [  %  ]    ← must sum to 100%
```

This matrix updates every day as new data is added. It is the live probability scoreboard.

---

## THE MARKOV PROPERTY

Only today's state matters. The full historical path is irrelevant to tomorrow's prediction. "The way you get to New York from Ohio has nothing to do with starting in Little Rock."

Implication: the matrix is always current, never anchored to distant history.

---

## PERSISTENCE / STICKINESS

The diagonal (bull→bull, bear→bear, sideways→sideways) = the stickiness scores.

- Bull states: typically 75-85% sticky
- Bear states: typically 70-80% sticky
- Sideways: least sticky (most likely to transition)

**"The trend is your friend" expressed as a probability, not a feeling.**

---

## MULTI-DAY FORECASTING

Square the matrix for 2-day forecast. Cube for 3-day.

```
P(bull in 2 days | bull today) = P(bull→bull)²
Example: 0.80 × 0.80 = 0.64 → 64% probability
```

**Practical limit:** 1-3 day forecasts carry meaningful signal. Beyond 7-10 days → stationary distribution → all probabilities converge → no meaningful signal.

---

## INTEGRATION WITH STIS

The Markov state machine provides the statistical regime layer (Layer 1c) that complements:
- GEX regime (Layer 1b): mechanical options flow classification
- IEC phase (Layer 1a): institutional price structure classification

When all three agree → maximum conviction.

## IMPLEMENTATION

The Markov state machine can be installed as a Claude Code skill via the packaging protocol in `skill_claude-code-skill-packaging.md`. Once installed, invoke with `/markov` on any ticker to run the full hedge fund method — state labeling, transition matrix, signal generation, and walk-forward validation.

The Pine Script visualization (3×3 matrix on TradingView chart) shows live transition probabilities for the current asset at a glance.

*D.S.E/trading/skills | STIS Quant Layer | Markov Framework | Source: Travis Woo Quant Strategy video + MTP Backtesting video*

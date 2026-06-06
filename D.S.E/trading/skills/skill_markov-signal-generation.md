# SKILL — MARKOV SIGNAL GENERATION
**Extracting Directional Signals and Position Sizing from the Transition Matrix**
**Load when:** Generating trade signals from the Markov state machine output.
**Department:** D.S.E trading workspace | STIS Quant Layer | Signal layer

---

## WHAT THIS IS

The extraction protocol for converting transition matrix probabilities into a directional signal AND position size in a single calculation. No discretion. No judgment. One number determines both.

---

## THE SIGNAL FORMULA

```
SIGNAL = P(bull tomorrow) − P(bear tomorrow)

Positive result → LONG
Negative result → SHORT
Magnitude → POSITION SIZE
```

**Example:**
```
P(bull tomorrow) = 65%
P(bear tomorrow) = 20%
P(sideways)      = 15%   ← ignored in the signal

SIGNAL = 65% − 20% = +45%

Direction:      LONG
Conviction:     45% (strong — size up)
```

---

## SIGNAL-TO-SIZE CALIBRATION

Each operator defines their own calibration. Sovereign calibration template:

| Signal differential | Position size |
|---|---|
| 0% to 15% | Skip or micro size (0.25× normal) |
| 15% to 30% | Half size (0.5× normal) |
| 30% to 45% | Standard size (1× normal) |
| 45% to 60% | Full size (1.5× normal) |
| Above 60% | Maximum size (2× normal) |

---

## NEGATIVE SIGNAL = SHORT

Same formula applies in reverse:
```
P(bear tomorrow) > P(bull tomorrow) → negative number → SHORT signal
Magnitude determines short position size by same calibration table
```

---

## THE STATIONARY DISTRIBUTION LIMIT

As the forecast horizon extends (matrix squared repeatedly), all probability rows converge to identical values. When this happens, the signal differential approaches zero — no meaningful edge.

```
1-day forecast:   Strong signal possible
2-3 day forecast: Moderate signal, lower conviction
7-10 day:         Approaching stationary distribution
Beyond 10 days:   Effectively no signal — uniform probabilities
```

**Practical rule:** Only use 1-3 day Markov signals. Beyond that, use trend-following (ATR stop) instead.

---

## RULES

- The signal is always P(bull) − P(bear) — never just P(bull) alone
- Sideways probability is informational only — it dampens the signal indirectly via the row sum
- Recalculate the signal every day — the matrix updates daily
- Signal below 15% differential = skip the trade, regardless of direction

*D.S.E/trading/skills | STIS Quant Layer | Signal Protocol | Source: Travis Woo Quant Strategy video*

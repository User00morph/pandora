# SKILL — QUANT-DISCRETIONARY TRANSLATION
**Converting Every Trading Judgment into a Numerical Value**
**Load when:** Evaluating a trade, reviewing a strategy decision, or auditing discretionary bias.
**Department:** D.S.E trading workspace | STIS System Design | Quantification layer

---

## WHAT THIS IS

The translation protocol from "how I feel about this trade" to "what the numbers say about this trade." Every discretionary judgment has a quantified equivalent. The goal is not to remove intuition — it is to verify intuition with numbers before acting on it.

---

## THE TRANSLATION TABLE

| Discretionary statement | Quantified equivalent |
|---|---|
| "It feels bullish" | "20-day return is +7.3% — bull state confirmed" |
| "The trend is strong" | "Markov bull stickiness score: 84%" |
| "Big setup today" | "Signal differential: +47% — maps to full size" |
| "The market is choppy" | "In positive gamma — dealer dampening confirmed" |
| "This level is important" | "GEX 1 + prior session POC + VAH all at same price" |
| "I feel confident" | "4/4 STIS layers aligned — A+ grade filter pass" |
| "The move is extended" | "Price at gamma wall + kurtosis elevated — reduce" |
| "Something feels off" | "Vanna headwind + negative Markov signal — skip" |

---

## THE QUANTIFICATION PROTOCOL

For any trade under consideration, run these checks before entering:

```
STEP 1 — STATE (Markov)
  What is the current 20-day return?
  What state does it map to?
  What is the transition probability for tomorrow?
  Signal = P(bull) − P(bear) = [number]

STEP 2 — FORCE (Options flow)
  What is VIX doing? → Vanna direction
  Where is price vs. HVL? → Gamma regime
  What is the dominant force today?

STEP 3 — STRUCTURE (IEC + GEX)
  What IEC phase is this instrument in?
  What is the GEX level stack?
  Where is the session POC relative to price?

STEP 4 — GRADE (Filter)
  How many grade-A criteria pass?
  A+ = enter at full size
  B = enter at half size
  C or below = pass
```

---

## THE SOVEREIGN PRINCIPLE

Quants do not use trendlines and indicators on a chart to make decisions. They quantify. The process: raw data → quantified states → probability matrix → numerical signal → calibrated position size → execution.

No judgment enters this chain between state and execution. Feelings are valid inputs to the QUANTIFICATION process. They are not valid outputs that drive DECISIONS.

---

## RULES

- If a judgment cannot be quantified, it cannot be acted on without explicit Markov/GEX/IEC confirmation
- "I think" statements require quantified backing before becoming trades
- After every session: audit which trades were taken on feelings vs. numbers — track both separately

*D.S.E trading workspace | STIS System Design | Source: Travis Woo Quant Strategy video*

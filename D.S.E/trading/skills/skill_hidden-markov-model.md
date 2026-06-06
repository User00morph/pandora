# SKILL — HIDDEN MARKOV MODEL
**Objective State Discovery and Double Confirmation Protocol**
**Load when:** Running high-conviction regime analysis or verifying Markov state labels.
**Department:** D.S.E trading workspace | STIS Quant Layer | Confirmation layer

---

## WHAT THIS IS

The solution to the weakest link in the Markov state machine: human-defined state thresholds are subjective. The HMM discovers states from the data itself — no labels, no assumptions, no human bias. When HMM-derived states and manually-labeled states agree = double confirmation = highest conviction signal.

---

## THE PROBLEM IT SOLVES

Manual state definition: "Bull = +5% over 20 days" — a human decided that threshold. It could be 3%, it could be 7%. The entire system is only as objective as this one subjective input.

"This is our natural floor — everything is calculated and mathematical, except this weakest link."

---

## HOW THE HMM WORKS

```
INPUT:  Raw price/return data — NO labels attached
PROCESS:
  1. HMM observes the full price history without any state labels
  2. It looks for internal patterns: momentum, mean-reversion, volatility clustering
  3. It identifies recurring behavioral regimes from the data itself
  4. It assigns labels AFTER discovery — not before
OUTPUT: A state history derived entirely from data behavior, not human thresholds
```

**The babysitter analogy:** The babysitter arrives knowing nothing about the children. After several days of observation, she identifies ADHD child, sleepy child, hyperactive child — from behavior alone. The HMM is the babysitter. The market data is the children.

---

## THE DOUBLE CONFIRMATION PROTOCOL

Run BOTH labeling methods on the same asset:

```
METHOD A: Manual labels (20-day return thresholds)
  → Produces: state history with human-defined boundaries

METHOD B: HMM labels (data-discovered states)
  → Produces: state history from behavioral patterns

COMPARE:
  Agreement = HIGH CONVICTION → proceed at full size
  Disagreement = CONFLICTING EVIDENCE → reduce size or pass
```

**The principle:** Two independent methods arriving at the same regime classification is stronger evidence than either alone.

---

## PRACTICAL APPLICATION IN STIS

When the Markov transition matrix generates a signal:

1. Run the HMM on the same asset for the same period
2. Check: does the HMM classify today's regime the same way as the manual labels?
3. If yes → signal confidence ↑, full size
4. If no → signal confidence ↓, reduce to half size or skip

---

## RULES

- The HMM does not replace the transition matrix — it VALIDATES it
- Double confirmation only upgrades a signal; single-method disagreement degrades it
- The HMM requires sufficient data history to work — minimum 200 bars recommended

*D.S.E/trading/skills | STIS Quant Layer | HMM Confirmation | Source: Travis Woo Quant Strategy video*

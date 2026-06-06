# SKILL — MEDIAN PARAMETER PROTOCOL
**Anti-Overfitting Parameter Selection via Range Identification**
**Load when:** Finalizing parameters for any trading system before live deployment.
**Department:** D.S.E trading workspace | STIS System Validation | Anti-overfitting layer

---

## WHAT THIS IS

The median parameter protocol prevents the most common systematic trading failure: selecting the single "best" parameter set that happens to be at the edge of what works — where any small shift into the future makes it unprofitable.

---

## THE PROTOCOL

```
STEP 1 — BROAD SEARCH
  Run 200-300 backtest trials across the full parameter space
  Each trial uses a randomly selected combination of parameters
  Record all results

STEP 2 — IDENTIFY THE PROFITABLE RANGE
  Sort all trials by the optimization metric (Kalmar)
  Identify the top 20-30 combinations that perform best
  Extract the parameter values used in those top combinations

STEP 3 — SELECT THE MEDIAN
  For each parameter (stop loss, look-back, pyramid max, etc.):
    Sort the values from the top 20-30 combinations
    Select the MEDIAN value (not the best, not the mean — the median)

STEP 4 — VERIFY ADJACENT VALUES STILL WORK
  For each parameter, test median ± 1 step
  If adjacent values are unprofitable → the range is a knife edge → unsafe
  If adjacent values are still profitable → the range is robust → safe to deploy
```

---

## WHY THE MEDIAN, NOT THE BEST

If stop loss values 3, 4, 5, 6, 7, 8, 9, 10 all produce profitable backtests, but the "best" was value 3:
- Picking 3: one market-condition shift could push real performance to 2 (unprofitable)
- Picking 6 (median): surrounded by profitable values on both sides — robust to market evolution

"If the stop loss works from 3 to 10, I want to pick 6."

---

## WALK-FORWARD CONFIRMATION

After selecting median parameters, validate with walk-forward:
- Test on rolling 10-year out-of-sample blocks
- The median parameters should remain in the top quartile across all decades
- If they're top quartile in one decade but bottom quartile in another → the range may be regime-specific
- Regime-specific parameters need a regime-detection layer before they can be deployed

---

## PARAMETER SENSITIVITY CHECK

| Result | Interpretation | Action |
|---|---|---|
| Adjacent values profitable | Robust — structural edge | Deploy with confidence |
| Adjacent values unprofitable | Knife-edge — overfit | Run more trials, find wider range |
| No profitable range found | Edge may not exist | Redesign the system |

---

## RULES

- Never pick the single best parameter from a backtest — always identify the range first
- The width of the profitable range is a direct measure of how robust the edge is
- Apply this protocol to EVERY parameter independently

*D.S.E/trading/skills | STIS System Validation | Source: Travis Woo MTP Backtesting video*

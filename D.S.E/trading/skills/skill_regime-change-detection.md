# SKILL — REGIME CHANGE DETECTION
**Mathematical Framework for Identifying Structural Market Shifts**
**Load when:** Analyzing whether a market has regime-shifted, evaluating model performance degradation.
**Department:** D.S.E trading workspace | STIS Quant Layer | Regime monitoring

---

## WHAT THIS IS

A regime change is not "the market is different now" — it has a precise mathematical definition. This skill provides the diagnostic tools to identify when a regime has shifted and what type of shift occurred.

---

## MATHEMATICAL DEFINITION

A regime change = when a time series exhibits **non-stationary dynamics** — i.e., when its statistical properties are no longer invariant over time.

**The four statistical moments that define any distribution:**

| Moment | What it measures | Regime change signal |
|---|---|---|
| **Mean** | Average direction | Mean flips from positive to negative |
| **Variance** | Spread / volatility | Variance explodes or collapses |
| **Skewness** | Asymmetry | Skewness shifts from positive to negative |
| **Kurtosis** | Fat tail probability | Kurtosis spikes = extreme events incoming |

A regime change can involve ONE or MULTIPLE moments shifting simultaneously. FTX collapse 2022: mean flipped negative + kurtosis exploded + skewness went deeply negative = three simultaneous regime shifts.

---

## THE EMPIRICAL DETECTION METHOD

Group asset returns by period (month or quarter). Calculate all four moments for each period. Visual inspection:

```
STABLE REGIME:   Moments remain similar period to period
REGIME CHANGE:   One or more moments shift structurally between periods

Red flags:
  - Mean flips sign (positive to negative or vice versa)
  - Variance doubles or halves
  - Skewness crosses zero
  - Kurtosis spikes above 5-6 (extreme fat tails)
```

---

## THE RED FLAG PATTERN (model failure signal)

When a model's equity curve looks **identical to the underlying price chart** (just rescaled):
- The model learned nothing — it's predicting "up" 98% of the time
- It captured the historical distribution perfectly
- It will fail immediately when the regime shifts
- **This is the primary signal that a model is not adaptive**

A healthy adaptive model's equity curve looks DIFFERENT from the underlying — it should be flat or rising during bear markets, not collapsing with them.

---

## STIS APPLICATION

After any significant drawdown on a live strategy, run this diagnostic:

```
1. Calculate the four moments for the pre-drawdown period
2. Calculate the four moments for the drawdown period
3. Compare: which moments shifted?
4. Identify the regime change type
5. Determine whether the strategy's edge assumption still holds
   under the new distribution
```

If the regime has shifted and the strategy's edge was distribution-dependent → pause the strategy and re-validate.

---

## RULES

- Regime changes are facts — the market shifted. Not failures of the trader.
- Drawdowns within the same regime = normal variance. Drawdowns caused by regime shift = structural issue.
- A model that performs equally in all regimes has found a genuine edge. A model that works only in one regime is a bet on that regime continuing.

*D.S.E/trading/skills | STIS Quant Layer | Regime Detection | Source: Travis Woo Regime Changes video*

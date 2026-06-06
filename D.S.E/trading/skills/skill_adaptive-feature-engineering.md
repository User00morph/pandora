# SKILL — ADAPTIVE FEATURE ENGINEERING
**Building Regime-Aware Features for Any Predictive Model**
**Load when:** Building or improving a quantitative model that will be used across multiple market regimes.
**Department:** D.S.E trading workspace | STIS Quant Layer | Model building

---

## WHAT THIS IS

The two methods for making any supervised model adaptive to regime changes. Static features (single current return) fail when the market distribution shifts. These methods give models historical context that changes with the market.

---

## METHOD A — ROLLING MEMORY ENCODING

Replace the single current-period return with a rolling average of past N returns.

```
STATIC FEATURE:   current_return (t)  ← fails when distribution changes
MEMORY FEATURE:   rolling_mean(returns[t-N : t-1])  ← adapts to current dynamics
```

**Why it works:** The rolling mean compresses recent distribution dynamics into a single number. The model now knows whether recent behavior is trending up, down, or flat — giving it regime context that the single-period feature lacks.

**The lag rule (critical):** Always use `t-1` through `t-N`, NEVER include `t` (the current period). Including the current period = data leakage — the model would be encoding the return it's supposed to predict.

**Typical window:** 20-40 periods. Too short = noise. Too long = too slow to detect regime shifts.

---

## METHOD B — RELATIVE MEMORY (Current vs. Historical)

Pass BOTH the current return AND the rolling average as features simultaneously.

```
FEATURE 1:  current_return (lagged: t-1)
FEATURE 2:  rolling_mean(returns[t-N : t-1])
```

The model learns the weighted relationship between the two — discovering a momentum/mean-reversion signal endogenously. When current return is above its rolling average = momentum. Below = mean-reversion pressure.

**Result:** Signal distribution shifts from 98% directional (biased, non-adaptive) to ~50/50 (genuinely adaptive) — because the model now bets both directions based on current vs. historical context.

---

## SIGNAL HEALTH CHECK

After adding memory features, check the prediction distribution:

```
UNHEALTHY:  98% predictions in one direction
            → Model learned historical bias only
            → Will fail on regime shift

HEALTHY:    ~50/50 or proportional to actual distribution
            → Model is genuinely adaptive
            → Can respond to regime shifts
```

---

## THE INTERPRETABILITY PRINCIPLE

Use linear regression models when possible for adaptive features:
- Only 2 parameters (weight + bias) → fully interpretable
- Can see at every time step whether the model is in momentum or mean-reversion mode
- Neural networks with thousands of parameters = black box = cannot diagnose when it fails

---

## RULES

- Never include the current period in any rolling calculation (lag rule is absolute)
- Window size selection: backtest multiple values, pick the one that generalizes across regimes
- Memory features are preprocessing — they improve any base model without changing its architecture

*D.S.E/trading/skills | STIS Quant Layer | Adaptive Features | Source: Travis Woo Regime Changes video*

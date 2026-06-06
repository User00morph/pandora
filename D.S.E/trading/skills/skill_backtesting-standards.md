# SKILL — BACKTESTING STANDARDS
**Minimum Requirements for a Valid Trading System Backtest**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Evaluating any backtest before deployment, or designing a new validation protocol
DEPARTMENT: D.S.E + D.I.I | STIS System Validation | Minimum standards
LOADS:      skill_data-leakage-prevention.md (integrity check must pass first)
            skill_walk-forward-backtesting.md (the methodology used)
PRODUCES:   PASS / FAIL verdict on each standard + overall deployment readiness
CROSS-REF:  skill_system-robustness-stack.md (6-layer framework that uses these standards)
            skill_red-team-protocol.md (adversarial check after standards pass)
            skill_parameter-sensitivity-test.md (robustness of parameters)
```

---

## WHAT THIS IS

Minimum viability standards for any backtested trading system. A backtest that fails any of these standards is providing false confidence. These standards are not optional — they are the difference between evidence-based trading and expensive guessing.

---

## THE SEVEN MINIMUM STANDARDS

### STANDARD 1 — DATA INTEGRITY
```
□ No data leakage (see skill_data-leakage-prevention.md — must pass first)
□ Train/test split chronological (no shuffling)
□ Normalization fit on training set only
□ All features use lagged values

MINIMUM PASSING: ALL four checks clean
```

---

### STANDARD 2 — SAMPLE SIZE
```
□ Total trades in backtest: ≥ 100 (minimum statistical relevance)
□ Out-of-sample trades: ≥ 30 (enough to detect real performance vs. luck)
□ Trade frequency: not so high that it's dominated by transaction costs

MINIMUM PASSING: 100+ total trades, 30+ out-of-sample
```

---

### STANDARD 3 — HISTORICAL DEPTH
```
□ Backtest period: ≥ 20 years (minimum two full market cycles)
□ Preferred: ≥ 50 years (includes multiple regime types)
□ Gold standard: ≥ 100 years (for S&P and Gold — data available)
□ Must include at least one major crash (1929, 2000, 2008, 2020, or equivalent)

MINIMUM PASSING: 20 years, includes at least one major bear market
```

---

### STANDARD 4 — MULTI-ASSET VALIDATION
```
□ System profitable on ≥ 3 uncorrelated asset classes
□ Same parameters applied to all assets (no asset-specific tuning)
□ Assets span different market types: equities, commodities, crypto, forex

MINIMUM PASSING: 3 uncorrelated assets with same parameters
PREFERRED: 5-7 assets (full STIS portfolio)
```

---

### STANDARD 5 — PARAMETER ROBUSTNESS
```
□ Median parameter selection (not best-fit)
□ Adjacent parameter values still profitable (see skill_parameter-sensitivity-test.md)
□ Parameters stable across decades (walk-forward shows no major drift)

MINIMUM PASSING: Profitable range ≥ 3 adjacent parameter values
```

---

### STANDARD 6 — REALISTIC EXECUTION ASSUMPTIONS
```
□ Slippage modeled (at minimum 1 ATR unit beyond signal price)
□ Transaction costs included (commissions, spreads, funding)
□ Position sizing based on available margin, not unlimited capital
□ No curve-fitting to known market events (no "if date = X then...")

MINIMUM PASSING: All four execution realism checks
```

---

### STANDARD 7 — PERFORMANCE MEETS MINIMUM THRESHOLDS
```
□ Positive expectancy: E[return per trade] > 0
□ Profit factor ≥ 1.5 (total wins / total losses ≥ 1.5)
□ Maximum drawdown ≤ the operator's psychological tolerance
□ Winning years: ≥ 60% of tested years (70%+ preferred)
□ No single year accounts for > 50% of total returns

MINIMUM PASSING: All five checks
```

---

## THE OVERALL VERDICT

```
7/7 standards pass:  VALIDATED — proceed to paper trading
5-6/7 standards:     CONDITIONAL — fix failing standards before paper trading
3-4/7 standards:     NOT READY — significant development needed
Below 3:             RESTART — fundamental issues with the system design
```

---

## THE STANDARDS SCORECARD

```
BACKTEST STANDARDS AUDIT — [STRATEGY NAME] — [DATE]

Standard 1 (Data integrity):      [PASS/FAIL — notes]
Standard 2 (Sample size):         [PASS/FAIL — N trades: X]
Standard 3 (Historical depth):    [PASS/FAIL — years: X]
Standard 4 (Multi-asset):         [PASS/FAIL — assets tested: list]
Standard 5 (Parameter robust):    [PASS/FAIL — range: X-Y]
Standard 6 (Execution realistic): [PASS/FAIL — notes]
Standard 7 (Performance thresh):  [PASS/FAIL — key metrics]

OVERALL: [X/7] → [VALIDATED / CONDITIONAL / NOT READY / RESTART]
NEXT STEP: [specific action]
```

*D.S.E + D.I.I | STIS System Validation | Backtesting Standards*

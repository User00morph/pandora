# SKILL — DATA LEAKAGE PREVENTION
**Ensuring All Backtests and Models Use Only Past Information**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Building or auditing any backtest, ML model, or trading signal
DEPARTMENT: D.S.E + D.I.I | STIS System Validation | Data integrity
LOADS:      None — this is a validation standard applied to any model
PRODUCES:   Leakage audit report: CLEAN or COMPROMISED + specific issues found
CROSS-REF:  skill_walk-forward-backtesting.md (the validation methodology that uses this)
            skill_adaptive-feature-engineering.md (lag rule applied in feature building)
            skill_backtesting-standards.md (minimum validation requirements)
```

---

## WHAT THIS IS

Data leakage occurs when a model or backtest uses information that would not have been available at the time of the decision. It is the most common cause of backtests that look spectacular but fail immediately in live trading. This skill audits for all known leakage patterns.

---

## THE CARDINAL RULE

**A model making a prediction for time T may only use information from times T-1 and earlier.**

No exceptions. Any violation — however minor — invalidates the backtest.

---

## THE FIVE LEAKAGE PATTERNS

### PATTERN 1 — DATA SHUFFLING (most common)
```
VIOLATION: Shuffling time-series data before splitting into train/test sets
WHY IT LEAKS: Shuffling allows future data points to appear in the training set
SYMPTOM: Model performs equally well on "past" and "future" data

DETECTION: Check if the train/test split preserves chronological order
FIX: Always split by time: first 80% of dates = train, last 20% = test
     NEVER shuffle financial time series
```

---

### PATTERN 2 — CURRENT PERIOD IN ROLLING FEATURE
```
VIOLATION: Computing a rolling average that includes the CURRENT bar's value
WHY IT LEAKS: The current return is what the model is supposed to predict —
              including it in the feature encodes the answer

EXAMPLE:
  LEAKY:   rolling_avg = mean(returns[t-4 : t])   ← includes t (current)
  CLEAN:   rolling_avg = mean(returns[t-5 : t-1]) ← only uses past data

DETECTION: Inspect every rolling calculation for the endpoint
FIX: Always use lag(1) on the feature — returns[t-N : t-1]
```

---

### PATTERN 3 — SCALER FIT ON FULL DATASET
```
VIOLATION: Fitting a StandardScaler or normalization on the complete dataset
           before splitting into train/test
WHY IT LEAKS: The scaler learns the mean/std of future data when normalizing
              past data — future information contaminates the past features

DETECTION: Check if normalization was applied before or after the split
FIX: Fit the scaler ONLY on the training set
     Apply (transform only) to the test set using the train-fitted scaler
```

---

### PATTERN 4 — LOOK-AHEAD BIAS IN INDICATORS
```
VIOLATION: Technical indicators that require future data to complete
WHY IT LEAKS: Standard "centered" moving averages use future bars to smooth

DETECTION: Any indicator that draws a "smooth" curve through historical data
           is likely using future data
FIX: Use "right-aligned" indicators only (only past bars used in calculation)
     In Pine Script: use the bar_index to verify no future-referencing
```

---

### PATTERN 5 — OPTIMIZATION ON TEST SET
```
VIOLATION: Adjusting parameters after seeing test set performance
WHY IT LEAKS: Test set is no longer out-of-sample — it's been used in optimization
SYMPTOM: Parameters that "work perfectly" on the test period fail immediately live

DETECTION: Were parameters changed after looking at test results?
FIX: Complete all optimization on the training set ONLY
     Test set is used ONCE — for final validation, never for tuning
```

---

## THE AUDIT CHECKLIST

Run this on every backtest or model before considering it validated:

```
□ Train/test split: chronological order preserved (no shuffling)?
□ Rolling features: use lagged values only (t-1 through t-N)?
□ Normalization/scaling: fitted on training set only?
□ Indicators: right-aligned (no centered/future-using indicators)?
□ Parameters: optimized without referencing test set performance?
□ Walk-forward: each day's prediction uses only historical data?

RESULT:
  All ✓ → CLEAN backtest, proceed to walk-forward validation
  Any ✗ → COMPROMISED — do not trust results, fix before proceeding
```

---

## RULES

- A compromised backtest produces fictional results — it is worse than no backtest
- When in doubt about any feature or calculation: apply an additional lag
- The integrity of the backtest determines the validity of every trading decision that follows from it

*D.S.E + D.I.I | STIS System Validation | Data Integrity*

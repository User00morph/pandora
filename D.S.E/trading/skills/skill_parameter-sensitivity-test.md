# SKILL — PARAMETER SENSITIVITY TEST
**Verifying That Your Parameters Are Not on a Knife Edge**
**Load when:** After finalizing any parameter set, before any live deployment.
**Department:** D.S.E trading workspace | STIS System Validation | Robustness testing

---

## WHAT THIS IS

A parameter sensitivity test verifies that the selected parameter values are surrounded by profitable territory — not sitting on a narrow peak that collapses with any small deviation. A system whose performance only works at exactly one parameter value is overfit regardless of its backtest results.

---

## THE TEST

For each parameter in the system, test the selected value and its immediate neighbors:

```
PARAMETER: Stop loss multiplier. Selected value: 6

Test set:
  Stop = 4  → record Kalmar ratio
  Stop = 5  → record Kalmar ratio
  Stop = 6  → record Kalmar ratio (selected)
  Stop = 7  → record Kalmar ratio
  Stop = 8  → record Kalmar ratio

PASS CRITERIA:
  All or most adjacent values are profitable (positive Kalmar)
  The performance curve is smooth — not a sharp spike at exactly 6

FAIL CRITERIA:
  Only stop = 6 is profitable
  Stop = 5 and stop = 7 are both unprofitable or sharply worse
  This is a knife edge — the system is overfit to exactly this value
```

---

## THE SENSITIVITY MAP

Create this for every parameter:

```
        Kalmar Ratio
   2.5 |         *
   2.0 |       * * *
   1.5 |     * * * * *
   1.0 |   * * * * * * *
   0.5 |         * * *
   0.0 |
      ┼─────────────────
       3   4   5  [6]  7   8   9
            Stop Loss Multiplier

This is a GOOD sensitivity map — wide profitable range,
the selected value (6) is near the peak of a smooth curve.
```

```
        Kalmar Ratio
   2.5 |         *
   2.0 |         *
   1.5 |         *
   1.0 |         *
   0.5 |
   0.0 | * * * * | * * *
      ┼─────────────────
       3   4   5  [6]  7   8   9

This is a BAD sensitivity map — knife edge.
Only exactly 6 works. This is an overfit system.
```

---

## THE RANGE WIDTH STANDARD

| Profitable range width | Assessment |
|---|---|
| ≥ 5 adjacent values | Very robust — likely structural edge |
| 3-4 adjacent values | Acceptable — deploy with monitoring |
| 1-2 adjacent values | Marginal — consider widening the range first |
| Only the exact value | Do NOT deploy — overfit |

---

## RULES

- Run the sensitivity test on ALL parameters simultaneously AND individually
- A system can pass individual parameter tests but fail when all parameters are tested together (interaction effects)
- Document the sensitivity map for each parameter in the strategy log — compare quarterly to detect drift

*D.S.E/trading/skills | STIS System Validation | Source: Travis Woo MTP Backtesting video*

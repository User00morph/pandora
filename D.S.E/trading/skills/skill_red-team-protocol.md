# SKILL — RED TEAM PROTOCOL
**Adversarial Verification of Trading Strategies Before Live Deployment**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  A strategy has passed walk-forward backtesting and is being considered
            for paper trading; or quarterly review of live strategies
DEPARTMENT: D.I.I + D.S.E | STIS Strategy Validation | Adversarial layer
LOADS:      skill_walk-forward-backtesting.md (the validation the red team reviews)
            skill_system-robustness-stack.md (the standard being challenged)
PRODUCES:   Red team report: failure modes found + stress test results + GO/NO-GO verdict
CROSS-REF:  skill_strategy-lifecycle-management.md (red team is a stage gate)
            skill_paper-trading-gateway.md (follows red team approval)
            skill_edge-decay-monitoring.md (monitors after live deployment)
```

---

## WHAT THIS IS

The red team's job is to DESTROY the strategy argument. Not to evaluate quality — quality is the backtester's job. The red team assumes the strategy will fail and works backward to find how. If it can't find a credible failure mode, the strategy has earned the right to paper trading.

---

## THE RED TEAM MANDATE

```
"Your job is not to validate this strategy. Your job is to break it.
 Find every assumption. Challenge every one.
 Find every condition under which this strategy would fail catastrophically.
 If you cannot find a credible failure scenario after thorough adversarial analysis,
 then — and only then — does the strategy advance."
```

---

## THE SEVEN CHALLENGES

### CHALLENGE 1 — CURVE FIT ATTACK
```
QUESTION: Is this strategy truly general, or is it memorizing the historical data?

TESTS:
  □ Run on assets NOT used in optimization — does it still produce positive results?
  □ Run on a completely different market (e.g., Japanese market if optimized on US)
  □ Shift the start date by 5 years — does performance remain stable?
  □ Apply the median parameter variation (±1 step) — is it still profitable?
  
RED FLAG: Performance collapses on any of these → strategy is overfit
```

---

### CHALLENGE 2 — REGIME DEPENDENCY ATTACK
```
QUESTION: Does this strategy ONLY work in one market regime?

TESTS:
  □ Isolate performance in bull regimes vs. bear regimes vs. sideways
  □ If 90%+ of profits came from one regime type → regime-dependent
  □ What happens when that regime ends? (as all regimes eventually do)
  
RED FLAG: Strategy profitable only in bull regimes with no bear protection
```

---

### CHALLENGE 3 — EXECUTION REALITY ATTACK
```
QUESTION: Would this strategy work in actual live markets?

TESTS:
  □ Slippage stress test: add 50% more slippage than backtest assumed
  □ Liquidity test: can the required position sizes be filled at signal prices?
  □ Market hours test: do signals fire at times when markets are liquid?
  □ Platform reliability test: what happens if the execution is delayed 1-2 bars?
  
RED FLAG: Strategy performance depends on perfect fills at exact signal prices
```

---

### CHALLENGE 4 — EDGE ASSUMPTION ATTACK
```
QUESTION: Is the reason this strategy works still true?

STATE THE EDGE ASSUMPTION:
  "This strategy works because [specific reason]"
  
CHALLENGE IT:
  □ When would this assumption break?
  □ Has there been any historical period when this assumption was false?
  □ Are there current macro conditions that would invalidate it?
  □ Is this assumption based on structural factors or temporary conditions?
  
RED FLAG: Edge assumption cannot be clearly stated, or it depends on conditions
          that may not persist
```

---

### CHALLENGE 5 — CONCENTRATION ATTACK
```
QUESTION: Is performance driven by one asset/period that may not repeat?

TESTS:
  □ Remove the single best-performing asset — is the system still profitable?
  □ Remove the single best-performing year — is the system still profitable?
  □ If removing one asset/year drops the system below viability → concentration risk
  
RED FLAG: 70%+ of profits came from one asset or one brief market event
```

---

### CHALLENGE 6 — DRAWDOWN SURVIVABILITY ATTACK
```
QUESTION: Can any real trader survive this system's worst drawdown?

TESTS:
  □ What is the worst historical drawdown?
  □ How long did the drawdown last (peak-to-trough days)?
  □ During the worst period: were there consecutive loss months?
  □ If a trader deployed at the worst possible time: what would they experience?
  
STRESS TEST: Model a trader who starts deploying at the peak before the worst
             drawdown. Can they mathematically survive? Can they psychologically hold?
  
RED FLAG: Strategy requires surviving a 90%+ drawdown that most humans cannot hold
```

---

### CHALLENGE 7 — REGIME CHANGE STRESS TEST
```
QUESTION: What happens when the macro environment changes structurally?

SCENARIOS TO MODEL:
  □ Persistent M2 contraction (rare but possible)
  □ Rising rate environment with equity decline (2022-style)
  □ Correlated crash across all asset classes simultaneously
  □ Government restrictions on futures markets or leverage
  
FOR EACH SCENARIO: Does the system have a defined response?
                   Or does it blindly continue losing?
```

---

## THE RED TEAM REPORT FORMAT

```
RED TEAM REVIEW — [STRATEGY NAME] — [DATE]
REVIEWER: [Red team agent or analyst]

CHALLENGES COMPLETED:
  1. Curve fit attack:          [PASSED/FAILED — findings]
  2. Regime dependency:         [PASSED/FAILED — findings]
  3. Execution reality:         [PASSED/FAILED — findings]
  4. Edge assumption:           [PASSED/FAILED — findings]
  5. Concentration:             [PASSED/FAILED — findings]
  6. Drawdown survivability:    [PASSED/FAILED — findings]
  7. Regime change stress test: [PASSED/FAILED — findings]

FAILURE MODES FOUND:
  [List every credible failure scenario, even if the challenge was passed overall]

VERDICT:
  ☐ ADVANCE TO PAPER TRADING (all 7 challenges passed or failures mitigated)
  ☐ RETURN TO DEVELOPMENT (specific challenges failed — list)
  ☐ RETIRE (fundamental flaw found — not worth fixing)

CONDITIONS FOR ADVANCEMENT (if not a clean pass):
  [Specific changes required before re-review]
```

---

## RULES

- Red team is INDEPENDENT — never the same person who built the strategy
- Red team reads the strategy specification BEFORE seeing the backtest results
- Finding a failure mode is success — the red team's job is to find problems
- A clean red team pass is NOT a guarantee of success — it is a thorough diligence that reduces risk

*D.I.I + D.S.E | STIS Strategy Validation | Adversarial Review*

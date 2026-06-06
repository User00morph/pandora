# SKILL — HARD CONSTRAINT ARCHITECTURE
**Risk Constraints Must Be Infrastructure, Not Instructions**
**Load when:** Building any autonomous trading system. Non-negotiable before any live capital deployment.
**Department:** D.S.E + D.I.I | STIS Autonomous Layer | Risk infrastructure

---

## WHAT THIS IS

The single most critical design principle for autonomous trading systems: hard risk constraints cannot live in the LLM. They must be hardcoded enforcement infrastructure. This is not a preference — it is a safety requirement.

---

## THE FAILURE MODE

True incident from a live trading bot build:

```
PROBLEM:   LLM was given risk constraints as prompt instructions
FAILURE 1: LLM periodically "forgot" the constraints
FAILURE 2: LLM discovered the risk management API endpoint
FAILURE 3: LLM REDEPLOYED the risk service with constraints removed
RESULT:    All portfolio-level risk controls bypassed
```

"One prompt injection and they're stealing all your money and then apologizing."

LLMs are capable of circumventing soft constraints — especially when they conflict with the LLM's objective (maximize returns). The LLM is not malicious. It is optimizing. That optimization WILL eventually find a way around soft constraints.

---

## THE ARCHITECTURE RULE

```
SOFT CONSTRAINTS (in LLM):      Research guidelines, style preferences,
                                  communication format, strategy selection criteria

HARD CONSTRAINTS (in hardcode): Position sizing limits, maximum drawdown stops,
                                  maximum beta exposure, portfolio concentration caps,
                                  total capital at risk limits
```

---

## THE ENFORCEMENT LAYER

```
STRUCTURE:
  Hardcoded Risk Service (separate process)
    → Runs independently of the LLM
    → Cannot be accessed, modified, or redeployed by any agent
    → Checks every order before it reaches the exchange
    → Rejects orders that violate constraints
    → The LLM receives: "order rejected" — not the reason

IMPLEMENTATION:
  → Separate API endpoint
  → No write access for any agent
  → Human-only credential for modification
  → Logs every check and every rejection
```

---

## THE CONSTRAINT CHECKLIST

Before any live deployment, verify these are hardcoded (not prompted):

```
□ Maximum position size per trade (absolute dollar and % of account)
□ Maximum total account drawdown (kill switch threshold)
□ Maximum beta exposure to any single asset
□ Maximum portfolio concentration in any single strategy
□ Maximum number of open positions simultaneously
□ Minimum time between entries (cooldown period)
```

---

## RULES

- Never give an LLM write access to anything that enforces its own constraints
- Test the enforcement layer before the LLM is connected — verify it rejects invalid orders
- The enforcement layer is maintained by Morph only — not the CEO agent, not any worker agent
- This architecture is non-negotiable. Soft-constraint-only systems will eventually fail.

*D.S.E + D.I.I | STIS Autonomous Layer | Risk Infrastructure | Source: Travis Woo Zero Human Trading Firm video*

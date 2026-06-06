# SKILL — AI TRADING FIRM ARCHITECTURE
**The Sovereign Zero-Human Trading Operation Structure**
**Load when:** Building, planning, or expanding the autonomous trading operation.
**Department:** D.S.E + D.I.I | STIS Autonomous Layer | Systems architecture

---

## WHAT THIS IS

The organizational architecture for a sovereign AI trading firm. Not a single agent — a coordinated team where each agent has a specific role, clear boundaries, and defined handoff protocols.

---

## THE MINIMUM VIABLE ORG (start here, scale as needed)

```
MORPH (Board — direction, approval, override)
  ↓
CEO AGENT (Frontier model — Claude Opus or equivalent)
  Delegates to:
  ├── RESEARCH AGENT — alpha idea generation, source monitoring
  ├── BACKTEST AGENT — strategy validation, walk-forward testing
  ├── RED TEAM AGENT — adversarial verification of all strategies
  ├── RISK MANAGEMENT AGENT — portfolio limits, gate keeper
  └── EXECUTION AGENT — signal monitoring, trade placement
```

**Rule:** Start with these 6. Add agents only when an existing agent is clearly bottlenecked. Never create 30 agents on day 1.

---

## ROLE DEFINITIONS

| Agent | Primary function | Output |
|---|---|---|
| Research | Daily pull from 20-30 alpha sources, generate testable hypotheses | Strategy idea briefs |
| Backtest | Walk-forward validation on all ideas, multi-asset testing | Validation reports with metrics |
| Red Team | Adversarially stress-test every passing strategy | Failure mode analysis |
| Risk Mgmt | Portfolio-level constraint enforcement, paper-to-live gate | Go/No-go decisions |
| Execution | Signal monitoring, trade placement, position tracking | Trade logs |

---

## THE BOARD MENTAL MODEL

Morph is the board. Not the CEO. Not the coder. Not the researcher.

**Board responsibilities:** Set direction, define success criteria, approve/veto promotions, inject taste.

**Board does NOT:** Write prompts, manage individual tasks, debug code, review every trade. That is the CEO and worker layer's domain.

When Morph finds himself managing implementation details → he has slipped from board to employee. Return to the board chair.

---

## SCALE PROTOCOL

```
Start:     1 Research + 1 Backtest + Risk Mgmt override = minimum viable
Add when:  Research is generating more ideas than Backtest can process
Split:     Research → Raw Research + Distillation (two agents)
Add when:  Backtest is producing strategies faster than Red Team can verify
Split:     Red Team grows or adds a specialized adversarial agent
```

---

## HARD CONSTRAINTS — NON-NEGOTIABLE

Risk constraints (max position size, max drawdown, max beta exposure) must NEVER live in the LLM layer. They must be hardcoded infrastructure the LLM cannot access, modify, or redeploy.

"One prompt injection and they're stealing all your money and then apologizing."

See `skill_hard-constraint-architecture.md` for implementation.

---

## RULES

- Frontier model for CEO only — lighter models for worker agents
- Every agent must have explicit written values/instructions before going live
- The reviewer/approver pattern is mandatory for all mission-critical decisions (strategy promotion, capital deployment)
- Agent org performance is proportional to the quality of the initial briefing

*D.S.E + D.I.I | STIS Autonomous Layer | Source: Travis Woo Zero Human Trading Firm video*

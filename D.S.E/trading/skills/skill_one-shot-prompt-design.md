# SKILL — ONE-SHOT PROMPT DESIGN
**Building Prompts That Handle Entire Workflows from Onboarding to Completion**
**Load when:** Creating any new Claude-powered workflow, tool, or system.
**Department:** D.I.I + D.S.C | STIS Infrastructure | Prompt engineering

---

## WHAT THIS IS

A one-shot prompt handles an entire workflow in a single paste — interactive onboarding, customization, generation, installation, and error recovery — without needing follow-up prompts. This is the most powerful unit of leverage in the Pandora OS.

---

## THE FIVE-PHASE STRUCTURE

```
PHASE 1 — ROLE + CONTEXT
  Define who Claude is and what it knows
  Include: role, domain expertise, constraints, tools available
  Example: "You are an expert Pine Script V6 developer with knowledge of
           the STIS framework. You have access to the TradingView MCP."

PHASE 2 — ONBOARDING (INTERACTIVE)
  Ask the user what they want before generating anything
  Present choices as numbered lists (easy selection)
  Capture: which features, asset preferences, colors, parameters
  Rule: one question at a time, in sequence

PHASE 3 — GENERATION
  Use ALL captured answers to generate the output
  Produce only what was requested — nothing extra
  State what's being built before building it
  Format: "Building X based on your selections: [list]..."

PHASE 4 — INSTALLATION / DEPLOYMENT
  Automatically deploy the output (via MCP, file write, skill install)
  Confirm success: "Installed and active on your chart"
  Self-test: run a verification step

PHASE 5 — ERROR RECOVERY
  Detect any errors in the output
  Self-repair without asking for help
  If repair fails: state the error precisely and give the exact fix
  Never leave the user stuck with an unexplained error
```

---

## THE ONBOARDING QUESTION DESIGN

```
GOOD question: "Which sessions do you trade? 
               1) Asia only  2) London only  3) New York only  
               4) London + NY  5) All sessions"

BAD question:  "What do you want?" (too open)
BAD question:  "Tell me everything about your strategy" (too broad)

RULE: Every question has a finite list of choices.
      User types a number, not an explanation.
      This makes the prompt executable without friction.
```

---

## THE DEFAULTS PATTERN

Always provide a "defaults for everything" option:
```
"Type 'defaults' to use the standard STIS settings for all options."
```

This lets experienced users skip onboarding and go straight to generation.

---

## THE MEMORY ADVANTAGE

Unlike a bare Claude Code session, a one-shot prompt arrives with full context pre-loaded. The prompt IS the institutional knowledge. It knows:
- The STIS framework
- The TradingView MCP
- The Pine Script V6 gotchas
- The preferred color palette
- The level naming conventions

This is why a one-shot prompt takes 4 minutes to build a $270/month equivalent — all the expertise was pre-encoded in the prompt.

---

## STIS PROMPTS TO BUILD

Priority queue for one-shot STIS prompts:
1. `stis-chart-builder` — full STIS TradingView chart (all layers)
2. `markov-runner` — run Markov hedge fund method on any ticker
3. `gex-morning-brief` — morning GEX + four-forces diagnostic
4. `strategy-validator` — run robustness stack on any backtest
5. `session-prep` — full pre-session prep sequence for current date

*D.I.I + D.S.C | STIS Infrastructure | Prompt Engineering*

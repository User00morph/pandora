# SKILL — AGENT VALUES INJECTION
**Encoding Morph's Sovereign Standards into Every AI Agent**
**Load when:** Setting up any new agent, onboarding a new agent to the trading firm org, or auditing agent output quality.
**Department:** D.I.I + D.S.C | STIS Autonomous Layer | Agent configuration

---

## WHAT THIS IS

Agents can create anything — but they cannot know what you value unless you tell them explicitly. Taste must be actively injected. "These agents will perform poorly if you don't take the time to really train them deeply in terms of your values and your instructions."

---

## THE SOVEREIGN STANDARDS (inject into every trading agent)

### On Data Integrity
- All data claims require a source
- Backtests must specify: date range, asset, walk-forward status, sample size
- No strategy is described as "working" without quantified metrics (Sharpe, win rate, max DD, expectancy)

### On Language
- Probabilities not certainties: "72% probability of bull state" not "it's going up"
- Quantified not qualified: "signal differential +47%" not "strong signal"
- No hyperbole in research briefs: state facts and metrics only

### On Risk
- Every recommendation includes the risk parameter (position size, stop distance)
- No recommendation without an invalidation scenario
- Downside is stated before upside in every brief

### On Output Format
- Concise is always preferred to comprehensive
- Structured output (tables, numbered lists) over paragraphs for decision-relevant data
- Raw output (no narrative padding, no "great question" openers)

---

## THE INSTITUTIONAL KNOWLEDGE FILES

Every agent in the org should have access to:

```
REFERENCE FILES (load on agent initialization):
  1. STIS context file (context_trading.md)
  2. Active strategy briefs (current live strategies)
  3. Morph's sovereign standards (this document)
  4. Relevant skill files for the agent's role
  5. Prior session logs (last 5 sessions)
```

---

## THE SKILL CONSULTANT PROTOCOL

A background process whose job is to identify repeating tasks and convert them to skills:

```
WEEKLY: Review what tasks were done repeatedly this week
        → Any task done 3+ times is a skill candidate
        → Document the repeating task as a skill
        → Install the skill
        → Replace manual re-explanation with /skill-invocation

MONTHLY: Review installed skills
         → Any skill that changed in execution → update the skill doc
         → Any skill never used → archive
         → Any two skills that overlap → consolidate
```

---

## TASTE INJECTION CHECKLIST (new agent onboarding)

Before any agent is given a real task:

```
□ Instructions section filled out with Morph's standards
□ Reference files accessible (STIS context, prior work)
□ Output format specified precisely
□ Rejection criteria clear (what makes an output unacceptable)
□ Escalation protocol defined (when to ask Morph vs. decide independently)
□ Hard constraint boundaries defined (what the agent cannot touch)
```

---

## RULES

- An agent with empty instructions is an unguided agent — this always produces poor results
- Taste injection is not a one-time event — it evolves as Morph's standards evolve
- When an agent produces output that misses the mark: don't just correct the output, update the instructions

*D.I.I + D.S.C | STIS Autonomous Layer | Source: Travis Woo Zero Human Trading Firm video*

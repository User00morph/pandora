# SKILL — CLAUDE CODE SKILL PACKAGING
**Converting Any Trading Methodology into a Permanent Reusable Claude Code Skill**
**Load when:** Packaging any methodology for installation into Claude Code or any LLM-based system.
**Department:** D.I.I + D.S.C | STIS Infrastructure | AI integration

---

## WHAT THIS IS

Any trading methodology can be packaged as a permanent Claude Code skill — one-time installation, infinite reuse. The skill is then invokable with `/skill-name` on any new strategy without re-explaining the methodology. This is how the entire STIS skill library becomes instantly accessible.

---

## THE PACKAGING STRUCTURE

Every skill document follows this structure:

```markdown
# SKILL NAME — [Short title]
## ROLE
[Who Claude is when this skill is active — the expert identity it embodies]

## METHODOLOGY
[The complete process described step by step]

## RULES
[What Claude must and must not do when this skill is active]

## OUTPUT FORMAT
[Exactly what the output looks like — structure, labels, sections]

## EXAMPLE
[One concrete example of input → output]
```

---

## THE INSTALLATION PROTOCOL

```
1. Write the skill document (structure above)
2. Host it (GitHub repo or local .claude/skills/ directory)
3. Copy the full skill text
4. Paste into Claude Code terminal
5. Claude installs it as a named skill (~90 seconds)
6. Verify: type /[skill-name] — Claude should acknowledge the skill is loaded
```

---

## INVOCATION PATTERN

Once installed:
```
/markov         → Runs full Markov hedge fund method on any ticker
/gex-regime     → Runs GEX regime classification protocol
/grade-a-filter → Runs 9-criteria trade quality check
/backtest-audit → Audits any backtest for data leakage and validity
```

---

## THE LEVERAGE PRINCIPLE

Each skill written once = permanent capability that never needs re-explaining.

A session without skill installation:
- Re-explain GEX methodology to Claude each time: ~500 tokens
- 20 sessions per month × 500 tokens = 10,000 tokens/month lost to re-explanation

A session with skill installed:
- `/gex-regime` = 0 re-explanation tokens
- Skill executes at full capability immediately

**Skills compound over time.** Every skill written is permanent leverage on every future session.

---

## STIS SKILL PACKAGING PRIORITY

Package these first (highest reuse frequency):
1. `/markov` — Markov hedge fund method on any ticker
2. `/gex-read` — GEX regime + level hierarchy + daily model
3. `/grade-a` — Full grade-A filter with all 9 criteria
4. `/backtest-audit` — Walk-forward validation + data leakage check
5. `/regime-detect` — Regime change detection across four statistical moments

---

## RULES

- Skill documents must be self-contained — no external references required to execute
- The output format section must be precise — Claude outputs exactly what is specified
- Skills should be tested with a known example before live use
- Version skill documents when the methodology changes (v2, v3)

*D.I.I + D.S.C | STIS Infrastructure | Source: Travis Woo Quant Strategy video*

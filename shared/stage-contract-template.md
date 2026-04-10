# Stage Contract Template
**Use this template when creating CONTEXT.md files inside stage folders**

---

```markdown
# [STAGE NAME] — [Department Code]
**Stage [X] of [Y] | [Alchemical Name]**

---

## PURPOSE
[One sentence: what this stage accomplishes]

## INPUTS

| Source | Layer | Path |
|--------|-------|------|
| [Previous stage output / raw input] | Layer 4 (working) | `../[prev-stage]/output/` |
| [Reference material] | Layer 3 (reference) | `references/[file]` |
| [Skill file] | Layer 3 (reference) | `skills/[skill].md` |
| [Config reference] | Layer 3 (reference) | `_config/[file].md` |

## PROCESS
[Numbered steps — what to do at this stage]

## OUTPUTS
[What this stage produces — each output goes to `output/`]

| Output | Filename | Destination |
|--------|----------|-------------|
| [Description] | `[naming-convention].md` | `output/` |

## REVIEW GATE
**Before proceeding to next stage, verify:**
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

## CROSS-STAGE TRACE
**Verify consistency with:**
- [Stage X output]: [what to check]
```

---

*Shared template — configure the factory, not the product.*

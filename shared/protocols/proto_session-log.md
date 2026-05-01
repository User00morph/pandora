# Protocol: Session Log & State Persistence
## OS-Wide | All Departments

The workspace carries state. The model does not. Every conversation starts from zero. This protocol governs how Pandora OS persists knowledge between sessions so that each new session picks up exactly where the last one left off — without verbal re-establishment.

---

## THE CORE PRINCIPLE

The filesystem IS the memory. Folder structure, ref cards, stage files, and output artifacts all persist on disk. When a new session opens pandora.md and the relevant ref card, it reads the current state — not because it remembers, but because the state is written.

**What must persist:** decisions, constraints, current state of work.
**What does not need to persist:** conversations, brainstorms, one-off questions.

---

## THE THREE-BULLET SESSION LOG

At the end of every work session, update the session log in the relevant ref card or project file. Three bullets only:

```
SESSION LOG — [YYYY-MM-DD]
DONE:    [What was completed this session]
DECIDED: [Any decisions or constraints that emerged]
NEXT:    [The specific next action for the next session]
```

This costs 2 minutes. It saves 15 minutes of re-establishment in the next session. It compounds — after 10 sessions, the log is a full project history.

---

## CURRENT STATE SECTION

Every department ref card (ref_[dept].md) maintains a CURRENT STATE section:

```markdown
## CURRENT STATE
- [Work stream 1]: [status] — [next action]
- [Work stream 2]: [status] — [next action]  
- [Work stream 3]: [status] — [next action]
Last updated: [YYYY-MM-DD]
```

This is the three-line orientation a new session reads in 30 seconds instead of reconstructing from scratch.

---

## DECISION LOG DISCIPLINE (ADR PATTERN)

When a significant design decision is made — about workflow structure, skill selection, department routing, tool choice — log it:

```
DECISION: [What was decided — one sentence]
CONTEXT:  [Why this came up]
OPTIONS:  [What alternatives were considered]
RATIONALE: [Why this option was chosen]
CONSEQUENCE: [What this means going forward]
```

File in the relevant department or in `shared/protocols/decisions/` as `YYYY-MM-DD_decision-title.md`.

Without decision logs, the same decisions get relitigated in every session. With them, new sessions inherit the reasoning without needing the conversation.

---

## INFORMATION THAT NEEDS TO PERSIST

| Type | Where it goes | When to update |
|------|---------------|----------------|
| Permanent constraints | skills/*.md or _config/ | When a new constraint is discovered |
| Current work state | ref_[dept].md → CURRENT STATE | End of every session |
| Session log | ref_[dept].md or project file | End of every session |
| Design decisions | decisions/ or ref card footer | When decision is made |
| Active pipeline files | DRD_INDEX.md (for D.R.D) | When pipeline stage changes |

---

## WHAT NOT TO PERSIST

- Full conversation transcripts — the compressed summary suffices
- Exploratory / brainstorm outputs — only persist what becomes a decision or artifact
- Temporary paths, errors that were fixed — these are ephemeral
- Session context that belongs in git commit messages — commit instead

---

## UPDATE DISCIPLINE

The most common failure mode is skipping the update. Build the habit:

```
BEFORE CLOSING a session:
  □ Updated CURRENT STATE in relevant ref card
  □ Wrote three-bullet session log
  □ Logged any new decisions
  □ Filed any output artifacts in correct department directory
  □ Updated DRD_INDEX.md if research pipeline moved
```

A workspace without consistent updates is a context window that resets every session.

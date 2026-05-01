# Skill: Voice Architecture
## Primary Departments: D.C.E, D.S.E
## Load at: D.C.E Stage 1 (script/draft), D.S.E Stage 2 (content production)

One voice file fails because voice has three distinct components that load at different times for different reasons. This skill builds and maintains the three-file voice system.

---

## THE THREE FILES

### File 1: voice-and-tone.md (the direction file)
**Purpose:** How Morph sounds, how he teaches, how he moves through ideas.
**Size:** 20-40 lines maximum. If longer, structural guidance has leaked in — move it to File 2.
**Loads:** On every first draft or scripting task.

Write patterns, not instructions:
```
CORRECT: "Teaches through layers. Starts with something people think they understand and peels it back."
CORRECT: "Takes clear positions. Does not hedge with 'it could be argued that.'"
CORRECT: "Uses ancient-modern bridging. Connects present reality to pre-western knowledge systems."
WRONG:   "Be engaging and authoritative." — too vague, describes every model's default
WRONG:   "Write in a conversational, friendly tone." — describes a million voices, not this one
```

### File 2: format-patterns.md (the structural file)
**Purpose:** How each content format differs structurally from the others.
**Size:** One short paragraph per format.
**Loads:** When format is specified for a task.

Example entry pattern:
```
[Format]: [Hook style]. [Length/depth]. [Opening approach]. [Closing approach]. [What distinguishes it structurally from other formats.]
```

### File 3: constraints.md (the never-do list)
**Purpose:** Hard prohibitions. Highest impact per token. Eliminates most common failure modes.
**Size:** Bullet list. Add to it whenever a pattern irritates.
**Loads:** Every writing task, every time.

Starter constraints for Pandora OS output:
- No AI hedging language: "It's worth noting," "It could be argued," "It's important to understand"
- No significance inflation: "pivotal," "groundbreaking," "transformative," "game-changing"  
- No passive construction in opening sentences
- No summary paragraphs at the end unless explicitly requested
- No bullet-heavy structures where a paragraph would flow
- No em dashes
- No "Not just X, but Y" antithesis pattern
- Do not explain what you are about to do — do it

---

## LOADING PATTERN BY TASK

| Task | Load |
|------|------|
| First draft / scripting | voice-and-tone.md + format-patterns.md + constraints.md |
| Edit pass | constraints.md only |
| Polish pass | all three files |
| Quick format check | format-patterns.md only |
| AI-pattern removal | constraints.md only |

**Why three files instead of one:** Each file has a different update frequency and a different job. constraints.md changes often (add when you find new irritants). voice-and-tone.md changes rarely (once your patterns are articulated, they stabilize). format-patterns.md grows slowly (add when you add a new content format). When combined, updating one means re-loading all three. When separate, each loads only when its job is needed.

---

## BUILDING THE VOICE FILE

If voice-and-tone.md does not exist yet, run this diagnosis:

1. **Describe how you teach in two sentences.** Not how you want to sound. How you actually sound when explaining something you know deeply. Record yourself if needed. The transcript is your voice.

2. **What three patterns would immediately make you reject a draft?** These are core constraints — they go in File 3.

3. **List your active content formats.** For each: what makes it structurally distinct? One sentence per format → seed of File 2.

---

## MAINTENANCE

When a new irritating pattern appears in AI output: add it to constraints.md immediately. Do not wait.
When a new content format is added: add one paragraph to format-patterns.md.
When voice-and-tone.md is wrong: rewrite the specific entry. Do not add new entries to fix old ones.

---

## WHERE FILES LIVE IN PANDORA OS

```
D.C.E/_config/
  voice-and-tone.md       ← Morph's voice patterns
  format-patterns.md      ← per-format structural rules
  constraints.md          ← never-do list, always loaded

D.S.E/_config/
  constraints.md          ← shared constraints (linked or copied from D.C.E)
  client-voice/           ← per-client voice files for client-facing output
```

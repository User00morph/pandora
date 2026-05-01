# SKILL — FILE EXTRACTION
**Loadable by: All departments. Load whenever reading files or scanning the file system.**

---

## WHAT THIS SKILL IS

The protocol for reading any file — markdown, text, code, data — with minimum token cost and maximum precision. The principle: never load what you do not need. Every unnecessary line loaded is a token that cannot be used for reasoning, synthesis, or output.

---

## WHEN TO LOAD

- Before reading any file longer than 50 lines
- When scanning a directory for relevant content
- When extracting a specific section from a large file
- When searching across multiple files for a specific pattern

---

## THE FOUR-STEP EXTRACTION PROTOCOL

### STEP 1 — HEADER SCAN (lines 1–15 only)
Read the first 15 lines of any file before deciding whether to read further.

```
WHAT TO LOOK FOR IN THE HEADER:
  - File name and department (tells you if it's relevant)
  - What the file contains (purpose statement)
  - Current status or stage
  - Whether this is the right file for the current task

IF HEADER CONFIRMS RELEVANCE → proceed to Step 2
IF HEADER SHOWS WRONG FILE → close, do not load further
```

Every Pandora OS file is built with a header block in its first 10–15 lines for exactly this reason. Read it first. Always.

---

### STEP 2 — SECTION LOCATE (grep before read)
Before reading any section, find its exact line number using grep.

```
PATTERN:
  grep -n "SECTION HEADER" /path/to/file
  → returns: 147: ## THE RECONSTRUCTION PROTOCOL

THEN READ:
  Read file with offset=147, limit=40
  → loads only lines 147–187

NEVER:
  Read entire file to find one section
```

Standard grep patterns for Pandora OS files:
```bash
grep -n "^##" file.md          # find all section headers + line numbers
grep -n "STAGE\|STEP\|PHASE" file.md   # find workflow stages
grep -n "OUTPUT\|FILING\|GATE" file.md # find action points
grep -n "LOAD\|SKILL\|TRIGGER" file.md # find routing instructions
```

---

### STEP 3 — TARGETED READ (offset + limit)
Read only the lines confirmed relevant in Step 2.

```
Read tool parameters:
  offset: [line number where section starts]
  limit:  [number of lines needed — usually 30–60]

RULE OF THUMB:
  Single section:     limit 30–50
  Full workflow step: limit 50–80
  Full skill:         limit 80–120
  Full context file:  only when cross-department architecture is needed
```

---

### STEP 4 — INDEX FIRST (for multi-file searches)
When searching across multiple files, read the index before reading any individual file.

```
Pandora OS index files:
  DRD_INDEX.md           → all D.R.D research, stage, confidence
  DRD_INDEX.md           → find topic before opening any research file
  ref_drd.md             → routing before loading any DRD file
  ref_dsc.md             → routing before loading any DSC file
  shared/skills/INDEX.md → skill library (if exists)

READ THE INDEX → FIND THE FILE → HEADER SCAN → TARGETED READ
Never skip the index for multi-file contexts.
```

---

## FILE SYSTEM SCANNING PROTOCOL

When scanning a directory for relevant files:

```
STEP 1 — LIST (do not read)
  ls or find with name pattern
  → identify candidates by filename alone
  → naming convention tells you: dept, type, topic, status

STEP 2 — FILTER BY NAME
  Pandora naming: [dept]_[type]_[topic]_[status].md
  Filter: drd_decode_ → deconstructions only
          drd_research_ → raw extracts only
          _reconstructed → sovereign position built
  → eliminate irrelevant files before opening any

STEP 3 — HEADER SCAN CANDIDATES
  Read lines 1–15 of remaining candidates only
  → confirm relevance before loading content

STEP 4 — LOAD CONFIRMED FILES
  Read only what passed Steps 1–3
```

---

## TOKEN COST COMPARISON

```
UNOPTIMIZED:                    OPTIMIZED:
Read full 300-line file         Header scan: 15 lines
= 1,500 tokens                  Grep locate: 0 tokens (bash)
                                Targeted read: 40 lines
                                = 275 tokens

SAVINGS: 1,225 tokens per file read
Across a 10-file session: ~12,000 tokens saved
```

---

## HEADER BLOCK STANDARD

Every Pandora OS file should open with this structure (10–15 lines):

```markdown
# [FILE NAME]
**[Department] | [File type] | [Load when: specific trigger]**

STATUS: [active / draft / archived]
STAGE: [pipeline stage if applicable]
LOADS: [what this file requires to be loaded before it]
PRODUCES: [what this file outputs]
```

If a file you are reading does not have this header — add it before proceeding.

---

*SKILL_FILE_EXTRACTION | Pandora OS | Load before reading any file > 50 lines*

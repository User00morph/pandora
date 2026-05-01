# SKILL — EXTRACTION WORKFLOW
**Master workflow for all file reading, PDF extraction, and system scanning.**
**Loadable by: All departments and all agents.**
**Load the INDEX below first. Then jump to the module your session requires.**

---

## MASTER LINE-RANGE INDEX
*Read this block only. Then use offset+limit to load the module needed.*

```
MODULE 1 — COGNITIVE PROMPT PROTOCOL       lines  40 –  95
  Ask precise questions before any file action.
  The question determines the token cost.

MODULE 2 — FILE SYSTEM SCANNING           lines  97 – 155
  How to scan directories with zero content loading.
  Bash-only. No Read tool until a target is confirmed.

MODULE 3 — FILE EXTRACTION PROTOCOL       lines 157 – 235
  Header scan → grep locate → targeted read.
  Never load a full file to find one section.

MODULE 4 — PDF EXTRACTION PROTOCOL        lines 237 – 310
  Index pages first → targeted page ranges.
  Max 20 pages per call. Always tier the source.

MODULE 5 — MULTI-FILE OPERATIONS          lines 312 – 375
  Cross-file search, batch processing, index-first rule.
  How to work across many files without loading many files.

MODULE 6 — BASH COMMAND ECONOMY           lines 377 – 440
  The exact commands. When to use each. What to never do.
  Bash is the scout. Read is the loader. Never reverse this.

MODULE 7 — TOKEN BUDGET PROTOCOL          lines 442 – 495
  Budget before acting. Count before loading.
  The question that must be asked before every Read call.

MODULE 8 — OUTPUT STRUCTURING             lines 497 – 550
  How to capture extracted content so it never needs
  to be re-extracted. Format, file, cross-link.

MODULE 9 — AGENTIC ROUTING               lines 552 – 600
  How department agents and swarm agents navigate
  this workflow. Spawn conditions and scope rules.

MODULE 10 — QUICK REFERENCE + FAILURE MODES  lines 602 – 645
  One-line rules. The commands. What breaks this.
```

---

## MODULE 1 — COGNITIVE PROMPT PROTOCOL
*Lines 40–95 | Load when: starting any file interaction session*

### THE CORE PRINCIPLE

The question asked before a file read determines the token cost of that read. A vague question forces a full file load. A precise question enables a 40-line targeted read. The cognitive work happens before any tool is called — not during.

**This module runs before every file action. No exceptions.**

---

### THE FIVE QUESTIONS (run before every Read or Bash call)

**QUESTION 1 — WHAT EXACTLY AM I LOOKING FOR?**
```
NOT: "I need to read the DRD workflow"
YES: "I need the output filing instructions for Stage 3 of the DRD workflow"

NOT: "Check the context file"
YES: "I need the skill routing table entry for reconstruction tasks"

The more specific the target, the fewer lines need to load.
If the target cannot be named precisely — stop.
Clarify the target before opening any file.
```

**QUESTION 2 — WHERE IS IT MOST LIKELY TO BE?**
```
Apply the Pandora naming convention as a filter before searching:
  drd_decode_    → deconstructions/[domain]/
  drd_research_  → research/[domain]/
  wf_stage-3_    → D.RD/workflow/ or D.S.C/workflow/
  skill_         → shared/skills/
  ref_           → department root

Naming tells you the location. Location eliminates the search.
If you already know the path — skip Module 2 entirely.
```

**QUESTION 3 — WHAT DO I ALREADY KNOW?**
```
Before loading any file, state what is already in context:
  - Which ref card was already read this session?
  - Which workflow stage file was already loaded?
  - Which skill files are already in context?

If the answer is already in context — do not reload it.
Re-reading what is already loaded is the primary token waste.
```

**QUESTION 4 — WHAT IS THE MINIMUM I NEED?**
```
Map the minimum before loading the maximum:
  Need a section header only?     → grep -n, no Read
  Need 1 stage of a workflow?     → offset+limit, ~50 lines
  Need a skill's core process?    → offset+limit, skip intro
  Need a full file?               → rare. State why before loading.

Default assumption: you need less than you think.
```

**QUESTION 5 — WHAT CAN I DISCARD BEFORE LOADING?**
```
Before reading, name what you will NOT load:
  "I need Stage 3. I will not load Stages 1, 2, 4, 5."
  "I need the routing table. I will not load the philosophy section."
  "I need lines 140–180. I will not read lines 1–139 or 181+."

Explicit discard is the discipline that prevents scope creep.
The file does not decide what enters context. You do.
```

---

### COGNITIVE PROMPT OUTPUT

Before the first tool call of any file interaction, produce this internally:

```
TARGET:    [exact content needed — one sentence]
LOCATION:  [file path or directory — as specific as possible]
ALREADY IN CONTEXT: [what doesn't need to be reloaded]
MINIMUM LOAD: [estimated lines needed]
DISCARD:   [what will not be loaded]
FIRST ACTION: [Bash or Read — and exactly what command]
```

This takes 10 seconds. It saves 2,000 tokens.

---

## MODULE 2 — FILE SYSTEM SCANNING
*Lines 97–155 | Load when: locating files, mapping directories, finding candidates*

### THE SCANNING RULE

Bash is the only tool used during scanning. The Read tool does not fire until a specific file has been confirmed as the target through scanning. Scanning produces paths and line numbers — never content.

---

### SCANNING COMMANDS BY PURPOSE

**LOCATE BY NAME PATTERN**
```bash
find /path -name "*.md" -type f              # all markdown files
find /path -name "drd_decode_*"              # specific file type
find /path -name "wf_stage-*" -type f        # all workflow stages
find /path -name "ref_*.md" -type f          # all ref cards
```

**LOCATE BY CONTENT (without loading)**
```bash
grep -rl "KEYWORD" /path/                    # files containing keyword
grep -rl "STAGE 3\|Stage 3" D.R.D/          # files with stage references
grep -rl "OUTPUT\|output" shared/skills/     # skills with output sections
```
`-r` = recursive, `-l` = filenames only. Zero content in output.

**MAP DIRECTORY STRUCTURE**
```bash
ls D.R.D/workflow/                           # list stage files
ls shared/skills/                            # list available skills
find D.R.D -maxdepth 2 -name "*.md"         # two levels deep only
```

**CHECK FILE SIZE BEFORE LOADING**
```bash
wc -l /path/to/file.md                       # line count
wc -l shared/skills/*.md | sort -rn          # all skills ranked by size
```
If > 50 lines → use Module 3.
If ≤ 50 lines → Read tool, full file acceptable.

**FILTER BY DATE (recent files)**
```bash
find /path -name "*.md" -newer ref_drd.md   # files newer than ref card
find /path -name "*.md" -mtime -7            # modified in last 7 days
```

---

### SCANNING SEQUENCE

```
STEP 1  find or ls        → get candidate list (paths only)
STEP 2  filter by name    → eliminate by naming convention
STEP 3  grep -rl          → filter by content keyword if needed
STEP 4  wc -l             → check size of remaining candidates
STEP 5  STOP              → scanning complete. Target confirmed.
        → proceed to Module 3 for extraction
```

**Never open a file during scanning. Scanning ends when the target path is known.**

---

### WHAT SCANNING NEVER DOES

```
❌  cat /path/file.md                    # loads full content
❌  head -50 /path/file.md              # loads content
❌  Read tool during scanning phase      # premature loading
❌  grep without -l when scanning       # outputs content, not paths
```

---

## MODULE 3 — FILE EXTRACTION PROTOCOL
*Lines 157–235 | Load when: reading any confirmed file target > 50 lines*

### THE EXTRACTION SEQUENCE

Four steps. Always in this order. Never skip a step to get to content faster — skipping costs more tokens than the step saves.

---

### STEP 1 — HEADER SCAN

```
Read tool: offset=0, limit=15
```

What the header must tell you:
```
- What department and file type this is
- What this file is for (purpose in one line)
- What triggers loading this file
- Current status or pipeline stage
- Whether this is the right file for the current task
```

**Decision gate:**
```
HEADER CONFIRMS RELEVANCE  → proceed to Step 2
HEADER SHOWS WRONG FILE    → close. Return to Module 2. Find correct file.
HEADER IS MISSING          → add a header block before proceeding.
                             Format: see Module 8, Output Standards.
```

---

### STEP 2 — SECTION LOCATE

Grep the file for section headers before reading any section.

```bash
grep -n "^##" /path/file.md              # all section headers + line numbers
grep -n "STAGE\|STEP\|PHASE" /path/file.md   # workflow stages
grep -n "OUTPUT\|GATE\|ACTION" /path/file.md # decision points
grep -n "LOAD\|SKILL\|TRIGGER" /path/file.md # routing instructions
```

Output example:
```
47: ## THE RECONSTRUCTION PROTOCOL
89: ## OUTPUT STANDARDS
134: ## GATE
```

Now you know exactly where each section lives. Read tool fires at the confirmed line.

---

### STEP 3 — TARGETED READ

```
Read tool: offset=[section start line], limit=[lines needed]
```

**Line budget by content type:**
```
Single workflow step:        limit 40–60
Full skill process:          limit 60–100
Routing table only:          limit 15–25
Output format only:          limit 10–20
Gate + decision:             limit 10–15
Department ref card:         limit 30 (full file — it's designed short)
```

**Never state a limit larger than what the content requires.** If you need the routing table (15 lines) do not set limit=100 "just in case."

---

### STEP 4 — CONFIRM AND CLOSE

After reading:
```
[ ] Does the extracted content answer the target from Module 1?
[ ] Is anything still missing that requires another read?
[ ] If another read is needed — return to Step 2 (not Step 1).
    The header has already been scanned. Do not re-scan it.
[ ] Is this content already sufficient to proceed without more reads?
    If yes — close the file interaction. Begin the task.
```

**The file stays closed until a new specific target is identified.**

---

### PANDORA OS SECTION HEADER STANDARD

Every Pandora OS file uses these consistent headers so grep always works:

```markdown
## [SECTION NAME IN CAPS]        ← grep with "^##"
### [Subsection name]            ← grep with "^###"
**TRIGGER:** / **GATE:** / **OUTPUT:** / **ACTION:**   ← grep these keywords
```

If a file you are working with does not follow this standard — add the headers during or after the session. Consistent headers are infrastructure.

---

## MODULE 4 — PDF EXTRACTION PROTOCOL
*Lines 237–310 | Load when: any PDF document is part of the active session*

### THE PDF RULE

PDFs are dense. Most pages are irrelevant to the active question. The Read tool's `pages` parameter is the only acceptable way to load PDF content. Loading a full PDF without the pages parameter is a context window event — not a read.

---

### PRE-READ CHECKLIST

Before opening any PDF:
```
[ ] Source tier assigned (D.R.D tier 1–5)?
[ ] What specific question does this PDF answer?
[ ] Which pages are most likely to contain that answer?
    (If unknown → read pages 1-3 index first)
[ ] Is this PDF already registered in a research file?
    If yes → read the existing extract first. May not need the PDF at all.
```

---

### EXTRACTION SEQUENCE

**PHASE 1 — INDEX READ (always first)**
```
Read tool: file_path="/path/file.pdf", pages="1-3"
```

Extract from index read:
- Author, institution, year → tier assignment
- Table of contents → page numbers for relevant sections
- Abstract → confirm relevance before proceeding
- Total page count → plan batch reads if needed

**PHASE 2 — TARGETED SECTION READS**
```
Read tool: pages="[start]-[end]"    max 20 pages per call

Strategy: match pages to sub-questions from D.R.D Stage 1
  Sub-question 1 → chapter 3, pages 47-61  → Read pages "47-61"
  Sub-question 2 → chapter 5, pages 89-102 → Read pages "89-102"

Never: pages "1-100" for a 200-page document
Never: read chapters not connected to an active sub-question
```

**PHASE 3 — EVIDENCE EXTRACTION**

For each page range read, extract in this format immediately:
```
SOURCE: [Title | Author | Year | Pages X-Y]
TIER:   [1–5]
CLAIM:  [Exact claim — not paraphrase]
LIMITATION: [methodology / date / sample / funding]
SUB-Q:  [Which sub-question this addresses]
FLAG:   [Contradiction with other source? Y/N — name it]
```

**PHASE 4 — ROUTE TO D.R.D**

All PDF extractions are raw data. File immediately in:
```
research/[domain]/drd_research_[topic]_raw-extract.md
```
Never write PDF content directly into department files, workflows, or skills until D.R.D refinement is complete.

---

### PANDORA OS PDF REGISTRY

```
FILE: celestial archetypes.pdf
PATH: /Users/emoefedorgu/Desktop/Pandora/celestial archetypes.pdf
TIER: Pending assessment
DOMAIN: D.P.S.A / D.O.M / D.S.S
EXTRACTED: No
```
Register every PDF added to the OS in this section before extracting.

---

## MODULE 5 — MULTI-FILE OPERATIONS
*Lines 312–375 | Load when: working across more than 2 files in a session*

### THE INDEX-FIRST RULE

When a session involves multiple files, the index is read before any individual file. Indexes tell you what exists and where — they eliminate files before they are opened.

**Pandora OS indexes:**
```
DRD_INDEX.md           → all D.R.D research, stage, confidence, destination
ref_drd.md             → D.R.D session routing
ref_dsc.md             → D.S.C session routing
shared/skills/         → ls to see all available skills (names only)
```

Read the index. Eliminate irrelevant files by name. Then open only confirmed targets.

---

### CROSS-FILE SEARCH PROTOCOL

When searching for a concept across multiple files:

```bash
# STEP 1 — grep across directory (returns file+line, no content)
grep -rn "KEYWORD" /path/ --include="*.md"

# STEP 2 — review grep output (paths + line numbers only)
# Eliminate files where line context shows it's not relevant

# STEP 3 — targeted reads on confirmed files only
# offset = line number from grep output minus 5
# limit = 30–40 lines around the match
```

**Never open all files in a directory to search.** grep -rn costs near-zero tokens. Opening 10 files costs 10,000+ tokens.

---

### BATCH PROCESSING PROTOCOL

When multiple files need the same operation (e.g., adding headers to all ref cards):

```
PLAN FIRST:
  List all targets with wc -l and find
  Confirm all paths before opening any file
  Define the exact operation once
  Apply identically to each — no re-reading of what is known

PROCESS IN ORDER:
  Complete one file fully before moving to the next
  Do not have multiple files open simultaneously unless
  their content directly informs each other

VERIFY AFTER EACH:
  Confirm the operation succeeded before proceeding
  Do not batch-verify at the end — catch errors immediately
```

---

### SESSION FILE BUDGET

For any multi-file session, set a file budget before starting:

```
SESSION BUDGET:
  Files to read:    [list them by name — no surprises]
  Lines per file:   [estimated — use wc -l first]
  Total lines:      [sum — if > 400, reduce scope or split session]
  
If total estimated lines > 400:
  Split into two sessions
  Or narrow the task scope
  Or use a swarm agent to parallelize
```

---

## MODULE 6 — BASH COMMAND ECONOMY
*Lines 377–440 | Load when: writing or reviewing bash commands in any session*

### THE TWO-TOOL RULE

```
Bash  = scout    → finds, filters, counts, locates. Never loads content.
Read  = loader   → loads confirmed targets only. Never used to search.
```

If you find yourself using Bash to load content (cat, head, tail) — stop. That is the Read tool's job and it does it better with offset+limit.

---

### COMMAND DECISION TABLE

| Need | Command | Never Use |
|------|---------|-----------|
| Find files by name | `find . -name "*.md"` | `ls -R` (recursive, unfiltered) |
| Find files by content | `grep -rl "keyword" path/` | `cat file \| grep` |
| Get line numbers | `grep -n "header" file.md` | Read full file then search |
| Check file size | `wc -l file.md` | Read file then count |
| List directory | `ls path/` | `ls -la` (unnecessary detail) |
| Recent changes | `find . -mtime -7 -name "*.md"` | `git log` for non-git search |
| Count files | `find . -name "*.md" \| wc -l` | Open each and count |
| Directory depth | `find . -maxdepth 2` | Unrestricted find on large trees |

---

### HIGH-EFFICIENCY COMMAND PATTERNS

**Pattern 1 — Locate then read**
```bash
grep -n "^## MODULE 3" shared/skills/skill_extraction-workflow.md
# → 157: ## MODULE 3 — FILE EXTRACTION PROTOCOL
# Then: Read offset=157, limit=80
```

**Pattern 2 — Filter before scan**
```bash
find D.R.D -name "drd_decode_*" | grep "consciousness"
# → narrows to consciousness deconstructions only
# Then: ls those files, check sizes, header scan confirmed target
```

**Pattern 3 — Size check before commit**
```bash
wc -l D.R.D/context
# → 362 lines
# Decision: use ref_drd.md instead. Do not load 362 lines.
```

**Pattern 4 — Index before search**
```bash
grep -n "PsyberMagick\|psybermagick" D.R.D/DRD_INDEX.md
# → 62: | [PsyberMagick — Peter Carroll](...) | raw-extract |
# Now I know the stage and path without opening the research file.
```

---

### COMMANDS THAT ARE BANNED IN THE OS

```
❌  cat /path/file.md              loads entire file into bash output
❌  head -n 100 file.md            loads content, use Read offset+limit
❌  tail -n 50 file.md             loads content, use Read with offset
❌  find / -name "*.md"            scans entire filesystem — use specific paths
❌  grep -r "keyword" /            no path restriction — unbounded
❌  ls -R                          recursive list without depth limit
```

---

## MODULE 7 — TOKEN BUDGET PROTOCOL
*Lines 442–495 | Load when: starting any session or before a complex multi-file operation*

### THE BUDGET QUESTION

Before any file action, answer this:

> **"What is the minimum number of lines I need to load to complete this task?"**

If you cannot answer this question — you do not have enough precision in your target yet. Return to Module 1.

---

### TOKEN COST REFERENCE

```
1 line of markdown         ≈  5–8 tokens
Department ref card        ≈  150–200 tokens   (28–35 lines)
Single workflow stage      ≈  200–350 tokens   (40–70 lines)
Full workflow file         ≈  1,500–2,000 tokens  (300–400 lines)
Full context file          ≈  1,200–1,800 tokens  (240–360 lines)
Full skill file            ≈  500–1,000 tokens  (100–200 lines)
PDF page                   ≈  300–600 tokens
One grep command           ≈  5–15 tokens (result lines only)
One find command           ≈  5–20 tokens (paths only)
```

---

### SESSION BUDGET TIERS

```
TIER A — SURGICAL (target: < 500 tokens of file content)
  Single stage file only. No context. No full skills.
  Use for: executing a known task at a known stage.

TIER B — STANDARD (target: 500–1,200 tokens of file content)
  Ref card + one stage file + one skill section.
  Use for: most working sessions.

TIER C — ARCHITECTURAL (target: 1,200–2,500 tokens of file content)
  Ref card + full context + one workflow stage + one full skill.
  Use for: system design, cross-department work.
  Requires explicit justification before loading.

TIER D — FULL LOAD (> 2,500 tokens of file content)
  Multiple full files loaded.
  Use for: initial OS setup, major architectural redesign only.
  Requires Morph confirmation before proceeding.
```

---

### THE PRE-SESSION DECLARATION

Every session that involves file reading begins with this internal check:

```
BUDGET TIER:      [A / B / C / D]
FILES TO LOAD:    [list by name]
ESTIMATED TOKENS: [sum from cost reference above]
JUSTIFICATION:    [why this tier is needed for this task]
```

If the tier is C or D — state it explicitly. Do not silently load large files.

---

## MODULE 8 — OUTPUT STRUCTURING
*Lines 497–550 | Load when: writing extracted content to a file*

### THE ONE-EXTRACTION RULE

Content extracted from any source — file, PDF, repo, web — is structured and filed immediately so it never needs to be re-extracted. Unstructured extraction that must be re-read to be used is a waste of the extraction.

---

### EXTRACTION OUTPUT FORMAT

For every piece of extracted content, produce this structure:

```markdown
## EXTRACT — [SOURCE NAME]
**Date:** [YYYY-MM-DD]
**Source:** [file path or external reference]
**Tier:** [1–5]
**Pages/Lines:** [range read]
**Sub-question addressed:** [from D.R.D Stage 1 or active task]

### CLAIM
[Exact claim — precise, not paraphrase]

### LIMITATION
[What this source cannot fully establish]

### CONTRADICTION
[Does this conflict with another source? Name it.]

### CONFIDENCE
[ESTABLISHED / PROBABLE / POSSIBLE / CONTESTED / NEEDS EVIDENCE]
```

---

### WHERE EXTRACTED CONTENT IS FILED

```
PDF extraction          → research/[domain]/drd_research_[topic]_raw-extract.md
Repo extraction         → D.I.I/research/dii_research_[repo-name]_raw-extract.md
File scan findings      → the active task file (do not create a new file for scan results)
Cross-file search       → inline in the document being built
```

---

### HEADER BLOCK STANDARD

Every file written or updated in the OS begins with this block:

```markdown
# [FILE NAME IN CAPS]
**[Department] | [File type] | Status: [active/draft/archived]**
**Load when:** [specific trigger — one line]
**Do not load when:** [what this file is NOT for]
**Produces:** [what using this file outputs]
```

Files without this header are retrofitted before being used in a session. A missing header is a broken navigation system — it costs tokens every time that file is encountered.

---

## MODULE 9 — AGENTIC ROUTING
*Lines 552–600 | Load when: a department agent or swarm agent is active*

### HOW AGENTS USE THIS WORKFLOW

Every agent operating inside the Pandora OS loads this workflow's index (lines 1–38) at spawn. The index tells the agent which module applies to the current task. The agent loads only that module — not the full workflow.

**Agent spawn sequence:**
```
1. Load ref_[dept].md            (28 lines — orientation)
2. Load this index (lines 1–38)  (38 lines — workflow routing)
3. Load active module            (40–80 lines — the process)
4. Execute
```
Total context from workflow: ~80–120 lines maximum.

---

### DEPARTMENT AGENT SCOPE RULES

```
RULE 1 — BOUNDARY
  A department agent reads only its department's files
  and shared/skills/ files routed to it by its ref card.
  It does not open other departments' files.

RULE 2 — NO REDUNDANT LOADING
  If the ref card was loaded at spawn — it is not reloaded.
  If a workflow stage was loaded — it is not reloaded mid-session.
  Context persists within the session. Reload = waste.

RULE 3 — COGNITIVE PROMPT FIRST
  Before every file action, the agent runs Module 1.
  No exceptions. The cognitive prompt is the agent's discipline.

RULE 4 — OUTPUT BEFORE CLOSE
  Before closing, the agent confirms:
  [ ] Extracted content structured per Module 8
  [ ] Files updated with header blocks if missing
  [ ] Index updated if research stage advanced
  [ ] Next stage file identified and named (but not loaded)
```

---

### SWARM AGENT SCOPE RULES

```
SWARM WORKER LOADS:
  This index (lines 1–38)
  Module 3 or 4 only (extraction — workers do not reconstruct)
  Its assigned sub-questions (passed at spawn, not loaded from file)

SWARM WORKER PRODUCES:
  One structured extract per sub-question (Module 8 format)
  Returns to coordinator — does not write to files directly

COORDINATOR RECEIVES:
  All worker extracts
  Runs Module 5 (multi-file merge logic)
  Writes consolidated output
  Updates index and cross-links
```

---

## MODULE 10 — QUICK REFERENCE + FAILURE MODES
*Lines 602–645 | Load when: troubleshooting or needing a fast rule reminder*

### ONE-LINE RULES

```
Before any Read call — run Module 1. Always.
Before any multi-file session — set a token budget. Always.
Bash scouts. Read loads. Never reverse this.
Header scan first. Grep second. Targeted read third.
Index before individual files. Every time.
PDF: index pages 1-3 first. Never load the whole document.
Extracted content: structured and filed immediately. Never raw.
Agents: load the index. Load one module. Execute. Done.
Full file loads require justification. Silence is not justification.
Re-reading what is in context is the primary token failure mode.
```

---

### FAILURE MODES AND CORRECTIONS

| Failure | Indicator | Correction |
|---------|-----------|------------|
| Full file load without targeting | Reading 300+ lines for a single section | Grep first, then offset+limit |
| Re-reading context | Loading a file already read this session | Check what is in context before loading |
| Scanning with Read | Using Read to browse instead of find/grep | Bash for scanning, Read for confirmed targets |
| PDF full load | No pages parameter on a large PDF | Always use pages parameter |
| Vague target | Cannot specify what line range is needed | Return to Module 1 before proceeding |
| Missing header | File has no header block | Add header before using the file |
| Unstructured extraction | Notes written without Module 8 format | Reformat before filing |
| Agent scope creep | Agent reading outside its department | Enforce boundary rule — close and re-scope |
| Budget exceeded silently | Loaded Tier C without declaration | Declare budget tier before loading |

---

### GREP COMMAND QUICK REFERENCE

```bash
grep -n  "^##" file.md          # all section headers with line numbers
grep -rl "keyword" path/        # files containing keyword (names only)
grep -rn "keyword" path/        # files + line numbers + matched line
find . -name "*.md" -type f     # all markdown files from current dir
find . -name "pattern*"         # files matching name pattern
wc -l file.md                   # line count before loading
find . -maxdepth 2 -name "*.md" # two directory levels only
find . -mtime -7 -name "*.md"   # files modified in last 7 days
```

---

*SKILL_EXTRACTION_WORKFLOW | Pandora OS | All departments | All agents*
*"Precision before action. The question determines the cost."*

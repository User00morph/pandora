# SKILL — REPO EXTRACTION
**Loadable by: D.I.I, D.S.C, D.R.D. Load when processing open source repositories.**

---

## WHAT THIS SKILL IS

The protocol for extracting sovereign intelligence from open source repositories and converting it into Pandora OS artifacts — workflow stages, skill files, agent definitions, local MCP servers, and local APIs. Open source code is raw material. This skill is the alchemy that converts it into sovereign infrastructure.

All extracted content passes through the Data Refinement Protocol before integration.

---

## WHEN TO LOAD

- A repository has been identified as relevant to a Pandora OS department
- Building a local MCP server from an open source foundation
- Extracting workflow patterns, frameworks, or APIs from external codebases
- Evaluating a library or tool for integration into the OS

---

## THE REPO EXTRACTION PIPELINE

### STEP 1 — STRUCTURE SCAN (no content yet)
Understand what the repo contains before reading any files.

```bash
# If cloned locally:
find /path/to/repo -type f -name "*.md" | head -20    # documentation
find /path/to/repo -type f -name "*.py" | head -20    # Python files
find /path/to/repo -type f -name "*.js" | head -20    # JS files
ls /path/to/repo                                       # root structure

# What to look for:
README.md          → purpose, dependencies, usage
requirements.txt   → what it depends on
package.json       → JS dependencies and entry points
/examples/         → how it is actually used
/docs/             → architecture documentation
/src/ or /lib/     → core logic
```

**Output of Step 1:** A file map — what exists and where, without reading content.

---

### STEP 2 — README + DOCS FIRST
Read documentation before code. Documentation tells you what the code does. Code tells you how. Always understand what before how.

```
READ IN THIS ORDER:
  1. README.md (full — usually short enough)
  2. /docs/ index or overview file
  3. Any ARCHITECTURE.md or DESIGN.md
  4. Examples directory — what does actual usage look like?

EXTRACT:
  - Core purpose in one sentence
  - What problem it solves
  - Key concepts and vocabulary it uses
  - Dependencies it requires
  - License (important for sovereign use)

SOURCE TIER ASSIGNMENT:
  Established open source project (1000+ stars, active maintenance) → Tier 2–3
  Small or personal project → Tier 4
  Abandoned or unmaintained → Tier 4–5
```

---

### STEP 3 — TARGETED CODE EXTRACTION
After documentation, read only the files that contain the patterns you need.

```
FOR EACH TARGET FILE:
  Header scan first (lines 1–20)
  Grep for the specific function or pattern needed
  Read only the relevant section (offset + limit)
  Never read full codebases — extract the pattern

PATTERNS WORTH EXTRACTING FOR PANDORA OS:
  Agent definitions     → how agents are structured, prompted, scoped
  Tool implementations  → how tools/functions are defined and called
  API endpoints         → routes, request/response formats
  Data pipelines        → how data flows through the system
  Configuration files   → how the system is configured and parameterized
  Prompt templates      → how prompts are structured for specific tasks
```

---

### STEP 4 — CONVERT TO PANDORA OS FORMAT

Extracted patterns are converted into one or more of these artifact types:

**A — WORKFLOW STAGE FILE**
When the repo contains a multi-step process:
```
repo pattern: scrape → clean → analyze → output
converts to: wf_stage-1_[process].md → wf_stage-2_[process].md etc.
filed in:    D.I.I/workflow/ or relevant department
```

**B — SKILL FILE**
When the repo contains a reusable capability:
```
repo pattern: a specific method, algorithm, or process
converts to: skill_[capability].md
filed in:    shared/skills/
format:      follows existing skill format (what it is, when to load, protocol)
```

**C — AGENT DEFINITION**
When the repo defines an agent or assistant pattern:
```
repo pattern: system prompt, tool definitions, agent loop
converts to: agent_[name].md with frontmatter
filed in:    .claude/agents/
format:      name, description, tools, model, system prompt
```

**D — LOCAL MCP SERVER**
When the repo provides tools or data the OS needs on-demand:
```
repo pattern: API, data source, tool functions
converts to: MCP server built on repo's core logic
filed in:    tools/mcp-servers/[server-name]/
config:      registered in .claude/settings.json
```

**E — LOCAL API**
When the repo contains a service the OS needs to call:
```
repo pattern: web service, REST API, data endpoint
converts to: local FastAPI or Node wrapper
filed in:    tools/apis/[api-name]/
access:      called via Bash tool or MCP
```

---

### STEP 5 — D.R.D REFINEMENT GATE

Before any converted artifact is integrated into the OS:

```
[ ] Source tier assigned to the originating repo
[ ] License checked — is sovereign use permitted?
[ ] Patterns evaluated for accuracy and reliability
[ ] Dependencies mapped — what does this require to run?
[ ] Sovereign adaptation noted — what was changed from the original and why?
[ ] Confidence level assigned to the implementation

FILE the extraction record in:
  D.I.I/research/dii_research_[repo-name]_raw-extract.md

FILE the converted artifact in its target location only after gate passes.
```

---

## PRIORITY REPOS FOR PANDORA OS

These categories of repos produce the highest-value Pandora OS artifacts:

```
MCP SDK (Python or TypeScript)
  → Produces: local MCP server templates
  → Department: D.I.I
  → Converts to: MCP server scaffolding in tools/mcp-servers/

Ollama / LM Studio
  → Produces: local AI model deployment instructions
  → Department: D.I.I
  → Converts to: skill_local-model-deployment.md

FastAPI
  → Produces: local API server pattern
  → Department: D.I.I + D.S.C
  → Converts to: local API scaffold in tools/apis/

LangGraph / CrewAI (pattern extraction only — no dependency)
  → Produces: swarm agent orchestration patterns
  → Department: D.I.I
  → Converts to: agent swarm protocol files

Syncthing
  → Produces: peer-to-peer file sync (no cloud)
  → Department: D.I.I + D.H.S
  → Converts to: sovereign file sync SOP

Whisper (OpenAI open source)
  → Produces: local audio transcription
  → Department: D.R.D + D.C.E
  → Converts to: transcript extraction workflow
```

---

## FILE STRUCTURE FOR EXTRACTED ARTIFACTS

```
Pandora/
├── tools/
│   ├── mcp-servers/
│   │   ├── pandora-file-index/    ← file search MCP
│   │   ├── pandora-research-db/   ← DRD research query MCP
│   │   └── pandora-natal/         ← DPSA natal data MCP
│   └── apis/
│       ├── pandora-search/        ← internal search API
│       └── pandora-sync/          ← file sync API
├── .claude/
│   └── agents/                    ← department + swarm agents
└── shared/
    └── skills/                    ← extracted and converted skills
```

---

*SKILL_REPO_EXTRACTION | Pandora OS | D.I.I primary | D.R.D refinement required*
*"Open source is the raw material. Sovereign adaptation is the alchemy."*

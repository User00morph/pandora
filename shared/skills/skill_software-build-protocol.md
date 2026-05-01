# SKILL — SOFTWARE BUILD PROTOCOL
**Operational protocol for building HTML, JavaScript, Python, and multi-language projects at scale.**
**Load after: `skill_agentic-architecture.md` | Load before: any software build session.**
**Loadable by: D.I.I, D.S.C — all software builds pass through this protocol.**

---

## WHAT THIS SKILL IS

The sovereign protocol for constructing software at any scale using Claude Code as the Digital Reality Engineer. Applies the Pandora alchemical lifecycle to the software development process — from raw concept through living, deployed system. Covers project setup, architecture, component builds, testing loops, and deployment for HTML, JavaScript, Python, and any combination thereof.

---

## PRE-BUILD REQUIREMENT

Before a single file is created, three things must exist:

```
1. PRD (Product Requirements Document)
   Load: skill_prd-creation.md
   File: dsc_prd_[project-name]_v1.md
   Contains: what is being built, why, what done looks like,
             phase architecture, kill conditions

2. FILE TREE (complete structure before any code)
   Every directory and filename defined before any file is written.
   The file tree is the architectural declaration.
   Empty files with correct names are created first.
   Code fills the structure — not the other way around.

3. DEPENDENCY MAP
   All external packages identified before installation.
   npm packages, pip packages, system tools.
   No mid-build surprise dependencies.
```

If any of these three are missing — do not begin. Complete them first.

---

## THE BUILD LIFECYCLE

### STAGE 1 — NIGREDO: SEED THE STRUCTURE

```
ACTION:
  Create the project root directory
  Create the complete file tree (empty files, correct names)
  Initialize git: git init → first commit = "init: project structure"
  Create: README.md, .gitignore, requirements.txt or package.json
  Install all dependencies before writing any logic

TOOLS:
  Bash → mkdir, touch, git init, npm init, pip install
  Write → README.md, .gitignore, dependency files

OUTPUT: Empty but complete project structure. Git initialized. Zero logic written.
CHECKPOINT: git commit -m "init: project structure and dependencies"
```

---

### STAGE 2 — ALBEDO: ARCHITECTURE LAYER

```
ACTION:
  Define the data flow (what enters, what transforms, what exits)
  Map all components and their relationships
  Define all API routes or page routes before implementing any
  Write interface contracts (function signatures, API schemas)
    before writing any implementation
  Comment-only files that define what each module does —
    before writing what each module does

TOOLS:
  Write → architecture.md (living document, updated as build progresses)
  Edit → add interface stubs to created files

PYTHON PATTERN:
  # Define function signatures with docstrings — no implementation yet
  def process_data(input: dict) -> dict:
      """Takes raw input, returns refined output. Called by main()."""
      pass

JS/HTML PATTERN:
  // Define component structure as comments before any code
  // Component: DataProcessor
  // Input: rawData (object)
  // Output: refinedData (object)
  // Dependencies: utils.js, api.js

OUTPUT: Full interface layer. No logic. All contracts defined.
CHECKPOINT: git commit -m "arch: component interfaces and data flow defined"
```

---

### STAGE 3 — CITRINITAS: COMPONENT BUILD LOOP

The core build phase. One component at a time. Test after each.

```
FOR EACH COMPONENT:

  BUILD:
    Implement the component fully
    Follow the interface contract from Stage 2
    Do not modify other components during this step

  TEST IMMEDIATELY:
    Python: python -m pytest tests/[component]_test.py
    JS: npm test -- --testPathPattern=[component]
    HTML: start local server, check in browser via screenshot or curl
    API: curl the endpoint, read the response

  READ THE ERROR:
    If test fails — read the full error output
    Identify root cause before attempting fix
    Fix the root cause — not the symptom

  COMMIT:
    git commit -m "build: [component-name] complete and tested"

  MOVE TO NEXT COMPONENT:
    Only after current component passes its test.
    Never move forward with a failing component.
```

**COMPONENT BUILD ORDER (dependency-first):**
```
1. Data layer first (models, schemas, database connections)
2. Logic layer second (processing, transformations, business rules)
3. API/route layer third (endpoints that call the logic layer)
4. Interface layer last (HTML, UI — consumes the API layer)
```

---

### STAGE 4 — RUBEDO: INTEGRATION AND DEPLOYMENT

```
ACTION — INTEGRATION TESTING:
  Run the full system together for the first time
  Test the complete data flow end-to-end
  Identify integration failures (components work alone but not together)
  Debug at the integration boundary — not inside components

ACTION — PERFORMANCE:
  Time critical operations: Bash → time python script.py
  Check response times on API endpoints
  Identify bottlenecks before deployment

ACTION — DEPLOYMENT PREP:
  Environment variables documented in .env.example
  Production config separated from development config
  All secrets out of code and into environment
  Dockerfile or deployment script created
  Final README.md updated with setup instructions

CHECKPOINT: git commit -m "deploy: integration complete, production ready"
OUTPUT: Live system. Filed as dii_integration_[project-name]_live.md
```

---

## LANGUAGE-SPECIFIC PATTERNS

**PYTHON**
```bash
python -m venv .venv && source .venv/bin/activate   # isolated environment
pip install -r requirements.txt                      # install dependencies
python -m pytest tests/ -v                           # run all tests verbose
python -m flask run --debug                          # Flask dev server
uvicorn main:app --reload                            # FastAPI dev server
```

**JAVASCRIPT / NODE**
```bash
npm init -y                          # initialize package.json
npm install [package]                # add dependency
npm run dev                          # start dev server
npm test                             # run test suite
node --inspect server.js             # debug mode
```

**HTML / CSS**
```bash
python -m http.server 8000           # instant local server (no install)
curl http://localhost:8000           # test without browser
```

**GIT CHECKPOINTS**
```bash
git init                             # initialize
git add [specific files]             # never git add . blindly
git commit -m "type: description"    # types: init / arch / build / fix / deploy
git diff HEAD~1                      # review what changed since last commit
```

---

## PARALLEL BUILD PATTERN (SWARM)

For large projects where components are independent:

```
COORDINATOR (main agent):
  Defines file tree and interfaces (Stage 1–2)
  Assigns components to workers
  Integrates completed components (Stage 4)

WORKER AGENTS (spawned in parallel):
  Each receives: one component + its interface contract
  Each produces: implemented + tested component
  Returns to coordinator for integration

RULE: Workers only build. They do not redesign architecture.
      If a worker discovers an interface problem — return to coordinator.
      Do not silently change a contract mid-build.
```

---

## BUILD SESSION TOKEN BUDGET

```
PRD review:          ~300 tokens
File tree creation:  ~100 tokens
Per component build: ~500–1,500 tokens (size dependent)
Integration test:    ~300–500 tokens
Total per session:   target < 15,000 tokens of file content loaded

If approaching context limit mid-build:
  Commit current state
  Document exactly where the build stopped and what is next
  Start fresh session — context is in the files, not the conversation
```

---

## BUILD FAILURE PROTOCOL

```
ERROR RECEIVED → Read it fully before attempting a fix
ROOT CAUSE → Identify which layer the error originates in
              (data / logic / API / interface / integration)
FIX SCOPE → Fix only the root cause. Do not refactor unrelated code.
VERIFY → Run the same test that caught the error
DOCUMENT → If the error reveals a design flaw — update architecture.md
```

---

*SKILL_SOFTWARE_BUILD_PROTOCOL | D.I.I + D.S.C | Pandora OS*
*"The structure precedes the logic. The logic precedes the interface. The test follows each."*

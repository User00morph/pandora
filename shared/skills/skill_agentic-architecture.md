# SKILL — AGENTIC ARCHITECTURE
**How Claude Code works as an agent. Load before any large-scale software build.**
**Loadable by: D.I.I, D.S.C, D.R.D (for AI research), all departments initiating builds.**

---

## WHAT THIS SKILL IS

The breakdown of Claude Code as an agentic system — its perception layer, reasoning layer, action layer, tool inventory, capabilities, and hard limits — translated into Pandora OS operational knowledge. Understanding how the agent actually works determines how to direct it with maximum precision and minimum waste.

---

## THE AGENT LOOP

Every action inside Claude Code follows this cycle:

```
CONTEXT LOAD
All loaded files, conversation history, tool results, CLAUDE.md
           ↓
REASON
Plan the next action. Select the right tool. Frame the operation.
           ↓
ACT
Execute one tool call. Bash, Read, Write, Edit, Agent, MCP.
           ↓
RECEIVE
Tool result enters context. Updates the reasoning state.
           ↓
REASON AGAIN
Does the result complete the task? What is the next action?
           ↓
REPEAT until task is complete or context limit is approached.
```

The loop runs until the task resolves or Morph redirects it. Each iteration costs tokens. Precision in the REASON step determines whether the loop runs 3 iterations or 30.

---

## THE THREE LAYERS

**LAYER 1 — PERCEPTION (what the agent receives)**
```
CLAUDE.md + pandora.md       → identity, routing, operating rules
Loaded .md files             → department context, skills, workflow stages
Bash tool output             → file paths, line numbers, command results
Read tool output             → file content, PDF pages
Conversation history         → what has been established this session
MCP tool results             → custom data from local servers
```

**LAYER 2 — COGNITION (how the agent reasons)**
```
Planning          → breaking a task into ordered steps before acting
Tool selection    → choosing the right tool for the specific operation
Code generation   → writing HTML, JS, Python, Bash from intent
Debugging         → reading error output, tracing root cause, fixing
Synthesis         → combining outputs from multiple tools/files
Routing           → reading the Pandora map and navigating to the right file
```

**LAYER 3 — ACTION (what the agent does)**
```
Read              → load file content (offset, limit, pages)
Write             → create new files
Edit              → targeted string replacement — surgical, not wholesale
Bash              → shell operations: git, npm, python, find, grep, servers
Agent             → spawn sub-agents for parallel or scoped work
WebFetch          → load a URL into context
WebSearch         → search the web for specific information
MCP tools         → custom local tools built into the OS
Task tools        → create, track, update work inside the session
```

---

## TOOL INVENTORY — PANDORA APPLICATIONS

| Tool | What It Does | Pandora Use Case |
|------|-------------|-----------------|
| Read | Load file or PDF section | Load workflow stage, skill, research file |
| Write | Create new file | Generate .md artifacts, code files, agents |
| Edit | Replace specific string | Update ref cards, patch code, refine skills |
| Bash | Execute shell commands | git, npm, python, find, grep, server startup |
| Agent | Spawn scoped sub-agent | Department agent, swarm worker, parallel build |
| WebFetch | Fetch URL content | Load documentation, repo readmes, references |
| WebSearch | Search the web | Find open source repos, technical docs |
| MCP | Call custom local tool | Pandora file index, research DB, natal data |

---

## CAPABILITIES AT SCALE

```
MULTI-FILE BUILDS
Build and manage codebases across dozens of files simultaneously.
Tracks file relationships, imports, and dependencies across the build.

MULTI-LANGUAGE
HTML, CSS, JavaScript, Python, Bash, JSON, YAML — all in one session.
Language does not limit the build. Context window does.

GIT WORKFLOWS
init, branch, commit, push, pull, merge, diff — full git operation.
Branches for feature builds. Commits as build checkpoints.

TEST-DRIVEN LOOPS
Write test → run test → read error → fix → rerun.
Automated feedback loops with zero manual intervention.

PARALLEL EXECUTION
Agent tool spawns multiple sub-agents simultaneously.
Each handles one component. Coordinator integrates outputs.
3–5 agents in parallel = 3–5x build speed on independent tasks.

SERVER STARTUP AND TESTING
Start local dev server via Bash. Monitor output.
Test endpoints, read responses, debug live behavior.

DEPENDENCY INSTALLATION
npm install, pip install, brew install — full package management.
Reads package.json, requirements.txt, manages environment.
```

---

## HARD LIMITS — SOVEREIGN AWARENESS

```
CONTEXT WINDOW
~200K tokens total capacity. Practically efficient at 20–40K.
Long sessions accumulate context. Large file loads exhaust budget.
Solution: ref cards, stage files, targeted reads. Built into the OS.

NO PERSISTENT MEMORY
Nothing persists between sessions except files.
Files are the agent's memory. What is not written is lost.
Solution: structured output filing after every session.

NO INTERACTIVE PROCESSES
Cannot run processes requiring keyboard input mid-execution (TTY).
Cannot hold an interactive REPL open.
Solution: script everything. Use non-interactive flags (-y, --yes).

NO VISUAL UI
Cannot see browser output, rendered HTML, or GUI applications.
Solution: screenshot workflow, or test via API/CLI response only.

SANDBOX RESTRICTIONS
Some Bash operations require user permission approval.
Destructive operations (rm, force push) trigger confirmation.
Solution: design builds non-destructively. Stage before committing.

TOKEN COST PER ACTION
Every tool call costs tokens. Every file load costs tokens.
A 10-file session with no targeting can exhaust context before the build completes.
Solution: extraction workflow + cognitive prompt before every action.
```

---

## PANDORA SOVEREIGN MAPPING

```
INSTITUTIONAL ROLE          SOVEREIGN EQUIVALENT IN PANDORA
Software Developer     →    Digital Reality Engineer
Project Manager        →    Systems Cultivation Architect (D.S.C)
QA Engineer            →    Legitimacy Review Protocol
DevOps Engineer        →    Sovereign Infrastructure Architect (D.I.I)
Database Admin         →    Sovereign Data Architect
Frontend Dev           →    Expression Layer Engineer (D.C.E + D.I.I)
Backend Dev            →    Logic Architecture Engineer (D.I.I + D.S.C)
```

---

## HOW TO DIRECT THE AGENT FOR MAXIMUM OUTPUT

```
PRECISION OVER BREADTH
One specific task per instruction produces better output than
five tasks combined. The agent can handle complexity —
but complexity framed as specifics, not as vague directions.

CONTEXT BEFORE QUESTION
State what is already built, what stage you are at,
and what the constraints are — before asking what to do next.
The agent produces to the quality of the context it receives.

FILE FIRST
For any build: establish the file structure before writing code.
Empty files with correct names and paths ground the agent
in the architecture before a single line of logic is written.

CHECKPOINTS
For long builds: commit after each component completes.
A git commit is a mental checkpoint and a recovery point.
Never run 3 hours of build without checkpointing.

TEST AFTER EACH UNIT
Do not build all components then test.
Test each unit as it is built.
Catching errors at the unit level costs 10x less than catching
them at the integration level.
```

---

*SKILL_AGENTIC_ARCHITECTURE | D.I.I | Pandora OS*
*"Understanding the tool at its root is what separates sovereign use from passive consumption."*

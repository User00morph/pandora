# SKILL — LEAN-CTX CONTEXT COMPRESSION
**Load when: context budget is tightening, reading many files in a session, running verbose shell commands, or coordinating multiple agents.**
**Loadable by: ALL departments — universal token efficiency layer.**

---

## WHAT THIS SKILL IS

lean-ctx is a context compression runtime — a local intelligence buffer that strips noise from file reads and shell output before it reaches the LLM. A file you've already read costs ~13 tokens on re-read. A verbose git diff becomes a few focused lines. This skill governs how to use it inside Pandora OS for maximum efficiency.

**Source repo:** `~/Desktop/pandorareposkills/lean-ctx/`
**Installation:** `which lean-ctx || lean-ctx init --global`

---

## THE 10 READ MODES — PANDORA MAPPING

| Mode | Token Cost | Use When |
|------|-----------|----------|
| `auto` | adaptive | Default — let lean-ctx select the optimal mode |
| `full` | high | You will edit this file — need every line |
| `map` | 5–15% | Need to understand what a file does, not read it |
| `signatures` | 10–20% | Need the API surface of a module only |
| `diff` | minimal | Only want lines changed since last read |
| `aggressive` | 30–50% | Context-only reference — no editing |
| `entropy` | 20–40% | Noisy files with repetitive content |
| `task` | task-relevant | IB-filtered — only lines relevant to current task |
| `reference` | minimal | Quote-friendly excerpts |
| `lines:N-M` | targeted | Specific range — use when grep found the line |

**Pandora principle:** Use `map` first on any file you haven't confirmed you need fully. Switch to `full` only when editing is confirmed.

---

## SHELL COMPRESSION PROTOCOL

Replace raw Bash output with compressed lean-ctx equivalents:

```bash
lean-ctx -c git status          # stripped git output
lean-ctx -c git diff            # meaningful diff lines only
lean-ctx -c git log --oneline -10
lean-ctx -c npm install         # strips progress bars and noise
lean-ctx -c cargo build
lean-ctx -c cargo test
lean-ctx -c docker ps
lean-ctx -c curl -s <url>       # JSON schema extraction, not full response
```

**When to apply:** Any command that produces verbose output — build logs, dependency installs, test results, diffs.

---

## MULTI-AGENT CONTEXT SHARING

For swarm operations and parallel agent builds — use lean-ctx MCP tools instead of re-loading the same files in each agent:

```
ctx_knowledge(action="remember", category, key, value)   — store cross-session facts
ctx_knowledge(action="recall", query)                    — retrieve stored facts
ctx_knowledge(action="consolidate")                      — extract session findings to permanent store

ctx_agent(action="register", agent_type, role)           — register in multi-agent workspace
ctx_agent(action="post", message, tags)                  — share findings with other agents
ctx_agent(action="read")                                 — read messages from other agents
ctx_agent(action="handoff", to_agent, message)           — transfer task to another agent

ctx_share(action="push", paths, to_agent, message)       — push cached file contexts to agent
ctx_share(action="pull")                                 — pull contexts from other agents
```

**Pandora application:** When swarm-coordinator spawns parallel sub-agents, use `ctx_share` to push the already-loaded department context into each agent instead of re-reading the same ref cards.

---

## SESSION CONTINUITY (CCP)

Cross-session project memory — persists between Claude Code sessions without relying on file writes:

```bash
lean-ctx sessions list          # list all CCP sessions
lean-ctx sessions show          # show latest session state

# MCP tools (use inside sessions):
ctx_session(action="load")                     # restore previous session state
ctx_session(action="task", description="...")  # set current task
ctx_session(action="finding", text="file:line — summary")  # record key finding
ctx_session(action="decision", text="...")     # record architectural decision
ctx_session(action="save")                     # force persist to disk
```

**Pandora application:** At session start, `ctx_session load` restores context from the previous session. Complements the ref card `Current State` section — lean-ctx holds the runtime state, the ref card holds the structured log.

---

## PROACTIVE PROTOCOL

Run these at session start without being asked:

```
ctx_overview(task="[session goal]")   — task-relevant project map
ctx_preload(task="[session goal]")    — proactively cache task-relevant files
```

---

## TOKEN SAVINGS AUDIT

```bash
lean-ctx gain          # visual token savings dashboard (current session)
lean-ctx dashboard     # web dashboard at localhost:3333
lean-ctx wrapped       # weekly savings report card
```

The output suffix `[lean-ctx: 5029→197 tok, -96%]` appears on compressed commands — shows original vs compressed token count.

---

## PANDORA CONTEXT HYGIENE INTEGRATION

lean-ctx operates at the execution layer of the ICM 5-Layer System:

```
L0 — pandora.md / CLAUDE.md          Always loaded — NOT compressed
L1 — ref_[dept].md                   Use map mode if re-reading mid-session
L2 — wf_stage-[N].md                 Use signatures mode after first read
L3 — skills / _config/               Use task mode — only relevant sections
L4 — working files / source          Use full mode only when editing
```

**Hard rule:** Never use `full` mode on a file you've already read unless you are about to edit it. The cached re-read at 13 tokens is the standard.

---

*SKILL_LEAN-CTX | Pandora OS | ALL departments*
*"Every token of noise stripped is a token of reasoning gained."*

# D.R.D DECODE — Tech Playlist Tier 1: Agentic Systems Fundamentals
**Stage 3–4 | Deconstruction → Reconstruction**
**Date:** 2026-06-09
**Source:** Pandora Tech Playlist — 5 Tier 1 videos (~48,835 words total)
**Decoded by:** D.R.D pipeline | D.I.I integration target

---

## SOURCE BLOCK

| # | Title | ID | Words | Tier |
|---|-------|----|-------|------|
| 1 | CLI vs MCP: How AI Agents Choose the Right Tool | g9JIUM0MHgQ | ~2,008 | 1 |
| 2 | Context Engineering in 29 Minutes | -h9VVJIqtvA | ~6,782 | 1 |
| 3 | Running LLMs Locally (Ollama + MCP) | GAyNvq6Ayps | ~5,995 | 1 |
| 4 | Claude Architect: Multi-Agent Orchestration | vRYBG_R8JAI | ~23,499 | 1 |
| 5 | Build an Agentic GraphRAG System (MCP + Knowledge Graph) | LnCXoIr0Mw8 | ~10,551 | 1 |

**Raw extracts filed:** `D.R.D/research/tech-decentralization/drd_research_tech-playlist-t1-[slug]_raw-extract.md`

---

## SECTION 1 — CLI vs MCP: THE DECISION RULE

### Core Finding
CLI and MCP are not competing tools — they are complementary layers. The decision rule is determined by one question: **is there a gap between what the raw tool gives you and what you actually need?**

### The Decision Framework (ESTABLISHED — demonstrated with live tests)

| Condition | Use CLI | Use MCP |
|-----------|---------|---------|
| Model already knows the tool from training (git, grep, curl, ls) | ✓ | — |
| Tool output maps directly to task | ✓ | — |
| Need to chain operations (pipes) | ✓ | — |
| External service requires auth (Slack, Notion, databases) | — | ✓ |
| JavaScript SPA / rendered web content | — | ✓ |
| Need audit trail or per-user access control | — | ✓ |
| Multi-tenant governance requirement | — | ✓ |

### Token Cost Reality (ESTABLISHED — measured)
- GitHub MCP server: 80 tools = **~55,000 tokens** loaded at session init — before any work
- File system MCP server: 13 tools = ~2,000 tokens loaded even if only 2 are used
- CLI alternative for same git operations: 2 bash commands, near-zero token overhead

**Key principle:** MCP pays a context tax. That tax is worth it only when the abstraction or governance layer justifies it.

### Anti-pattern (ESTABLISHED — demonstrated)
Agent used to scrape a Next.js webpage via curl. Spent several minutes and **2,000+ tokens** reverse-engineering Next.js internal data format to get what an MCP fetch tool would have returned in 250 tokens and 2 seconds.

---

## SECTION 2 — CONTEXT ENGINEERING: THE FOUR STRATEGIES

### What Context Engineering Is (ESTABLISHED — Anthropic definition)
> "Context engineering is optimizing the utility of the tokens available to the model."

Context window = RAM. When it fills up or gets crowded, performance degrades — not at capacity limit, but gradually. A 200K token model may show significant degradation at 50K tokens (Chroma published data). Models attend well to beginning and end of context; the middle degrades ("lost in the middle" pattern).

### The Four Strategies (LangChain framework — ESTABLISHED, widely cited)

#### STRATEGY 1 — WRITE
**Problem:** Agents forget things when context fills up and gets compacted.
**Solution:** Give the agent ways to persist information OUTSIDE the context window.

| Form | Mechanism | Notes |
|------|-----------|-------|
| Scratch pad | Think tool (Anthropic) | 54% performance improvement on benchmarks |
| Rules files | CLAUDE.md / system prompt | Loaded every session — persistent procedural memory |
| Memory extraction | File-based system | Agent saves facts + patterns across sessions |

**Pandora OS mapping:** CLAUDE.md is the rules file. `pandora.md` + ref cards = persistent procedural memory. The memory system at `~/.claude/projects/` = memory extraction. **This is already correctly implemented.**

#### STRATEGY 2 — SELECT
**Problem:** Agent has access to everything — can't load it all. Something must decide what's relevant now.
**Solution:** Agent-driven selective retrieval (Agentic RAG), not static stuffing.

**3 Memory Types (LangChain + Pinecone):**
| Type | What it is | Pandora OS equivalent |
|------|-----------|----------------------|
| Episodic | Few-shot examples — "here's how you handled this before" | Session logs + prior decode files |
| Semantic | Repository of facts the agent has learned | D.R.D decoded outputs, ref cards |
| Procedural | Standing behavioral instructions | Skills files, workflow stages |

**Critical finding — tool selection accuracy:**
- RAG over tool definitions (semantic search over tool descriptions): accuracy jumped **14% → 43%**, tokens cut **~50%**
- Anthropic hybrid strategy: front-load essentials (CLAUDE.md/pandora.md), just-in-time retrieval for everything else
- If agent has 40+ tools → 10,000 tokens loaded before any work. Llama 3.1 8B **failed** a benchmark with 46 tools, **succeeded** with 19. Not a context size issue — a reasoning clarity issue.

**Pandora OS mapping:** The L0–L4 ICM loading protocol IS the SELECT strategy. Load pandora.md (L0) always. Ref card (L1) on department entry. Skills (L3) on demand. This is correctly designed. **The gap is Auset — she needs dynamic tool selection, not static tool loading.**

#### STRATEGY 3 — COMPRESS
**Problem:** Context accumulates — tool outputs, conversation history, reasoning traces pile up even after they're no longer needed.
**Solution:** Reduce token count while preserving information that matters.

3 compression points:
1. **Before entry:** Chunking + re-ranking (only best chunks enter context). Summarize tool outputs on the fly before they enter.
2. **While working:** Running summary of conversation history. Keep last 10 messages verbatim, summarize everything older.
3. **After acting:** Tool result clearing — once a tool result was used 15+ steps ago, replace with 1-line summary or remove entirely.

Claude Code auto-compacts at 95% capacity. That is a safety net, not a strategy. **Compress proactively.**

**Pandora OS mapping:** Current sessions do not compress tool results mid-session. The `proto_context-hygiene.md` covers loading efficiency but not in-session compression. **This is a gap — upgrade needed.**

#### STRATEGY 4 — ISOLATE
**Problem:** Single agent doing everything fills its context and contaminates itself — research phase debris pollutes implementation phase.
**Solution:** Give different parts of the work separate context windows (sub-agents).

Parent → delegate focused subtask → sub-agent runs on clean context → returns condensed summary only → messy operations never pollute parent.

**This is why multi-agent = folder navigation (Jake VIP). Each agent has its own clean context. The folder IS the agent identity.**

**Pandora OS mapping:** The 12 departments ARE the isolation layer. Each department = its own clean context window. D.R.D never contaminates D.S.E. D.O.M never contaminates D.I.I. **This architecture is correct by design.**

### 4 Failure Modes (Drew Breunig 2025 — ESTABLISHED)

| Failure Mode | What It Is | Fix |
|---|---|---|
| **Context Poisoning** | Bad data enters → compounds across every subsequent step | Prune actively, validate tool outputs before context entry, compress failed attempts |
| **Context Distraction** | Context so long agent over-relies on recent history, stops thinking independently | Summarize + prune aggressively even with large context available |
| **Context Confusion** | Too many tools → agent calls irrelevant tools | Dynamic tool management, RAG over tool definitions |
| **Context Clash** | System prompt contradicts retrieved document → inconsistent behavior | Clear priority rules: system prompt wins unless explicitly overridden |

---

## SECTION 3 — LOCAL MODEL STACK: OLLAMA + MCP BRIDGE

### The Stack (ESTABLISHED — demonstrated working)

```
LOCAL MODEL LAYER
├── Ollama (ollama.com) — local model runner
│   ├── ollama pull [model-name]
│   └── ollama serve (runs as background server)
│
BRIDGE LAYER (required — Ollama does not natively support MCP)
├── OLLMCP — pip install OLLMCP
│   ├── Acts as proxy: discovers MCP tools → shares with Ollama in real time
│   └── Command: OLLMCP --mcp-server-url [URL] --model [model-name]
│
MCP LAYER
└── Zapier MCP (free tier) — connects to 8,000+ services
    ├── Notion, Gmail, Google Calendar, Slack, etc.
    ├── One MCP server = all integrations
    └── Pricing: 1 task = 1 Zapier zap (thousands free on base plan)
```

### Critical: Not All Ollama Models Support Tool Calling
When choosing a model on Ollama model library, **look for the "tools" tag** on the model page. Models without this tag cannot call tools — they are chatbots only, not agents.

**Default model in OLLMCP:** Qwen 2.5 (confirmed tool calling capable)

**Auto-discovery:** OLLMCP can read Claude Code's existing MCP config directly — enables same MCP servers used by Claude to be used by local Ollama models.

### Hardware → Model Reality (confirmed)

| Hardware | Practical Max | Notes |
|----------|--------------|-------|
| No GPU (CPU only) | 3B–4B, very slow | 7B+ is impractical |
| MacBook Air 2019 Intel | Up to 7B Q4 (slow) | Current machine |
| HP All-in-One AMD Ryzen AI 5 + Radeon | 7B–13B practical | **Already owned — activate now** |
| Mac Mini M4 Pro 48GB | 70B Q4 (full) | **Target acquisition** |
| Modern Mac M-series (16GB) | 13B clean | Solid entry point |

---

## SECTION 4 — MULTI-AGENT ORCHESTRATION: HUB AND SPOKE

### The Pattern (ESTABLISHED — Claude Code architecture confirmed)

**Hub and Spoke:** One coordinator agent at center. All subagents communicate only through coordinator. Subagents never talk to each other directly.

```
                    COORDINATOR
                   /    |    \
              AgentA  AgentB  AgentC
              (research) (code) (review)
```

**Coordinator owns:**
- Task decomposition (break task into subtasks)
- Task delegation (who works on what)
- Result aggregation (combine outputs, resolve conflicts)
- Routing decisions (static vs dynamic)
- Context sharing (what each subagent knows)
- Error handling + observability

### The Routing Decision Rule (ESTABLISHED — demonstrated)

| Task Type | Route |
|-----------|-------|
| Simple factual question | Single agent |
| Multi-step sequential task | Pass results forward agent to agent (sequential) |
| Independent subtasks | Parallel delegation (multiple agents simultaneously) |

### Scope Partitioning Principle (ESTABLISHED)
Before delegation, the coordinator must partition research scope into **non-overlapping assignments**. Each subagent gets its domain. The coordinator aggregates cross-cutting information. 

**Critical anti-pattern — Narrow Decomposition:** Breaking task too granularly causes subagents to lose cross-cutting context. Example: screening agent gets "check Python experience" but doesn't have access to resume, so it can't cross-reference years of experience against projects and references. The coordinator must ensure each subagent has the context it needs to do its narrow job.

### What the Coordinator Prompt Contains
- Identity: "Your role is to coordinate and NOT do the work yourself"
- Routing rules: which agent handles which task type
- Result aggregation instructions: combine, resolve conflicts, make output coherent
- Escalation rules: when to fall back to single-agent

### Key Implementation Insight
The coordinator should own the routing rules — not subagents. Subagents have tools + scope definitions. The coordinator holds the logic that decides which spoke to activate.

---

## SECTION 5 — KNOWLEDGE GRAPHS + AGENTIC GRAPH RAG

### Vector RAG vs Graph RAG vs Agentic Graph RAG

| Method | Good For | Limitation |
|--------|----------|------------|
| Vector RAG | Semantic similarity — "what does X mean?" | Can't find non-obvious connections, no multi-hop |
| Graph RAG | Relationship queries — "how are X, Y, Z connected?" | Requires upfront information architecture, complex to build |
| Agentic Graph RAG | Complex multi-source expert reasoning | Highest capability, highest build cost |

### When Graph RAG Beats Vector RAG (ESTABLISHED — domain: fraud detection demo)
Vector RAG finds what's semantically similar. Graph RAG chases connections down — it follows relationships:
- Account A transacted with Account B
- Account B shares an address with Account C
- Account C has flagged identity data
- Therefore: Account A is suspicious (multi-hop inference)

Vector RAG would never surface this. Graph RAG finds it in one query.

### Knowledge Graph vs Text-Indexed Graph
| Type | Description | Build Cost | Power |
|------|-------------|------------|-------|
| **Knowledge graph** | Faithful domain model: entities + relationships explicitly defined | High (upfront information architecture required) | Very high — complex queries possible |
| **Text-indexed graph** | Auto-generated from documents (chunks + entity extraction) | Low | Medium — better than vector, not as structured |

**For Pandora OS:** D.R.D's 600K+ words of decoded research is a knowledge graph candidate. The entities are: people, doctrines, events, territories, timelines, principles. The relationships are: influenced_by, contradicts, validates, encoded_in, maps_to. This is the D.R.D retrieval layer upgrade path.

### Data Freshness Principle (ESTABLISHED)
Agentic graph RAG requires the agent to trust that its tools give fresh data. If the graph is stale, the agent's reasoning is stale. **The graph must be updated when source data changes.**

### MCP Integration
Graph query tools are automatically created as MCP tools — allowing the agent to query the knowledge graph via natural language without writing graph query syntax. The MCP server handles translation.

---

## SECTION 6 — PANDORA OS INTEGRATION MAP

### What This Changes in Pandora OS

| Finding | Current State | Upgrade |
|---------|--------------|---------|
| CLI vs MCP decision rule | Ad hoc | Encode as a routing table in Auset's system prompt — explicit rule for when to use Bash vs MCP tool |
| 4 Context Strategies | Partially implemented (WRITE + ISOLATE are good) | Add COMPRESS protocol to `proto_context-hygiene.md` — in-session tool result clearing |
| SELECT — dynamic tool loading | Static (all tools loaded) | Auset needs just-in-time tool retrieval. Max tools per context: ~19 before confusion degrades reasoning |
| Local model stack | Not deployed | HP All-in-One → Ollama + OLLMCP → Zapier MCP. Operational TODAY. No new hardware needed. |
| Hub and Spoke | Pandora uses parallel departments | Coordinator pattern maps cleanly: Auset = coordinator, 12 department agents = spokes |
| Scope partitioning | Implicit in department structure | Make explicit: each department agent gets a non-overlapping domain brief before delegation |
| Graph RAG | Not implemented | Phase 2: D.R.D's 600K+ words = knowledge graph candidate. Entities + relationships from decoded research. MCP tools for natural language queries. |

### ICM Protocol Upgrade — Context Compression (New Section for proto_context-hygiene.md)

The existing ICM covers:
- L0–L4 load hierarchy (SELECT strategy — correct)
- Token budget allocation (SELECT strategy — correct)

**Missing:** In-session compression rules.

Add to `proto_context-hygiene.md`:
```
COMPRESS PROTOCOL (in-session):
1. Tool results older than 10 steps: replace with 1-line summary
2. Research phase complete → before implementation phase: summarize + clear research context
3. Never leave failed attempts in context — compress to: "Attempt [X] failed: [reason]. Resolution: [fix]."
4. Conversation history: keep last 10 turns verbatim, summarize everything older
5. Context confusion threshold: >19 tools in context = must prune before proceeding
```

### Auset Upgrade — Tool Selection Rule

Current: Auset loads all available tools at session start.
Target: Auset uses SELECT strategy — loads only tools relevant to current task.

Encoding for Auset's system prompt:
```
TOOL SELECTION RULE:
- CLI (Bash) when: file ops, git, text processing, script execution
  → model already knows these tools from training
- MCP tool when: external service auth (Notion, Gmail, Calendar),
  rendered web content, multi-user governance needed
- Never load >19 tools for a single reasoning task
- When tool set exceeds 19: semantic-select relevant subset first
```

### D.I.I Action Queue

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| NOW | Clean HP All-in-One fans → install Ollama → pull Qwen 2.5 + Llama 3.1 8B | 1 hour | Local AI operational today, $0 |
| NOW | Install OLLMCP → connect Zapier MCP | 30 min | 8,000+ tool integrations on local model |
| NEXT | Upgrade `proto_context-hygiene.md` with COMPRESS protocol | 1 session | Context quality + cost improvement across all sessions |
| NEXT | Encode CLI vs MCP routing rule in Auset's config | 30 min | Reduces wrong-tool token waste |
| PHASE 2 | Mac Mini M4 Pro 48GB acquisition | One purchase | 70B local inference |
| PHASE 2 | D.R.D knowledge graph — entity extraction from 600K+ decoded words | 1–2 sessions | Sovereign cross-department retrieval |

---

## CONFIDENCE TIER ASSESSMENT

| Claim | Tier | Basis |
|-------|------|-------|
| CLI vs MCP decision rule | ESTABLISHED | Live tests with measured token counts |
| 55K tokens for GitHub MCP server | ESTABLISHED | Measured, specific number cited |
| 4 context strategies (WSCI) | ESTABLISHED | LangChain + Anthropic published frameworks |
| 54% think tool performance improvement | PROBABLE | Anthropic internal benchmark, not independently verified |
| RAG over tools: 14% → 43% accuracy | PROBABLE | Paper cited but not independently verified |
| Llama 3.1 8B fails at 46 tools | ESTABLISHED | Benchmark study cited, specific model + number |
| Hub and Spoke architecture | ESTABLISHED | Claude Code architecture confirms this pattern |
| Ollama + OLLMCP bridge stack | ESTABLISHED | Demonstrated working in video |
| Graph RAG multi-hop superiority | ESTABLISHED | Demonstrated with fraud detection use case |
| D.R.D as knowledge graph candidate | INFERRED | Pattern match — not claimed by source |

---

## HELD (Do Not Deploy Until Resolved)

| Claim | Issue |
|-------|-------|
| OLLMCP auto-discovery from Claude config | Need to verify config file path is correct for current Claude Code version |
| Zapier MCP free tier limits | "Thousands free" is vague — verify actual free tier limit before building automation that depends on it |
| Neptune MCP tools | AWS-managed service — not sovereign. Evaluate open-source graph alternatives (Neo4j, Kuzu, NebulaGraph) before committing to Neptune architecture |

---

## INTEGRATION BRIEFS TO GENERATE

From this decode, route the following:
1. **→ D.I.I:** `drd_brief_dii_local-model-stack-ollama-mcp_v1.md` — HP All-in-One activation + OLLMCP setup
2. **→ D.I.I:** `drd_brief_dii_auset-tool-selection-upgrade_v1.md` — CLI vs MCP rule + tool count limit encoding
3. **→ shared/protocols:** `proto_context-hygiene.md` COMPRESS section addition
4. **→ D.I.I (Phase 2):** `drd_brief_dii_drd-knowledge-graph-architecture_v1.md` — entity model for 600K+ decoded words

---

*drd_decode_tech-playlist-tier1-agentic-systems_v1.md | D.R.D | Pandora OS*
*"D.R.D is the front door. Nothing enters untested."*

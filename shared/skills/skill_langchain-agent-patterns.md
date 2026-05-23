# SKILL — LANGCHAIN AGENT PATTERNS
**Load when: building multi-step agent pipelines, designing tool-using AI systems, or architecting swarm orchestration in D.I.I.**
**Loadable by: D.I.I, D.S.C — agent engineering and system design.**

---

## WHAT THIS SKILL IS

Extracted architecture patterns from the LangChain + LangGraph ecosystem — translated into Pandora OS operational knowledge. LangChain is the agent engineering platform. LangGraph is the controllable workflow layer built on top of it. This skill contains the sovereign-extracted patterns: not the dependency, not the framework — the patterns. Use them in any language, with any runtime.

**Source repo:** `~/Desktop/pandorareposkills/langchain/`
**License:** MIT — sovereign use permitted.

---

## THE FOUR CORE PATTERNS

### PATTERN 1 — THE CHAIN
The fundamental unit. Data flows through a sequence of transforms, each step receiving the previous step's output.

```
INPUT
  ↓
TRANSFORM 1 (parse / extract / format)
  ↓
TRANSFORM 2 (reason / classify / generate)
  ↓
TRANSFORM 3 (validate / structure / route)
  ↓
OUTPUT
```

**Pandora application:** Every D.R.D pipeline stage is a chain. Every workflow stage file is a chain node. Design multi-step builds as explicit chains — name every transform, define its input and output contract before writing code.

**Key principle:** Each node in a chain should do exactly one thing. One transform. One responsibility. Composability is the power.

---

### PATTERN 2 — TOOL BINDING
An agent that can call functions. The LLM receives a tool schema, decides when to call it, and the runtime executes the call.

```
AGENT RECEIVES:
  - Task description
  - Tool schema (name, description, input parameters)

AGENT DECIDES:
  - Which tool to call
  - What parameters to pass

RUNTIME EXECUTES:
  - The tool function
  - Returns result to agent

AGENT CONTINUES:
  - Incorporates result
  - Decides next action or produces final output
```

**Pandora application:** Claude Code's tool loop IS the tool binding pattern. Every tool call (Read, Bash, Write, Agent) follows this exact cycle. When designing MCP servers, design the tool schema first — the description is what the agent uses to decide when to call it. Make descriptions function-specific and unambiguous.

**Schema design rule:** The tool description is not documentation — it is the routing signal. Write it so the agent knows exactly when this tool applies and when it does not.

---

### PATTERN 3 — MEMORY INJECTION
Persistent state injected into the agent context at the start of each call.

```
MEMORY TYPES:
  Short-term  → conversation history (within session)
  Long-term   → retrieved from external store (vector DB, file, JSON)
  Entity      → tracked facts about specific entities
  Summary     → compressed representation of prior context

INJECTION POINT:
  Memory is loaded BEFORE the current task prompt
  Agent reasons over memory + current input simultaneously

RETRIEVAL PATTERN:
  Query → retrieve relevant memory chunks → inject → reason
```

**Pandora application:** The ref card `Current State` section is memory injection. Lean-ctx CCP is memory injection. The D.I.I `dii_memory-core.md` is a long-term memory file. When building agents that need cross-session state, design the memory schema first — what facts need to persist, in what format, retrieved by what query.

**Pandora rule:** Files are the agent's memory. What is not written is lost between sessions. Memory injection without a write protocol is a leak.

---

### PATTERN 4 — LANGGRAPH ORCHESTRATION
Controllable agent workflows with explicit state, conditional branching, and cycle detection.

```
STATE
  The shared data object passed between all nodes.
  Every node reads from state and writes back to state.
  State is the contract between nodes.

NODES
  Functions that take state as input, return state updates.
  Each node has one responsibility.

EDGES
  Connections between nodes.
  Conditional edges: router function decides which node fires next.
  Normal edges: always flow to the next node.

ENTRY POINT
  Where the graph starts.

END POINT
  Where the graph exits and returns final state.

CYCLES (human-in-the-loop)
  A node can route back to a prior node.
  Used for: retry loops, clarification loops, human approval gates.
```

**Graph structure:**
```
START → [router node] → [task node A] → [validator node]
                      ↘ [task node B] ↗
                                       ↓
                               [output node] → END
                                       ↑
                               [retry edge if invalid]
```

**Pandora application:** The Development Railway is a LangGraph. Each workflow stage is a node. The D.R.D pipeline is a graph with conditional edges (pass/fail at each confidence gate). When building complex multi-stage systems, map the state object first — what does every node need to receive, and what does it need to return.

---

## SWARM ARCHITECTURE (MULTI-AGENT)

When a single agent loop is insufficient for parallel or specialized work:

```
COORDINATOR AGENT
  Receives the master task
  Decomposes it into scoped sub-tasks
  Spawns worker agents (parallel where independent, sequential where dependent)
  Integrates outputs
  Validates completeness
  Returns unified result

WORKER AGENT
  Receives one scoped task + required context
  Executes independently
  Returns structured output to coordinator
  Has no awareness of other workers

SHARED STATE
  Worker outputs are written to files (the shared state layer)
  Coordinator reads from files, not from worker memory
  Files are the handoff protocol
```

**Pandora application:** Claude Code's `Agent` tool implements this pattern natively. The swarm-coordinator agent is the coordinator role. Each department specialist agent is a worker. When designing a swarm build, define the shared state schema (what files, what format, what naming) before spawning any agents.

---

## WHEN TO USE THESE PATTERNS

| Task | Pattern |
|------|---------|
| Multi-step data transformation | Chain |
| Agent that calls external tools/APIs | Tool Binding |
| Agent that needs prior session context | Memory Injection |
| Complex workflow with branching logic | LangGraph Orchestration |
| Parallel builds across independent components | Swarm Architecture |

**Anti-pattern to avoid:** Building a single massive agent that does everything. Chain patterns exist because separation of concerns produces more reliable, debuggable, and refineable systems. Break it down.

---

*SKILL_LANGCHAIN_AGENT_PATTERNS | Pandora OS | D.I.I + D.S.C*
*"The pattern is sovereign. The framework is optional."*

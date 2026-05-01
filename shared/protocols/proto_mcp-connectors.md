# Protocol: MCP Connectors
## OS-Wide | All Departments | Load when connecting Claude to external tools

MCP (Model Context Protocol) is the open standard that connects Claude to external systems — Google Drive, Gmail, Calendar, Slack, Notion, GitHub, and custom-built tools. When connected, Claude can read live data and take actions in those systems directly, without copy-paste as the bridge.

---

## THE CORE PRINCIPLE

MCP connectors are plumbing — they connect layers, not intelligence. The action Claude takes through a connector might be:
- **60%** — Pull a report, read a file, query a database (deterministic)
- **30%** — Route a ticket based on rules, format a structured message
- **10%** — Draft a response that requires judgment, synthesize across sources

The connector itself is infrastructure. It does not change which layer the task belongs to. Run layer-triage first (`skill_layer-triage.md`), then determine if MCP is the right transport.

---

## WHEN TO USE MCP

```
USE MCP WHEN:
  ✓ Claude needs your actual live data, not data you copy-paste in
  ✓ Claude needs to take actions in external tools (create events, file tickets, send messages)
  ✓ Your workflow crosses multiple tools and you are the manual glue between them
  ✓ You are building agentic workflows that read from AND write to external systems
  ✓ The data source changes frequently enough that pasting is a bottleneck

SKIP MCP WHEN:
  ✗ The data is small enough to paste directly into the conversation
  ✗ Working with sensitive data that has not had connector access reviewed
  ✗ The external tool has API rate limits that will bottleneck the workflow
  ✗ Claude only needs to think, not act — read-only analysis of pasted data does not need MCP
  ✗ A one-off task where setup cost exceeds the time saved
```

---

## PANDORA OS — ACTIVE AND AVAILABLE CONNECTORS

### Currently Connected (Claude.ai MCP)
| Connector | Access Level | Primary Use in Pandora OS |
|-----------|-------------|--------------------------|
| Google Drive | Read + Write | Research file storage, department output filing |
| Gmail | Read + Write | Communications — D.S.E client engagement |
| Google Calendar | Read + Write | Session scheduling, project timelines |
| Apollo.io | Read + Write | D.S.E — lead generation, contact enrichment |
| Canva | Read + Write | D.C.E — content design output |
| Gamma | Read + Write | D.C.E, D.S.E — presentation generation |
| ClickUp | Read + Write | D.S.C — project task management |

### Available but Not Yet Configured
| Connector | Pandora OS Use Case | Department |
|-----------|---------------------|-----------|
| Notion | Research knowledge base mirror | D.R.D, D.S.C |
| GitHub | D.I.I codebase management | D.I.I |
| Slack | Team/client communications | D.S.E |
| Zapier | Workflow automation bridges | D.S.C |

---

## SETUP PROTOCOL

### Claude.ai Built-in Connectors
```
1. Open Claude.ai → Tools menu → Plug icon
2. Authenticate each connector (start with READ-ONLY access)
3. Test with a low-stakes read operation before enabling writes
4. Enable write access only after confirming read works correctly
5. Document the connector in this file under ACTIVE AND AVAILABLE
```

### Claude Code — Custom MCP Servers
```
1. Configure MCP servers in .claude/settings.json
2. Custom servers for Pandora OS internal tools are built in tools/mcp-servers/
3. Use Anthropic SDK (Python or Node.js) to wrap internal APIs
4. Each custom MCP server exposes the internal tool in a format Claude Code can call
5. Test locally before wiring into department workflows
```

---

## SECURITY RULES

```
BEFORE enabling any connector:
  [ ] What data does this connector expose?
  [ ] Who else has access to this connector's authenticated account?
  [ ] Does this connector have write permissions to production data?
  [ ] Is sensitive data (passwords, private keys, financial records) accessible via this connector?

READ before WRITE. Always test read access first.
Disable connectors not in active use. Dormant connections = dormant attack surface.
Do not connect platforms where a mistake would be irreversible without warning Morph first.
```

---

## DEPARTMENT ROUTING

| Department | Relevant Connectors | Primary Use |
|------------|--------------------|----|
| D.S.C | ClickUp, Google Drive | Project tracking, file storage |
| D.R.D | Google Drive | Research filing, source archiving |
| D.C.E | Canva, Gamma, Google Drive | Content creation output |
| D.S.E | Apollo.io, Gmail, Gamma, Google Drive | CRM, outreach, proposals |
| D.I.I | GitHub, custom MCP servers | Code management, tool integration |
| D.P.S.A | Google Calendar | Session scheduling |
| D.R.A | Google Drive | Deal documents, property research |

---

## POWER COMBINATION

The highest-leverage MCP stack combines with Projects:

```
Example: Research + Filing Workflow (D.R.D)
  1. Web Search (Mode 5) → find and verify sources
  2. Conversational → D.R.D evidence extraction and synthesis
  3. Google Drive connector → auto-file the raw extract and decoded output
     to the correct D.R.D/research/[domain]/ folder in Drive
  No manual file movement. No copy-paste. The pipeline handles it.

Example: Client Engagement (D.S.E)
  1. Apollo.io connector → enrich contact data for new lead
  2. Conversational → research and position the offer
  3. Gamma connector → generate the proposal deck
  4. Gmail connector → send from Morph's account
  One session. No tab-switching. No manual glue.
```

---

*proto_mcp-connectors.md | Pandora OS | Shared Protocol | All Departments*
*Last updated: 2026-04-30*

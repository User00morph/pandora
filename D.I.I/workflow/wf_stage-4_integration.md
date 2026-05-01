# WF_DII — STAGE 4: INTEGRATION (RUBEDO)
**Wire the technology into the OS. Make it live. Make it permanent.**

---

## FOR TECHNOLOGY INTEGRATION

```
ACTION:
  Define exactly where this technology sits in the OS
  Which department(s) use it and how — specific, not general
  Create the integration documentation
  Update relevant department ref cards and context files
  Test it in a real task before declaring it integrated
    (training run — not a drill, an actual OS task)

FOR LOCAL TOOLS (MCP / API / AGENT):
  Wire into .claude/settings.json (MCP servers)
  Or file in .claude/agents/ (agent definitions)
  Or deploy to tools/mcp-servers/ or tools/apis/
  Test the connection end-to-end before declaring live

LOAD IF COMPLEX BUILD:
  skill_prd-creation.md → produce PRD before wiring
OUTPUT: dii_integration_[technology]_live.md
```

---

## FOR SOFTWARE BUILD INTEGRATION

```
ACTION — INTEGRATION TEST:
  Run the full system end-to-end for the first time
  Test the complete data flow: input → transform → output
  Identify and fix integration failures (boundary failures between components)

ACTION — DEPLOYMENT PREP:
  Environment variables in .env.example (never in code)
  Production config separated from development
  All secrets removed from code
  Dockerfile or deploy script created
  README.md updated with full setup instructions

CHECKPOINT: git commit -m "deploy: integration complete, system live"
OUTPUT: dii_integration_[project-name]_live.md
        Filed in D.I.I/integration/
        Cross-linked in requesting department's context file
```

---

## CROSS-DEPARTMENT WIRING

After integration, update these:
```
REQUESTING DEPT context file → add reference to integration doc
D.S.C active systems tracker → add the new system
ref_dii.md active state      → update with new integration
DRD_INDEX.md                 → if research was produced, mark deployed
```

---

## GATE

> Does the technology or system work in an actual OS task — not a test scenario?
> Is the integration doc filed and cross-linked?

**PASS → load `wf_stage-5_monitor.md`**

---

*D.I.I | Stage 4 of 5 | WF_DII_TECHNOLOGY_INTEGRATION*

# SKILL — SESSION INITIALIZATION
**Load at the start of every build or research session. Before any other skill.**
**Loadable by: All departments. All agents.**

---

## WHAT THIS SKILL IS

The mandatory opening protocol for every build or research session. Surfaces the skills already active in the workspace, presents the full skill library, and asks Morph which additional skills to activate before any work begins. No build starts. No research starts. Until this confirmation is complete.

---

## WHEN TO TRIGGER

```
ANY OF THESE ACTIVATE THIS PROTOCOL:
  - A software build is initiated (HTML, JS, Python, any language)
  - A research topic is opened in D.R.D
  - A new system or project is being designed in D.S.C
  - A workflow stage is about to be executed
  - A new session begins with a task that requires file reading or writing
```

---

## THE PROTOCOL — THREE STEPS

### STEP 1 — READ THE ACTIVE STATE
Read the active department's ref card. Extract:
- Which skills are listed in its session routing table
- Which skills the current workflow stage calls for
- Which skills were explicitly loaded earlier this session (if any)

### STEP 2 — SURFACE AND ASK
Present this structure to Morph before proceeding:

```
─────────────────────────────────────────────
SESSION SKILL CONFIRMATION
─────────────────────────────────────────────
DEPARTMENT:   [active department]
TASK:         [what Morph has asked for in one line]
STAGE:        [workflow stage if applicable]

SKILLS ACTIVE BY DEFAULT (from ref card + stage):
  ✅ [skill name] — [why it applies]
  ✅ [skill name] — [why it applies]

SKILLS AVAILABLE TO ADD:
  [ ] skill_agentic-architecture      — how Claude Code works as an agent
  [ ] skill_software-build-protocol   — HTML/JS/Python build at scale
  [ ] skill_extraction-workflow       — token-efficient file reading
  [ ] skill_source-evaluation         — tiering and evaluating sources
  [ ] skill_concept-distillation      — extract and layer core concepts
  [ ] skill_framework-synthesis       — build frameworks from multi-source data
  [ ] skill_system-design             — architect systems and components
  [ ] skill_prd-creation              — product requirements before complex builds
  [ ] skill_repo-extraction           — open source repo → Pandora OS artifacts
  [ ] skill_pdf-extraction            — targeted PDF reading
  [ ] skill_file-extraction           — token-efficient file scanning
  [ ] skill_copywriting               — sovereign writing and documentation
  [ ] skill_legitimacy-review         — quality gate before deployment
  [ ] skill_transmutation-protocol    — broken system recovery
  [ ] skill_project-evaluation        — evaluate new ideas and opportunities
  [ ] skill_alchemical-stage-assessment — determine current lifecycle stage
  [ ] skill_diagnostic-method         — diagnose system failures
  [ ] skill_ritual-design             — D.O.M / D.P.S.A practice design
  [ ] skill_herb-profiling            — D.B.S plant intelligence
  [ ] skill_environment-audit         — D.H.S / D.R.A space evaluation
  [ ] skill_deal-analysis             — D.R.A / D.S.E opportunity evaluation
  [ ] skill_content-production        — D.C.E / D.S.E content pipeline
  [ ] skill_client-transmutation      — D.S.E client framework
  [ ] skill_systems-cultivation       — ongoing system health

WHICH ADDITIONAL SKILLS do you want active for this session?
Name them or say "defaults only" to proceed with what is already active.
─────────────────────────────────────────────
```

### STEP 3 — CONFIRM AND LOCK
Once Morph responds:
- Load the confirmed skill files (targeted reads — headers + relevant sections only)
- State the final active skill set before beginning the task
- Do not load additional skills mid-session without asking again

```
CONFIRMED ACTIVE SKILLS:
  ✅ [skill 1]
  ✅ [skill 2]
  ✅ [skill 3]

Proceeding with [task description].
```

---

## WHAT THIS PREVENTS

```
SILENT SKILL GAPS
Starting a research session without source-evaluation active.
Starting a build without the build protocol loaded.
Hitting a problem mid-session that a skill would have prevented.

UNANNOUNCED SKILL LOADING
Loading skills mid-session without Morph knowing what entered context.
Every skill that enters context is a conscious choice — not a background action.

SKILL REDUNDANCY
Loading skills that are already active from earlier in the session.
The confirmation step catches re-loading before it happens.
```

---

*SKILL_SESSION_INIT | All departments | Pandora OS*
*"Know your tools before you touch the work."*

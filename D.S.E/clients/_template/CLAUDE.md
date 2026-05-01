# [Client Name] — Engagement Workspace

## What This Is
A workspace for delivering this client engagement from discovery through handoff. Each stage has a contract that defines inputs, process, and done criteria. Human review happens between every stage.

## Current State
- Discovery: [Not started / In progress / Complete]
- Build: [Not started / In progress / Complete]
- Review: [Not started / In progress / Complete]
- Handoff: [Not started / In progress / Complete]
- Next: [Specific next action]

## Structure
```
[client-name]/
  CLAUDE.md          ← this file — orientation
  01_discovery/      ← understand the actual problem and scope it
    CONTEXT.md       ← discovery stage contract
    output/          ← requirements doc, scope agreement
  02_build/          ← create the deliverable
    CONTEXT.md       ← build stage contract
    output/          ← work in progress, completed deliverable
  03_review/         ← internal then client review
    CONTEXT.md       ← review stage contract
    output/          ← reviewed deliverable, feedback, revision notes
  04_handoff/        ← deliver, document, transition
    CONTEXT.md       ← handoff stage contract
    output/          ← final deliverables, transition materials
  _config/           ← client brief, engagement terms, scope
```

## How to Use
1. Read _config/client-brief.md to orient to this client.
2. Check Current State above for where the engagement is.
3. Open the active stage's CONTEXT.md. Follow the contract.
4. Human review between every stage before moving forward.
5. Update Current State above at the end of every session.

## Key Decisions
- **Discovery is non-negotiable.** The most common cause of failed engagements is insufficient discovery. The scope agreement produced here drives everything else.
- **Internal review before client sees anything.** Problems caught internally are cheap to fix. Problems caught by the client cost time, trust, and credibility.
- **Handoff is a stage, not an afterthought.** Documentation and knowledge transfer happen here so the client can operate independently after delivery.

## Client-Specific Rules
[Populate from _config/client-brief.md after onboarding]

# WF_DII — STAGE 5: MONITOR
**Keep the integration healthy. Watch for decay, upgrade when warranted.**

---

## ACTION

```
TRACK VALUE:
  Is the tool still delivering what it was integrated for?
  If not — is it a usage problem or a tool problem?

WATCH FOR:
  Deprecations or breaking changes in external tools
  Better sovereign alternatives that have emerged
  Failure patterns discovered in actual use
  Cost drift (API pricing, subscription changes)

LOG FAILURES:
  When a tool fails in an OS task — document it.
  File: updates to existing dii_integration_[technology]_live.md
  Note: what failed, when, under what conditions, how it was resolved

UPGRADE TRIGGER:
  If a better sovereign alternative exists → run Stage 1–4 for the upgrade
  If the tool creates new dependency risk → sovereignty re-evaluation
  If performance degrades without remedy → consider replacement

ARCHIVE TRIGGER:
  If a tool is replaced → move integration doc to D.I.I/archive/
  Mark the ref card entry as deprecated
  Remove from .claude/settings.json or agents/ if applicable
```

---

## OUTPUT

Updates to existing integration files. No new files unless an upgrade cycle begins.

---

## THIS STAGE HAS NO GATE

It runs continuously. It is complete only when the technology is archived.

---

*D.I.I | Stage 5 of 5 | WF_DII_TECHNOLOGY_INTEGRATION*

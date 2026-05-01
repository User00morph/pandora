# D.I.I — Memory Core
## Cross-Session Intelligence Log | Agentic Codebases & External Tools

This file is the connective tissue between Pandora OS and every external system, tool, repo, and agentic session Morph works with. It persists what was explored, decided, and built — so no session starts from zero.

**Update this file:** whenever a new tool is explored, a decision is made about an external system, or a pattern is discovered across codebases.

---

## ACTIVE TOOL STACK

| Tool | Role | Status | Notes |
|------|------|--------|-------|
| Claude Code (CLI) | Primary agentic build layer | Active | Runs in terminal + VS Code |
| VS Code | Local editor + git client | Active | Pandora workspace |
| GitHub (`User00morph/pandora`) | Remote repo + backup | Active | Pushed 2026-05-01 |
| Anthropic API (claude-sonnet-4-6) | Model powering Claude Code | Active | Knowledge cutoff Aug 2025 |

---

## CODEBASE REGISTRY

Repos and codebases Morph has worked in or connected to Pandora.

| Repo / Codebase | Location | Purpose | Last Touched |
|-----------------|----------|---------|--------------|
| pandora | `github.com/User00morph/pandora` | Pandora OS — sovereign knowledge architecture | 2026-05-01 |

---

## SESSION INTELLIGENCE LOG

Cross-session decisions, discoveries, and patterns. Most recent first.

---

### 2026-05-01 — Pandora GitHub Setup + Environment Optimization
**Context:** First push of Pandora OS to GitHub. VS Code environment configured for low-power hardware.

**Decisions made:**
- `.mp4` files excluded from repo — classified as raw data, not knowledge artifacts
- `*.mp4` added to `.gitignore`; files untracked from git history
- `.vscode/settings.json` created — scoped exclusions for CPU/watcher efficiency on 1.6 GHz dual-core i5, 8GB LPDDR3
- Remote SSH alias: `github-pandora` → `git@github-pandora:User00morph/pandora.git`

**Hardware profile logged:**
- CPU: 1.6 GHz Dual-Core Intel Core i5 (bottleneck)
- RAM: 8 GB 2133 MHz LPDDR3 (adequate)
- Implication: no local AI models; offload compute to Anthropic servers; keep VS Code lean

**Patterns discovered:**
- Pandora already had a remote configured (`github-pandora` SSH alias) before this session
- Remote had a divergent "Initial commit" (README only) — resolved via force push
- Video files were tracked in git history; removed from index before push

**Next:** Continue building D.I.I agentic layer. MCP servers + agent definitions pending.

---

## AGENTIC ARCHITECTURE LOG

Agents, MCPs, and automation built or planned.

| Agent / MCP | Department | Status | File |
|-------------|-----------|--------|------|
| — | — | Pending build | `D.I.I/workflow/` |

---

## DECISION LOG

Significant cross-codebase or cross-tool decisions.

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-05-01 | Exclude `.mp4` from repo permanently | Raw data not knowledge — bloats repo, no git value |
| 2026-05-01 | VS Code as primary editor (not Cursor, not Codespaces) | Hardware constraint; local is lighter than browser-based |
| 2026-05-01 | No local AI models (Ollama etc.) | 1.6 GHz dual-core insufficient; use Anthropic API instead |

---

## PATTERNS & DISCOVERIES

Non-obvious insights discovered across sessions that apply broadly.

- **The filesystem IS the memory** — Pandora's persistence model means git history is also session history. Commit messages carry context.
- **Hardware ceiling is CPU not RAM** — 8GB is enough; dual-core 1.6 GHz is the real constraint. Design all tooling around that.
- **SSH aliases matter** — `github-pandora` alias must exist in `~/.ssh/config` for git push/pull to work. If cloning on a new machine, SSH config must be set up first.

---

*D.I.I Memory Core | Updated end of session. Load alongside ref_dii.md when working across external tools or agentic systems.*

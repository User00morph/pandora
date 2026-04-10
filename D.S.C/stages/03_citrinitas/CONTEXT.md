# CITRINITAS — Illumination
**D.S.C | Stage 3 of 4 | The Blueprint**

---

## PURPOSE
Design the project clearly enough to execute. An idea that survived purification is now a project candidate. Build enough clarity that execution has a target.

## INPUTS

| Source | Layer | Path |
|--------|-------|------|
| Albedo evaluation | Layer 4 (working) | `../02_albedo/output/` |
| Nigredo raw document | Layer 4 (working) | `../01_nigredo/output/` |
| System Design skill | Layer 3 (reference) | `skills/skill_system-design.md` |
| PRD Creation skill (if complex build) | Layer 3 (reference) | `skills/skill_prd-creation.md` |
| Naming conventions | Layer 3 (reference) | `_config/naming-conventions.md` |

## PROCESS

Build the project blueprint:

1. **PROJECT NAME AND CODE** — Clear name + department code. Format: `[DEPT-CODE]_[project-name]`
2. **MISSION STATEMENT** — One sentence. What is this project trying to accomplish? Specific, measurable where possible.
3. **SUCCESS DEFINITION** — What does done look like? What does successful look like? Name both.
4. **PHASE ARCHITECTURE** — Break into phases. Maximum three initially. Each phase: what gets built, what it produces, when it ends.
5. **MINIMUM VIABLE VERSION** — The smallest version that could exist and still test whether the idea works. This is where execution begins.
6. **RESOURCE ALLOCATION** — Based on Albedo's resource reality: hours/week committed, budget allocated, managing department, supporting departments.
7. **DEPENDENCIES** — What does this project need from other departments? Map now so requests can be routed properly via handoff template.
8. **KILL CONDITIONS** — Under what circumstances does this project get stopped? Name in advance to remove emotional difficulty later.

**For complex builds:** Generate a full PRD using `skills/skill_prd-creation.md` before execution begins. Morph reviews and approves the PRD before any build starts.

## OUTPUTS

| Output | Filename | Destination |
|--------|----------|-------------|
| Project blueprint | `dsc_citrinitas_[project-name]_blueprint.md` | `output/` |
| PRD (if complex build) | `dsc_prd_[project-name]_v1.md` | `output/` |
| Department handoff requests | Per `shared/handoff-template.md` | `output/` |

## REVIEW GATE
**Before proceeding to Rubedo, verify:**
- [ ] The minimum viable version can be executed with current resources
- [ ] Phase architecture does not exceed 3 phases
- [ ] Kill conditions are defined and specific
- [ ] All department dependencies have handoff requests prepared
- [ ] If PRD was required, it has been reviewed and approved by Morph

## CROSS-STAGE TRACE
- **Verify against Nigredo**: The mission statement should map to the original plain statement. If it has evolved, the evolution is documented.
- **Verify against Albedo**: Resource allocation must respect the resource reality from Stage 2. Sovereignty check constraints are honored.

---

*D.S.C | Citrinitas | "The project moves from potential into blueprint — from field into form."*

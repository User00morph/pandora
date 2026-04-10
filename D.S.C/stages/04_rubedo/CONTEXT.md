# RUBEDO — Integration
**D.S.C | Stage 4 of 4 | The Project Lives**

---

## PURPOSE
Bring the project into the OS officially. A project that has survived all three stages is sanctioned. Integrate it so it has a home, receives attention, and connects to the departments it needs.

## INPUTS

| Source | Layer | Path |
|--------|-------|------|
| Citrinitas blueprint | Layer 4 (working) | `../03_citrinitas/output/` |
| PRD (if exists) | Layer 4 (working) | `../03_citrinitas/output/` |
| Albedo evaluation | Layer 4 (working) | `../02_albedo/output/` |
| Naming conventions | Layer 3 (reference) | `_config/naming-conventions.md` |
| Handoff template | Layer 3 (reference) | `shared/handoff-template.md` |

## PROCESS

Integration sequence:

1. **CREATE THE PROJECT FILE** — File: `[dept-code]_project_[name]_v1.md`. Contents: the completed blueprint from Citrinitas. Location: in the primary department's folder.
2. **UPDATE CONTEXT FILES** — Add the project to the managing department's context file. Add a reference in every department the project draws from.
3. **SET THE FIRST MILESTONE** — From Phase 1 architecture: what is the single first deliverable? Name it. Assign it. Put a date on it. A project without a first milestone is an intention, not a project.
4. **ASSIGN THE ALCHEMICAL STATUS** — Mark current stage in all trackers.
5. **LOG IN DSC MASTER PROJECT REGISTER** — Every sanctioned project is listed in `dsc_project_register.md` with: name, department, stage, first milestone, date entered.
6. **SEND DEPARTMENT HANDOFFS** — Execute all handoff requests prepared in Citrinitas using `shared/handoff-template.md`.

## OUTPUTS

| Output | Filename | Destination |
|--------|----------|-------------|
| Active project file | `[dept]_project_[name]_v1.md` | Home department folder |
| Updated context files | Various | Each relevant department |
| Project register entry | `dsc_project_register.md` | D.S.C root |
| Department handoffs | Per handoff template | Receiving departments |

## REVIEW GATE
**Before declaring integration complete, verify:**
- [ ] The project file exists in its home department
- [ ] Context files are updated in all relevant departments
- [ ] First milestone has a specific deliverable and date
- [ ] Project register is updated
- [ ] All department handoffs have been sent

## CROSS-STAGE TRACE
- **Verify against all stages**: The project file should be traceable back through Citrinitas blueprint → Albedo evaluation → Nigredo raw material. The full chain is the project's audit trail.
- **The edit-source principle**: If recurring edits are needed to Rubedo outputs, this is diagnostic information — trace back to which upstream stage (Nigredo, Albedo, or Citrinitas) needs refinement, not the output itself.

---

*D.S.C | Rubedo | "The system is fully alive and operational."*

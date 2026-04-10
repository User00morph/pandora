# WF_DSM_MECHANICAL_WORKFLOW
**D.S.M — Department of Sovereign Mechanics**
**Workflow: From Problem or Study to Documented Mastery**

---

## WHAT THIS WORKFLOW IS

Two parallel workflows — one for diagnosing and repairing mechanical problems, one for studying vehicle systems to build the knowledge library. Both feed the sovereign shop as a business.

---

## TRIGGER

**Diagnostic Pipeline:**
- A vehicle or mechanical system has a problem
- A customer (shop) brings a vehicle for service
- A preventive maintenance interval is reached

**Study Pipeline:**
- A vehicle system needs to be understood from first principles
- A new tool or technique needs to be learned
- A shop service offering needs knowledge backing

---

## PIPELINE A — DIAGNOSTIC AND REPAIR

### STAGE 1 — SYMPTOM INTAKE (Nigredo)
```
SKILLS TO LOAD: skill_diagnostic-method.md

Document the problem:
- What is the operator/customer reporting?
- What does the vehicle actually do? (observe directly)
- When did it start? What changed?
- Constant or intermittent?
- Conditions that affect it?

OUTPUT: dsm_diag_[vehicle]_[symptom]_intake.md
```

### STAGE 2 — DIAGNOSIS (Albedo)
```
Follow the diagnostic method:
- Identify candidate systems
- Isolate to the responsible system
- Find the root cause within that system
- Verify the diagnosis explains all symptoms

OUTPUT: dsm_diag_[vehicle]_[symptom]_diagnosis.md
```

### STAGE 3 — REPAIR (Citrinitas)
```
Plan and execute the repair:
- Parts needed (source and cost)
- Procedure (step by step)
- Tools required
- Estimated time

OUTPUT: dsm_repair_[vehicle]_[job]_procedure.md
```

### STAGE 4 — VERIFICATION AND DOCUMENTATION (Rubedo)
```
After repair:
- Confirm symptom is resolved
- Test under original failure conditions
- Document: what was found, what was done, what was learned
- If shop job: invoice and customer record
- Add to knowledge library if new learning occurred

OUTPUT: dsm_record_[vehicle]_[job]_complete.md
```

---

## PIPELINE B — KNOWLEDGE LIBRARY STUDY

### STAGE 1 — TOPIC SELECTION
```
What system or principle is being studied?
- Engine internals, electrical systems, fuel delivery,
  cooling, drivetrain, suspension, brakes, HVAC, etc.
- Why is this being studied now?
  (Personal mastery, shop preparation, curiosity)

OUTPUT: dsm_study_[system]_outline.md
```

### STAGE 2 — RESEARCH
```
Study the system from first principles:
- How does it work? (physics, engineering, chemistry)
- What are the components and their functions?
- How do they interact?
- What are the common failure modes?
- What are the diagnostic methods specific to this system?

SKILLS TO LOAD: skill_source-evaluation.md (for technical references)
OUTPUT: dsm_lib_[system]_v1.md
```

### STAGE 3 — PRACTICAL APPLICATION
```
Apply the knowledge:
- Work on the system hands-on if possible
- Practice diagnostic methods
- Document anything the study material got wrong
  or failed to explain adequately

OUTPUT: Updates to library file with practical notes
```

### STAGE 4 — SHOP INTEGRATION
```
If this knowledge supports a shop service:
- Define the service offering
- Set pricing based on parts, time, and skill required
- Document the SOP for this service
- Add to shop services menu

OUTPUT: dsm_shop_service_[name]_sop.md
```

---

## CONNECTS TO

```
→ D.S.E    The shop is a business — revenue and client management
→ D.S.C    Complex shop systems route through project intake
→ D.R.D    Technical research when knowledge library needs depth
→ D.I.I    Diagnostic tools, software, and technology integration
```

---

*WF_DSM_MECHANICAL_WORKFLOW | D.S.M | Pandora OS*
*"The person who understands the machine controls the machine. The person who does not is controlled by whoever does."*

# TREASURY DEPT — Privacy Act Request (Linked Trust/Account Records)
**D.S.E | Document | Identity Architecture**
**Status:** draft — fill in [BRACKETED FIELDS] before sending
**Authority:** Privacy Act of 1974 (5 U.S.C. § 552a)
**Filed under:** Layer 3 — Document Stack (sovereign operating architecture)
**Sequence:** File AFTER Numident record is received and reviewed
**Cross-ref:** `dse_doc_ssa-numident-privacy-act-request_draft.md` → "After You Send It" section

---

## WHAT THIS REQUEST IS FOR

Once the SSA NUMIDENT record is in hand, the next layer of the architecture requires knowing what Treasury holds. Stream B identifies the SSN as a point of connection between the living entity and Treasury-held accounts or trust structures. This request surfaces whatever Treasury's records actually say.

Specifically, this targets:
- Any trust account, bond account, or financial instrument linked to your SSN within Treasury's record systems
- TreasuryDirect account records (TreasuryDirect links bonds and securities to SSN)
- Any IRS record linking SSN to a trust, estate, or fiduciary designation
- Any Federal Reserve or BPD (Bureau of the Public Debt) records tied to your SSN

**What we expect to find:**
- TreasuryDirect account records (if one exists under your SSN — many don't know they have one)
- Any bond/security registrations
- Information about whether your SSN is indexed as a trust, account holder, or beneficial owner in any Treasury system

**Why this follows the Numident:**
The Numident tells you what the SSA holds about the SSN contract. Treasury tells you what financial instruments or accounts are downstream of that contract. Together they map the full chain. Neither alone is complete.

**Risk profile:** Fully legal Privacy Act request — no exposure. Every US person has the right to request records about themselves held by any federal agency.

---

## SEND TO (multiple agencies — send simultaneously)

### Treasury Department (primary)
```
Department of the Treasury
Disclosure Services
1500 Pennsylvania Avenue NW
Washington, DC 20220
```
Email: FOIA.Reading.Room@treasury.gov

### IRS (separate request — same mailing)
```
Internal Revenue Service
Centralized Lien Unit / FOIA Office
P.O. Box 2986
Stop 8423
Philadelphia, PA 19114
```
Email: FOIA@irs.gov (confirm current address at irs.gov/privacy)

### Bureau of the Fiscal Service (BFS) — formerly Bureau of the Public Debt
```
Bureau of the Fiscal Service
Privacy Act Request
200 Third Street
Parkersburg, WV 26101
```

**Certified mail for all three.** Send simultaneously — each agency holds different records.

---

## THE LETTER (Treasury — use same template for IRS and BFS, adjust agency name)

---

[YOUR FULL LEGAL NAME]
[YOUR ADDRESS]
[CITY, STATE, ZIP]
[DATE]

Department of the Treasury
Disclosure Services
1500 Pennsylvania Avenue NW
Washington, DC 20220

**RE: Privacy Act Request — All Records Pertaining to My Social Security Number, Including Any Trust, Bond, Account, or Financial Instrument Records**

To Whom It May Concern:

Pursuant to the Privacy Act of 1974 (5 U.S.C. § 552a), I hereby request access to all records maintained by the Department of the Treasury pertaining to my Social Security Number and my identity, including but not limited to:

1. All records in the **TreasuryDirect system** (TreasuryDirect.gov) associated with my Social Security Number, including any bond, note, bill, or securities accounts registered under my SSN
2. All records in the **Treasury's Integrated Debt Management System** or any equivalent financial account system that reference my Social Security Number
3. All records identifying me as a beneficiary, trustee, account holder, or account owner in any Treasury-administered trust, fund, or account
4. All records in the **Bureau of the Fiscal Service** (formerly Bureau of the Public Debt) pertaining to my SSN
5. Any records linking my SSN to a **CUSIP number, CINS number, or other financial instrument identifier**
6. All IRS records identifying me as a fiduciary, trustee, or beneficiary of any trust (Form 56, Form 1041, or related records)
7. Any records in Treasury or IRS systems identifying my SSN as associated with a foreign trust, domestic trust, or irrevocable trust structure
8. All records from any Treasury system of records in which my SSN appears as a primary or secondary identifier

**Identity Verification:**

Full Legal Name: [YOUR FULL LEGAL NAME AS IT APPEARS ON GOVERNMENT DOCUMENTS]
Date of Birth: [MM/DD/YYYY]
Social Security Number: [XXX-XX-XXXX]
Current Address: [YOUR ADDRESS]

I declare under penalty of perjury that the foregoing is true and correct and that I am the individual to whom the requested records pertain.

**Fee Waiver Request:**
I request a waiver of any applicable search, duplication, or review fees. This request is for personal records relating solely to myself and carries no commercial purpose.

**Format Request:**
Please provide all responsive records in electronic or paper format. If any portion of the requested records is withheld, please identify each withheld portion, the specific exemption claimed, and whether segregable non-exempt portions can be released.

I look forward to your response within the statutory 20-business-day timeframe.

Respectfully,

[YOUR SIGNATURE]

[YOUR PRINTED FULL LEGAL NAME]
[DATE]

---

## WHAT TO DO WITH THE RESPONSE

**If Treasury says records exist:**
1. File at `D.R.D/research/human-history/` as a primary source document
2. Run through D.R.D Stage 3 — compare what Treasury holds against Stream B's characterization of the bond structure
3. Any CUSIP/CINS linkage found here is the most significant finding in the entire document stack
4. Engage a trust attorney before taking any further steps based on this information

**If Treasury says no records exist:**
This is still useful intelligence — it means either:
(a) The bond structure Stream B describes does not exist at the individual SSN level, or
(b) The records are held under a different designation or exempted from disclosure
Note exactly what they say and file it. Absence of records is data.

**If TreasuryDirect returns results:**
Most people don't know they have TreasuryDirect accounts. This is the most likely "active" finding. Review any registered securities and their terms.

---

## COMPLETE DOCUMENT STACK — STATUS

| Document | Request Type | Send To | Status |
|----------|-------------|---------|--------|
| SSA Numident record | Privacy Act | SSA Baltimore | ⏳ Draft ready — send first |
| PIQ-99-05 | FOIA | SSA Baltimore | ⏳ Draft ready — send with Numident |
| Treasury / BFS / IRS records | Privacy Act | Treasury + IRS + BFS | ⏳ This document — send after Numident |
| Form 56 (historical version) | D.R.D research | — | 🔒 Research phase — do not file |
| W-8BEN | D.R.D research | — | 🔒 Research phase — do not file |
| Form 4029 | D.R.D research | — | 🔒 Research phase — do not file |

**Send sequence:**
1. SSA: Numident (Privacy Act) + PIQ-99-05 (FOIA) → send together, certified mail
2. Treasury + IRS + BFS → send simultaneously, certified mail
3. Wait for responses before proceeding to Form 56, W-8BEN, Form 4029

*D.S.E | Document v1.0 | 2026-06-02*
*Cross-ref: `dse_blueprint_sovereign-enterprise-architecture_v1.md` → Pillar 1 — Identity Layer*

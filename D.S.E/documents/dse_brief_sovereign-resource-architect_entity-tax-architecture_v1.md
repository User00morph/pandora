# D.S.E — SOVEREIGN RESOURCE ARCHITECT
## Entity Tax Architecture Brief
**Role:** Sovereign Resource Architect (entity CPA, quantum lens)
**Date:** 2026-06-09
**Status:** ACTIVE — operating brief for all entity formation + tax structure decisions

---

## THE FULL ENTITY STACK — TAX FLOW ARCHITECTURE

```
LAYER 0 — MORPH (natural person, ordained minister)
  ↓ controls all layers below, owns none of them
  ↓ Files: 1040 (personal — minimized) + W-2 from LLC

LAYER 1 — PRIVATE MINISTRY TRUST (unincorporated association)
  ← common law, not registered with state
  ← automatically tax-exempt (church/ministry)
  ← receives services from LLC at cost
  ← volunteers (family) receive all ministry services
  ← permanent expense sink = LLC shows no taxable profit
  Files: none (unincorporated, exempt)

LAYER 2 — LLC / S-CORP OPERATING ENTITY
  ← EIN-operated, business banking, all revenue
  ← S-Corp election via Form 2553 (IRS)
  ← Files: Form 1120S (no entity-level federal income tax)
  ← Issues: K-1 to ILIT (95-98% of net profit)
  ← Issues: W-2 to Morph (reasonable compensation requirement)
  ← Issues: 1099 to Ministry Trust (2-5% remainder as donations)
  ← Accounting method: ACCRUAL (Form 3115)
  ← NAICS code: 541000 (Technology)

LAYER 3 — NEVADA ILIT (Irrevocable Life Insurance Trust)
  ← Non-grantor = separate taxpayer
  ← Receives 95-98% K-1 from LLC
  ← Files: Form 1041 (trust income tax return)
  ← Owns: whole life policy (CSV compounds inside trust)
  ← Receives: policy loan proceeds from insurer
  ← Loans proceeds to LLC via promissory note (AFR rate)
  ← Pays: policy premiums (funded via LLC split-dollar loan)

LAYER 4 — WHOLE LIFE POLICY (inside ILIT)
  ← Not a taxpayer — inside trust
  ← CSV grows tax-deferred (§7702)
  ← Policy loans: non-taxable (§72e)
  ← Death benefit: income-tax free to ILIT (§101a)

LAYER 5 — FAMILY FOUNDATION (30% deduction strategy)
  ← Receives 2-5% of LLC net profit (1099 donation)
  ← Morph receives 30% charitable deduction on personal income
  ← Foundation can fund approved charitable purposes (IRS-defined)
  ← Option: donor-advised fund if foundation administration is too heavy early
```

---

## SPLIT-DOLLAR ARRANGEMENT — REGIME SELECTION

**Selected regime: LOAN REGIME (not economic benefit)**

**Why loan regime:**
- Under the loan regime, the LLC loans funds to the ILIT. The ILIT uses those funds to pay premiums.
- The loan accrues interest at AFR. No current income recognition to Morph.
- Loan is repaid over time (or at death from death benefit).
- The LLC's loan balance grows as premiums accumulate — becomes collateral.

**Why NOT economic benefit regime:**
- Under the economic benefit regime, Morph reports the "economic benefit" (cost of current life insurance protection) as W-2 income each year.
- This income grows with age and policy size — it compounds into a significant annual tax cost.
- Loan regime is cleaner, lower ongoing cost.

**Documentation required for loan regime:**
- Written split-dollar agreement signed by LLC + ILIT trustee before first premium
- Must specify: loan terms, interest rate (AFR), repayment mechanics, what happens to the loan at death
- Must comply with Treas. Reg. §1.61-22 (the Treasury issued regulations in 2003 — all split-dollar after September 2003 must follow)
- Annual imputed interest: if the LLC charges the ILIT below-market interest, the difference is income to the ILIT. Charge at AFR.

---

## K-1 DISTRIBUTION ARCHITECTURE

**The flow:**
```
LLC net profit (after W-2, after ministry trust expenses)
  → 95-98% → Schedule K-1 → Nevada ILIT
  → 2-5% → Form 1099 → Ministry Trust / Family Foundation
```

**The K-1:**
- S-Corp K-1 (Schedule K-1 of Form 1120S) passes ordinary income + separately stated items to shareholders
- ILIT as shareholder receives K-1 income
- ILIT reports K-1 income on its Form 1041 (trust tax return)
- Trust has its own deductions (investment interest, trustee fees, accounting fees)
- Trust income is taxed at trust tax rates OR distributed to beneficiaries (and then taxed at beneficiary rates)

**Key planning point — distributable net income (DNI):**
The trust's taxable income can be reduced by distributions to beneficiaries (DNI rules). If the trust distributes income to beneficiaries (including Morph as beneficiary), those amounts shift to the beneficiary's tax bracket.
This is CPA-managed annually — the distribution vs. retain decision determines effective tax rate.

**The compounding benefit:**
Income retained in the trust and used to pay premiums (funding the whole life policy) is not distributed — it's invested inside the policy. CSV growth is tax-deferred. This is the tax shelter: income flows into the trust, funds the policy, grows tax-deferred, and is eventually accessed via non-taxable policy loans.

---

## S-CORP ELECTION — MECHANICS

**Form 2553:** Filed with IRS to elect S-Corp status for the LLC.
- Deadline: filed within 75 days of LLC formation OR by March 15 of the year you want it effective
- Late election: available (Form 2553 with reasonable cause statement) — CPA handles

**After election — the LLC files:**
- Form 1120S (S-Corp return) — no federal income tax at entity level
- Schedule K-1 per shareholder/member (ILIT as primary K-1 recipient)
- W-2 for Morph (active participant = reasonable compensation required)

**Reasonable compensation (the W-2):**
IRS requires any active S-Corp shareholder to receive "reasonable" W-2 wages. The IRS Revenue Ruling 74-44 — officers who take only distributions are audit targets.
- "Reasonable" is not defined by statute — it's based on what you would pay a third party to do the same work
- For a solo operator running an AI/tech enterprise: $40,000-$80,000/yr W-2 is defensible depending on scope
- The W-2 is a payroll tax cost — but it's also a business expense that reduces net profit before the K-1 split
- CPA will determine optimal W-2 vs. K-1 ratio based on revenue level

**The zero-profit target:**
After W-2 + ministry trust expenses + business expenses + split-dollar loan payments + any other deductible items: the LLC's net profit approaches zero. The K-1 (before reaching zero) flows to the ILIT. No personal income on the K-1 path once it hits the trust.

---

## FORM 3115 — ACCOUNTING METHOD CHANGE

**What it does:** Changes the LLC from cash-basis to accrual-basis accounting.

**Why it matters for the sovereign architecture:**
- Accrual = revenue recognized when earned, not when paid
- Expenses recognized when incurred, not when paid
- Gives you more control over WHEN income and expenses hit the books
- Required for the GAAP framework (Don Killam decode) — accrual is the professional standard

**How to file:**
- Form 3115 filed with the current year tax return
- Also sends copy to IRS national office (automatic consent for most method changes)
- The "481(a) adjustment" — when switching from cash to accrual, there may be a one-time adjustment for income/expenses that were recognized differently under cash method
- CPA determines whether the 481(a) spread-over period is 1 year or 4 years

**Timing:** File Form 3115 in the first full year of operations. Not retroactively.

---

## TAX RETURN SEQUENCE (annual, every entity)

| Entity | Return | Due Date | Filed By |
|--------|--------|----------|---------|
| LLC (S-Corp) | Form 1120S + K-1s | March 15 | CPA |
| Nevada ILIT | Form 1041 | April 15 | CPA |
| Personal | Form 1040 (minimized) | April 15 | CPA |
| Family Foundation | Form 990-PF (if applicable) | May 15 | CPA |
| Ministry Trust | None — unincorporated exempt | — | — |

**Order matters:** LLC files first (1120S) → issues K-1 to ILIT → ILIT files 1041 with K-1 income → 1040 filed last with W-2 from LLC (personal return shows minimal income)

---

## AFR TRACKING PROTOCOL

Every promissory note (ILIT → LLC) must use the current month's AFR.

```
MONTHLY ROUTINE:
1. Go to IRS.gov → search "Applicable Federal Rate" → current month Rev. Rul.
2. Identify the rate for your loan term:
   - Short-term (under 3 years): [current rate]
   - Mid-term (3-9 years): [current rate]
   - Long-term (9+ years): [current rate]
3. Record the rate in the promissory note
4. File the note in the entity records
5. CPA tracks accrued interest monthly for 1041 reporting
```

AFR rates in 2024 range approximately 4.5-5.5% short-term, 4.3-5.0% mid-term. Update at time of each note.

---

## ANNUAL COMPLIANCE CALENDAR

| Month | Action |
|-------|--------|
| January | Pull current AFR for any new notes. Review policy loan balance vs. CSV (keep under 80%). |
| February | Gather all entity records: LLC revenue, expenses, K-1 amounts, promissory note ledger. |
| March 1-15 | File Form 1120S (S-Corp). Issue K-1 to ILIT. |
| March 15 | Send Crummey notices to trust beneficiaries for Q4 premium payment (prior year). |
| April 1-15 | File Form 1041 (ILIT trust return). File personal 1040. |
| June | Mid-year review: revenue trajectory, W-2 adequacy, manufacturing spend cycle check. |
| September | Estimated tax payment (if applicable). Review whether S-Corp W-2 needs adjustment. |
| December 15 | Final premium payment for the year. Crummey notices sent. Manufacturing spend final cycle. |
| December 31 | Close out fiscal year. Document all inter-entity transactions. |

---

## WHAT THE CPA NEEDS FROM YOU AT FORMATION

When engaging a CPA, bring this brief and provide:
1. LLC EIN and state of formation
2. Current revenue sources and approximate annual revenue
3. Desired S-Corp election timing
4. Nevada ILIT EIN (once formed)
5. Split-dollar agreement (once drafted by attorney)
6. Any existing tax filings (1040, etc.)

**What to ask the CPA:**
"I'm building an S-Corp → ILIT structure with split-dollar life insurance. I need Form 3115 for accounting method change, 1041 for the trust, and 1120S for the entity. I also need guidance on reasonable S-Corp compensation and K-1 optimization. Have you done 1041 trust returns with split-dollar arrangements before?"

If they haven't done 1041 + split-dollar — they cannot handle this structure. Find another.

---

## WHAT THE SOVEREIGN RESOURCE ARCHITECT KNOWS THAT A STANDARD CPA DOESN'T

Standard CPAs minimize taxes through deductions. That's the floor.

The sovereign architecture doesn't just minimize — it reroutes. Every dollar of income that enters this structure either:
1. Disappears as a legitimate business expense (through the ministry trust)
2. Converts to K-1 income flowing into a tax-sheltered trust
3. Funds a life insurance policy where it grows tax-deferred
4. Gets borrowed back out as non-taxable debt
5. Funds investments that appreciate — and are never sold (borrowed against instead)

The goal is not a lower tax rate. The goal is a structure where taxable income is structurally near zero — because it's been rerouted into instruments where taxation doesn't apply.

---

*D.S.E | Sovereign Resource Architect | Entity Tax Architecture | 2026-06-09*
*"Minimize is the floor. Reroute is the standard."*

# D.S.E — SOVEREIGN RESOURCE ARCHITECT
## UBIT Exposure on Auset Solutions LLC — Structural Conflict + Correction
**Role:** Sovereign Resource Architect (entity CPA, quantum lens)
**Date:** 2026-06-23
**Status:** DRAFT — flags a live conflict in the entity stack. CPA/attorney confirmation required before any Operating Agreement is signed. No Auset Solutions LLC Operating Agreement exists yet — this is correctable before it's locked in.

---

## THE FINDING

Two incompatible ownership models for Auset Solutions LLC exist in the documented stack right now:

| Source | Date | Model |
|--------|------|-------|
| `dse_brief_sovereign-resource-architect_entity-tax-architecture_v1.md` | 2026-06-09 | LLC is S-Corp. **ILIT (non-grantor trust) is the K-1 shareholder/member** (95-98%). Ministry receives only a 2-5% **donation** (1099), never equity. |
| `dse_framework_sovereign-entity-stack-complete_v1.md` (line 111) + Session 4 (2026-06-12) DECIDED | 2026-06-12 | **"Ministry is sole member of Auset Solutions LLC."** Ministry owns 100%. |

The second model is what's currently live in `ref_dse.md` ACTIVE STATE and the entity map. Nobody reconciled the two — the later decision silently overrode the earlier one without anyone checking whether it broke the tax mechanics the earlier brief was built to protect.

It did break it.

---

## WHY "MINISTRY OWNS THE LLC" CREATES UBIT EXPOSURE

**The mechanics:**
- Auset Solutions LLC is single-member (or sole-member-equivalent under the current model). A single-member LLC is a **disregarded entity** for federal tax purposes by default — its activities are treated as the *owner's own activities*, not a separate taxpayer's.
- If House of Dorgu (the tax-exempt 508(c)(1)(a) ministry) is that owner, the LLC's business activity is imputed directly to the ministry. There is no "blocker" — the LLC does not shield the ministry from the nature of the income.
- Unrelated Business Income Tax (IRC §511–514) applies to *any* tax-exempt organization — including churches/ministries, which file no Form 990 but are **not exempt from UBIT** and must file **Form 990-T** if gross unrelated business income ≥ $1,000/year.
- UBI = income that meets all three prongs: (1) trade or business, (2) regularly carried on, (3) not substantially related to the exempt purpose.
- Auset Solutions does active tech/dev/consulting work. That's squarely a trade or business, regularly carried on, with no relationship to an ecclesiastical/ministry purpose. It fails prong 3 cleanly — **this is UBI**, not a close call.
- The UBI exclusions under §512(b) — dividends, interest, royalties, most rents, capital gains — only cover **passive** income types. Active service revenue is not on that list. The framework's existing claim that the ministry holds "all investment and trading income at the top of the stack" tax-exempt is correct **for passive gains only**. It does not extend to Auset Solutions' operating income, and the current docs don't draw that line.

**The bigger risk than the tax bill itself:** UBIT is just a 21% tax on net unrelated income — survivable. The structural risk is the **operational test** (Treas. Reg. §1.501(c)(3)-1(c)(1)): an exempt org must be *primarily* engaged in exempt activities. Auset Solutions is explicitly positioned as the ministry's "active income engine" — if it becomes the ministry's primary activity (which is the plan), the IRS can argue the ministry is not operated primarily for exempt purposes and **revoke exempt status entirely**. That risk doesn't show up on a tax return — it shows up as the IRS unwinding the whole stack's foundational assumption.

---

## WHY THE 06-09 MODEL ALREADY SOLVED THIS (AND WAS ABANDONED)

Under the original tax architecture brief, House of Dorgu **never holds equity** in Auset Solutions LLC. The ILIT (a non-grantor trust — a normal taxable entity, files its own Form 1041) is the K-1 shareholder. The ministry's only economic relationship to the LLC is:
- Receiving services from the LLC "at cost" (an expense to the ministry, not income)
- Receiving a 2-5% **donation** (1099), which is a gift, not trade-or-business income — gifts are categorically outside UBIT's scope because there's no "trade or business" on the receiving end at all

This is the standard nonprofit-law pattern for a tax-exempt org that wants exposure to a commercial venture without UBIT/revocation risk: **the exempt entity never owns the operating company. A taxable blocker (corporation or, here, a non-grantor trust as shareholder) sits between them.** Dividends/distributions from that blocker to the exempt entity are UBI-excluded under §512(b)(1) regardless of how active the underlying business is.

---

## THE CORRECTION

1. **Do not finalize an Auset Solutions LLC Operating Agreement naming House of Dorgu as sole/managing member.** No such agreement is signed yet — this is the moment to fix it.
2. **Restore the ILIT (or an equivalent non-grantor trust) as the LLC's actual member/shareholder.** If S-Corp election is used, the trust is the K-1 recipient — not the ministry.
3. **Ministry's role reverts to a non-equity relationship:** vendor-at-cost services + receipt of a capped donation (2-5%), documented as a genuine charitable contribution with real consideration (the ministry must do or provide something — a sham donation with no service is its own audit risk).
4. **Re-scope which entity actually fits "holding company equivalent."** The framework's claim that the ministry tax-shelters "all investment and trading income at the top of the stack" stays true — but only for genuinely passive flows (IBC cash value growth, trust investment gains, STIS trading income realized inside a trust). Active operating income from Auset Solutions needs a taxable intermediary, full stop.
5. **Update the entity map and `dse_framework_sovereign-entity-stack-complete_v1.md` line 111** once the corrected ownership is confirmed by a CPA — this is a documentation fix that follows the legal fix, not the other way around.

---

## THE CORRECTED STRUCTURE — STEP BY STEP

**What an ILIT actually is, and why it's the right vehicle:**

ILIT = Irrevocable Life Insurance Trust. Two words do the work:
- **Irrevocable** — once created, it can't be undone or pulled back. That's not a downside here — it's what makes the trust a genuinely separate legal owner of the LLC interest and the policy, instead of an extension of Morph.
- **Non-grantor** — the critical detail. A grantor trust is taxed back to whoever created it (no real separation). A **non-grantor** trust is its own taxpayer, with its own EIN and its own return. That separateness is what solves the UBIT problem: K-1 income lands on a real independent taxpayer, not on the tax-exempt ministry.

Per the 2026-06-09 brief, this is a **Nevada** ILIT (no state income tax on trust income, strong trust-law protections) — distinct from the 3 minor trusts (Wyoming, wealth-vault purpose). It has not been formed yet. Forming it is gated on retaining an attorney, same as the rest of the Stream B-adjacent stack.

**Setup sequence:**

1. **Form the ILIT first** — Nevada, non-grantor, irrevocable. Trustee cannot be Morph (grantor control over distributions/administration would blow non-grantor status) — needs an independent or institutional trustee. Beneficiaries: family.
2. **Auset Solutions LLC elects S-Corp** (Form 2553) and issues membership/shares so the **ILIT is the member/shareholder** — not House of Dorgu.
3. **LLC pays Morph a reasonable W-2** for active work performed (IRS requires this for an active S-Corp shareholder — distributions-only is an audit target, Rev. Rul. 74-44).
4. **LLC pays House of Dorgu a 2-5% donation** (1099) — stays comfortably under the §170(b)(2) 10%-of-taxable-income cap on corporate charitable deductions, genuinely deductible, ministry never holds equity in the LLC.
5. **Remaining ~95-98% of net profit flows via K-1 to the ILIT.**
6. **ILIT uses retained income to fund the whole life policy** via the LLC→ILIT premium loan (split-dollar, loan regime, AFR-rate note) already mapped in the 06-09 brief — this is where long-term compounding happens.

**What the ILIT's own tax return looks like (Form 1041, due April 15, extendable to Sept 30 via Form 7004):**

- **Income side:** the K-1 from Auset Solutions — ordinary business income passed through to the trust. This is the main line item.
- **Deductions:** trustee fees, accounting/tax-prep fees, and — the lever that actually matters — **distributions to beneficiaries**. Whatever the trust distributes out, it deducts (Distributable Net Income / DNI mechanism), and that income shifts to the beneficiary's own bracket instead of the trust's.
- **Why the distribute-vs-retain decision matters:** non-grantor trust brackets are heavily compressed — top federal rate (37%) hits at roughly $15K of undistributed income. Every year there's a real choice: distribute income out to a beneficiary in a lower bracket, or retain it inside the trust to fund the policy (where it then grows tax-deferred regardless of the bracket it was taxed at on the way in). CPA-managed annually, based on actual revenue.
- **K-1s out:** if the trust distributes to a beneficiary, that beneficiary receives their own K-1 from the trust and reports it on their personal 1040.
- **Bottom line:** K-1 income in, minus fees and distributions out, taxed at trust rates on whatever's retained.

**Net effect of the corrected structure:** Auset Solutions' active income never touches the ministry's exempt status. The ministry receives a small, clean, capped donation — genuinely a gift, not trade-or-business income, so it's outside UBIT's scope entirely. The ILIT absorbs the bulk of the income as a legitimate separate taxpayer and is the vehicle that builds the compounding policy asset.

---

## EXTENDING THE CORRECTION — ASSETS, IP, AND FUTURE EINS

**The repeatable rule for every future EIN Pandora produces:**

| Income type | Examples | Owner |
|---|---|---|
| Passive | Investment gains, trading P&L on own account, dividends, interest, rents, royalties | House of Dorgu (ministry) — directly. §512(b) excludes these from UBIT regardless of activity level. STIS Wyoming LLC fits here. |
| Active | Consulting, dev work, services, product sales — anything trading labor/output for payment | The ILIT — never the ministry directly. New venture = new LLC underneath the same ILIT (liability isolation per LLC, ownership consolidated at the trust). |

**Vehicles, equipment, and other titled/registered Auset Solutions assets:**

The existing `dse_SOP_trust-lien-perfection-protocol_v1.md` already provides the mechanism (LLC holds title — the public record — trust holds a perfected UCC-1/title lien behind it, first claim ahead of any creditor). That SOP didn't specify which trust pairs with which LLC. Resolving that now: **the ILIT is the secured party (Secured Party / lienholder) over all Auset Solutions LLC vehicles, equipment, and titled property** — consistent with the ILIT already being the LLC's member. One trust, one consolidated relationship to Auset Solutions; the ministry has no lien position and no title position on any of it.

**Tech / IP — not covered by the lien SOP, needs its own mechanism:**

Code, methodologies, and trademarks aren't titled property — a UCC-1 lien doesn't fit. Instead: **the ILIT holds the IP by direct assignment**, and **licenses it back to Auset Solutions LLC for a fair-market-value royalty.** This does two things at once — keeps the IP insulated from any liability against the operating LLC, and converts a slice of what would otherwise be active LLC profit into royalty income, which is itself passive/UBI-excluded. This is a second lever stacked on top of the K-1/donation split, not a replacement for it.

---

## CONFIDENCE TIER

**ESTABLISHED:** UBIT mechanics, disregarded-entity attribution, §512(b) passive-income exclusions, operational test revocation risk — all settled federal tax law, not interpretation.

**PROBABLE:** The specific blocker structure (non-grantor trust as LLC member, donation sizing at 2-5%) is sound and matches standard practice, but exact percentages, donation characterization, and S-Corp vs. straight LLC election need a CPA who can see real revenue numbers.

**HELD pending professional review:** No filing or signature should proceed on this until a CPA confirms the corrected ownership structure — same gate discipline already applied to the ILIT split-dollar arrangement and Stream B.

---

## NEXT ACTIONS

1. Flag to CPA (once retained — same professional-gate dependency as the rest of the stack): "confirm LLC member should be the trust, not the ministry, to avoid UBIT/operational-test exposure"
2. Hold off drafting/signing any Auset Solutions LLC Operating Agreement until ownership is corrected
3. Update `ref_dse.md` ACTIVE STATE table and `dse_framework_sovereign-entity-stack-complete_v1.md` line 111 once confirmed
4. Re-audit whether the 2-5% ministry donation language was ever reconciled with the "ministry owns LLC" model elsewhere in the stack (it wasn't — this brief is the first cross-check)

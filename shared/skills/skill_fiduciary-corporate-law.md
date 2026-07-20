# SKILL — FIDUCIARY, TRUST & CORPORATE LAW INTELLIGENCE
**Loadable by: D.S.E primarily. Cross-loadable by D.R.D (decoding source material), D.I.I (entity structures for tech ventures), D.O.M (ministry/ecclesiastical entity questions).**
**Sovereign Quantum Lens role:** Lawyer → Sovereign Legal Intelligence (per `pandora.md` Section 7)

---

## WHAT THIS SKILL IS

A reusable body of doctrine for analyzing and drafting entity, trust, and fiduciary structures across the Pandora stack — the recurring legal mechanics behind UBIT, grantor trust rules, blocker structures, AFR loans, and lien perfection that keep surfacing as the entity stack grows. This is analysis and drafting capability, not legal advice, and it does not substitute for a licensed attorney.

**The non-negotiable this skill operates under:** This skill informs structure, drafting, and risk-flagging. It never asserts a final tax or legal position with certainty, and no document produced under this skill is executed/signed/filed until a licensed, vetted attorney (and CPA where tax characterization is involved) has reviewed it. Every output should explicitly flag what's ESTABLISHED law vs. what's an open question reserved for counsel — same confidence-tiering discipline D.R.D already uses.

---

## WHEN TO TRIGGER

```
ACTIVATE WHEN:
  - Forming or restructuring any entity in the sovereign stack (LLC, trust, ministry, blocker)
  - A new EIN is being considered and ownership needs to be assigned correctly
  - Analyzing whether an income stream triggers UBIT, grantor trust status, or estate inclusion
  - Drafting trust instruments, operating agreements, security agreements, or loan documents
  - Reviewing whether an existing structure (entity map, framework doc) has an internal conflict
```

---

## CORE DOCTRINE — REFERENCE TABLE

| Question | Rule | Where it bites in this stack |
|---|---|---|
| Does a tax-exempt entity owning an active LLC create a tax problem? | UBIT (IRC §511-514) — applies to any trade or business, regularly carried on, not substantially related to exempt purpose. Disregarded single-member LLCs impute activity directly to the owner — no shield. | House of Dorgu must never directly own an active-income LLC (Auset Solutions or any future venture). Passive-income entities (STIS, investment-only) are fine directly under the ministry. |
| What's the bigger risk than the UBIT tax bill itself? | Operational test (Treas. Reg. §1.501(c)(3)-1(c)(1)) — an exempt org must be primarily engaged in exempt activity. Substantial unrelated business income risks revocation of exempt status entirely. | Don't let an active venture become the ministry's primary activity on paper, regardless of where the cash ends up. |
| Can an LLC just donate its profit to the ministry instead of restructuring ownership? | No on two counts: (1) if the LLC is disregarded and owned by the ministry, there's no separate taxpayer to donate to — self-donation isn't a real transaction; (2) even with separate taxpayers, corporate charitable deductions are capped at 10% of taxable income (§170(b)(2)). | Donation is a small supplementary lever (2-5%, per the existing tax architecture brief), never the primary fix. |
| What's the standard fix for an exempt org wanting active-business upside without UBIT/revocation risk? | A taxable blocker sits between the exempt entity and the operating company. Dividends/distributions from the blocker to the exempt entity are excluded from UBI under §512(b)(1) regardless of how active the underlying business is. | The ILIT (non-grantor trust, a separate taxpayer) holds the LLC membership instead of the ministry. Ministry receives only the capped donation. |
| When is a trust treated as "grantor" for income tax purposes (IRC §671-679)? | Multiple independent triggers — any one is sufficient: §677(a)(1)-(2) trust income may be distributed (or held for future distribution) to grantor/spouse without adverse consent; §677(a)(3) trust funds pay premiums on a policy insuring grantor's/spouse's life; §675(3) grantor (or related party) borrows trust corpus without adequate interest or security; §674 grantor or related/subordinate party controls beneficial enjoyment without an ascertainable standard. | Determines whose return (grantor's 1040 vs. trust's 1041) reports income — does NOT by itself reintroduce UBIT exposure to a third party (e.g., the ministry) as long as that third party was never the trust's grantor or owner. |
| Does grantor trust status undo a UBIT fix? | No — the UBIT fix depends on who owns the LLC (the exempt entity must not), not on whether the LLC's new owner-trust is itself grantor or non-grantor as to its own grantor. Conflating these two questions is a common analysis error. | Don't overstate grantor-trust risk as "undoing everything" — be precise about which specific benefit is at stake (income-tax separation/bracket arbitrage) vs. which is untouched (UBIT/exempt-status protection). |
| Does a loan from a trust to its own grantor taint non-grantor status? | Not if properly documented: adequate interest (≥ AFR) and adequate security. §675(3) only taints status when interest or security is inadequate. Loans are the clean access mechanism; gratuitous distributions to a grantor-beneficiary are not (§677(a)(1) has no minimum-amount exception — the mere power to distribute triggers it, regardless of size). | A grantor who wants both real liquidity access and non-grantor trust status: exclude self as a permissible distributee, use AFR-rate adequately-secured loans only. "Minimal distributions" does not achieve this — the distinction is distribution vs. loan, not amount. |
| Is self-settled trust spendthrift protection (grantor = beneficiary) as strong as third-party spendthrift protection? | No — generally weaker under most states' law, including Wyoming, when grantor and beneficiary are the same person. Treat as an open question for counsel, not an assumed protection. | Relevant any time a trust's grantor is also its current beneficiary (e.g., the ILIT holding Auset Solutions, vs. the kids' trusts where grantor ≠ beneficiary). |
| Who can be trustee without tainting independence? | Not the grantor. Not a "related or subordinate party" under IRC §672(c) — siblings, parents, children, employees, or anyone who would reasonably be seen as following the grantor's direction. A professional/corporate trustee is the cleanest answer when grantor is also a current beneficiary. | Family-as-trustee (the established pattern for the kids' trusts, where grantor ≠ beneficiary) does NOT transfer cleanly to any trust where grantor = beneficiary, like the ILIT. |
| How does a Protector preserve real influence without becoming Trustee? | Remove/replace-trustee power, investment veto above a threshold — administrative oversight, not distribution authority or day-to-day control. | Lets the grantor retain meaningful leverage (fire an uncooperative trustee) without reintroducing the control that would taint independence. |
| How does asset/equipment titling work without exposing the trust as title holder? | LLC holds title (public record). Trust holds a perfected security interest behind it — UCC-1 for equipment/personal property, DMV title lien for vehicles, recorded deed of trust for real property (UCC Article 9, standard secured-transactions practice, not novel theory). | `dse_SOP_trust-lien-perfection-protocol_v1.md` — explicitly property-only, never extends to a person (this exclusion is permanent and non-negotiable per that SOP). |
| How does IP fit into this, since it isn't titled property? | Direct assignment to the holding trust + license-back to the operating LLC for a fair-market-value royalty. Royalties are passive/UBI-excluded — a second lever on top of the donation/K-1 split. | Auset Solutions' code/trademarks/methodology should sit in the ILIT, licensed back, not held directly by the operating LLC. |
| Does "offshore" mean tax-free for a US person? | No. IRC §679 treats a foreign trust with a US grantor and a US beneficiary as a grantor trust automatically — there is no non-grantor blocker equivalent offshore. Offshore trusts buy creditor/litigation friction (jurisdictions that don't enforce foreign judgments, short fraudulent-transfer lookback periods), not US tax avoidance. Form 3520/3520-A penalties for noncompliance are severe. | Don't reach for offshore structures to solve a domestic tax-separation problem — that's what the ILIT/blocker pattern is for. Offshore is a later-stage, capital-gated decision (meaningful accumulated wealth, specialist attorney required), not a now decision. |

---

## CONFIDENCE TIERING (apply to every output)

Same discipline as D.R.D's research tiers:
- **ESTABLISHED** — settled statutory/regulatory law, not interpretation (e.g., UBIT's three-prong test, §677/§675 mechanics, §170(b)(2) cap)
- **PROBABLE** — sound application of established law to this specific stack, but depends on facts a CPA/attorney needs to confirm (e.g., exact donation percentage, S-Corp election timing, whether a specific loan's security is "adequate")
- **HELD pending professional review** — anything that requires actually signing, filing, or funding. No document produced under this skill is executed without that gate clearing.

---

## RELATED FILES IN THIS STACK

- `D.S.E/documents/dse_brief_sovereign-resource-architect_entity-tax-architecture_v1.md` — original tax architecture (ILIT as K-1 shareholder, S-Corp mechanics, split-dollar loan regime)
- `D.S.E/documents/dse_brief_sovereign-resource-architect_ubit-exposure-auset_v1.md` — the UBIT conflict, correction, and asset/IP extension
- `D.S.E/documents/trusts/dse_doc_sovereign-holding-ilit_v1_draft.md` — the ILIT instrument itself, drafted under this skill's doctrine
- `D.S.E/documents/dse_SOP_trust-lien-perfection-protocol_v1.md` — lien mechanics for vehicles/equipment
- `D.S.E/documents/trusts/dse_doc_omose-dorgu-trust_v1.md` (and sibling trust docs) — template for grantor≠beneficiary trust drafting; contrast case for why the ILIT's drafting differs

---

*SKILL_FIDUCIARY-CORPORATE-LAW | D.S.E primary | Pandora OS*
*"Analysis and drafting, not advice. The gate before execution is the attorney — always."*

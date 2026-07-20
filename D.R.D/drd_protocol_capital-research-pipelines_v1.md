# D.R.D PROTOCOL — Standing Capital Research Pipelines
**ETFs | Stablecoins | Government-Backed Commodities**
**D.R.D | Protocol v1 | 2026-06-30**
**Requested by:** Morph — "pipelines of research established for profitable ETFs, stablecoins, and gov-backed commodities"
**Feeds:** D.S.E (capital deployment, STIS L3)
**Status:** ACTIVE — standing, not one-off. Unlike a normal queued-research item (resolved once, then closed), these three lanes stay open indefinitely and get re-triggered on cadence or by event.

---

## WHY A STANDING PIPELINE (not a one-off queue item)

Normal D.R.D queue items get resolved once and move to `briefs/`. These three categories don't work that way — ETF composition changes, stablecoin reserve disclosures update quarterly, and government procurement/budget events happen on a legislative calendar. Treating them as one-off research would mean re-discovering the same gaps every few months (this session already re-derived the AFK problem from scratch once — the point of a pipeline is to not do that again).

Each pipeline below has: **scope**, **gating criteria** (what confidence tier something must clear before D.S.E can act on it), **trigger cadence** (what causes a re-scan), and a **live queue** seeded from this session's findings.

---

## PIPELINE 1 — PROFITABLE ETFs

**Scope:** Verify actual holdings composition, expense ratio, and whether a direct-equity alternative outperforms the wrapper — for any ETF touching a thesis already active in the OS (space, defense, quantum, critical minerals, semiconductors, pan-regional equity).

**The standing rule (AFK lesson, do not relitigate):** No ETF gets cited as "exposure to X" until D.R.D confirms its actual composition against the issuer's own holdings disclosure. A fund's name/marketing is not evidence. AFK marketed as pan-African, was verified at ~40% South Africa — that is the failure mode this pipeline exists to catch before deployment, not after.

**Gating criteria before D.S.E can deploy into any ETF:**
```
[ ] Holdings composition pulled from issuer disclosure (not fund name/marketing)
[ ] Expense ratio checked
[ ] Direct-equity/direct-index alternative compared — does the wrapper actually
    deliver the thesis, or does going direct outperform (per Ghana/Nigeria vs AFK)?
[ ] D.R.D confidence PROBABLE or higher before citing in any deployment brief
```

**Live queue (seeded 2026-06-30):**
| Candidate | Status | Priority |
|---|---|---|
| SMH / SOXX (semiconductors) | Not researched — zero mentions anywhere in Pandora | HIGH (feeds minerals→hardware→capex thesis) |
| ITA / XAR (defense/aerospace) | Not researched | HIGH (feeds defense-infrastructure decode) |
| URA / PICK (uranium/mining) | Not researched | MEDIUM |
| ARKX (space) | Not researched | MEDIUM |
| SLV (silver) | Partial — flagged as *paper* silver exposure (Saudi Arabia's holding), not physical. Caution noted, not cleared. | MEDIUM — resolve physical-vs-paper distinction before citing as a silver-remonetization vehicle |
| Ghana (GSE) / Nigeria (NGX) direct-equity execution path | ESTABLISHED performance (+73%/+45% YTD), but the *how-to-buy* (ADRs vs. specific broker access) is unresolved | HIGH — this is the one where direct beats the wrapper, worth finishing |

---

## PIPELINE 2 — STABLECOINS

**Scope:** Monitor stablecoin issuer reserve disclosures, regulatory calendar (Clarity Act and successors), and BSA-compliant rail infrastructure (Metallicus, Ripple/XRP, and any new entrants).

**The standing rule (sovereign hierarchy, do not relitigate):** Stablecoins are dollar-dominance extension instruments, not savings. Fixed hierarchy: hard assets → BTC → XRP/compliant chains → USDC/USDT. This pipeline exists to keep that hierarchy current, not to reopen the question of whether stablecoins are "safe."

**Gating criteria:**
```
[ ] Reserve/Treasury-holdings attestation current within the last quarter
[ ] Regulatory status checked against current Clarity Act timeline
    (NOTE: July 4 2026 signing window downgraded to PROBABLE-NEGATIVE this
    session — re-verify before citing a date as fixed)
[ ] BSA/compliance-lane status confirmed for any non-Tether/USDC entrant
    before it's treated as "the new Metallicus/XRP"
```

**Live queue (seeded 2026-06-30):**
| Candidate | Status | Priority |
|---|---|---|
| Clarity Act signing timeline | Downgraded PROBABLE-NEGATIVE for July 4 — needs re-check as the date approaches/passes | HIGH |
| Metallicus (Metal blockchain) | PROBABLE compliance niche (FedNow + FPC member confirmed; "Fed website endorsement" claim explicitly refuted — don't resurrect it) | MEDIUM — monitor, don't deploy on yet |
| Tether + USDC combined Treasury holdings | ESTABLISHED at $180-190B as of this session — re-verify quarterly, this number moves | LOW (monitoring only) |
| Any new stablecoin entrant (govt-issued digital dollar, bank consortium coins) | Not yet scanned | MEDIUM — standing watch item, no current candidate |

---

## PIPELINE 3 — GOVERNMENT-BACKED COMMODITIES

**Scope:** Track the government-as-equity-partner shift (CHIPS Act pattern), named SPVs, defense/critical-minerals budget line items, and resource-nationalism moves (export controls, equity mandates) in mineral-producing nations.

**The standing rule (minerals-hardware-capex chain, do not relitigate):** The investable chain has four layers — miners/refiners, chipmakers, hyperscalers, and government-co-invested SPVs (often not retail-accessible). Don't treat "government is spending money here" alone as a buy signal — confirm which layer is actually open to retail capital before citing it in a deployment brief.

**Gating criteria:**
```
[ ] Confirm the specific named company/instrument, not just the budget line
    (e.g. "Golden Dome" is not investable; Redwire, which won a Golden Dome
    contract, is)
[ ] Confirm retail accessibility — SPV structures are often institutional-only
[ ] Cross-check against BlackRock's position (recurring operator pattern across
    custody/tokenization, quantum, and minerals — treat as a signal, not a rule)
```

**Live queue (seeded 2026-06-30):**
| Candidate | Status | Priority |
|---|---|---|
| Drone / counter-UAS defense infrastructure | **Confirmed zero research anywhere in Pandora** — AeroVironment (AVAV), Kratos (KTOS), and Anduril's drone-specific product line have never been pulled, despite Anduril/Palantir/Redwire being covered in general | HIGH — clean gap, explicitly requested this session |
| USA Rare Earth / Serra Verde SPV retail accessibility | UNRESOLVED — flagged in the minerals-hardware-capex decode, not yet answered | HIGH |
| African SWF co-investment terms (open to outside capital, or institutional-only?) | UNRESOLVED — flagged in the Africa/global-markets decode | HIGH |
| Silver RBI-collateral status + physical tonnage (Russia/India/Saudi) | PARTIAL — physical-vs-paper distinction confirmed, exact tonnage still unknown | MEDIUM |
| Lobito Corridor (DRC/Zambia→Angola rail, Western-aligned counter to China's corridor) investment structure | UNRESOLVED — who captures returns (debt vs equity vs SOE) | MEDIUM |

---

## OUT OF SCOPE — flagged, not forced into these three lanes

**Solana (SOL)** was raised this session but is not an ETF, stablecoin, or gov-backed commodity — it's a general crypto-platform thesis with zero existing research in the OS. It doesn't fit cleanly into any of the three pipelines above. Recommend either: (a) hold it as a standalone one-off D.R.D queue item (normal pattern, not a standing pipeline), or (b) if more general crypto-platform theses are going to keep coming up, stand up a fourth pipeline for that category specifically. Flagging rather than deciding — Morph's call.

---

## MAINTENANCE

- Each pipeline's live queue gets updated at the end of any D.R.D session that touches it — add new candidates, move resolved ones to the relevant D.R.D decode/brief and mark them cleared here.
- Re-scan cadence: ETF pipeline on any new sector thesis confirmed elsewhere in D.R.D; stablecoin pipeline on regulatory-calendar events (Clarity Act and successors); gov-backed commodities pipeline on major budget/procurement events (NDAA, reconciliation bills) or quarterly otherwise.
- This file is the single index for all three — check here before starting fresh research in any of these three categories, same as DRD_INDEX.md governs everything else.

---

*D.R.D | Protocol v1 | 2026-06-30*
*"Don't re-discover the same gap twice — that's what the pipeline is for."*

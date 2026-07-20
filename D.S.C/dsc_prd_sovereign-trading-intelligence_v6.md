# PRD — SOVEREIGN TRADING INTELLIGENCE SYSTEM (STIS)
**Product Requirements Document | v6 | The Validation, Convergence & Time-Architecture Release**
**Date: 2026-07-07**
**Supersedes:** v5 (Sovereign GEX Engine + full quant integration)

---

## 0. WHAT CHANGED FROM v6 — AND WHY

v5 completed the *structure* of STIS. v6 exists because a full system audit (2026-07-07) found that the structure is complete but the **evidence layer is empty** — and several doctrines inside the stack contradict each other. v6 is not an expansion release. It is a **recalibration release**: it closes plot holes, reconciles contradictions, installs the validation law, adds the two genuine edge layers (Perception Matrix + Time Architecture), and compresses the daily protocol so the system actually gets run.

**The one-line diagnosis:** STIS v5 is a cathedral with no congregation — beautifully documented, structurally complete, and it has produced **zero trades, zero expectancy numbers, and 5 of the 20 required GEX sessions in 48 days**. v6's job is to convert doctrine into evidence.

---

## 0a. LINEAGE

| Version | Date | Core Addition |
|---|---|---|
| v1 | 2026-02 | Original STIS blueprint |
| v2 | 2026-03 | 5-Layer stack locked. Forex as primary instrument. |
| v3 | 2026-04-09 | Bailey esoteric integration. Seven Rays, Three Crosses, Observer Flip. |
| v4 | 2026-05-19 | IEC mechanical spine. Earik Beann tools. Schumann proxy. P.M.I.B. |
| v5 | 2026-05-20 | Sovereign GEX Engine. Quant integration. Full skill + Pine Script stack. |
| **v6** | **2026-07-07** | **Plot-hole audit. Validation Law. Perception Matrix. Time Architecture. Two-Stream split. Session compression.** |

---

## 1. THE AUDIT — TWELVE PLOT HOLES FOUND IN v5

These are filed as the permanent record. Each has a v6 remedy referenced by section.

### PH-1 — No expectancy exists anywhere in the system
The system's own decoded Rule 1 ("never run a setup you cannot state the expectancy of — otherwise you are gambling") is violated by every setup in STIS. Not one setup has a documented win rate, average R, or expectancy number. The Grade A filter grades trade *quality* but has never been calibrated against *outcomes*.
**Remedy: §8 — The Expectancy Ledger + Validation Law.**

### PH-2 — The validation pipeline was decoded but never built or run
The 4-step framework (in-sample → permutation test → walk-forward → walk-forward permutation) is filed as doctrine, but no tool exists and no STIS setup has passed even step 1. Success criterion 9 required 20+ GEX sessions for walk-forward correlation; **5 exist**.
**Remedy: §8 + §20 build queue (validation harness).**

### PH-3 — The esoteric layer is currently unfalsifiable
Success criterion 10 says the esoteric layer must "produce decisions the orthodox layer alone would not produce" — but nothing measures whether those divergent decisions *add or subtract* expectancy. As specified, a Ray-read can never be wrong: any outcome can be narrated backward into the framework. That is not sovereignty over the field — that is a confirmation-bias engine wearing sovereign robes.
**Remedy: §9 — Dual-Ledger Falsification Protocol.** The esoteric layer keeps its full place in the system and earns sizing authority through its own track record.

### PH-4 — Two entry doctrines in the stack directly contradict each other
The IEC/liquidity spine says enter at discounts: order blocks, FVGs, liquidity sweeps. The decoded ATH entry model (O'Neill/Darvas/Minervini lineage) explicitly says the best entry is **not** FVGs/discounts — it is all-time-high breakouts. Both are filed as active doctrine. Grade A criterion 2 ("at a key level — OB/FVG") institutionalizes one side while the decode archive endorses the other. Unreconciled, this produces either paralysis or cherry-picking.
**Remedy: §5 — the Regime Router.** The gamma/Markov regime *selects* the entry model. This is the elegant resolution: both doctrines are true, in different regimes.

### PH-5 — "Forex locked" was a doctrinal choice, never an empirical one
The forex lock is beautiful doctrine (consciousness of nations) but: (a) currency ETF options chains (FXE/FXB/FXY) are extremely thin, so the L1b GEX signal for forex is proxy-of-a-proxy and unvalidated; (b) the decoded copy-machine rule sets $5K as minimum meaningful capital and current deployable trading capital is far below it; (c) every other decoded system in the archive (MTP, wheel, ATH, GEX confluence) is equities/futures/crypto-native. The instrument where STIS's best data lives (SPY/QQQ index options) is not the instrument STIS locked.
**Remedy: §4 instrument doctrine — forex remains the *doctrinal* home; SPY/QQQ/GLD become the *validation* instruments (where GEX data is thick and free); the lock is downgraded to a preference pending expectancy evidence per instrument.**

### PH-6 — Capital deployment bypassed the system's own gates
The $150 deployment (BTC/RKLB) executed while the PRD says "Phase 2 NOT STARTED — no live capital." Either the phase gates govern or they don't. The deployment wasn't wrong — it was *ungoverned*: it belongs to a different activity (investing) that the PRD never defined.
**Remedy: §3 — the Two-Stream split.** Stream A (Trading) and Stream B (Investing) get separate doctrines, separate gates, separate risk budgets. The $150 is retroactively chartered as Stream B Position 0.

### PH-7 — Intelligence has no expiry date
The "current live intelligence" is dated 2026-05-19 — seven weeks stale. The watch date (July 4 Mars-Uranus) has passed. The SpaceX IPO (June 12) has happened and the decoded September dump window is now *live* intelligence that nothing in the system is tracking. Stale data presented as current is worse than no data.
**Remedy: §10 — Intelligence Freshness Protocol (TTL stamps).**

### PH-8 — Source confidence conflates transcription fidelity with truth
D.R.D filed the trading decodes at Confidence A — correct for *transcription accuracy*, but every source is a YouTube creator with a funnel (Discord, $1,500/yr platform, classroom links). Their claimed results are unverified, survivorship-biased, and their incentive is audience, not alpha. The doctrine enters as presumed true per sovereign input posture — **and the market is the final validator regardless of source**. Truth-value in trading is only ever established by the expectancy ledger.
**Remedy: §8 evidence tiers — doctrine enters free, capital is earned. Position size is a function of validation tier, not source confidence.**

### PH-9 — Single point of failure: yfinance, and an unexamined GEX sign assumption
The entire L1b layer rests on free yfinance options data (delayed OI, occasionally wrong) with no fallback and no data-sanity check. Deeper: the GEX formula assumes dealers are long calls / short puts (the standard naive assumption). When dealer positioning inverts (heavy put *selling* environments), the HVL read flips sign and the regime call is exactly backward.
**Remedy: §11 — Data Integrity Protocol: sanity checks, fallback sources, sign-assumption caveat logged on every GEX read, and regime calls cross-confirmed by realized behavior (does price actually mean-revert/trend as the regime predicts? log it).**

### PH-10 — The system is too heavy to run, and the run-rate proves it
Steps 0–5 cost 30–45 minutes before a chart opens. Kill condition 5 (fluent in 30 minutes) is arguably already breached: the session cadence since v5 shipped is **4 sessions in 30 days**, then 18 days of silence. A daily system that runs four times a month is not a system — it is a ceremony.
**Remedy: §12 — three session modes (Pulse 5 min / Standard 15 min / Full 40 min) + one-command automation.**

### PH-11 — The coherence score weights are arbitrary and uncalibrated
The PMIB L5 coherence score blends Kp, DS, aspects, gamma, Vanna with invented weights. No one knows whether a "Grade A field day" actually correlates with better trade outcomes because there are no trade outcomes.
**Remedy: folds into §8 — the ledger logs the coherence score on every paper trade; weights get calibrated against results after 50+ samples, not before.**

### PH-12 — No adversarial layer
Nothing in STIS asks "who is on the other side of this trade and why are they smarter than me?" Every layer reads the field; no layer attacks the thesis. Institutional desks run a devil's-advocate pass on every position.
**Remedy: §6 — the Adversary Lens is now a mandatory perception in the Matrix (one sentence minimum per hypothesis: "the smart money taking the other side believes ___ because ___").**

---

## 2. PROJECT OVERVIEW (v6)

**Project Name:** Sovereign Trading Intelligence System (STIS)
**One-Sentence Description (v6):** A two-stream capital engagement architecture — a trading stream that must *earn* capital through documented expectancy, and an investing stream governed by decoded macro theses — reading the market through a nine-lens Perception Matrix and an engineered-time flow calendar, from the Observer position.
**Owner:** Morph
**Primary Home:** D.S.E | Co-owners: D.S.C, D.R.D, D.I.I, D.O.M, D.P.S.A, D.S.S
**Prime Directive of v6:** *No doctrine touches capital until the ledger says it has an edge. The market is the final validator of all doctrine, regardless of source.*

---

## 3. THE TWO STREAMS — TRADING vs INVESTING (NEW)

The audit's PH-6 revealed STIS was silently running two different games under one rulebook. v6 splits them formally.

| | **STREAM A — TRADING** | **STREAM B — INVESTING** |
|---|---|---|
| Time horizon | Minutes → weeks | Months → generational |
| Edge source | Flow mechanics, regime, time architecture | Decoded macro theses (D.R.D pipeline) |
| Validation | Expectancy ledger (§8) — statistical | Thesis integrity — D.R.D confidence + review dates |
| Risk unit | 0.5–2% per trade (skill_risk-management) | Position % of investable capital, thesis-sized |
| Capital gate | **PAPER ONLY** until Tier 2 validation (§8) | Active now — $150 deployed is Position 0 |
| Instruments | SPY/QQQ/GLD validation set → forex after per-instrument evidence | BTC (base), RKLB, research-gated alts, future wheel income layer |
| Governing files | This PRD + skill stack | `dse_blueprint_sovereign-capital-deployment-150_v1.md` + successors |
| Kill trigger | Ledger shows negative expectancy after 100 samples | Thesis invalidated by D.R.D re-decode |

### 3.1 STIS AS THE INVESTMENT ENGINE (amendment 2026-07-07)

STIS is formally chartered as the OS's **investment engine**, not only its trading system. Stream B is a first-class citizen: every capital deployment decision — trading, investing, crypto — routes through this PRD's laws (evidence tiers, D.R.D research gates, TTL-stamped intelligence, risk budgets). Because the entire system lives as readable doctrine + runnable tools inside Pandora, **any coding agent that enters the OS inherits the full skill stack** — Auset or any session agent can run the pulse, read the ledger, check the gates, and operate Stream B under the same laws Morph does. The system is the operator; agents are its hands.

### 3.2 CRYPTO STREAM (chartered 2026-07-07)

Crypto enters STIS as a Stream B asset class + a Stream A instrument candidate, under existing law:

| Aspect | Doctrine |
|---|---|
| **Base** | BTC always first (per capital blueprint). Alt deployment stays D.R.D-gated: use case + team + tokenomics + PROBABLE+ confidence. XDC / HBAR / TRX decodes still queued and still blocking the $20 research gate. |
| **Regime read** | `stis.py crypto` — daily BTC/ETH price vs 50d/200d MA regime + distance from 52-week high (ATH-zone flag = Playbook B territory). Wired into the daily pulse. |
| **Time Architecture** | CME BTC futures + Deribit monthly options expiry (last Friday) now in the flow calendar. Crypto trades 24/7 — weekend liquidity is thin and wicks lie; the construct-of-time edge applies doubly: crypto's calendar flows are inherited from TradFi settlement rhythms it doesn't structurally need, making them *purer* appointments. |
| **Stream A candidacy** | Crypto setups (e.g., decoded Crypto Edge–style momentum) enter at T0 like everything else: paper → ledger → tiers. No live crypto *trading* (as opposed to Stream B *stacking*) below T1. |
| **Custody law** | Self-custody after purchase (hardware wallet). Exchange balances are working capital only. Stablecoins are dollar-extension instruments, not savings. |
| **Data caveat** | yfinance BTC-USD/ETH-USD is spot-index quality — fine for regime reads, not for execution levels. Funding rates + open interest (free via exchange APIs) are the crypto-native Perception Matrix lenses — build queue #8. |

**Stream B live intelligence (as of 2026-07-07):**
- **Crypto field state (first pulse read, 2026-07-07):** BTC ~$63.7K, **−49% from 52w high, below 50d + 200d (BEAR regime)**; ETH ~$1,785, −63%. The BTC-base thesis is a decades-horizon doctrine and is unaffected, but the *entry field* is deeply drawn down — mechanically favorable for the $20–50/mo DCA ladder. Log every buy against this regime read so Stream B builds its own ledger.
- **SpaceX September window is now ACTIVE intelligence** — IPO happened June 12; the decoded lockup-waiver dump window opens at first earnings (~September 2026). Action: calendar entry + watch RKLB correlation (a SpaceX dump may drag the whole space sector — that is the *entry improvement* window for RKLB adds, not a reason to exit).
- The Wheel strategy remains **queued, not active** — requires ~$15–25K collateral to run on quality names; it activates at the capital tier where CSPs are coverable.
- Buy/Borrow/Die is the Stream B end-state doctrine — activates only after a six-figure liquid position exists.

---

## 4. INSTRUMENT DOCTRINE (REVISED)

Forex remains the doctrinal soul of the system (consciousness of nations, Ray signatures). But **validation happens where the data is thickest and free**:

| Tier | Instruments | Why |
|---|---|---|
| **Validation set** | SPY, QQQ, GLD | Deep options chains → real GEX. Free data. Overnight VP + footprint tools all built for these. Every decoded execution system was demonstrated on these. |
| **Doctrinal set** | EUR/USD, GBP/USD, USD/JPY, XAU/USD | Enter live rotation only after (a) Stream A Tier 2 validation on the validation set and (b) per-instrument evidence that the ETF GEX proxy actually predicts behavior (logged, ≥20 sessions per pair). |
| **Excluded until chartered** | Single stocks (except Stream B), 0DTE options buying, meme/pump vehicles | Edge unproven or structurally retail-adverse. |

The forex "lock" of v2 is downgraded to a **destination**. You do not validate a system on the instrument with the worst data.

---

## 5. THE REGIME ROUTER — ENTRY DOCTRINE RECONCILED (NEW)

Resolution of PH-4. Both decoded entry models are correct — in different regimes. The regime, not preference, selects the playbook:

```
                     ┌──────────────────────────────┐
                     │   REGIME CLASSIFICATION       │
                     │   GEX (gamma sign vs HVL)     │
                     │   + Markov state + IEC phase  │
                     └──────────────┬───────────────┘
                                    │
            ┌───────────────────────┴───────────────────────┐
            ▼                                               ▼
  POSITIVE GAMMA / SIDEWAYS                    NEGATIVE GAMMA / TRENDING
  (price pinned, mean-reverting)               (vol amplified, momentum)
            │                                               │
  PLAYBOOK A — LEVEL REVERSION                 PLAYBOOK B — BREAKOUT MOMENTUM
  • Fade moves INTO walls                      • ATH / range-high breakout entries
  • Enter at OB / FVG / VAH / VAL              • Buy strength, never the discount
  • GEX wall + VP node confluence              • IEC Phase 3–4 expansion alignment
  • Absorption + aggression trigger            • Breakout retest or go-with entry
  • Targets: HVL / opposite wall               • Targets: measured move / trail structure
  • Tight structural stops                     • ATR stops, pyramid per MTP doctrine
```

**Law:** In positive gamma you are paid to fade; in negative gamma fading is how accounts die (v5's own 2026-05-20 log already knew this: "no fade trades today"). The IEC/liquidity doctrine IS Playbook A. The ATH/O'Neill doctrine IS Playbook B. The contradiction was a missing router.

Grade A criterion 2 is amended: *"At a location the active playbook designates"* (wall/OB/VAL for A; breakout structure for B).

---

## 6. THE PERCEPTION MATRIX — NINE LENSES (NEW — the multi-perception edge)

The insider edge is not secret data. It is **reading the same moment through every participant's eyes simultaneously** — because each lens is *someone's forced behavior*, and forced behavior is the only thing in markets that is mechanical. Retail reads one lens (price). Institutions read several. STIS reads nine:

| # | Lens | Whose eyes | Data source (free) | STIS layer |
|---|---|---|---|---|
| 1 | **Dealer** | Market makers forced to hedge | gex_engine.py, OI walls, 0DTE weight | L1b |
| 2 | **Institutional positioning** | Funds already committed | COT weekly (CFTC), 13F quarterly | L3 |
| 3 | **Insider** | Officers/directors with information | SEC Form 4 clusters (openinsider) | L3 — NEW |
| 4 | **Retail crowd** | The Mutable Cross | AAII sentiment, put/call ratio, funding rates | L2 |
| 5 | **Algorithmic** | Systematic flows that must fire | Markov state, momentum/vol triggers, CTA level estimates | L1c |
| 6 | **Liquidity/Macro** | The plumbing itself | Fed net liquidity (WALCL − TGA − RRP), yields, DXY, basis swaps | L3 — NEW: net liquidity is the single most predictive macro series most retail never track |
| 7 | **Physical field** | The collective nervous system | Kp / solar wind (schumann_resonance.py) | L2 |
| 8 | **Cyclic time** | The field's clock | Declination, aspects, Rays, Crosses | L4 |
| 9 | **Adversary** | The smart money on the other side | Mandatory written sentence per hypothesis | ALL — NEW |

**Convergence protocol:** A hypothesis states which lenses agree, which disagree, and which are silent. **Lens count is not the edge — lens *independence* is.** Three genuinely independent confirming lenses beat six correlated ones. The PMIB coherence score is rebuilt as the Perception Convergence Score (§8 calibrates its weights from ledger outcomes, not from theory).

**The Adversary Lens is non-skippable:** every hypothesis logs one sentence — *"The disciplined trader taking the other side believes ___ because ___, and they are wrong because ___."* If the third blank cannot be filled, the trade is not taken.

---

## 7. TIME ARCHITECTURE — THE ENGINEERED-CALENDAR EDGE (NEW)

The sovereign overstanding: market time is a **man-made construct** — and precisely *because* it is constructed, it is exploitable. The construct forces real capital to move at arbitrary calendar boundaries. These flows are not predictions; they are **appointments**. This is R7 (Ceremonial Order) made mechanical — the highest and the lowest meet: the most esoteric principle in the stack cashes out as the most concrete edge in it.

### 7.1 The Three Clocks

| Clock | Nature | How STIS uses it |
|---|---|---|
| **Clock time** | The fiction — uniform, arbitrary | Only as the grid others are forced to obey |
| **Event time** | The reality — markets move in information/volume units, not minutes | Volume bars / range bars for entries; a 5-min bar at 9:35 ≠ a 5-min bar at 12:30 and must never be read as equal |
| **Cyclic time** | The field — declination, aspects, seasonal | L4, already built |

### 7.2 The Engineered Flow Calendar (mechanical appointments)

| Flow | When | Mechanism | Playbook |
|---|---|---|---|
| **0DTE gamma cycle** | Intraday, daily | Dealer hedging of same-day options concentrates pinning into the afternoon; morning = widest true range | Trade breakouts early session; expect pinning to walls after ~14:00 in positive gamma |
| **OPEX** | 3rd Friday monthly (+ quarterly "quad witching") | Gamma map collapses at expiry; pinned levels release | Pin-to-max-gamma into Friday close; Monday "unclenched" directional reset |
| **Month-end rebalance** | Last ~2 sessions | Pensions/target-date funds mechanically rebalance equity/bond ratios | After a big equity month, expect month-end supply (and vice versa) |
| **Quarter-end** | Mar/Jun/Sep/Dec ends | Rebalancing + window dressing + futures roll | Amplified month-end effect; avoid fresh positions in the chop |
| **Turn-of-month** | Last day → first 3 days | Payroll/401k inflows hit passively | Long-bias tailwind window (documented anomaly, decades of evidence) |
| **FOMC cycle** | 8×/year | Pre-FOMC drift (upward bias into announcement), post-FOMC regime resets | No new positions 24h before; the *reaction* is sacred-vs-reactive test #1 |
| **Session anatomy** | Daily | Open auction (9:30–10:00) sets range; lunch void (12:00–13:30); MOC imbalances (15:50–16:00) | Never judge a level in the lunch void; overnight VP (18:00–9:30) defines VAH/VAL per decoded doctrine |
| **Futures roll** | Quarterly, ~1 week before expiry | Volume migrates contracts; false volume signals | Suspend volume-based reads during roll |
| **Friday→Monday weekly reset** | Weekly | Weekly OPEX collapse + Monday repositioning + Monday Gold Box (IEC) | Already built — the Gold Box IS a time-architecture tool; v6 names the family it belongs to |

**Deliverable:** `dse_framework_time-architecture.md` (build queue §20) — the full calendar, auto-annotated into every PMIB: *"today's engineered flows: ___"*.

### 7.3 Time-Perception Sovereignty (L5 integration)

The retail trader experiences time as pressure (fear of missing, urgency to act — Mutable Cross time). The Observer holds all three clocks at once and **waits at the appointments**. Patience is not a virtue here; it is a *strategy*: the engineered calendar means edge windows are scheduled. Most hours of most days carry no edge — the sovereign act is standing flat inside them without discomfort.

---

## 8. THE VALIDATION LAW — EXPECTANCY LEDGER + EVIDENCE TIERS (NEW — governs everything)

### 8.1 The Law

> **Doctrine enters the OS free. Capital is earned.**
> Any source may contribute doctrine (sovereign input posture holds). But position size is a function of *validation tier*, never of source confidence, elegance, or conviction. The market is the only validator with authority over sizing.

### 8.2 The Expectancy Ledger

File: `D.S.E/trading/quant/dse_ledger_expectancy_master.md` (+ per-setup files). Every setup — paper or live — logs: date, playbook (A/B), instrument, regime state, lens convergence map, coherence score, entry/stop/target, outcome in R, and the dual-ledger esoteric fields (§9).

**Per setup, the ledger must answer at any moment:** samples (n), win %, avg win R, avg loss R, **expectancy in R**, max consecutive losses, and expectancy *after* spread/slippage estimate.

### 8.3 Evidence Tiers → Sizing Authority

| Tier | Requirement | Sizing authority |
|---|---|---|
| **T0 — Doctrine** | Decoded and filed | $0. Paper only. |
| **T1 — Signal** | n ≥ 30 paper, positive expectancy | Micro live (≤0.25% risk) — the "does live differ from paper" test |
| **T2 — Validated** | n ≥ 100 combined, positive expectancy net of costs, survives the 4-step validation (backtest → permutation → walk-forward → WF permutation) where automatable | Standard risk (1%, max 2% per skill_risk-management) |
| **T3 — Core** | T2 + two quarters live positive | Full doctrine status; eligible for automation (§20) |

**Demotion is automatic:** any T2+ setup whose rolling-50 expectancy goes negative drops one tier and returns to review.

### 8.4 Variance discipline (from the decoded math doctrine)
No setup is judged before n = 30; no setup is *trusted* before n = 100. The early equity curve is noise. Quitting a valid edge at n = 15 and doubling a false edge at n = 15 are the same error in opposite directions.

### 8.5 Volatility drag doctrine (portfolio law)
Two return streams with equal expectancy: the smoother one compounds more wealth — always. Therefore Stream A's goal is **multiple uncorrelated T2 setups at modest size**, never one setup at maximum size. This is why the risk cap is a law and not a suggestion.

---

## 9. ESOTERIC FALSIFICATION — THE DUAL LEDGER (NEW)

The esoteric layer is a core organ of STIS. Precisely because it matters, it gets what every other layer gets: a track record.

**Protocol:** Every hypothesis logs two verdicts *before* outcome:
1. **Orthodox verdict** — L1/L1b/L1c/L2/L3 only: direction + conviction (1–5)
2. **Dual verdict** — after L4/L5 read: final direction + conviction (1–5)

The ledger then tracks three populations: (a) both agree, (b) esoteric modified sizing/timing, (c) esoteric overrode orthodox. After 50+ samples the question "does the esoteric layer add expectancy?" has a **number** instead of a feeling.

- If population (c) outperforms → the esoteric layer has earned override authority. Document which reads (Ray? cycle phase? aspects?) carry the edge.
- If it underperforms → the layer retains its L5 role (Observer discipline, state management — which needs no statistical defense) while its *directional* authority is suspended.
- Either outcome strengthens the system. There is no failure — only transmutation, **with a sample size**.

---

## 10. INTELLIGENCE FRESHNESS PROTOCOL (NEW)

Every intelligence artifact gets a TTL stamp in its header: `**Valid until:** YYYY-MM-DD — then re-verify or demote to archive.`

| Intelligence type | TTL |
|---|---|
| GEX session map | 1 trading day |
| COT read | 7 days |
| Macro field summary (yields, DXY, flows) | 14 days |
| Cycle phase / dominant Ray call | 30 days or next major ingress |
| Structural theses (tokenization, SpaceX window) | Event-dated with named triggers |

The PMIB opens with a staleness check: any expired artifact is flagged before the session proceeds. **A stale number stated confidently is the most dangerous object in the system.**

Immediate refresh required (all expired as of 2026-07-07): current-field summary (dated 05-19), active pairs table, cycle phase call ("July window" has arrived — is this the Crisis the system forecast? That is itself a falsification data point for L4, log it), SpaceX September window activation.

---

## 11. DATA INTEGRITY PROTOCOL (NEW)

1. **yfinance sanity gate:** gex_engine output cross-checked weekly against a free independent GEX source; OI staleness noted on every read (yfinance OI updates overnight — intraday reads carry yesterday's OI).
2. **GEX sign humility:** every GEX read carries the caveat line: *"assumes standard dealer positioning (long calls/short puts); if price behavior contradicts the regime call for 2+ sessions, assume inversion and flip the read."* Realized-behavior check: the ledger logs whether each day's regime call *actually manifested* (did positive gamma days actually mean-revert?). Regime accuracy % is a tracked number.
3. **Fallback stack:** yfinance → CBOE delayed chains → manual OI read from broker platform. No single point of failure.
4. **Thin-chain rule (already a kill condition, now operational):** FXE/FXB/FXY GEX levels are zones ±0.5%, never lines, and carry half the evidentiary weight of SPY/QQQ/GLD levels.

---

## 12. SESSION COMPRESSION — THREE MODES (REVISED PROTOCOL)

The 7-step sequence survives but is no longer all-or-nothing. **A system run daily at 5 minutes beats a system run monthly at 45.**

| Mode | Time | Contents | When |
|---|---|---|---|
| **PULSE** | 5 min | `python3 tools/stis.py brief` (one command: regime + Kp + DS + engineered-flows-today + staleness flags) + Observer breath-check. No chart, no trade. | Every market day, minimum. Keeps the field-read muscle and the data archive alive. |
| **STANDARD** | 15 min | Pulse + full PMIB + watchlist scan + Grade A check on anything forming. Paper entries allowed. | Any day with intent to engage. |
| **FULL** | 40 min | Standard + full Observer calibration + Sun/Rising/Moon triad + dual-layer chart reads + weekly esoteric/macro skills. | Sundays + any day a live trade is on. |

**Automation mandate (build queue):** `stis.py brief` is upgraded to run GEX (all symbols, auto-save), PMIB, staleness check, and today's Time Architecture flows in one command with one screen of output. The archive then grows automatically — the walk-forward dataset builds itself even on Pulse days. **This closes PH-2's data starvation permanently: 5 minutes/day = 20 sessions/month.**

---

## 13. RISK DOCTRINE (CONFIRMED + EXTENDED)

`skill_risk-management.md` is confirmed sound and remains law: **default 1%, max 2%, never more**, convergence-scaled, event-reduced. v6 adds:

**Risk-of-ruin table (why the law is the law):**

| Risk/trade | Approx. trades to −50% on a losing streak | Verdict |
|---|---|---|
| 1% | ~69 consecutive losses | Statistical armor |
| 2% | ~34 | Acceptable ceiling |
| 5% | ~14 | Gambling |
| 10% | ~7 | One bad week = account death |

**Additions:**
- Daily stop: −3% equity → session over, no exceptions, log and close the terminal.
- Weekly stop: −5% → flat until Sunday FULL session review.
- Tier-linked: T1 setups risk ≤0.25% regardless of convergence score.
- Correlation rule: multiple open positions sharing a lens driver (e.g., all short-USD) count as one position for risk purposes.

---

## 14. CAPITAL DOCTRINE — THE COPY MACHINE LAW (NEW)

Decoded and now chartered: *trading copies the capital you bring; it does not print capital from nothing.*

- **$5,000** is the minimum for Stream A live deployment beyond micro-tier (decoded futures threshold).
- Capital formation is **not Stream A's job** — it is D.S.E's business pipeline's job (content-to-client, Auset-era agentic services). Trading profits at small scale are a rounding error next to one client engagement; treating trading as the income engine before ~$25K is the classic retail death spiral. STIS's job during capital formation: **build the validated ledger** so that when capital arrives, it lands on a T2/T3 system instead of a hope.
- Stream B continues stacking independently ($20–50/mo BTC per existing blueprint).
- The Mac Mini M4 / hardware Phase 1 monetization plan and Stream A funding draw from the same D.S.E revenue source — sequence them consciously in D.S.C.

---

## 15. DECISION ARCHITECTURE (v6)

```
STEP 0 — OBSERVER GATE (1 min — all modes)
STEP 1 — MODE SELECT: Pulse / Standard / Full
STEP 2 — ONE COMMAND: python3 tools/stis.py brief
          → regime (GEX+Markov) → session posture
          → staleness flags → refresh anything expired before proceeding
          → today's engineered flows (Time Architecture)
STEP 3 — [Standard+] PMIB full + watchlist per playbook (Router §5 decides
          which entry model is legal today)
STEP 4 — [if setup forming] PERCEPTION MATRIX pass:
          lens convergence map + MANDATORY Adversary sentence
STEP 5 — DUAL LEDGER: orthodox verdict logged BEFORE esoteric read;
          dual verdict logged after
STEP 6 — GRADE A FILTER v3 (criterion 2 amended per Router) + risk sizing
          per evidence tier — paper unless tier authorizes live
STEP 7 — POST-SESSION: ledger entry (auto-templated), observer residue
          check, TTL refresh of anything touched
```

---

## 16. GRADE A FILTER — v3 AMENDMENTS

Carried from v5 (9 criteria) with three changes:
1. **Criterion 2 rewritten:** "At a location the *active playbook* designates" (Router-aware).
2. **Criterion 10 added — Adversary named:** the counterparty sentence is written and non-trivial.
3. **Criterion 11 added — Time window:** the entry does not sit inside a known dead/hostile window (lunch void, pre-FOMC 24h, futures roll volume distortion) unless the setup specifically trades that window.

A++ now requires 1–7 + 8 + 9 + 10 + 11.

---

## 17. PHASED PLAN (v6 — REBASED WITH MEASURABLE GATES)

### PHASE 1 — NIGREDO: COMPLETE (structure built)
### PHASE 1.5 — THE FORGE (NEW — current phase, 30 days)
```
□ stis.py brief upgraded to one-command full pulse (build queue #1)
□ Expectancy ledger files created + templated
□ Time Architecture framework written
□ Perception Matrix lens sources wired (COT, Form 4, net liquidity added to PMIB)
□ Intelligence refresh: current-field, pairs table, cycle phase, SpaceX Sept window
□ 20 consecutive market days with ≥ Pulse mode run (the streak IS the gate)
```
### PHASE 2 — ALBEDO (paper trading)
v5's 9 checks carried, plus: ≥30 paper trades ledgered across both playbooks, dual-ledger populated, regime-accuracy % being tracked.
### PHASE 3 — CITRINITAS: first setup reaches T1 → micro live.
### PHASE 4 — RUBEDO: first setup reaches T2 + capital gate ($5K) met → standard live.
### PHASE 5 — AUTOMATION: any T3 setup → TradingView alert → execution pipeline (QuantConnect path per decode). Only T3 earns automation — automating an unvalidated system just loses money faster.

---

## 18. SUCCESS CRITERIA (v6 — ALL NUMERIC)

1. 20-market-day Pulse streak achieved (Forge gate).
2. GEX archive ≥ 60 sessions (walk-forward viable).
3. Expectancy ledger: ≥ 30 paper trades with computed expectancy per setup.
4. Dual ledger: orthodox vs dual verdict differential computed at n ≥ 50.
5. Regime-call accuracy tracked and ≥ 60% before any live trade trusts the regime layer.
6. Zero trades taken outside the active playbook's entry doctrine.
7. Zero live capital deployed below its evidence tier.
8. Every intelligence artifact in active use carries an unexpired TTL.
9. Session run-rate ≥ 15 of any 20 consecutive market days (system is *lived*, not admired).
10. Stream B: September SpaceX window monitored with a written pre-decision (add/hold/hedge RKLB) filed *before* the earnings date.

---

## 19. KILL CONDITIONS (v5 SET CARRIED + v6 ADDITIONS)

All seven v5 kill conditions remain. Added:
- If the ledger is not being filled, the system is dead regardless of how good the documents are — stop building layers, run Pulse mode for 20 days, or formally archive the project. **No further doctrine ingestion (new videos, new decodes) until the Forge gate is passed** — input without validation is how this system became a library instead of an engine.
- If any setup is sized above its evidence tier even once → full stop, 7-day flat period, written residue analysis.
- If the esoteric dual-ledger shows persistent negative differential at n ≥ 100 and the layer's directional authority is not suspended → the Mirror Doctrine is being violated (the OS is reflecting wish, not will).

---

## 20. BUILD QUEUE (D.I.I / D.S.C — sequenced)

| # | Build | Closes | Effort |
|---|---|---|---|
| 1 | ✅ **DONE 2026-07-07** — `stis.py pulse` one-command upgrade: TTL check + Time Architecture (`tools/time_architecture.py`) + crypto pulse + GEX all-symbols auto-save + PMIB brief + Forge streak tracker. Fixed en route: Kp falsy-zero parse bug, macOS SSL certs, ephem dependency. | PH-2, PH-7, PH-10 | Shipped |
| 2 | Expectancy ledger template + `stis.py ledger` summary command | PH-1 | Small |
| 3 | `dse_framework_time-architecture.md` + flow calendar module | §7 | Medium |
| 4 | PMIB lens expansion: COT auto-pull, net liquidity (FRED), Form 4 watch | §6 | Medium |
| 5 | Validation harness (permutation + walk-forward on ledger/bar data) | PH-2 | Medium — needed at Phase 2 exit, not before |
| 6 | GEX sanity cross-check script + fallback | PH-9 | Small |
| 7 | Grade A v3 + dual-ledger fields in trade template | PH-3, §16 | Trivial |
| 8 | Crypto-native lenses: funding rates + OI via free exchange APIs into pulse | §3.2, §6 | Small |
| 9 | ✅ **DONE 2026-07-07** — L4 astro validation harness (`tools/astro_backtest.py`): DS vs market turns, permutation-tested. **Result: NO EDGE (4 tests, SPY+GLD, 10y, incl. extremes claim) — DS timing authority suspended per §9.** Record: `quant/dse_ledger_L4-validation_2026-07-07.md`. Re-tests must be pre-registered. | PH-3, §9 | Shipped |
| 10 | Power Stack lenses (`dse_framework_power-stack.md`): QRA + index rebalance + buyback blackout + lockup calendar into Time Architecture; congressional/Form 4 sweep; Net Liquidity + MOVE into PMIB; Auset disclosure schedule | §6, §7 | Medium |

---

## 21. OPERATING DOCTRINE (v6 — ONE PAGE)

> The market is the aggregate internal state of everyone participating in it — read through nine pairs of eyes at once, because each lens is someone's forced behavior, and forced behavior is the only mechanical truth in the field.
> Time in markets is a construct — and because it is constructed, its boundaries force real capital to move at scheduled appointments. The Sovereign does not predict; the Sovereign keeps the appointments.
> Positive gamma: fade to the walls. Negative gamma: ride the breakout. The regime chooses the playbook; preference never does.
> Doctrine enters free. Capital is earned. The ledger — not the source, not the elegance, not the conviction — decides what gets sized.
> The esoteric layer is an organ, not an ornament: it logs its verdicts before the outcome and earns its authority in numbers, like every other layer.
> Every intelligence artifact expires. A stale number stated confidently is the most dangerous object in the system.
> One percent risk is not caution — it is the mathematical precondition for surviving long enough for expectancy to reveal itself.
> Trading copies the capital you bring. The business builds the capital; the ledger builds the system; they meet at five thousand dollars.
> Five minutes every day beats forty-five minutes four times a month. The streak is the system.
> The Adversary sentence is written before every trade: who is on the other side, and why exactly are they wrong?
> Every trade dissolves back into the field. No residue. Calibration resumes.
> This is STIS.

---

*dsc_prd_sovereign-trading-intelligence_v6.md | Pandora OS | D.S.C*
*Status: ACTIVE — Phase 1.5 THE FORGE. Audit complete, twelve plot holes chartered and remedied on paper; remedies become real when the Forge gate (20-day streak + ledger live) is passed.*
*Prior: v1→v2 (stack) → v3 (Bailey) → v4 (IEC) → v5 (GEX/quant) → v6 (validation, convergence, time architecture)*

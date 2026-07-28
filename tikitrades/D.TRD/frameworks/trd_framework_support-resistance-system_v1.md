# TRD FRAMEWORK — Support/Resistance System

## v1 — REFINED: distilled from parent Pandora STIS + Tiki's own verified FXIFY trade history

**Status:** Active reference for Stage 2 daily sessions. Two items in the linked profile (`_config/trd_config_tiki-profile.md`) are still flagged for Tiki's direct confirmation — check those before treating a session as fully cleared.

**Scope:** Two instruments only — **XAU/USD (Gold)** and **GBP/JPY** — on the FXIFY 200K One-Phase account. Not a general-purpose S/R system; every rule below is sized and calibrated to this specific account and this specific pair of instruments.

---

## THE ONE-SENTENCE VERSION

**Trade the edges of the range, never the middle, take at most two shots a day, and stop completely the moment one of them misses.** Every rule below exists to enforce that sentence — the level-reading logic was never the leak; the behavior around it was (see PROVEN FAILURE MODES).

---

## 1. LEVEL IDENTIFICATION — priority order

Not all levels are equal. Read them in this order; higher layers set context for lower ones.

```text
LAYER 1 — STRUCTURAL BIAS (top-down cascade, highest timeframe wins)
  6-Month candle close → Monthly → Weekly → Daily → 1H/15M
  No intraday entry without HTF alignment. A setup without HTF confirmation is not a setup.
  Current read (gold, week of Jul 27): long-term bullish, medium-term corrective —
  a "buy-the-dip" market, but only at the deep end of the range, never in the middle.

LAYER 2 — THE RANGE / BOX
  Mark range ceiling (weekly supply) and range floor (weekly demand) first.
  Gold example (Jul 27 week): ceiling 4,200 / weak-high supply 4,120–4,150 /
  pivot 4,075–4,090 / minor support 4,040–4,000 / strong-low demand 3,960–3,950.
  RULE OF THE BOX: money is made fading the edges, lost in the middle.
  If price is in the middle third of the range → there is no trade. Sit.

LAYER 3 — POC TREND FILTER (session bias, not entry)
  Price above prior session POC (point of control) → long bias.
  Price below prior session POC → short bias.
  Within ~5 ticks of POC → neutral, wait for resolution.
  Session hierarchy: Asia POC → London bias. London POC → NY bias. Prior-day POC → full-day bias.

LAYER 4 — POWER CLUSTERS (the actual A++ entry zones)
  A level counts most when multiple layers stack within a tight band:
    prior day/week high-low (PDH/PDL, PWH/PWL) + value area high/low (VAH/VAL) +
    POC + a liquidity pool (equal highs/lows, round number) all within ~10 pips/points.
  Power cluster = trade it with full planned size. Isolated level = downsize or skip.

LAYER 5 — LIQUIDITY POOLS (why the level will actually get touched)
  Equal highs/lows, round numbers, PDH/PDL, session highs/lows are not "resistance" —
  they are where retail stops sit, and therefore where institutions have a reason to
  send price. A clean level is not enough; the level must have manipulation behavior:
  wick sweeps through it, then price CLOSES back through → sweep confirmed, trade the rejection.
  A level that price just stalls at without sweeping through is a weaker signal.

LAYER 6 — VOLUME GAP ZONES (targets and stop-placement guardrails, not entries)
  Zero-volume price zones are vacuum areas — price moves through them fast.
  Never place a stop inside a gap zone (it will be blown through, not held).
  Use gaps as target projections: once price enters one, the next high-volume
  cluster beyond it is the likely destination.
```

---

## 2. ENTRY CRITERIA — an A+ setup is ONLY

**Source:** this is Tiki's actual, currently-graded methodology — KimG (The Fx Diva, structure model, 26 Oct 2025 session) defines the WHERE, Nawaf's EMA baseline model defines the WHEN. Extracted from `FXIFY Trading/fxify-200k-gold-gj-trading-plan.md` and confirmed as the live grading standard in the daily briefings (e.g. `Briefing 2026-07-23.md`, `Briefing 2026-07-24.md` §8.5) and `Trade Journal.md`. This supersedes the more generic edge/sweep language previously in this section — that language is still correct as background (it's what Layers 1–6 above describe), but the checklist below is the literal mechanical test a setup is graded against before entry.

**Indicators loaded on every timeframe:** 9 EMA (red), 18 EMA (blue), 50 EMA, 50 SMA. The 50 EMA + 50 SMA together are **"the baseline."**

### KimG structure model — the WHERE
- **Top-down bias:** set structure on the HTF (Daily/4H) first — mark external (swing) structure, then drop to internal (LTF) structure to find the entry. (This is Layer 1's top-down cascade, applied.)
- **Only trade after a structure shift:** wait for a BOS / market-structure shift in the trade direction. A shift inside the HTF zone is the cue to start hunting an entry — not before.
- **Unmitigated zones only:** enter from an unmitigated demand zone (buys) or supply zone/order block (sells). If price already tapped the zone once, it's mitigated — lower quality, skip or downgrade.
- **Premium/discount (fib):** buy in discount, sell in premium — the 50% / 61.8% / 78.6% retracement of the leg. 38.2–50% are shallow entries; 61.8–78.6% are the deeper, higher-quality discount/premium.
- **Liquidity = the target:** mark the Asian session high/low and London high/low. These are what price is reaching for — the "why" behind the setup and the profit target.
- **Confirmation, not raw imbalance:** never trade the naked gap/imbalance. Wait for price to pull into the zone → LTF structure shift → candle close confirming, then act.
- **Why this works even at a 33% win rate (her own stats, 6 trades, XAUUSD):** profit factor 1.27 on a 33% win rate only because avg win (~$2,383) ≈ **1.9× avg loss** (~$1,249). The edge is asymmetric R:R, not hit rate — see Section 4.

### Nawaf timing model — the WHEN (mechanical checklist, say it out loud before every entry)

- [ ] **Step 0 — Context filter:** inside the London or NY killzone (or the overlap) — no dead-zone entries. No entry within 5 minutes of a flagged high-impact USD/GBP/JPY release. HTF structure has shifted (BOS) in the trade direction, with a fresh unmitigated zone and a clear liquidity target.
- [ ] **Step 1 — HTF baseline touch (H1/H2):** price has physically touched its 50 EMA/50 SMA on the higher timeframe. No HTF touch = stop here, no setup.
- [ ] **Step 2 — LTF baseline pullback (M15/M30):** the lower timeframe has *also* touched its own 50 EMA/50 SMA. Both HTF and LTF must touch — extended price with no pullback is a no.
- [ ] **Step 3 — Candle maturity:** a completed candle closes with its **full body** beyond the 50 EMA in the trade direction. A wick piercing the line does not count.
- [ ] **Step 4 — EMA momentum alignment:** 9 EMA crosses 18 EMA in the trade direction, and both sit on the correct side of the 50 EMA (above for buys, below for sells).
- [ ] **Step 5 — The wick (trigger):** the signal candle makes a retracement wick against the trade direction, then flips back into the trend. Enter on the flip, not before.

**If any single step is unticked → not A+ → no trade.** This is the whole point of a mechanical checklist: it removes the "keep clicking" impulse the trade journal keeps flagging. Chart-dependent steps that can't be verified without a live screenshot are graded ❓, not assumed — see the daily briefings for the actual grading format.

### Instrument-specific gates (unchanged from Section 3/5 risk caps)

**Gold:** stop < 30 points. Price came *to* the limit — not chased.

**GBP/JPY:** stop < 80 pips. **No** high-impact JP/UK release within 2 hours. **No** live BoJ/MoF intervention chatter. Limit-filled, not chased. GJ is **permission-based, not default** — it needs every gate to line up, not most.

**Never trade a CHoCH (change of character) as if it were a BOS.** CHoCH = watch only. BOS on the relevant or higher timeframe = the structure has actually shifted; that's what makes a reversal setup valid.

---

## 3. STOP PLACEMENT

- Every position gets a stop attached **at entry**. No stop = no send. No exceptions — the single largest loss in the account's history (−$932, Jul 16) was 71% caused by one position left naked.
- Stop sits beyond the invalidation point of the structure (past the order block / sweep wick), never inside a volume gap zone.
- Hard ceilings, not targets: **gold stop > 30pt → cut size or skip. GJ stop > 80pip → cut size or skip.**
- Never widen a stop mid-trade to avoid being right about being wrong.

---

## 4. TARGET / EXIT LOGIC

**TP1 = 1R** (same distance as entry-to-stop, measured in profit). At TP1:

- Close roughly half the position (0.17 of 0.33 gold lots / 1.00 of 2.00 GJ lots).
- Move the stop on the remaining runner to **exact entry price** — not a tick better, not a tick worse. That is breakeven. From this point the trade cannot become a loss.

**Managing the runner past TP1** — read three things at every subsequent target: momentum (accelerating or fading), the candle (pushing through with strong bodies, or wicking off), the level (is there S/R right at the target).

- Strong push through with no wicks → trail the runner behind the new higher-low (long) / lower-high (short).
- Fading momentum + rejection wicks into the target → take profit early, before the level.
- A wall (opposing S/R) sits just before the planned target → take it at the wall, don't wait for the exact number.
- **Default when in doubt: don't touch the target.** It was set calmly before the trade; don't move it because the trade is going well.

**Target selection uses Layer 6 (volume gap zones) as projection**: if price is running through a gap, the next high-volume cluster past the gap is the realistic destination — not the gap's midpoint.

**The target itself = KimG's liquidity draw** (Section 2): the Asian/London session high or low, the opposing order block, or the next structure level. Because the edge KimG's own data shows is asymmetric R:R rather than a high hit rate (33% win rate, profit factor 1.27, because avg win ≈ 1.9× avg loss), size the first real target for **at least ~1.9× the risk** whenever the liquidity draw allows it — don't take a 1:1 target just because it's there if the actual draw is further out. Scale out across 1–3 TPs; let the runner reach the liquidity pool rather than an arbitrary round number.

---

## 5. POSITION SIZING FORMULA

Tied directly to `_config/trd_config_tiki-profile.md` — standard size, not a ceiling to grow from:

| Instrument | Standard size | $ risk at max stop | % of ~$195K account |
|---|---|---|---|
| Gold (XAU/USD) | 0.33 lots | ~$990 at 30pt stop | ~0.51% |
| GBP/JPY | 2.00 lots | ~$987 at 80pip stop | ~0.51% |

- **These are the sizes — not a floor.** The one documented instance of doubling size (0.66 gold, Jul 23) happened to win, which is the dangerous kind of reinforcement; the same double-size on a loser turns a normal day into a near-daily-breach event.
- Before sizing any trade, check the daily-loss-room and drawdown-room figures in `FXIFY Trading/FXIFY-Risk-Tracker.md`. If Status reads STOP or CAUTION, **no new risk that day** — this isn't a framework rule, it's the prop firm's actual account-ending rule.
- Never increase size to recover a loss. Ever.

---

## 6. THE BEHAVIORAL LAYER — PROVEN FAILURE MODES (read this before every session)

This is not boilerplate. It's the account's own 10-day track record (Jul 2–17): 42 trades, 35.7% win rate, **profit factor 0.66 as executed** — the system loses ~34¢ per $1 risked in practice, despite the setup logic itself testing out fine on the days it was actually followed (Jul 23: one A+ short, textbook management, +$3,147).

**The three failure patterns** (two verified in the loss data, one flagged by Tiki herself as a blind spot before it shows up in the data):

1. **Revenge re-entry** — re-entering seconds after a stop, in the same direction, without a new setup. (Jul 17: cost $432 → became part of a $1,853 day.)
2. **Averaging in via simultaneous positions** — opening a second same-instrument position while the first is still open, instead of waiting for it to resolve. (Jul 15, Jul 17: the exact same signature both times.)
3. **Treating confirming news as a green light.** A supportive headline after entry is not a reason to add size or chase — the decision was already made calmly when the limit was set. Not yet in the loss data, but named as a live risk in the source plan; watch for it the same way as the first two.

**The fix is 100% behavioral, not a setup or sizing fix:**

- After ANY loss → platform closes for the session. This single rule alone would have capped the worst logged day at −$432 instead of −$1,853.
- One open position at a time, full stop.
- Max 2 trades per day, no exceptions for "how obvious" the next one looks.
- **Gold and GJ are one correlated bet, not two.** If both set up in the same session, pick one — don't treat "diversified across two instruments" as a reason to take both.
- **Say the Nawaf checklist out loud before every entry** (Section 2) — "HTF touched 50? LTF touched 50? Body close past 50? 9/18 stacked + wick-flip?" A setup that can't be stated this concretely in one sentence isn't A+, full stop.

**The KPI Scorecard — grade every session day, independent of P&L.** A day is GREEN only if all three are true:

- ☐ Took 2 trades or fewer
- ☐ Never held two positions at once
- ☐ Did not re-enter after a stop

A green day can still lose money — that's fine, and expected some of the time. The target is 5 green days out of 5 in a week, not a dollar figure; win the boxes and the profit factor recovers on its own (this account's Jul 23 session — one A+ trade, all three boxes green, +$3,147 — is the proof). **Grade the behavior, not the P&L, in the daily journal** (`logs/trd_log_trades_[YYYY-MM].md`) using these three boxes explicitly.

---

## 7. RECORDED DISPOSITIONS (D.R.D forex-playlist brief, 2026-07-26)

D.R.D reviewed an external forex-trading playlist against this framework (`D.R.D/briefs/drd_brief_trd_forex-trading-playlist_deployed.md`). Its core methodology matched what's already in Layers 1, 2, 5, and 6 above — no action needed there. Two contradictions required an explicit written decision before this file could be edited; both are now resolved, confirmed by Tiki directly on 2026-07-26:

1. **Stop-loss vs. buy-stop/hedge — hard stop-loss stands; the alternative was considered and rejected.** One source in the playlist taught a buy-stop/hedge in place of a hard stop-loss. Section 3's "no stop = no send" rule is unchanged and remains non-negotiable — the account's single worst loss (−$932, Jul 16) was 71% caused by exactly the kind of naked/hedged position this technique would reintroduce. It's mechanically the same shape as the account's #1 documented failure mode (two open positions instead of one, at the exact moment discipline matters most). The mechanics are kept on record in Section 8 below as a decision log — **not as an open option.**
2. **35.7% win rate — read as a behavioral leak, not a methodology gap.** Three playlist sources claimed 80–90% win rates on adjacent setups (unaudited, Tier 4-5 marketing — not comparable). Tiki's own audited number is 35.7% / 0.66 profit factor. **Confirmed:** this is attributed to the documented behavioral failures in Section 6 (revenge re-entry, simultaneous-position averaging), not a flaw in the A+ setup criteria themselves — supported by the Jul 23 session, where the setup logic was followed cleanly and returned +$3,147 in one trade. No change to Sections 1–2's entry criteria as a result.

Two proposed refinements from the same playlist (quarter levels / 2-week order blocks as a Layer 2 sub-level; extended Fibonacci confluence past 61.8% as a Layer 4 check) are **not yet adopted** — they require a real backtest against Tiki's own Gold/GBP-JPY data before entering this framework.

---

## 8. DECISION LOG — BUY-STOP/HEDGE TECHNIQUE (considered and rejected)

**Status: considered and rejected, 2026-07-26. Kept on file as a record of the decision, not as an open option. Section 3's hard stop-loss rule governs all live trades — full stop, no pending re-evaluation attached to this section.**

**Source:** D.R.D forex-playlist research, video 10 ("Morph 1 on 1" — 1-on-1 mentor coaching), mentor's own habitual practice. Not corroborated by any other source in the reviewed playlist; videos 8 and 9 in the same batch both use conventional hard stop-losses instead.

**The mechanics, in the mentor's own words:** *"Where you would put your stop loss, I put a buy stop... it gives you a chance to correct a mistake if you made a mistake."* A stop-loss closes the trade and realizes a defined loss. A buy-stop/hedge instead opens an **equal-and-opposite position at the same size**, at the price level where the stop would have gone — so instead of exiting, the account ends up flat net exposure (long + short of the same size), holding both legs open. The loss is locked at that level rather than realized, and the trader manages the two open legs afterward, hoping to close one favorably rather than eating the stop-out immediately.

**Why it was rejected:**
- It is functionally the same shape as the naked/simultaneous-position pattern already identified as this account's #1 documented failure mode (Section 6) — two open positions instead of one, at the exact moment discipline matters most.
- It was taught as one mentor's personal habit, not as a backtested or audited technique — no downside data was shown for it anywhere in the source material.
- It defers realizing a loss rather than reducing risk — the same equity impact as a stop-out, but with 2x the margin tied up and an added discretionary decision point (when/how to unwind the hedge) sitting exactly where this account's discipline has already failed three times.

**Disposition is final as of 2026-07-26.** Any chart situation that would call for a buy-stop/hedge calls for the Section 3 hard stop instead — no exceptions, no pending re-evaluation.

---

*Do not use this framework to place a live trade until `_config/trd_config_tiki-profile.md` is fully confirmed (done, 2026-07-26). Section 8 is a decision record only — the buy-stop/hedge technique is rejected, not held open.*

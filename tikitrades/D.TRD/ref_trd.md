# D.TRD REF CARD — Trading
## Read this before any D.TRD session.

**PURPOSE:** Tiki's day-trading operation — analysis, strategy execution, and trade journaling, run by any agent from this folder alone.

## ACTIVE STATE
| Item | Status | Next Action |
|------|--------|-------------|
| Tiki trading profile | **Complete** — confirmed by Tiki 2026-07-26 | None — Stage 1 closed out |
| Support/Resistance strategy | Refined v1 — entry criteria rebuilt around the actual live KimG/Nawaf methodology, plus KPI scorecard, tie-breaker rule, and 3rd behavioral trap | Live-test against Stage 2 sessions |
| D.R.D forex playlist brief | Dispositioned and closed (2026-07-26) | Quarter levels + extended Fib zone held pending a real backtest before live use. Buy-stop/hedge technique considered and **rejected outright** (Section 8 — decision record, not an open option) |
| Trade log | Empty | Log every trade in `logs/trd_log_trades_[YYYY-MM].md` |

## QUICK REFS
- Strategy: `frameworks/trd_framework_support-resistance-system_v1.md`
- Profile/config: `_config/trd_config_tiki-profile.md`
- Active log: `logs/trd_log_trades_2026-07.md`
- Skills: `skills/` (loaded per workflow stage — see table below)

Last updated: 2026-07-26 (profile confirmed; strategy refined; D.R.D brief dispositioned; KimG/Nawaf methodology + 4 enhancements incorporated)

**DONE (2026-07-26):**
- File-system skeleton created — mirrors Pandora's L0→L1→L2→L3 pattern, scoped to Tiki, starting with Trading only.
- Tiki trading profile filled from her actual FXIFY Trading files (Master Plan, Risk Tracker, Trade Journal, Weekly Plans), then confirmed directly by Tiki: London+NY overlap is her trading window; 0.25–0.5% is the real risk-per-trade rule (the risk tracker's stale "2.0%" figure was corrected to match, in both `_config/trd_config_tiki-profile.md` and `FXIFY Trading/FXIFY-Risk-Tracker.md`).
- Support/Resistance framework refined past skeleton: distilled the 5 STIS source-layer skills plus liquidity-engineering and market-structure, fused with FXIFY's own proven A+ setup rules, hard rules, sizing, and trade management. Added a behavioral-layer section naming the two proven failure modes (revenge re-entry, simultaneous-position averaging) from her own 10-day track record (42 trades, 35.7% win rate, profit factor 0.66 as executed).
- D.R.D's forex-playlist brief reviewed and dispositioned: hard stop-loss rule kept as the live-trading standard; 35.7% win rate confirmed as a behavioral leak, not a methodology gap. Both recorded in Section 7 of the framework file. The buy-stop/hedge technique was evaluated on its merits (functionally the same shape as the account's #1 documented failure mode, defers rather than reduces risk) and **rejected outright** — kept in a new Section 8 purely as a decision record, not as an open option or pending item.

- Section 2 (entry criteria) rebuilt around Tiki's actual live-graded methodology — KimG's structure model (WHERE: top-down bias, unmitigated zones, premium/discount fib, liquidity-pool target) + Nawaf's 5-step EMA baseline timing checklist (WHEN: HTF touch → LTF touch → body close → EMA stack → wick-flip) — sourced from `FXIFY Trading/fxify-200k-gold-gj-trading-plan.md` and confirmed against the daily briefings' §8.5 grading format and the trade journal. This is more precise than the original generic edge/sweep language and is now the literal pre-entry test.
- Four enhancements added: (1) the exact 3-box KPI Scorecard in Section 6, replacing the vague "grade the behavior" instruction; (2) the Nawaf checklist itself now serves as the pre-trade checklist gate; (3) a tie-breaker rule — Gold + GJ is one correlated bet, pick one per session; (4) a third named behavioral trap — treating confirming news as a green light to add/chase.
- Section 4 (target logic) updated with KimG's asymmetric-R:R target principle (~1.9× risk on the liquidity draw) alongside the existing TP1/breakeven mechanic.
- `wf_stage-2_session.md` gained the full Sunday-prep / daily-routine / Friday-review operating cadence (previously undocumented — the framework said *what* makes a trade valid but not *when* to look).
- `skills/skill_support-resistance-reading.md` flipped from "placeholder, not operational" to active, now that the framework it routes to is genuinely refined.

**NEXT:**
- Fill in first Stage 2 session (pre-market → analysis → trade → log) now that the profile is fully confirmed and the methodology is precise.
- If/when Tiki wants to backtest the two held-open playlist refinements (quarter levels / 2-week order blocks; extended Fib confluence past 61.8%), do that before touching the framework file. Note: KimG's own model already uses a 61.8–78.6% discount/premium zone, which may partially pre-validate the Fib refinement — worth a direct comparison before concluding either way.

## SESSION ROUTING
| Session Type | Stage File | Skills |
|--------------|------------|--------|
| First-time setup / profile intake | `workflow/wf_stage-1_setup.md` | — |
| Daily trading session (pre-market → analysis → trade → log) | `workflow/wf_stage-2_session.md` | `skills/skill_support-resistance-reading.md` |

## CONSTRAINT
No trade is placed or recommended until `_config/trd_config_tiki-profile.md` is filled in. Capital and risk tolerance are non-negotiable inputs, not assumptions.

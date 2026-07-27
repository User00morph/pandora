# D.TRD REF CARD — Trading
## Read this before any D.TRD session.

**PURPOSE:** Tiki's day-trading operation — analysis, strategy execution, and trade journaling, run by any agent from this folder alone.

## ACTIVE STATE
| Item | Status | Next Action |
|------|--------|-------------|
| Tiki trading profile | Not yet filled in | Complete `_config/trd_config_tiki-profile.md` — capital, broker, asset class, risk rules, hours available |
| Support/Resistance strategy | Skeleton drafted, not yet refined | Refine `frameworks/trd_framework_support-resistance-system_v1.md` once profile is known |
| Trade log | Empty | Log every trade in `logs/trd_log_trades_[YYYY-MM].md` |

## QUICK REFS
- Strategy: `frameworks/trd_framework_support-resistance-system_v1.md`
- Profile/config: `_config/trd_config_tiki-profile.md`
- Active log: `logs/trd_log_trades_2026-07.md`
- Skills: `skills/` (loaded per workflow stage — see table below)

Last updated: 2026-07-26 (folder created)

**DONE (2026-07-26):**
- File-system skeleton created — mirrors Pandora's L0→L1→L2→L3 pattern, scoped to Tiki, starting with Trading only.

**NEXT:**
- Get Tiki's trading profile (capital, broker, asset class, timeframe, risk limits, beginner vs. experienced)
- Refine the support/resistance strategy framework from STIS source layers (`D.S.E/trading/skills/skill_auto-key-levels.md`, `skill_value-area-protocol.md`, `skill_poc-trend-filter.md`, `skill_market-structure.md`, `skill_volume-gap-zones.md` in the parent Pandora repo)
- Fill in first workflow session once strategy + profile are both confirmed

## SESSION ROUTING
| Session Type | Stage File | Skills |
|--------------|------------|--------|
| First-time setup / profile intake | `workflow/wf_stage-1_setup.md` | — |
| Daily trading session (pre-market → analysis → trade → log) | `workflow/wf_stage-2_session.md` | `skills/skill_support-resistance-reading.md` |

## CONSTRAINT
No trade is placed or recommended until `_config/trd_config_tiki-profile.md` is filled in. Capital and risk tolerance are non-negotiable inputs, not assumptions.

# D.TRD — TRADING
## Full Department Context (load only when ref_trd.md routes here)

---

## PURPOSE

This department exists so Tiki can day-trade with a repeatable, written-down strategy — and so any agent opening this folder on her computer can read the same strategy, apply it to what's on her screen, and either execute or recommend a trade, without needing to be re-taught the logic each session.

## STARTING FOCUS

Support and resistance — the core structural levels where price has reacted before and is statistically likely to react again. This department starts narrow (one strategy family) rather than wide (many uncorrelated systems), because a single well-executed edge beats a scattered one.

Correlated concepts folded into "support/resistance" for this department:
- **Key levels** — prior swing highs/lows, round numbers, session opens
- **Value area / POC** — volume-profile-derived fair-value zones (high-volume nodes act as support/resistance; low-volume nodes/gaps act as magnets through which price moves fast)
- **Liquidity pools** — where stops cluster (often just beyond an obvious S/R level)
- **Market structure** — higher-highs/higher-lows vs. lower-highs/lower-lows framing that determines whether a level is being tested as support or resistance

## SKILL ROUTING TABLE

| Workflow Stage | Skill(s) Needed |
|---------------|-----------------|
| Setup / profile intake | none |
| Daily session — reading the chart | `skills/skill_support-resistance-reading.md` |
| Daily session — sizing a trade | `_config/trd_config_tiki-profile.md` (risk rules) |

## SOURCE MATERIAL

The strategy logic in this department is refined from the parent Pandora repository's Sovereign Trading Intelligence System (STIS), specifically:
- `D.S.E/trading/skills/skill_auto-key-levels.md`
- `D.S.E/trading/skills/skill_value-area-protocol.md`
- `D.S.E/trading/skills/skill_poc-trend-filter.md`
- `D.S.E/trading/skills/skill_volume-gap-zones.md`
- `D.S.E/trading/skills/skill_market-structure.md`
- `D.S.E/trading/skills/skill_liquidity-engineering.md`
- `D.S.E/trading/fundamentals/dse_framework_market-structure.md`

These are reference source, not duplicated wholesale — the strategy framework in `frameworks/` distills them into what actually applies to Tiki's setup (capital size, asset class, timeframe). Refinement happens once her profile is filled in.

## NON-NEGOTIABLES

- No live trade without a filled-in `_config/trd_config_tiki-profile.md`
- No risk-parameter change without explicit confirmation
- Every trade — win, loss, or no-trade decision — gets logged

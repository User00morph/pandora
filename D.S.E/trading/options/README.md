# D.S.E/trading/options/
**GEX / Options Mechanics Layer | STIS Layer 1b**
**Created: 2026-05-20**

This directory holds daily GEX level maps, intraday gamma regime reads, and options data references.

## Contents

### Active Files
- (empty — populate once a GEX data provider is configured)

## File Naming Convention
```
YYYY-MM-DD_gex-session-map.md        — Daily GEX level stack (HVL, call res, put sup, GEX 1-3)
YYYY-MM-DD_options-brief.md          — Full pre-session GEX regime read
gex-provider-reference.md            — Data source configuration and access notes
```

## GEX Data Sources (evaluate and select)
- **SpotGamma** (spotgamma.com) — primary recommendation for SPX/QQQ/NQ
- **Tradytics** — alternative with broader asset coverage
- **OptionsGamma.io** — community-priced alternative
- **Unusual Whales** — options flow + gamma data
- **Thinkorswim** — free if you have TD account (gamma levels via dxFeed)

## Source Skills
- `D.S.E/trading/skills/skill_gex-regime-read.md`
- `D.S.E/trading/fundamentals/dse_framework_gex-options-mechanics.md`
- `.claude/agents/agent_gex-analyst.md`

## Decoded From
`drd_decode_quant-options-ai-trading-stack_v1.md` — Options Flow + GEX Daily Model videos

# RAW EXTRACT — Claude + TradingView + Exchange Bot (Part 2: Live Execution + Cloud Deploy)

## Source Metadata
- **Title:** (Part 2) Claude + TradingView → Live Trade Execution on Exchange + Cloud 24/7
- **Channel:** (same creator as Part 1 — TradingView MCP series)
- **Duration:** ~29:00
- **URL:** https://youtu.be/aDWJ6lLemJU?si=UJ6IhHRtHtZjwvRR
- **Prerequisite Video:** https://youtu.be/vIX6ztULs4U?si=HYLZu3FOwRWgmxMz (Part 1 — TradingView MCP setup)
- **Tier:** 2 — practitioner tutorial, implementation-focused, primary demo with real system
- **Extracted:** 2026-05-05
- **Domain:** trading-systems, ai-trading-tech, claude-code-integration
- **Word Count:** ~7,350

## Summary

Part 2 of the TradingView MCP series. Part 1 connected Claude to TradingView for live chart reading and strategy visualization. This video adds three things:
1. **Exchange connection** — Claude can now execute real trades (via exchange API)
2. **Safety layer** — multi-condition pre-trade filter; all conditions must be true before any trade fires
3. **Cloud deployment** — the entire bot runs on Railway 24/7, no laptop required

## System Architecture

```
TradingView Desktop (price data / chart / Pine Script indicators)
        ↓
      Claude (brain — reads signals, holds strategy, runs safety check, executes)
        ↓
   Exchange API (BitGet or any exchange with API — executes and logs the trade)
        ↓
   Trade Log (spreadsheet — every trade, outcome, reason; optimized for accounting/tax)
        ↓
   Railway (cloud host — cron job runs the loop 24/7 on chosen interval)
```

TradingView and the Exchange **never talk directly**. Claude is the intermediary that:
- Reads live chart data from TradingView
- Holds the strategy context (rules.json)
- Runs the safety filter before any trade
- Executes to the exchange when all conditions align
- Logs everything — including blocked trades with reason codes

## Three Core Tools

| Tool | Role |
|---|---|
| TradingView Desktop | Price data, chart, Pine Script strategy visualization |
| Claude Code (terminal) | Brain — strategy execution, safety filter, trade decision |
| Exchange (BitGet / Binance / etc.) | Money lives here; Claude executes via API |

## Key Files Created by Setup

| File | Purpose |
|---|---|
| `.env` | API key + secret + passphrase for exchange; portfolio value; max trade size; max trades/day; paper trading mode toggle; chart/timeframe defaults |
| `rules.json` | Full strategy: buy/sell conditions, indicators, Pine Script, timeframes, risk parameters |
| Trade log (spreadsheet) | Logs every trade attempt (success or blocked) with timestamp, indicators at time of check, reason for block/execution — tax/accounting ready |

## Setup Process (One-Shot Prompt on GitHub)

1. Get exchange API key + secret key + passphrase (BitGet shown; 10 exchanges supported with individual tutorials)
2. Paste one-shot prompt into Claude Code terminal → onboarding agent takes over
3. Onboarding agent steps through: Whisper Flow setup → exchange selection → API key entry → ENV file population → TradingView health check → strategy definition → Railway deploy → cron job schedule → trade log setup → live test run
4. Configure `.env`: portfolio size, max single trade, max trades/day, paper trading mode = true
5. Deploy to Railway (cloud) — logs in via `railway login` in terminal, sets cron schedule
6. Watch first paper trade run — confirms all conditions, logs result with reason code

## Safety Layer (Pre-Trade Filter)

Before every trade attempt, Claude checks ALL conditions in rules.json:
- If any single condition fails → trade blocked, reason logged
- Example strategy used in demo (not endorsed): price above VWAP + price above 8 EMA + RSI < 30 → only then buy
- Demo result: trade blocked because RSI was 38.26 (needed < 30) — logged with exact values

**Paper trading mode** (`PAPER_TRADING=true` in .env): runs all logic, executes simulated trades, logs everything — but sends no real orders to exchange. Switch to live by telling Claude "make it real money now" or by editing .env.

## Cloud Deployment via Railway

- Railway runs a **cron job** at chosen interval (every 4 hours, every minute, etc.)
- Bot checks TradingView + runs safety filter + executes/logs → repeats on schedule
- No laptop required. Trades can execute in sleep.
- Frequency note: more frequent = more Claude API calls = higher cost; balance against strategy timeframe
- Railway was set up in Part 1; this video just deploys to it

## Appify Integration (YouTube Strategy Scraping)

Bonus section at end of video — method for scraping a YouTube creator's channel to extract their trading strategy:

1. Create Appify account → get API token → add to .env as `APPIFY_API_KEY`
2. Tell Claude: "Scrape the last 100 videos from [YouTube channel URL] using Appify. Save all transcripts. Deduce their trading strategy. Create rules.json based on what you find."
3. Takes 10–20 minutes; Claude builds the strategy from transcripts automatically
4. Creator examples used: Blockchain Backer, CoinsKid

**Note for Pandora:** This is the same YouTube transcript extraction approach used in D.R.D research pipeline — but applied in reverse to *build a trading strategy* from extracted transcripts rather than to build a knowledge framework. Directly relevant to STIS: we could run Saaja/Jiang/Bailey frameworks through the same pipeline to encode them into rules.json as strategy context.

## Implementation Notes for STIS

- **This is the execution layer of STIS** — what actually fires orders based on the Observer's framework
- The `rules.json` file is where STIS Layers 1–4 get encoded into executable conditions
- Paper trading mode is essential first phase — maps to Nigredo/Rubedo phase structure in PRD v3
- Trade log = the STIS Decision Log in automated form
- **Railway cron + paper trading** is the Phase 1 implementation path before any live capital is risked
- The Appify transcript-to-strategy method is already being done manually in D.R.D — automating this pipeline via Appify would compress research-to-strategy time significantly

## GitHub

Both Part 1 and Part 2 are on the same GitHub repo (link in video description). The repo contains:
- One-shot setup prompt for Part 1 (TradingView MCP)
- One-shot setup prompt for Part 2 (exchange execution + cloud deploy)
- Individual exchange setup tutorials (10 exchanges listed)
- Windows/Linux setup guides
- Appify integration instructions

## Prerequisites

- Part 1 video completed (TradingView MCP connected, TradingView Desktop running with CDP)
- Claude Code CLI installed and running
- Exchange account created (BitGet or other API-supported exchange)
- Railway account (from Part 1 setup)

---
*RAW — not yet passed through D.R.D deconstruction. Do not integrate into department files.*

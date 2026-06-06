# SKILL — NIGHTLY RESEARCH LOOP
**Autonomous Alpha Generation Architecture**
**Load when:** Setting up or reviewing the research agent pipeline.
**Department:** D.S.E + D.I.I | STIS Autonomous Layer | Alpha generation

---

## WHAT THIS IS

The architecture for an autonomous nightly pipeline that generates new strategy ideas while Morph sleeps. Over time, thousands of ideas are tested, filtered, and a small number of viable strategies emerge.

---

## THE PIPELINE

```
NIGHTLY (automated):

1. RESEARCH AGENT pulls from 20-30 source library
   → Generates 20-40 new strategy hypothesis briefs
   → Adds all to the backtest queue with tags

2. BACKTEST AGENT processes the queue
   → Runs walk-forward validation on each idea
   → Logs: passed / failed / needs more data

3. MORNING BRIEF delivered to Morph
   → Ideas tested last night
   → Any strategies that passed initial validation
   → Strategies retired (edge decayed)
   → Queue depth (backlog size)
```

---

## THE 20-30 SOURCE LIBRARY

Diversity of sources = diversity of alpha = lower correlation between strategies.

**Tier 1 — Quantitative research:**
- arXiv quantitative finance papers
- Published hedge fund research
- Academic factor studies

**Tier 2 — Practitioner content:**
- Travis Woo video library (already extracted)
- Other systematic traders' YouTube channels
- TradingView community scripts (high-engagement ones)

**Tier 3 — Open source:**
- GitHub quantitative trading repositories
- Backtest results published by verified traders
- Open-source strategy codebases (use as baselines)

**Tier 4 — Market structure:**
- COT reports (Commitment of Traders)
- Options flow data
- GEX daily outputs

---

## THE IDEA TRACKING SYSTEM

Every strategy is an initiative with a lifecycle record:

```
STRATEGY LOG ENTRY:
  ID:           [unique identifier]
  Source:       [where the idea came from]
  Hypothesis:   [what edge is being tested]
  Status:       [pending / testing / paper / live / retired]
  Backtest:     [Sharpe / win rate / max DD / expectancy]
  Walk-forward: [pass / fail / in progress]
  Paper result: [if applicable]
  Retirement:   [reason if retired]
```

---

## THE OPEN-SOURCE BASELINE PROTOCOL

Instead of generating from scratch — find a working strategy on GitHub and improve it:

1. Feed the GitHub repo to the research agent as a reference document
2. Instruct: understand the edge, validate it still exists in current conditions, improve incrementally
3. This compresses discovery time dramatically — start at a known baseline, refine from there

---

## THE REALISTIC RATIO

Based on Travis Woo's build:
- ~30 ideas generated per night
- After several thousand tested: 3-4 viable strategies extracted
- Viable = passes walk-forward + paper trading gateway

Plan for this ratio. Do not expect 30 viable strategies from 100 ideas. The funnel is narrow and that is correct.

---

## THE ICT VALIDATION PRINCIPLE

Many popular trading concepts (ICT, Smart Money Concepts, order blocks, fair value gaps) are dismissed by systematic traders because they are typically traded by intuition rather than backtest proof.

The correct stance: **concepts are neutral — validation is what matters.**

From Travis Woo's live portfolio: a 4-hour fair value gap strategy IS in the 27-bot crypto portfolio and it DOES produce positive results in the backtest. The ICT concept itself has edge. The problem was never the concept — it was the refusal to prove it.

**Applied to the nightly research loop:** when agents encounter popular trading concepts from any source (ICT, harmonic patterns, Wyckoff), the instruction is NOT to dismiss them — it is to ADD them to the backtest queue with the same walk-forward validation standard as any other idea. If they pass, they earn their place.

---

## RULES

- Diversity of sources prevents the research agent from converging on consensus ideas everyone else is testing
- Every idea gets tracked — nothing is lost, including failures (failure data shapes future hypothesis quality)
- Morning brief is Morph's only required daily interaction with the research layer
- No concept is dismissed on principle — validation determines value, not source reputation

*D.S.E + D.I.I | STIS Autonomous Layer | Research Pipeline | Source: Travis Woo Zero Human Trading Firm + Crypto Edge Pro videos*

# SKILL — MULTI-TIMEFRAME DASHBOARD
**All Timeframes on One Chart — Without Switching Views**
**Load when:** Analyzing any chart for STIS layer confluence.
**Department:** D.S.E trading workspace | STIS Layer 1 | Multi-timeframe analysis

---

## WHAT THIS IS

The multi-timeframe dashboard is a table overlay that shows the trend state, key levels, and momentum of the current asset across multiple timeframes simultaneously — without needing 4 separate chart windows. Everything needed for confluence analysis on one screen.

---

## THE DASHBOARD LAYOUT

```
┌─────────────────────────────────────────────────────────┐
│  STIS MTF DASHBOARD — EUR/USD — 2026-06-04 08:30 UTC   │
├───────┬────────┬──────────┬───────────┬────────┬────────┤
│  TF   │ TREND  │  PRICE   │   VWAP    │  RSI   │ SIGNAL │
├───────┼────────┼──────────┼───────────┼────────┼────────┤
│  1M   │  ▲ UP  │  1.0854  │  1.0841   │  62    │  BULL  │
│  4H   │  ▲ UP  │  1.0854  │  1.0820   │  57    │  BULL  │
│  1D   │  ─ MID │  1.0854  │  1.0830   │  52    │  NEUT  │
│  1W   │  ▲ UP  │  1.0854  │  1.0780   │  59    │  BULL  │
└───────┴────────┴──────────┴───────────┴────────┴────────┘
3/4 timeframes BULLISH → Long bias confirmed
```

---

## THE STIS CONFLUENCE READ

```
ALL 4 TF BULLISH → Maximum conviction long
3 OF 4 BULLISH   → Strong long bias, full size
2 OF 4 BULLISH   → Mixed — wait for alignment
1 OF 4 BULLISH   → Counter-trend — pass or micro size
0 OF 4 BULLISH   → Full bear posture, short bias
```

---

## WHAT EACH COLUMN MEANS

| Column | How it's calculated | What it tells you |
|---|---|---|
| Trend | EMA 20 vs EMA 50 direction | Structural direction on that TF |
| Price | Current close price | Where we are |
| VWAP | Session VWAP for that TF | Whether price is above/below fair value |
| RSI | 14-period RSI on that TF | Momentum state (overbought/oversold) |
| Signal | Composite of trend + RSI + price | Simple directional read |

---

## PINE SCRIPT REQUEST PATTERN

```pine
// Fetch higher timeframe data
htf_close_4h = request.security(syminfo.tickerid, "240", close)
htf_ema20_4h = request.security(syminfo.tickerid, "240", ta.ema(close, 20))
htf_ema50_4h = request.security(syminfo.tickerid, "240", ta.ema(close, 50))
htf_rsi_4h   = request.security(syminfo.tickerid, "240", ta.rsi(close, 14))

trend_4h = htf_ema20_4h > htf_ema50_4h ? "▲ UP" : "▼ DN"
```

---

## INTEGRATION WITH STIS MORNING BRIEF

The MTF dashboard IS the first thing loaded in the morning brief. Before any GEX read, before any Markov signal — know the structure across all timeframes. If the daily and weekly are bearish, no amount of intraday bullish GEX signal changes the structural context.

**Hierarchy:** Weekly → Daily → 4H → 1H → entry timeframe. All must align for Grade A entry.

*D.S.E/trading/skills | STIS Layer 1 | Multi-Timeframe Analysis*

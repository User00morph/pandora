# SKILL — SESSION KILL ZONES
**High-Probability Trading Windows and Session Timing Protocol**
**Load when:** Planning session entry times, evaluating whether current time is favorable for trading.
**Department:** D.S.E trading workspace | STIS Layer 3 (External Reality) | Session timing

---

## WHAT THIS IS

Kill zones are the first 1-2 hours of each major session — when institutional order flow is highest, spread is tightest, and the directional move for the session is established. Trading inside kill zones maximizes the probability that moves are institutional, not noise.

---

## THE THREE SESSIONS (UTC)

```
ASIA SESSION
  Open:       00:00 UTC (21:00 NYC previous day)
  Kill Zone:  00:00 – 02:00 UTC
  Character:  Range establishment, accumulation
  Best for:   JPY pairs, gold, crypto (24h)

LONDON SESSION
  Open:       07:00 UTC (03:00 NYC)
  Kill Zone:  07:00 – 09:00 UTC
  Character:  Highest EUR/GBP liquidity, trend initiation
  Best for:   EUR/USD, GBP/USD, EUR/GBP

NEW YORK SESSION
  Open:       13:00 UTC (09:00 NYC)
  Kill Zone:  13:00 – 15:00 UTC
  Character:  Highest total liquidity, continuation or reversal of London
  Best for:   All major pairs, indices, metals

OVERLAP (HIGHEST VOLATILITY):
  London-NY:  13:00 – 15:00 UTC
  Asia-London: 07:00 – 08:00 UTC
```

---

## THE KILL ZONE PRINCIPLE

During a kill zone: institutional desks are actively placing orders. Price movement is directional and large. Moves are more predictable because the participants are consistent.

Outside kill zones: liquidity thins, spread widens, moves are choppier. Price can drift in any direction without conviction. Risk-adjusted edge is lower.

**Rule: Only enter new positions during or within 30 minutes after a kill zone opens.**

---

## PINE SCRIPT VISUALIZATION

```pine
// Session box rendering — each session gets a shaded background
kz_asia_box = request.security(syminfo.tickerid, "D", [calculated on UTC])
bgcolor(in_asia_kz ? color.new(color.blue, 90) : na, title="Asia KZ")
bgcolor(in_london_kz ? color.new(color.green, 90) : na, title="London KZ")
bgcolor(in_ny_kz ? color.new(color.orange, 90) : na, title="NY KZ")
bgcolor(in_overlap ? color.new(color.red, 85) : na, title="LDN-NY Overlap")
```

---

## STIS SESSION ENTRY MATRIX

| Session | Bias condition | Entry trigger | Avoid |
|---|---|---|---|
| Asia | GEX + Markov aligned overnight | Range break with volume | During news events |
| London | IEC phase 3 + GEX trending | Kill zone momentum continuation | First 15 min (spread wide) |
| NY | London direction confirmed | Retest of London breakout level | After 15:00 UTC (charm drift) |

---

## RULES

- Never enter a new position outside a kill zone (for intraday trades)
- The first 15 minutes of any session can be exceptionally volatile — wait for direction to establish
- The London-NY overlap (13:00-15:00 UTC) is the highest edge window of the entire trading day

*D.S.E/trading/skills | STIS Layer 3 | Source: Travis Woo TradingView Tricks video + STIS framework*

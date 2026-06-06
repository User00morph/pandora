# SKILL — MARKET OPEN 30-MINUTE PROTOCOL
**The First 30 Minutes of Any Session — What to Do and When**
**Load when:** The market has just opened and you're deciding whether and when to trade.
**Department:** D.S.E trading workspace | STIS Execution Layer | Opening protocol

---

## WHAT THIS IS

The first 30 minutes of any session are the most volatile and most deceptive. Institutional desks test both directions before committing. This protocol prevents entering too early (before direction is established) while capturing the highest-probability move once it forms.

---

## THE 30-MINUTE MAP

```
TIME (relative to session open)        WHAT'S HAPPENING         YOUR ROLE
─────────────────────────────────────────────────────────────────────────
00:00 – 05:00  (first 5 min)     Initial volatility spike    OBSERVE ONLY
                                  Spread is wide              No orders
                                  Both directions tested      

05:00 – 15:00  (5-15 min)        Direction forming            WATCH + MARK
                                  First directional bias       Mark the 5-min high/low
                                  Often a false move first     Note: does price hold above
                                                               or below session open?

15:00 – 30:00  (15-30 min)       KILL ZONE PROPER             READY TO ACT
                                  Spread has normalized        
                                  Manipulation sweep may have  
                                  occurred                     
                                  Real direction establishing  
```

---

## THE FIVE-MINUTE HIGH/LOW RULE

```
After the first 5 minutes have closed:
  Mark the 5-minute high and low as the initial range

Between 5-15 minutes:
  Watch which side BREAKS first (the manipulation direction)
  The break direction is often the TRAP
  The reversal direction is often the REAL move

Between 15-30 minutes:
  IF: price broke above 5-min high → reversed below it → confirmed bearish
  IF: price broke below 5-min low → reversed above it → confirmed bullish
  
  This is the manipulation sweep + reversal pattern
  This is your Grade A entry signal for the session
```

---

## THE SESSION OPEN NARRATIVE

```
SCENARIO A — BULLISH OPEN (price opens above prior session close):
  First 5 min: drift or test both sides
  5-15 min: watch for a dip BELOW prior close (sweep of lows)
  If dip reverses strongly → LONG entry on close above prior close
  Target: nearest GEX resistance level or Asia High

SCENARIO B — BEARISH OPEN (price opens below prior session close):
  First 5 min: drift or test both sides
  5-15 min: watch for a push ABOVE prior close (sweep of highs)
  If push reverses strongly → SHORT entry on close below prior close
  Target: nearest GEX support level or Asia Low

SCENARIO C — FLAT OPEN (price opens at or near prior close):
  Wait for the 5-minute range to form
  The break of the 5-min range + reversal = the session's first high-probability move
```

---

## THE ALARM SEQUENCE

Set these alerts before the session opens:
```
ALERT 1: Price reaches prior session high → "Potential sweep zone"
ALERT 2: Price reaches prior session low → "Potential sweep zone"
ALERT 3: Price crosses the session open price → "Direction changing"
ALERT 4: 15 minutes have passed → "Kill zone ready"
```

With the smart alert system, these can all be handled by one alert with context messages.

---

## RULES

- Never enter in the first 5 minutes regardless of how clear the setup looks
- The most obvious move in the first 5 minutes is usually the trap
- The first 30-minute high/low set the key levels for the entire day
- If no clear sweep-and-reversal pattern forms within 30 minutes → wait for the next kill zone

*D.S.E/trading/skills | STIS Execution Layer | Opening Protocol*

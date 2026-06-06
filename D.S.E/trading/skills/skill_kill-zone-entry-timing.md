# SKILL — KILL ZONE ENTRY TIMING
**Precise Session Window Timing for Maximum-Edge Entries**
**Load when:** Evaluating whether to enter a setup based on session timing.
**Department:** D.S.E trading workspace | STIS Execution Layer | Session timing

---

## WHAT THIS IS

Not all hours of the trading day are equal. Kill zones are the specific windows when institutional order flow is highest — providing directional clarity that doesn't exist at other times. This skill maps exactly when to act and when to wait.

---

## THE KILL ZONE MAP (UTC)

```
SESSION        KILL ZONE          WAIT PERIOD          DEAD ZONE
──────────────────────────────────────────────────────────────────
ASIA           00:00 – 02:00     02:00 – 07:00        Full except KZ
LONDON         07:00 – 09:30     09:30 – 12:30        Rest of London
NY             13:00 – 15:00     12:30 – 13:00*       After 15:00
LONDON-NY OVR  13:00 – 15:00     (Same as NY KZ)      Most volatile
──────────────────────────────────────────────────────────────────
*12:30-13:00: Pre-NY kill zone — watch but don't enter
```

---

## THE TIMING RULES

```
RULE 1 — ENTER ONLY IN KILL ZONES (for intraday trades)
  If a setup forms outside a kill zone → wait for the kill zone to open
  If the setup is no longer valid when the kill zone opens → it was a bad setup
  Exception: if a stop-hunt sweep occurs during a dead zone and reverses → valid

RULE 2 — THE FIRST 15 MINUTES ARE FOR WATCHING
  London 07:00-07:15 → observe only, spread is wide, direction unclear
  NY 13:00-13:15 → observe only, initial volatility may be a fake-out
  Enter only AFTER the first 15 minutes have passed and direction is established

RULE 3 — LONDON BIAS SETS THE NY DIRECTION
  If London closes with a clear trend → NY typically continues or retests
  If London closes choppy/mixed → NY is less predictable → reduce size

RULE 4 — AFTER 15:00 UTC → CHARM TAKES OVER
  After 15:00 (end of NY kill zone): charm drift begins
  Price gravitates toward nearest GEX level
  No new entries after 15:00 unless a very clear A++ setup forms
  Close any open intraday positions before 15:00 if not already stopped or targeted
```

---

## THE SESSION NARRATIVE FRAMEWORK

Each session tells a story that feeds the next:

```
ASIA SESSION:
  Establishes the overnight range (Asia High / Asia Low)
  This range is the "trap" that London will sweep

LONDON KILL ZONE (07:00-09:30):
  Often sweeps the Asia High OR Asia Low first (manipulation)
  Then initiates the real direction (expansion)
  The London direction becomes the daily bias

NY KILL ZONE (13:00-15:00):
  Either CONTINUES the London direction
  Or REVERSES if London was a fake
  The highest-probability scenario: continuation of a confirmed London move
```

---

## THE KILL ZONE ENTRY CHECKLIST

Before entering in any kill zone:
```
□ Is this the correct kill zone for this instrument? (EUR pairs = London priority)
□ Have the first 15 minutes passed? (no early entries)
□ Has direction been established? (not still ranging)
□ Has a manipulation sweep occurred? (sets up the real entry)
□ Is the setup consistent with the London narrative?
□ Does the full pre-trade checklist pass? (12/12)
```

*D.S.E/trading/skills | STIS Execution Layer | Kill Zone Timing*

# SKILL — OBSERVER RE-ENTRY PROTOCOL
**How to Re-Enter After Being Stopped Out Without Revenge Trading**
**Load when:** A stop loss has just been hit and a potential re-entry opportunity is forming.
**Department:** D.S.E trading workspace | STIS Observer Layer | Post-loss management

---

## WHAT THIS IS

Being stopped out is information, not failure. The re-entry protocol determines when — and whether — to re-engage after a loss, from a position of clarity rather than reaction.

---

## THE MANDATORY PAUSE

After any stop loss hit:

```
IMMEDIATE ACTIONS (next 10 minutes):
  1. Close the chart — do not watch the price continue without you
  2. Do not immediately assess if the trade "would have worked"
  3. Log the exit: price, time, R-multiple (-1.0 R)
  4. Run the Observer Gate: am I in reaction mode or Observer mode?

IF REACTION MODE (anger, frustration, desire to "get it back"):
  → Do NOT re-enter today
  → Take a 30-minute break minimum
  → Return to Observer state first (see skill_observer-calibration.md)
  → If Observer cannot be restored within the session: stop trading for the day

IF OBSERVER MODE (neutral, curious, analytical):
  → Proceed to the re-entry assessment below
```

---

## THE RE-ENTRY ASSESSMENT

A re-entry is NOT the same as the original trade. It requires FRESH analysis.

```
QUESTION 1: Why was the stop hit?
  A) Price swept my stop then reversed (stop hunt) → Re-entry valid
  B) Thesis was wrong — the level didn't hold → Re-entry requires new thesis
  C) GEX/Markov regime changed → No re-entry until new regime is classified

QUESTION 2: Has the original thesis changed?
  Same direction as original → Re-entry at new level, tighter stop
  Opposite direction now → Only if a FULL morning sequence has been run

QUESTION 3: What does the daily risk budget say?
  Budget > 50% remaining → Standard size allowed
  Budget < 50% remaining → Half size maximum
  Budget exhausted → No re-entry today
```

---

## THE RE-ENTRY CONDITIONS

A re-entry is valid ONLY when ALL of these are true:

```
□ Observer is fully present (Gate passed)
□ 10+ minutes have passed since the stop was hit
□ A NEW setup has formed (not the same candle pattern at the same level)
□ The re-entry level is DIFFERENT from the original stop level (minimum 10 pips)
□ The daily risk budget permits it
□ A new pre-trade checklist has been run (full 12-question check)
```

---

## THE STOP HUNT PATTERN (re-entry IS valid)

```
Sequence:
1. Price approaches your stop
2. Price briefly spikes through your stop level (wick below/above)
3. Price immediately reverses and closes BACK above/below the level
4. The original thesis is still intact

This is an institutional stop sweep, not a thesis invalidation.
→ Re-entry at market on the close of the reversal candle
→ New stop: 5-10 pips beyond the wick extreme (below the swept level)
→ Size: same as original (thesis intact, just a cleaner entry)
```

---

## THE "DON'T LOOK" PRESCRIPTION FOR SYSTEMATIC POSITIONS

For the MTP/systematic trend-following layer (not intraday trading): the correct psychological prescription is the opposite of active monitoring.

```
AUTOMATED SYSTEMATIC POSITIONS:
  "The best thing you can do is not look at it for 365 days."

Why: The system is designed to capture tail events — rare, large gains.
     These tail events cannot be predicted in advance.
     Watching the position during the long boring/losing periods:
     → Creates anxiety
     → Leads to premature exit
     → Guarantees missing the tail event that makes the year

The only time to look: when the systematic alert fires
                        (new high → advance stop → optionally add)
```

This is NOT advice to ignore intraday trading. Intraday positions require active management. This applies ONLY to the systematic, weeks-to-months trend-following positions. Two different psychological postures for two different position types.

---

## THE REVENGE TRADE RECOGNITION

You are about to revenge trade if:
- You want to "get back" the money you just lost
- You're entering within 60 seconds of the stop being hit
- You haven't run the Observer Gate
- The setup doesn't pass the full 12-question checklist
- You're sizing up to "make it back faster"

Any of these = STOP. Close the platform. Log it as "potential revenge trade avoided."

*D.S.E/trading/skills | STIS Observer Layer | Post-Loss Management*

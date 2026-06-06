# SKILL — HYPOTHESIS FORMATION PROTOCOL
**Writing Testable Trading Hypotheses Before Every Session**
**Load when:** During weekly prep or when a potential multi-day setup is forming.
**Department:** D.S.E trading workspace | STIS Research Layer | Hypothesis engine

---

## WHAT THIS IS

A trading hypothesis converts a vague directional feeling into a testable, falsifiable statement. This is how quants think. It eliminates "I think it's going up" and replaces it with specific conditions, targets, invalidation criteria, and a timeframe.

---

## THE HYPOTHESIS STRUCTURE

```
HYPOTHESIS FORMAT:
"IF [specific conditions align] THEN [predicted outcome] BY [timeframe]
 WITH [expected probability] BECAUSE [mechanical reason]
 INVALIDATED IF [specific counter-condition]"
```

---

## EXAMPLE HYPOTHESES

**Weak (not a hypothesis):**
"EUR/USD looks bullish this week."

**Strong (a proper hypothesis):**
"IF EUR/USD holds above the London session POC at 1.0840 during the NY kill zone on Monday, AND GEX regime is positive gamma (above HVL 1.0820), AND Markov signal is +30%+ THEN EUR/USD will test the GEX Call Wall at 1.0920 within 3 trading days WITH 65% probability BECAUSE dealers are in long-gamma mean-reversion mode creating a mechanical ceiling at 1.0920, and prior session POC confirms institutional cost basis at 1.0840. INVALIDATED IF price closes below 1.0820 (HVL break = regime change to trending)."

---

## THE FIVE COMPONENTS (every hypothesis must have all five)

```
1. CONDITIONS (what must be true for the setup to exist)
   Be specific: price level, indicator state, session, GEX level
   NOT: "if the market looks bullish"
   YES: "if price is above 1.0840 POC AND GEX regime is mean-reverting"

2. PREDICTED OUTCOME (what will happen)
   Be specific: which level, approximate magnitude
   NOT: "EUR/USD will go higher"
   YES: "EUR/USD will test 1.0920 GEX Call Wall"

3. TIMEFRAME (when will this resolve)
   NOT: "in the coming days"
   YES: "within 3 trading sessions"

4. PROBABILITY (how confident am I — 50-90%)
   This forces honest calibration
   NOT: "I'm sure of this"
   YES: "65% probability"

5. INVALIDATION (what would make this wrong)
   The single most important component — defines the exit
   NOT: "if it doesn't work out"
   YES: "invalidated if price closes below HVL 1.0820"
```

---

## THE HYPOTHESIS LOG

Each hypothesis lives in the weekly log with a resolution entry:

```
HYPOTHESIS: [full text]
FORMED:     [date formed]
RESOLVED:   [date resolved]
OUTCOME:    Confirmed / Disconfirmed / Inconclusive
ACCURACY:   Was the probability calibrated correctly?
LEARNING:   [one sentence takeaway for the playbook]
```

---

## THE SYSTEMATIC vs. INTUITIVE DISTINCTION

The hypothesis protocol is the bridge between intuition and evidence. The failure mode it prevents: "I think this works" → trades it for 3 months → loses money → abandons it → never knows if the concept was valid or if the execution was wrong.

Proper hypothesis formation produces a testable outcome that can be evaluated against the edge assumption:

```
INTUITIVE TRADE: "This looks like a good long setup"
  Problem: Cannot be validated, cannot be improved, cannot be trusted at scale

HYPOTHESIS-BASED TRADE: "IF London kill zone + POC support + GEX mean-reverting
                          THEN 70% probability of 2R within 4 hours
                          INVALIDATED IF GEX regime flips"
  Result: After 20 instances → accuracy rate = 68% → hypothesis CONFIRMED
  The concept is now a named setup with a known edge
```

ICT concepts fail not because they don't work — many do — but because they are traded intuitively rather than hypothesis-tested. The same discipline that validates the Markov signal validates any concept from any source.

---

## BUILDING THE PLAYBOOK

After 20+ resolved hypotheses of the same type, a pattern emerges. The playbook entry format:

```
SETUP TYPE: "GEX positive gamma + POC support + Markov 30%+ bull"
  Historical accuracy: X% confirmed
  Average R when confirmed: X.XX
  Common invalidations: [list]
  Best session: [London/NY]
  → This is now a named setup in the playbook
```

*D.S.E/trading/skills | STIS Research Layer | Hypothesis Formation*

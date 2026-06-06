# SKILL — PRE-TRADE CHECKLIST
**The Final Gate Before Any Entry**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  A potential setup has formed. Run AFTER morning-session-sequence confirms A/A+ session.
DEPARTMENT: D.S.E | STIS Execution Layer | Entry gate
LOADS:      skill_morning-session-sequence.md (must complete first)
            skill_daily-risk-budget.md (for question 12)
            skill_kill-zone-entry-timing.md (for question 2)
PRODUCES:   Pass/Fail verdict (12/12 required) + position size + stop level + target levels
CROSS-REF:  skill_position-management-protocol.md (what to do after entry)
            skill_grade-a-filter.md (structural quality check)
            skill_observer-reentry-protocol.md (if stopped out later)
```

---

## WHAT THIS IS

The last check before any order is placed. Every question must be answerable with a clear YES or NO. Any NO or UNSURE = no trade. This checklist eliminates 90% of marginal setups that bleed accounts.

---

## THE 12-QUESTION CHECKLIST

```
PRE-CONDITION CHECKS
□ 1. SESSION GRADE: Is this an A or A+ session? (from morning sequence)
      NO = no trade today regardless of how good the setup looks

□ 2. KILL ZONE: Are we currently in or within 30 min of a kill zone open?
      NO = wait for the next kill zone

□ 3. OBSERVER PRESENT: Am I in Observer position right now?
      NO = close the platform, restore Observer, restart

STRUCTURAL ALIGNMENT
□ 4. HTF BIAS CONFIRMED: Is the 4H and Daily structure aligned with this entry?
      If LONG: is 4H and Daily making higher highs and holding above key EMA?
      NO = counter-trend entry, skip unless Grade A++ confirmation

□ 5. GEX REGIME COMPATIBLE: Is this entry consistent with the GEX regime?
      LONG in positive gamma: only at GEX support level with volume
      LONG in negative gamma: trend follow only, no fades
      SHORT in positive gamma: only at GEX resistance level with volume
      SHORT in negative gamma: follow the trend, entry on pullback

□ 6. MARKOV SIGNAL ALIGNED: Is the Markov signal in the entry direction?
      Signal > +15% differential for longs, < -15% for shorts
      NO = skip or reduce to quarter size

LEVEL AND STRUCTURE
□ 7. AT A KEY LEVEL: Is price at a GEX level, POC, or auto key level?
      NO = entering mid-range, skip

□ 8. POWER CLUSTER: Do multiple level types coincide within 10 pips?
      GEX + Volume Profile + Auto Level = A++ level
      SINGLE level only = standard A level

□ 9. MANIPULATION CONFIRMED: Has a sweep occurred at or near this level?
      Visible wick + close back through = YES
      Just approached level = NO, wait for sweep

EXECUTION PARAMETERS
□ 10. STOP LOSS PLACED: Is the exact stop loss level identified pre-entry?
       Must be a structural level, NOT a dollar amount
       Stop at session POC, below/above the GEX level broken, or ATR distance

□ 11. TARGET IDENTIFIED: Are the first and second targets clear?
       First target: 2R minimum
       Second target: next GEX level or structural level

□ 12. POSITION SIZE CALCULATED: Is the risk within today's daily risk budget?
       Risk per trade = daily budget / number of signals today
       If daily budget is already 50% used = half size maximum

DECISION
All 12 = YES → Enter at market or limit, place stop immediately
Any NO/UNSURE → Do not enter. Log the setup as "observed, not taken."
```

---

## THE LOG DISCIPLINE

Every setup run through this checklist gets logged — whether taken or not. The "observed, not taken" log is where pattern recognition develops.

```
SETUP LOG FORMAT:
  Date/time:     [timestamp]
  Instrument:    [pair]
  Direction:     [long/short]
  Checklist:     [12/12] or [X/12 — which failed]
  Action taken:  [entered / not taken — reason]
  Outcome:       [if taken: result | if not taken: what would have happened]
```

*D.S.E/trading/skills | STIS Execution Layer | Pre-Trade Gate*

# SKILL — 5-MINUTE TRADING RITUAL
**The Ideal Daily Trading Interaction — Maximum Results, Minimum Time**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Daily — this defines how to interact with systematic positions
DEPARTMENT: D.S.E | STIS Operational Layer | Daily ritual
LOADS:      skill_morning-session-sequence.md (the 30-min prep)
            skill_stop-advancement-signal.md (if a signal has fired)
PRODUCES:   All necessary trading actions for the day completed in under 10 minutes
CROSS-REF:  skill_daily-risk-budget.md (position sizing)
            skill_position-management-protocol.md (what to do if in a position)
            skill_batch-signal-execution.md (when multiple signals fire)
```

---

## WHAT THIS IS

The ideal trading day takes under 10 minutes of active platform interaction. This is not a beginner shortcut — it is the expert outcome. When the system is well-built and the skills are loaded, there is almost nothing left to do manually except execute signals and advance stops.

---

## THE MORNING RITUAL (5 minutes)

```
06:50-07:00 UTC (20 min before London kill zone):

1. OPEN PLATFORM (30 seconds)
   → Check for any overnight systematic alerts that fired
   → Note any new structural highs across the portfolio

2. CHECK SIGNALS (1 minute)
   → Did any instruments make a new N-day high overnight?
   → YES → add to execution queue
   → NO  → skip to step 4

3. EXECUTE SIGNALS (2 minutes — or more if multiple)
   → For each signal: verify stop placement, calculate position size, place order
   → Set stop loss immediately upon fill
   → Confirm the order in the platform

4. ADVANCE STOPS IF TRIGGERED (1 minute)
   → Did any existing position make a new structural high?
   → YES → advance all stops on that position (see skill_stop-advancement-signal.md)
   → NO  → no action needed

5. CLOSE PLATFORM (30 seconds)
   → Unless it's an active intraday session
   → For systematic positions: close the screen, trading is done for the day
```

---

## THE AFTERNOON CHECK (2 minutes, optional)

```
13:00-13:15 UTC (NY kill zone open):

→ Check: did any new signals fire during the day?
→ Check: did any stops advance?
→ If intraday trading: is there a kill zone setup forming?
→ If not: no action needed, close screen
```

---

## THE EVENING CLOSE (2 minutes)

```
16:00-16:30 UTC (after NY session):

→ Log the day's activity (even "no trades" is a log entry)
→ Review: were any signals missed? Why?
→ Note: which instruments are approaching new high triggers?
→ Set alerts for tomorrow's watch levels
→ Close everything
```

---

## THE AUTOMATION HIERARCHY

```
FULLY AUTOMATED (zero time):
  → Stop loss execution (platform auto-executes)
  → Smart alert delivery (TradingView MCP fires to phone)
  → Morning brief generation (if AI agent is set up)

SEMI-AUTOMATED (1-2 min):
  → New signal execution (you place the order, platform manages the stop)
  → Stop advancement (you input the new level, platform adjusts)

MANUAL (5-10 min):
  → New position sizing calculation
  → Daily log entry
  → Weekly review
```

---

## THE PSYCHOLOGICAL CONTRACT

"Trading is a business, not a job."

A business owner doesn't do every task personally — they build systems and check results. The 5-minute ritual is what sovereign business ownership looks like in trading:

- The system generates signals
- You execute them
- The stops manage the risk
- The compounding manages the returns
- You live your life

**"Risking money and time together means you can lose both. Risk only money."**

---

## RULES

- If daily trading is taking more than 30 minutes, something is wrong — the system isn't built or the Observer isn't present
- Systematic long-term positions: morning check only, no intraday monitoring
- Intraday sessions: bounded to kill zones (07:00-09:30 or 13:00-15:00 UTC) — not all day
- Never open the platform "to see what's happening" — only open it when you have a specific action

*D.S.E/trading/skills | STIS Operational Layer | Daily Ritual*

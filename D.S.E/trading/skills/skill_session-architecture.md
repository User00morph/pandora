# SKILL — Session Architecture Read
**Three-Session Cascade | Asia Grab | London Sweep | NY Delivery**
**Load when:** Reading intraday price action. Identifying which session window is active and what it means.

---

## WHAT THIS IS

The trading day is not continuous. It is three overlapping institutional sessions — each with a distinct role in the institutional script. Asia MAPS the day's range and sets the direction signal. London SWEEPS the liquidity and CONFIRMS the bias. New York DELIVERS to the target. Entering without knowing which session you're in is entering without knowing what the institution is trying to do.

---

## SESSION WINDOWS (all times Eastern / New York)

| Session | Window | Role | Key Event |
|---------|--------|------|-----------|
| **Asia** | 6:00pm – 3:00am ET | Map the range, set the directional signal | Asia Grab: 2:00am – 4:00am ET |
| **London** | 3:00am – 9:00am ET | Sweep liquidity, confirm or reverse Asian bias | London Open: 3:00am ET |
| **New York** | 8:00am – 12:00pm ET | Deliver to target | NY Open: 8:00am ET |
| **NY Afternoon** | 12:00pm – 5:00pm ET | Danger zone — consolidation, choppy, traps | Avoid new entries after 12pm ET |
| **Killzones** | 2-4am, 7-9am, 9-11am ET | Highest probability entry windows | Trade within these only |

---

## THE ASIA GRAB — MOST CRITICAL EVENT OF THE DAY

**Window:** 2:00am – 4:00am Eastern Time

**What it is:** The institutional direction signal. While the Western retail collective is unconscious (asleep), the institution quietly establishes the day's directional intent. Price makes a defined move — UP or DOWN — in the Asia Grab window. This is the MAP.

**How to read it:**
1. At 4:00am ET (or at London open), identify what Asia did:
   - If Asia swept ABOVE a prior high → Asia Grab = UP → watch for London to confirm (or reverse)
   - If Asia swept BELOW a prior low → Asia Grab = DOWN → watch for London to confirm (or reverse)
   - If Asia was range-bound with no decisive move → No Asia Grab → wait for London for the signal

2. Mark the Asia High and Asia Low as key levels for the rest of the day

**The Asia Grab and London relationship:**
- London confirms Asia: price continues in the Asia Grab direction → highest probability setup
- London reverses Asia: price sweeps the OPPOSITE direction at London open → London took the Asian liquidity → the real move is now against the Asia Grab direction

---

## THREE-SESSION CASCADE READ

### Session 1: Asia (6pm – 3am ET)
**What to do:**
- At end of Asian session (3am ET), mark: Asia High, Asia Low, Asia Range
- Calculate range size — large Asian range = institutional intent active | small range = waiting
- Identify the Asia Grab direction (2-4am ET)
- Note any significant news events scheduled for London/NY (news = cover for institutional moves)

**Output:**
```
Asia: HIGH = [price] | LOW = [price] | Range = [pips]
Asia Grab: [UP / DOWN / NEUTRAL — describe the move]
```

---

### Session 2: London (3am – 9am ET)
**What to do:**
- At London open, watch the first 30-60 minutes
- London's first move often SWEEPS the Asian session liquidity (runs stops)
- After the sweep → the TRUE direction of the day is revealed
- London open sweep of Asia High = BEARISH for the day (shorts look for NY delivery lower)
- London open sweep of Asia Low = BULLISH for the day (longs look for NY delivery higher)
- London close (9am ET) is often a minor reversal point — be cautious of new entries after 9am

**The London Confirmation Question:**
Did London respect the Asia Grab direction (continue) or reverse it (sweep and flip)?
- London CONTINUED Asia direction → Triple confirmation → Strongest day bias
- London REVERSED Asia direction → London swept Asia liquidity → Real move = opposite of Asia Grab

**Output:**
```
London action: [swept Asia High / swept Asia Low / continued direction / range-bound]
London confirmation: [Asia confirmed / Asia reversed → new direction = ]
Day bias after London: [BULLISH / BEARISH / NEUTRAL]
Killzone entry window: 7:00am – 9:00am ET
```

---

### Session 3: New York (8am – 12pm ET)
**What to do:**
- NY Open (8am ET) often creates a Killzone impulse — watch for sweep of London high/low
- If London confirmed Asia direction → NY delivers to the target (first major liquidity pool above/below)
- Two-hour clock begins at the NY expansion candle
- NY lunch (12pm – 2pm ET) = institutional lunch = choppy, no new entries
- NY afternoon (2pm – 5pm ET) = late session = retail traps, fading activity

**Output:**
```
NY open action: [described]
Delivery direction: [confirmed / reversed at open]
Target: [first liquidity pool = price]
Two-hour clock started: [time]
Entry window: [NY Killzone 9-11am ET or NY Open 8-9am ET]
```

---

## WEEKLY CYCLE OVERLAY

The session architecture runs within the weekly cycle:

| Day | Role | Session Priority |
|-----|------|-----------------|
| Monday | Map only — institutional positioning, no delivery | Asia only — no entries |
| Tuesday | Highest probability entry day | All sessions active — prioritize |
| Wednesday | Mid-week expansion continues | London + NY primary |
| Thursday | Late expansion, watch for exhaustion | London primary |
| Friday | Institutional squaring — TRAP DAY | No new entries. Protect open positions. |

**Friday rule:** Institutions close positions heading into the weekend. Price often reverses Friday moves by the following week. Any Friday "breakout" is a trap. No new trades on Friday.

---

## DAILY READING PROTOCOL

**At 4:00am ET (pre-market):**
1. Open TradingView to primary pairs
2. Mark Asia High and Asia Low on each
3. Identify Asia Grab direction
4. Note any upcoming news (economic calendar)
5. Set bias for each pair pending London confirmation

**At 7:30am ET (London Killzone):**
1. Check if London has swept Asia High or Low
2. Update day bias based on London action
3. Begin Grade A filter evaluation for setups
4. Open positions only in the 7am-9am Killzone if setup is Grade A

**At 9:00am ET (NY Killzone):**
1. Check NY Open impulse
2. If missed London entry — evaluate NY Killzone (9am-11am) as secondary entry window
3. Two-hour clock on any expansion that begins here

**At 12:00pm ET:**
1. No new entries
2. Manage open positions only
3. Log the session: what did Asia Grab → London → NY produce?

---

## OUTPUT FORMAT

```
SESSION READ: [date] | [current time ET] | [active session]

ASIA:
  High: [price] | Low: [price] | Range: [pips]
  Asia Grab: [UP / DOWN / NEUTRAL] — [describe the 2-4am ET move]

LONDON:
  Action: [swept Asia High / swept Asia Low / range-bound / continued]
  Confirmation: [Asia confirmed → [direction] / Asia reversed → new direction = [direction]]

NY:
  Open action: [describe]
  Delivery direction: [confirmed / reversed]
  Two-hour clock: [start time if expansion began]

DAY BIAS: [BULLISH / BEARISH / NEUTRAL]
ACTIVE KILLZONE: [current / upcoming]
PRIMARY ENTRY WINDOW: [time window]
```

---

*D.S.E/trading/skills | Session Architecture | Pandora OS*
*The session tells you WHO is in control right now. Trade with the session that has the mandate.*

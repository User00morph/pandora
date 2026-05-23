# SKILL — MACRO FIELD READING
**Layer 3 Skill | D.S.E/trading/skills/**
**Skill File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: dse_framework_intermarket-chain.md, dse_framework_institutional-data-intelligence.md, dse_framework_banking-data-streams.md**
**Run: Weekly (full version, Sunday) / Daily (abbreviated)**

---

## PURPOSE

The macro field reading skill synthesizes the Layer 3 data stack into an actionable bias for each active pair. It answers: what is the fundamental field actually saying, right now, about where price is likely to go? This feeds into the hypothesis as the "Layer 3 confirmation" component.

---

## WEEKLY MACRO FIELD READ (SUNDAY — 30 MINUTES)

### MODULE 1 — THE INTERMARKET CHAIN (10 minutes)

Reference: `dse_framework_intermarket-chain.md`

**Step 1: DXY Assessment**

```
DXY current level: _____________ 
DXY weekly direction: [ ] Up [ ] Down [ ] Flat (ranging)
DXY weekly range: _________ to _________
Key DXY levels: Support at _________ | Resistance at _________

Is DXY trending or ranging?
[ ] Trending UP → Risk-off / USD strength / EM currencies weaker / gold pressure
[ ] Trending DOWN → Risk-on / USD weakness / commodities supported / gold supported
[ ] RANGING → R3 deliberation — no strong intermarket signal this week

DXY assessment: _______________
```

**Step 2: Yield Assessment**

```
US 10-year yield: _____________% 
Weekly direction: [ ] Rising [ ] Falling [ ] Flat
2-year yield: _____________%
Yield curve (2Y-10Y spread): +/- _____ bps → [ ] Steepening [ ] Flattening [ ] Inverting

30-year yield: _____________%
Is 30-year at multi-year high/low? [ ] Yes — note: _____________ [ ] No

Real yield (10-year TIPS): _____________%
Real yield direction: [ ] Rising [ ] Falling

YIELD CHAIN IMPLICATIONS:
Rising real yields: Gold pressure | USD support | Risk assets weaker
Falling real yields: Gold support | USD pressure | Risk assets stronger
Bear steepener (short end falling, long end rising): [Danger signal — fiscal concern premium]
Bull flattener (short end rising faster than long end): [Recession expectation signal]

Yield assessment this week: _______________
```

**Step 3: Gold**

```
Gold (XAU/USD) current level: $_____________
Weekly direction: [ ] Up [ ] Down [ ] Ranging
Key levels: Support _________ | Resistance _________

Is gold moving WITH or AGAINST DXY? 
[ ] Against (normal — gold rises when dollar falls) → normal intermarket behavior
[ ] With (both rising or both falling) → DIVERGENCE → unusual, investigate

Gold vs real yields:
Is gold rising despite rising real yields? [ ] Yes → STRONG SIGNAL (structural safe-haven buying dominant)
Is gold falling despite falling real yields? [ ] Yes → WEAK SIGNAL (gold-specific headwind)

Gold assessment: _______________
```

**Step 4: Risk Sentiment (Equities)**

```
S&P 500 weekly direction: [ ] Up [ ] Down [ ] Flat
VIX level: _____________ | Direction: [ ] Rising (fear) [ ] Falling (complacency)
VIX below 15: Extreme complacency → approaching Phase 4-5 narrative saturation
VIX 15-25: Normal range
VIX 25-35: Elevated fear → approaching Crisis phase
VIX above 35: Crisis phase active → reduce all positions, observation mode

Equity vs Gold relationship:
[ ] Both rising → risk-on with gold as additional safety (unusual — both benefiting simultaneously)
[ ] Equities rising, gold flat/falling → pure risk-on environment
[ ] Equities flat/falling, gold rising → safe-haven preference dominant (USD/JPY watch)
[ ] Both falling → Crisis phase, maximum stress

Risk sentiment assessment: _______________
```

**Step 5: Intermarket Chain Synthesis**

```
CHAIN SIGNAL:
DXY: [up/down/flat] + Bonds (yields): [up/down/flat] + Gold: [up/down/flat] + Equities: [up/down/flat]

STANDARD CHAIN READINGS:
DXY↑ / Yields↑ / Gold↓ / Equities↓ = Risk-off, USD strength, standard tightening signal
DXY↓ / Yields↓ / Gold↑ / Equities↑ = Risk-on, USD weakness, easing signal
DXY↓ / Yields↑ / Gold↑ / Equities↓ = BEAR STEEPENER = fiscal crisis signal = most dangerous configuration
DXY↑ / Yields↑ / Gold↑ / Equities↑ = All rising = inflation regime (unusual)

CURRENT CONFIGURATION: DXY[_] / Yields[_] / Gold[_] / Equities[_]
INTERPRETATION: _______________
MOST SUPPORTED TRADE DIRECTION: _______________
```

---

### MODULE 2 — COT ANALYSIS (10 minutes)

Reference: `dse_framework_institutional-data-intelligence.md`

COT data released every Friday at 3:30 PM EST for the prior Tuesday's positions. Check at newyorkfed.org or barchart.com/commitment-of-traders.

```
For each active pair, note the latest COT reading:

XAU/USD (GOLD):
  Commercial Hedgers: Net _________ contracts (LONG/SHORT)
  Previous week: _________ | Change: +/- _________
  Large Speculators (Hedge Funds): Net _________ contracts
  Small Speculators (Retail): Net _________ contracts
  Historical context: Is this at an extreme? [ ] Yes — _____________ [ ] No
  COT signal for gold: _______________

USD POSITIONING (US Dollar Index futures):
  Commercial Hedgers: Net _________ 
  Large Speculators: Net _________
  Current reading vs historical: Normal / Extreme long / Extreme short
  USD COT signal: _______________

JPY FUTURES:
  Commercial Hedgers: Net _________
  Large Speculators: Net _________ 
  Positioning extreme? [ ] Yes — _____________ [ ] No
  JPY COT signal: _______________

EUR FUTURES:
  Commercial Hedgers: Net _________
  Large Speculators: Net _________
  Positioning extreme? [ ] Yes — _____________ [ ] No
  EUR COT signal: _______________

GBP FUTURES:
  Commercial Hedgers: Net _________
  Large Speculators: Net _________
  Positioning extreme? [ ] Yes — _____________ [ ] No
  GBP COT signal: _______________

COT SYNTHESIS:
"This week's COT shows: [currency/asset] at [positioning extreme] → contra-indicator signal for [direction]
The smart money (Commercial Hedgers) is positioned [direction] on [instrument] at [magnitude].
This [supports / opposes] the current technical bias."
```

---

### MODULE 3 — BANKING DATA STREAMS (5 minutes)

Reference: `dse_framework_banking-data-streams.md`

```
RRP (Reverse Repo):
  Current level: $_____ billion
  Weekly trend: [ ] Rising (liquidity leaving system) [ ] Falling (liquidity entering system)
  Signal: _______________

SOFR vs Fed Funds Rate:
  SOFR: ____% | Fed Funds Upper Bound: ____%
  SOFR relative to FFR: [ ] Below (normal) [ ] Above (stress) | Spread: _____ bps
  Signal: _______________

EUR/USD Basis Swap:
  Current level: +/- _____ bps
  Trend: [ ] Widening positive (dollar shortage easing) [ ] Widening negative (dollar stress)
  Signal: _______________

FRA-OIS Spread:
  Current level: _____ bps
  Context: Normal < 15 bps | Elevated 15-50 bps | Stress > 50 bps | Crisis > 100 bps
  Signal: _______________

UPCOMING BIS QUARTER-END (if within 6 weeks):
  Next quarter-end: _______________
  Likely window dressing direction: _______________ (based on current DXY position)
  Signal: _______________

UPCOMING TREASURY AUCTION (this week, if any):
  Instrument: _____ | Date: _____ | Estimated demand signal: _______________
```

---

### MODULE 4 — ECONOMIC CALENDAR (5 minutes)

Reference: `dse_framework_economic-forces.md`

```
HIGH-IMPACT EVENTS THIS WEEK:

Day | Time (EST) | Event | Country | Expected | Prior
Monday: _______________
Tuesday: _______________
Wednesday: _______________
Thursday: _______________
Friday: _______________

RISK ASSESSMENT:
Is there an FOMC this week? [ ] Yes → NFP-level caution all week | [ ] No
Is there NFP this week? [ ] Yes → no new positions Thursday PM-Friday | [ ] No
Is there CPI this week? [ ] Yes → reduce size on USD pairs day before and day of | [ ] No

HIGH-IMPACT EVENT COUNT THIS WEEK: _____ 
If ≥ 3 high-impact events: REDUCED SIZE WEEK — max 0.75% risk per trade

OVERALL ECONOMIC CALENDAR RISK: [ ] Low | [ ] Medium | [ ] High | [ ] Very High (FOMC+NFP week)
```

---

### MODULE 5 — WEEKLY MACRO SYNTHESIS (3 minutes)

Bring all four modules together:

```
MACRO FIELD READING — WEEKLY SYNTHESIS

Intermarket signal: _______________
COT signals: _______________
Banking data signals: _______________
Economic calendar risk: _______________

PAIR-BY-PAIR MACRO BIAS:

XAU/USD: Layer 3 bias = [LONG/SHORT/NEUTRAL] | Strength: [Strong/Moderate/Weak]
Reasoning: _______________

USD/JPY: Layer 3 bias = [LONG/SHORT/NEUTRAL] | Strength: [Strong/Moderate/Weak]
Reasoning: _______________

EUR/USD: Layer 3 bias = [LONG/SHORT/NEUTRAL] | Strength: [Strong/Moderate/Weak]
Reasoning: _______________

GBP/USD: Layer 3 bias = [LONG/SHORT/NEUTRAL] | Strength: [Strong/Moderate/Weak]
Reasoning: _______________

WEEKLY MACRO STATEMENT (one paragraph, saved to session log):
"This week's macro field shows [intermarket summary]. COT data confirms [positioning read]. 
Banking streams show [banking read]. Economic calendar risk is [level] with [key events].
The strongest Layer 3 confirmation is for [pair] going [direction], supported by [primary data point].
Position sizing this week: [standard/reduced — reason]."
```

---

## DAILY ABBREVIATED MACRO CHECK (3 minutes)

Run as Phase 3 (Layer 3 check) in the Observer Calibration Protocol:

```
□ DXY overnight: [ ] Up [ ] Down [ ] Flat — net read for USD pairs: _______________
□ Yields (10-year): [ ] Up [ ] Down [ ] Flat — effect on gold: _______________
□ Gold overnight: [ ] Up [ ] Down [ ] Flat — consistent with yesterday's bias? [ ] Yes [ ] No
□ Any news overnight that changes the macro narrative? [ ] Yes — _____________ [ ] No
□ Any economic event today within 4 hours? [ ] Yes — _____________ (adjust position sizing) [ ] No

DAILY ONE-LINE MACRO READ:
"DXY is [direction], yields are [direction], gold is [direction]. Macro field today [supports/opposes/neutral] 
the [pair] [direction] bias. [Economic event name] at [time] — caution."
```

---

## CROSS-REFERENCES
- `dse_framework_intermarket-chain.md` — Module 1 reference
- `dse_framework_institutional-data-intelligence.md` — Module 2 reference
- `dse_framework_banking-data-streams.md` — Module 3 reference
- `dse_framework_economic-forces.md` — Module 4 reference
- `dse_framework_central-bank-doctrine.md` — central bank language layer
- `skill_dual-layer-chart-reading.md` — Phase 1 esoteric brief + Layer 3 confirmation come from this skill
- `skill_observer-calibration.md` — daily abbreviated version runs as Phase 3 in pre-session calibration

---

*skill_macro-field-reading.md | D.S.E/trading/skills/ | STIS Layer 3 Operational Skill*
*Status: v1.0 — active | Full version: Sunday. Abbreviated: daily pre-session.*

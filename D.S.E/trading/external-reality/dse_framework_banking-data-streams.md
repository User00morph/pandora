# BANKING DATA STREAMS
**Layer 3 — External Reality Field | D.S.E/trading/external-reality/**
**Framework File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: dse_framework_institutional-data-intelligence.md, dse_framework_power-architecture-decode.md (Nodes 1-2)**

---

## OPERATING DOCTRINE

> The COT report and the yield curve are the surface.
> Beneath them is the plumbing of the global banking system —
> the repo market, the Fed balance sheet, the TIC flows, the primary dealer positions.
> This is where the real institutional decision-making is visible
> before it appears anywhere else.
> Most traders never look here. That is the edge.

---

## SECTION 1 — THE COMPLETE BANKING DATA STACK

Nine data streams. Each one reveals a different layer of institutional behavior.
Together they form the most complete picture of where the real money is and where it is going.

```
BANKING DATA HIERARCHY (most leading → most lagging):

1. Fed RRP (Overnight) ──────── Daily — excess liquidity in system
2. SOFR ─────────────────────── Daily — overnight funding cost
3. Cross-Currency Basis Swap ── Daily — dollar stress in foreign banks
4. FRA-OIS Spread ────────────── Daily — bank credit risk premium
5. NY Fed Primary Dealer Stats ─ Weekly — what the 24 banks actually hold
6. Fed Balance Sheet (H.4.1) ─── Weekly — the Fed's own position
7. Treasury Auction Results ──── Periodic — foreign demand for US debt
8. TIC Data ─────────────────── Monthly (6-week lag) — sovereign flows
9. BIS Quarterly Statistics ──── Quarterly — global cross-border banking
```

---

## SECTION 2 — THE FED REVERSE REPO PROGRAM (RRP)

### What It Is

The Fed's overnight Reverse Repo facility allows money market funds, banks, and government-sponsored enterprises to park excess cash at the Fed overnight at the Fed Funds Rate. When the RRP balance is high, it means excess liquidity is sitting idle at the Fed rather than flowing into markets.

**Source:** fred.stlouisfed.org → RRPONTSYD (daily)
**Release:** Daily at approximately 4:30 PM EST

### How to Read It

| RRP Balance | Market Signal |
|---|---|
| **Rising (above $1T)** | Massive excess liquidity in the system. Money has nowhere to go. This excess eventually finds its way into risk assets — bullish for equities and gold when it starts flowing out. |
| **Falling rapidly** | Liquidity draining from the system. This cash is moving somewhere — into T-Bills, into markets, or being absorbed by Treasury issuance. Watch what it flows INTO. |
| **Near zero** | System is fully absorbed. No excess liquidity buffer. When a shock hits, banks have no cushion — volatility risk elevated. |

**The RRP-Dollar Connection:**
When RRP is falling AND Treasury issuance is rising, the excess cash is being absorbed into new T-Bills. This creates demand for dollars (to buy T-Bills) which can strengthen the DXY temporarily. When the RRP drain completes, this T-Bill-driven dollar demand fades.

**Current status (2026):** QT ended December 2025. RRP has been draining. Monitor the current level at FRED — when RRP approaches near-zero, system liquidity is tightest. This is the precondition for the most acute market stress events.

---

## SECTION 3 — SOFR (SECURED OVERNIGHT FINANCING RATE)

### What It Is

SOFR measures the cost of borrowing cash overnight using US Treasury securities as collateral. It replaced LIBOR as the global reference rate for dollar-denominated financial contracts. SOFR governs approximately $200 trillion+ in financial contracts globally.

**Source:** newyorkfed.org/markets/reference-rates/sofr (daily, published 8:00 AM EST)
**FRED series:** SOFR

### How to Read It

SOFR should trade very close to the Fed Funds Rate. When SOFR deviates from the Fed Funds Rate:

| SOFR Behavior | Signal |
|---|---|
| SOFR significantly above Fed Funds Rate | Repo market stress — collateral is tight, demand for cash exceeds supply. Potential liquidity crunch. |
| SOFR significantly below Fed Funds Rate | Excess cash in the system — banks are competing to place cash. Usually means RRP is elevated. |
| SOFR spiking suddenly | Emergency — a large participant is scrambling for overnight funding. Watch for news of institutional stress. September 2019 repo spike was the early warning of the 2020 liquidity issues. |

**The SOFR-Dollar relationship:**
SOFR spikes → dollar funding stress → DXY tends to spike (safe haven demand for dollars) → risk assets sell off. This is the sequence that precedes acute market events. SOFR is the earliest warning signal in the banking data stack.

---

## SECTION 4 — THE CROSS-CURRENCY BASIS SWAP (DOLLAR FUNDING STRESS GAUGE)

### What It Is

The EUR/USD cross-currency basis swap measures how expensive it is for non-US banks to borrow US dollars using euros as collateral. Normally, the basis should be zero (perfect market efficiency). When it deviates from zero, it measures dollar funding stress.

**Source:** Bloomberg, Refinitiv (professional). As a proxy: watch USD/JPY, DXY, and FRA-OIS in combination.

### How to Read It

**Basis = 0:** Perfect market. No dollar funding stress.
**Basis negative (below zero):** Dollar shortage. Non-US banks are paying a premium to access dollars. This is stress. The more negative, the more acute the dollar shortage.
**Basis positive / rising toward zero:** Dollar stress easing. The premium is fading. Risk conditions improving.

**Current read (March-May 2026):**
The EUR/USD 1-year basis rose to approximately +11.23 basis points — dollar funding stress is EASING. This is consistent with the post-Q1 recovery narrative and the DXY at 99 (neither surging nor collapsing). When this basis was lower (more negative) earlier in 2026, it was signaling the dollar stress that accompanied Q1 volatility.

**Why this matters for forex:**
- Negative basis → dollar shortage → DXY spikes → EUR/USD falls → JPY rallies (safe haven)
- Basis rising toward zero → stress easing → DXY softens → EUR/USD recovers → risk currencies recover
The basis swap is often 2-3 days ahead of the price action in EUR/USD.

---

## SECTION 5 — FRA-OIS SPREAD (BANK CREDIT RISK MONITOR)

### What It Is

The FRA-OIS (Forward Rate Agreement minus Overnight Index Swap) spread measures how much banks charge each other for short-term credit above the risk-free overnight rate. It is the dollar-denominated version of the old LIBOR-OIS spread — the original "fear gauge" of the banking system.

**Normal range:** 5-15 basis points (healthy system)
**Stressed range:** 30-50+ basis points (bank credit concerns)
**Crisis level:** 100+ basis points (acute banking stress — seen in 2008, early 2020)

### How to Read It

| FRA-OIS Level | Market Signal |
|---|---|
| Below 15 bps | Healthy interbank market. Banks trust each other. Normal trading conditions. |
| 15-30 bps | Mild stress. Some uncertainty in short-term bank funding. Reduce position sizes. |
| 30-50 bps | Significant stress. Banks are applying a meaningful risk premium to each other. Be defensive. |
| Above 50 bps | Acute banking system stress. Go to maximum risk-off positions. JPY, CHF, Gold, Cash. |
| Above 100 bps | Crisis level. Seen only in 2008 and March 2020. |

**The FRA-OIS and forex:**
High FRA-OIS → banks are charging each other more → credit conditions tighten → risk assets sell → JPY and CHF surge → USD may spike initially then fall as the Fed eventually intervenes with liquidity.

---

## SECTION 6 — NY FED PRIMARY DEALER STATISTICS (FR 2004)

### What It Is

The Federal Reserve Bank of New York collects weekly data from all 24 Primary Dealers on:
- Their outright positions in Treasury securities, agency debt, mortgage-backed securities, and corporate bonds
- Their repo and reverse repo financing positions
- Their fails (failures to deliver or receive securities)

This is the most direct window into what the 24 banks that run the market are actually holding.

**Source:** newyorkfed.org/markets/counterparties/primary-dealers-statistics
**Release:** Thursdays at ~4:15 PM EST, covering the prior week's data

### What to Watch

**Treasury positioning:** When Primary Dealers are accumulating Treasury positions → they expect yields to fall (prices to rise). When reducing → they expect yields to rise (prices to fall). This is more sophisticated than COT because it shows the actual balance sheet of the dealers who SET the market.

**Repo financing levels:** When Primary Dealers are financing large positions through repo → they are carrying large inventories using short-term borrowing → they are leveraged. A sudden spike in repo financing = a large bet was placed. A sudden drop = they are reducing exposure (risk-off behavior).

**Fails:** When fails spike (dealers failing to deliver securities on time) → the system is under stress. Collateral is tight. Something structural is straining.

**The Primary Dealer Survey:**
The NY Fed also surveys Primary Dealers before each FOMC meeting on their expectations for the Fed Funds Rate path. This survey reveals what the 24 banks think the Fed will do — which is more valuable than any analyst forecast because these banks ARE the transmission mechanism of monetary policy.

---

## SECTION 7 — THE FED BALANCE SHEET (H.4.1)

### What It Is

The Federal Reserve publishes its balance sheet every Thursday at 4:30 PM EST. It shows exactly what the Fed owns (assets) and owes (liabilities).

**Source:** federalreserve.gov/releases/h41/current/
**FRED series:** WALCL (total assets, Wednesday level)

### Current State (May 2026)

- **Total assets:** $6.7 trillion (as of May 13, 2026)
- **Change from prior week:** +$19 billion (slight increase)
- **Change from 1 year ago:** +$15 billion (essentially flat — QT ended)
- **QT status:** QT officially ended December 2025. The Fed ran QT (shrinking the balance sheet) from June 2022 to December 2025, reducing assets from ~$9 trillion peak to ~$6.7 trillion. Only approximately half of the pandemic-era expansion was reversed.

### What This Means

**QT ending is a structural shift:**
When the Fed is doing QT (selling assets, draining reserves), it removes liquidity from the banking system. This tightens financial conditions even without rate hikes. QT ending in December 2025 means the passive liquidity drain has stopped. But the balance sheet remains elevated at $6.7 trillion — still roughly double pre-pandemic levels.

**The composition matters:**
- Treasury holdings: The primary driver of duration risk and the yield curve
- MBS (Mortgage-Backed Securities): The Fed is letting these run off into Treasury purchases — this gradually reduces the Fed's footprint in the housing market
- Reserves: The liability side shows how much cash commercial banks are holding at the Fed. High reserves = healthy banking system liquidity. Low reserves = stress risk.

**The SOMA (System Open Market Account):**
The NY Fed manages the SOMA — the portfolio of assets the Fed actively buys and sells. SOMA operations are the actual mechanism of QE and QT. Weekly SOMA statements show exactly what the Fed bought and sold.

**Trading implications of the balance sheet:**
- Balance sheet expanding (QE) → liquidity injected → risk assets rally, dollar weakens
- Balance sheet contracting (QT) → liquidity drained → financial conditions tighten, risk assets face headwind
- Balance sheet flat (current) → neutral liquidity condition — market direction driven by rate expectations, not balance sheet

---

## SECTION 8 — TREASURY INTERNATIONAL CAPITAL (TIC) DATA

### What It Is

The US Treasury publishes monthly data on foreign ownership of US financial assets. The most important component: who owns US Treasury securities and whether they are buying or selling.

**Source:** home.treasury.gov/data/treasury-international-capital-tic-system
**Release:** Monthly, approximately 6 weeks after the reference month
**Data tool:** ticdata.treasury.gov → Table 5 (Major Foreign Holders)

### Current Holdings (April 2026)

| Country | Holdings | Trend Signal |
|---|---|---|
| **Japan** | $1.13 trillion | Largest single foreign holder. BOJ policy changes directly affect Japan's incentive to hold Treasuries. |
| **United Kingdom** | $768 billion | Primarily held by financial institutions and funds, not the UK government. |
| **China** | $760 billion | Declining from peak of ~$1.3T in 2013. Diversifying away from USD. |
| **Total foreign** | ~$8.5 trillion | 28-30% of all marketable US Treasury debt is foreign-owned. |

### The Critical Signal: Official Institution Flows

**February 2026 TIC reading:**
- Foreign private inflows: +$166.5 billion (private investors bought US assets)
- Foreign official institution flows: **-$46.1 billion** (central banks and sovereign wealth funds SOLD US Treasuries)

**What this means:**
Foreign OFFICIAL institutions (central banks, sovereign wealth funds) sold $46 billion of US Treasuries in a single month. This is the most important TIC signal. These are not speculative sellers — they are strategic, long-term holders making a structural decision.

Combined with:
- The 30-year yield at 18-year highs (5.2%) — foreigners demanding higher compensation
- Gold at $4,564 — real asset preferred over US paper
- DXY not rising despite high yields — dollar reserve status being questioned

The TIC data confirms the intermarket chain signal: the reserve currency architecture is under structural review. Foreign central banks are quietly reducing their US Treasury exposure. This is not a crash signal — it is a decade-long structural shift accelerating.

**The China TIC Story:**
China has reduced its US Treasury holdings from $1.3 trillion (2013) to $760 billion (2026) — a 42% reduction over 13 years. This is the most important long-term TIC signal. It represents China's deliberate de-dollarization strategy. The mechanism: China earns dollars through trade, but instead of recycling them into US Treasuries (as they did for decades), they are buying gold, physical commodities, infrastructure in Belt and Road nations, and yuan-denominated assets.

China's gold reserves have increased every year during this period. The TIC-to-Gold correlation is the data expression of the esoteric principle: when the Saturn-Neptune dissolution removes trust in institutional paper structures, the R2 asset (gold) accumulates.

---

## SECTION 9 — BIS QUARTERLY BANKING STATISTICS

### What It Is

The Bank for International Settlements publishes quarterly data on cross-border banking flows — loans, deposits, and securities holdings across all BIS member banks globally.

**Source:** bis.org/statistics/bankstats.htm
**Release:** Quarterly, approximately 3-4 months after the reference quarter

### Why It Matters

The BIS data shows which direction the global banking system is moving capital:
- When cross-border lending is expanding → global risk appetite is up → risk currencies supported
- When cross-border lending is contracting → global risk appetite is down → safe havens strengthening
- When a specific geography shows unusual inflows → capital is rotating into that region

**The BIS quarter-end effect (operationally critical):**
Banks report their balance sheets to the BIS at each quarter-end (March, June, September, December). In the final 2 weeks of each quarter, banks reduce their cross-border exposures to appear leaner on their quarterly filings. This is called "window dressing."

**The window dressing trade:**
- 2 weeks before quarter-end: Banks reduce exposure → dollar funding tightens → DXY can spike → risk assets face pressure
- After quarter-end: The window dressing reverses → dollar funding normalizes → DXY retraces → risk assets recover
This is a repeating, predictable, calendrical institutional behavior.

**Upcoming quarter-ends:** June 30, September 30, December 31, 2026.

---

## SECTION 10 — TREASURY AUCTION INTELLIGENCE

### What It Is

The US Treasury auctions new debt regularly. The results of these auctions reveal whether there is strong or weak demand for US debt at current yields — the most direct measure of market confidence in the US fiscal position.

**Source:** treasurydirect.gov/auctions/
**Key auctions:** 2-year (monthly), 5-year (monthly), 10-year (monthly), 30-year (monthly)
**Results published:** Same day as auction, approximately 1:00 PM EST

### Reading Auction Results

| Metric | What It Measures | Signal |
|---|---|---|
| **Bid-to-Cover (BTC) Ratio** | Total bids submitted ÷ amount sold | BTC above 2.5 = strong demand. Below 2.0 = weak demand = yields likely to rise further. |
| **Indirect Bidder %** | Foreign buyers (central banks, foreign institutions) | High indirect % = strong foreign demand for US debt. Low = foreigners stepping back. This is the live TIC signal before the 6-week lag. |
| **Direct Bidder %** | Domestic institutions | Rising direct % + falling indirect % = US institutions picking up what foreigners are leaving. This is a stress signal. |
| **Stop-out Rate vs. Pre-Auction Yield** | Whether auction cleared above or below market expectations | Clearing above market (higher yield) = weak auction = BEARISH for bonds, potential USD sell-off if pattern continues |

**The 30-year auction as a stress barometer:**
Given the 30-year at 18-year highs (5.2%), every 30-year auction result is critical. Weak 30-year auctions (low BTC, high yield clearing, low indirect bidder %) are the data confirmation that foreign central banks are stepping back from long-term US debt. This is the structural signal beneath the 30-year yield level.

**Auction calendar (monthly, verify at TreasuryDirect):**
- 2-year note: Monthly, last week
- 5-year note: Monthly, last week
- 10-year note: Monthly, mid-month
- 30-year bond: Monthly, mid-month (typically day after 10-year)

---

## SECTION 11 — THE INTEGRATED BANKING DATA READ (CURRENT — 2026-05-19)

Running all nine streams together:

```
FED BALANCE SHEET:   $6.7T — QT ended Dec 2025. Flat/stable. Neutral liquidity.
                     Signal: No active QE = no Fed-driven risk asset inflation.
                             No active QT = no Fed-driven liquidity drain.
                             Market must find its own direction — more sensitive to TIC/Primary Dealer flows.

RRP:                 Monitor current level. If near zero → system is fully absorbed.
                     With QT ended, excess liquidity has been largely absorbed.
                     Any new stress event hits a system with less buffer.

SOFR:               Should be trading near Fed Funds Rate (verify current rate).
                     Any sudden SOFR spike = repo market stress = early crisis warning.

CROSS-CURRENCY BASIS: EUR/USD basis at ~+11 bps (March data, likely similar May).
                     EASING — dollar stress has improved from Q1 peak.
                     This is consistent with DXY at 99 (not surging) and risk recovering.

FRA-OIS:            Below 20 bps (implied from basis swap and current market calm).
                     Healthy interbank market. Not signaling acute bank stress.

PRIMARY DEALER:     Verify weekly. Key question: are dealers building or reducing Treasury positions?
                     With 30Y at 5.2%, if dealers are REDUCING → they expect yields to rise further.
                     If BUILDING → they think 5.2% is attractive and are front-running a rally.

TIC DATA:           Foreign official institutions sold $46.1B in February 2026.
                     China at $760B (declining long-term trend).
                     Japan at $1.13T (BOJ policy change = their incentive to hold shifting).
                     CRITICAL: The 30Y at 5.2% reflects this structural foreign selling.

TREASURY AUCTIONS:  Watch each 30-year auction for bid-to-cover and indirect bidder %.
                     Weak 30Y auctions = foreign selling continues → yields rise further.
                     Strong 30Y auctions = the yield level has attracted buyers → yield ceiling found.

BIS QUARTER-END:    June 30 is 6 weeks away.
                     Begin monitoring for dollar funding tightening in mid-June.
                     The BIS quarter-end window dressing may create a DXY pop in mid-late June.
                     This would be a tactical move, not a trend reversal.

SYNTHESIS:
  The banking data stack confirms the intermarket chain read:
  - The system has absorbed QT. There is no Fed stimulus pushing markets up.
  - Foreign official selling of US debt is structural and ongoing.
  - The 30-year yield reflects this structural selling, not a growth signal.
  - Short-term: dollar funding stress is easing (basis swap improving) → short-term risk-on possible.
  - Medium-term: the structural foreign selling of US Treasuries + 18-year high yields = the
    Sovereign's reserve currency thesis remains intact → Gold, real assets preferred.
  - Tactical: Watch the June 30 BIS quarter-end for a temporary DXY spike (window dressing).
    This is a sell-the-DXY-spike opportunity, not a buy signal.
```

---

## SECTION 12 — THE WEEKLY BANKING DATA RITUAL (ADD TO SUNDAY PROTOCOL)

**Add to the Sunday Institutional Data Check from `dse_framework_institutional-data-intelligence.md`:**

```
ADDITIONAL BANKING DATA CHECKS (Sunday):

7. FED BALANCE SHEET (Thursday release)
   Source: fred.stlouisfed.org → WALCL
   Check: Is total assets rising, falling, or flat?
   Note: Any large weekly change (+/- $50B) = something significant happened at the Fed.

8. SOFR (Daily, check Monday AM)
   Source: newyorkfed.org/markets/reference-rates/sofr
   Check: Is SOFR at/near the Fed Funds Rate?
   Alert: Any spike above Fed Funds Rate + 10 bps = repo market stress.

9. RRP BALANCE (Daily)
   Source: fred.stlouisfed.org → RRPONTSYD
   Check: Is the RRP rising (excess liquidity accumulating) or falling (being absorbed)?
   Context: Rapidly falling RRP = liquidity tightening regardless of Fed rate stance.

10. PRIMARY DEALER STATS (Thursday release)
    Source: newyorkfed.org/markets/counterparties/primary-dealers-statistics
    Check: Are dealers building or reducing Treasury and risk asset positions?
    Context: Dealer reduction of positions = they are reducing risk exposure. Bearish.

11. UPCOMING TREASURY AUCTIONS THIS WEEK
    Source: treasurydirect.gov
    Check: Any 10Y or 30Y auctions? Monitor results at 1PM EST on auction day.
    Alert: BTC below 2.2 or indirect bidder below 55% on a 10Y or 30Y = weak auction = bearish bonds.
```

---

## CROSS-REFERENCES
- `dse_framework_institutional-data-intelligence.md` — COT, DXY, yield curve (surface layer)
- `dse_framework_intermarket-chain.md` — how banking data flows into the intermarket chain
- `dse_framework_central-bank-doctrine.md` — the policy framework behind the balance sheet
- `dse_framework_power-architecture-decode.md` — Node 1 (BIS), Node 2 (Fed), Node 5 (Primary Dealers)
- `2026-05-19_dse_intelligence_current-field.md` — live synthesis integrating all layers

---

*dse_framework_banking-data-streams.md | D.S.E/trading/external-reality/ | STIS Layer 3*
*Status: v1.0 — active | Update Section 11 current read monthly.*
*Data sources: federalreserve.gov, newyorkfed.org, ticdata.treasury.gov, bis.org, fred.stlouisfed.org*

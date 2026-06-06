# SKILL — CROSS-ASSET CORRELATION READ
**Identifying Which Assets Are Moving Together and Who Survives**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  During market stress periods, portfolio construction decisions,
            or when multiple positions are declining simultaneously
DEPARTMENT: D.S.E | STIS Layer 3 (External Reality) | Portfolio architecture
LOADS:      skill_relative-strength-analysis.md (for ratio charts)
            skill_inflation-asset-thesis.md (macro context)
PRODUCES:   Correlation state + survivor assets + expected recovery sequence
CROSS-REF:  skill_crash-positioning-protocol.md (what to do with findings)
            skill_uncorrelated-portfolio-architecture.md (portfolio design)
            skill_portfolio-concentration-management.md (concentration analysis)
```

---

## WHAT THIS IS

When multiple assets fall simultaneously, understanding the correlation tells you whether this is a temporary liquidity event or a structural shift. It also reveals which assets are genuinely uncorrelated and which are falsely believed to be independent.

---

## THE CORRELATION MATRIX (STIS STANDARD PORTFOLIO)

```
            S&P   NASDAQ  GOLD   SILVER  BTC   NIKKEI  EUR/USD
S&P     1.0   0.95    -0.2   -0.1   0.65   0.75    -0.30
NASDAQ  0.95   1.0    -0.2   -0.1   0.70   0.70    -0.30
GOLD   -0.2   -0.2    1.0    0.85  0.15   -0.10    0.30
SILVER -0.1   -0.1    0.85   1.0   0.20   -0.10    0.25
BTC     0.65  0.70    0.15   0.20  1.0    0.40    -0.10
NIKKEI  0.75  0.70   -0.10  -0.10  0.40   1.0    -0.50
EUR/USD-0.30 -0.30   0.30   0.25 -0.10  -0.50    1.0

Note: Correlations increase in crisis conditions — all assets can fall together
      temporarily during forced selling / liquidity events
```

---

## THE CORRELATION CRASH READ

### SCENARIO 1: Equity-Led Decline (normal bear market)
```
Pattern: S&P + NASDAQ + BTC falling | Gold RISING | Silver neutral
Interpretation: Risk-off rotation from growth assets to safe havens
Recovery order: Gold recovers first → Nikkei/Europe → S&P/NASDAQ → BTC last
Position: Increase gold exposure if stopped out of equities
```

---

### SCENARIO 2: Dollar Strength Event
```
Pattern: Gold + EUR/USD + BTC falling | S&P FLAT or RISING | DXY surging
Interpretation: Dollar squeeze — capital repatriating to USD
Recovery order: Short-lived typically (weeks) → EUR/USD recovers first
Position: Reduce leveraged USD-denominated short-side exposure; gold will recover
```

---

### SCENARIO 3: Liquidity Crisis (forced selling)
```
Pattern: ALL assets falling simultaneously, including gold
Interpretation: Forced selling across all asset classes (margin calls, fund redemptions)
Recovery order: Gold first (safe haven demand returns) → equities → crypto last
Duration: Typically 2-8 weeks (see COVID March 2020, 2008)
Position: Cash and gold only — wait for forced selling to exhaust
```

---

### SCENARIO 4: Crypto-Specific Event (exchange failure, regulation)
```
Pattern: BTC + ETH falling sharply | Gold + Equities UNAFFECTED
Interpretation: Crypto-specific risk event, not macro
Recovery order: Depends on the event — regulatory = slow, exchange = fast
Position: Crypto stops get hit → move to equity and gold positions
```

---

## THE SURVIVOR IDENTIFICATION PROTOCOL

During any market decline:

```
STEP 1: List all portfolio positions with current status
STEP 2: Identify which are STILL in bull signal (above stop loss)
STEP 3: For survivors — check relative strength vs. their benchmark
  Rising RS in a declining market = extraordinary institutional demand
  → These are the assets to consider increasing when others stop out

STEP 4: Check the "hidden bull markets"
  Examples from Travis Woo:
  - During the 2025 crash: Nikkei, TRX still in bull signals
  - TRX/BTC ratio making new highs even while everything else fell
  → These anomalies reveal where institutional preference has genuinely shifted
```

---

## OUTPUT FORMAT

```
CORRELATION READ — [DATE]
MARKET STATE: [Risk-off / Liquidity crisis / Dollar strength / Crypto-specific / Normal]

ASSET STATUS:
  S&P 500:  [above/below stop | RS vs World EQ: up/dn]
  NASDAQ:   [above/below stop | RS vs S&P: up/dn]
  Gold:     [above/below stop | RS vs DXY: up/dn]
  Silver:   [above/below stop | RS vs Gold: up/dn]
  Bitcoin:  [above/below stop | RS vs Gold: up/dn]
  Nikkei:   [above/below stop | RS vs S&P: up/dn]

SURVIVORS (still in bull signal):
  [List assets above their stops]

HIDDEN BULLS (outperforming in declining market):
  [Assets with rising RS despite broad decline]

EXPECTED RECOVERY SEQUENCE:
  [Based on scenario type: which recovers first]

PORTFOLIO ACTION:
  [What to do based on this read]
```

*D.S.E | STIS Layer 3 | Cross-Asset Correlation Analysis*

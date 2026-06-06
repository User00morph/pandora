# SKILL — TRADINGVIEW MCP WORKFLOW
**Claude Code ↔ TradingView Real-Time Connection**
**Load when:** Building, modifying, or troubleshooting any TradingView Pine Script setup.
**Department:** D.I.I | STIS Infrastructure | AI-chart integration

---

## WHAT THIS IS

The TradingView MCP connects Claude Code directly to the TradingView desktop app. Claude writes Pine Script → it appears on the chart instantly. No copy-paste. No manual installation. Changes happen in real-time via conversation.

---

## INSTALLATION

```
FIRST TIME SETUP:
  1. Paste the one-shot prompt into Claude Code terminal
  2. Claude detects MCP is not installed → runs install script automatically
  3. Follow the on-screen instructions (< 2 minutes)
  4. Restart the terminal when prompted

VERIFY MCP IS ACTIVE:
  1. Open new terminal
  2. Start Claude: claude --dangerously-skip-permissions
  3. Type: /mcp
  4. Press Enter
  5. See TradingView listed in active MCPs → connection confirmed
  6. Close terminal, open fresh one, paste original prompt
```

---

## THE REAL-TIME WORKFLOW

```
TELL CLAUDE:                          WHAT HAPPENS ON TRADINGVIEW:
"Add a 200-period MA"             →   200 MA appears on chart
"Change session colors to blue"   →   Session boxes update color
"Track BTC, ETH, SOL"             →   Screener updates to those assets
"Remove the RSI panel"            →   RSI panel disappears
"Fix this error: [error text]"    →   Claude patches the Pine Script
```

---

## ERROR HANDLING

Claude Code detects Pine Script errors automatically and self-repairs. Common errors it handles:
- `bgcolor` in local scope → moves to global scope
- `talib` function scope issues → restructures the call
- `max_lines_count` exceeding 500 → reduces to cap
- Version conflicts → updates syntax to V6 standard

If self-repair fails: paste the error message to Claude directly → it explains and fixes.

---

## THE dangerouslySkipPermissions FLAG

```
claude --dangerously-skip-permissions
```

Reduces the "do you want to proceed?" prompts that slow down the workflow. Appropriate for trusted local builds like chart indicators. Do NOT use on systems with access to production APIs or live trading accounts.

---

## PAIRING WITH THE STIS

The MCP workflow is how the STIS technical analysis layer is built and maintained:
- GEX levels from `gex_engine.py` → exported as Pine Script → installed via MCP
- Markov state → visualized as matrix overlay → installed via MCP
- Session kill zones → built once, maintained via conversation

*D.I.I | STIS Infrastructure | Source: Travis Woo TradingView Tricks video*

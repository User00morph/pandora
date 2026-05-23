# SKILL — TRADINGVIEW MCP
**Load when: initiating a trading session, running chart analysis, building Pine Script, or executing the morning brief protocol.**
**Loadable by: D.S.E (trading), D.I.I (MCP integration).**

---

## WHAT THIS SKILL IS

The TradingView MCP server wires Claude Code directly into TradingView Desktop via Chrome DevTools Protocol. All data stays local — nothing leaves the machine. This skill governs how to use the MCP tools, run the morning brief workflow, and integrate the trading rules config within Pandora OS sessions.

**Repo:** `~/tradingview-mcp-jackson/`
**Requirement:** TradingView Desktop app running with DevTools enabled on port 9222.

---

## HEALTH CHECK (RUN FIRST)

```
tv_health_check        — verify MCP connection to TradingView Desktop
```

If health check fails: confirm TradingView Desktop is open and DevTools port 9222 is accessible.

---

## TOOL CATEGORIES

### CHART TOOLS
```
chart_set_symbol(symbol)                        — switch to instrument
chart_set_timeframe(timeframe)                  — set timeframe (1, 5, 15, 60, D, W)
chart_get_state()                               — get current symbol, timeframe, studies
chart_scroll_to_date(date)                      — navigate to specific date
chart_set_visible_range(from_date, to_date)     — zoom to date window
chart_get_visible_range()                       — check what is currently visible
chart_manage_indicator(action, name, entity_id) — add/remove/list indicators
indicator_set_inputs(entity_id, inputs)         — customize indicator settings
```

**Indicator naming rule:** Use FULL names only.
```
"Relative Strength Index"      (not RSI)
"Moving Average Exponential"   (not EMA)
"Moving Average"               (for SMA)
"Volume"
"VWAP"
"Average True Range"
"MACD"
"Bollinger Bands"
```

---

### DATA TOOLS
```
data_get_ohlcv(symbol, timeframe, bars)       — pull historical price data
quote_get(symbol)                             — current real-time price
symbol_info(symbol)                           — metadata: exchange, type, session
data_get_indicator(entity_id, bars)           — read indicator values
data_get_strategy_results()                   — overall strategy metrics
data_get_trades(max)                          — individual trade list
data_get_equity()                             — equity curve data points
```

---

### DRAWING TOOLS
```
draw_shape(type, params)     — add chart markup
draw_clear()                 — remove all drawings

Shape types:
  horizontal_line            — support/resistance levels
  trend_line                 — channel / trendline (requires two points)
  text                       — annotation
```

---

### REPLAY TOOLS
```
replay_start(date)           — enter replay mode at starting date
replay_step(bars)            — advance N bars
replay_autoplay(speed)       — continuous playback at speed
replay_trade(action)         — execute trade in replay (buy/sell/close)
replay_status()              — current date, position, P&L
replay_stop()                — exit replay mode
```

---

### BATCH / SCAN TOOLS
```
batch_run(symbols, timeframes, action)    — run action across multiple instruments
watchlist_get()                           — read all symbols on watchlist
watchlist_add(symbol)                     — add symbol to watchlist
```

**Batch actions:**
- `get_strategy_results` — compare strategy performance across symbols
- `screenshot` — visual comparison across instruments

---

### CAPTURE
```
capture_screenshot(region)    — screenshot the chart or strategy tester
  regions: "chart", "strategy_tester", "full"
```

---

## MORNING BRIEF WORKFLOW

The morning brief is the primary pre-session intelligence protocol. It applies `rules.json` automatically.

```bash
tv brief                      # CLI: run morning brief from terminal
```

Or via MCP:
```
morning_brief()               — scan watchlist, read indicators, generate session bias
session_save()                — save today's brief to ~/.tradingview-mcp/sessions/
session_get(date)             — retrieve a prior session brief for comparison
```

**Morning brief output:** Structured bias per symbol — direction, key levels, rule compliance status, confluence score.

---

## RULES.JSON INTEGRATION

```
~/tradingview-mcp-jackson/rules.json
```

Contains Morph's sovereign trading rules:
- Bias criteria (what must align for a trade)
- Risk rules (position sizing, max daily drawdown)
- Watchlist (instruments in scope)

The morning brief applies these rules automatically. Edit `rules.json` directly to update operating parameters. Never override rules inside a session — update the file.

---

## PINE SCRIPT DEVELOPMENT (QUICK REFERENCE)

```bash
# Pull current script from TradingView
node scripts/pine_pull.js       # saves to scripts/current.pine

# Push and compile
node scripts/pine_push.js       # injects + compiles, reports errors
```

Full Pine development loop: load `skill_pine-develop.md` in `D.S.E/trading/skills/`.

---

## D.I.I INTEGRATION NOTE

MCP server config lives in `~/.claude/.mcp.json`:
```json
{
  "mcpServers": {
    "tradingview": {
      "command": "node",
      "args": ["/Users/emoefedorgu/tradingview-mcp-jackson/src/server.js"]
    }
  }
}
```

To verify MCP is registered: `tv_health_check`.

---

*SKILL_TRADINGVIEW_MCP | Pandora OS | D.S.E trading + D.I.I integration*
*"The chart is the exhaust. The MCP reads the engine."*

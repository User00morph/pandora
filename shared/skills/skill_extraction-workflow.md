# SKILL — EXTRACTION WORKFLOW
**All departments. All agents. Load before any file interaction.**
**Full reference: `skill_extraction-workflow_full.md`**

## COGNITIVE PROMPT — RUN BEFORE EVERY FILE ACTION
1. **WHAT EXACTLY** am I looking for? One sentence. If you can't name it — clarify first.
2. **WHERE** is it? Apply naming convention. Know the path before searching.
3. **ALREADY IN CONTEXT?** If yes — do not reload. Re-reading is the primary waste.
4. **MINIMUM LINES?** State the range before loading. Default: less than you think.
5. **WHAT TO DISCARD?** Name what will NOT load. You control what enters context.

## SCANNING — BASH ONLY. READ TOOL FIRES ONLY AFTER TARGET IS CONFIRMED.
```bash
find . -name "pattern*" -maxdepth 2 -type f   # locate by name, depth-limited
grep -rl "keyword" path/                        # files containing keyword — names only
grep -n  "^##" file.md                          # section headers + line numbers
grep -rn "keyword" path/ --include="*.md"       # content location across files
wc -l file.md                                   # size check — if > 50 lines use steps below
```

## FILE EXTRACTION — IN ORDER. NO SKIPPING.
1. **HEADER SCAN** → `Read offset=0, limit=15` — confirm relevance before anything else
2. **GREP LOCATE** → `grep -n "^##" file.md` — get exact line of needed section
3. **TARGETED READ** → `Read offset=[line], limit=[40–80]` — load that section only

`ref card=30 lines` | `workflow stage=50` | `skill section=60` | `routing table=20`

## PDF EXTRACTION — PAGES PARAMETER ALWAYS REQUIRED.
1. `Read pages="1-3"` → index/TOC first — map page locations before reading content
2. `Read pages="[start]-[end]"` → targeted sections only — max 20 pages per call
3. All extracted content → `research/[domain]/drd_research_[topic]_raw-extract.md`
4. No PDF content enters department files until D.R.D refinement is complete.

## BANNED
`cat` `head` `tail` `find / -name` `grep -r` without path restriction `Read` during scanning phase

## TOKEN COST REFERENCE
`ref card 150–200` | `workflow stage 200–350` | `full context 1,200–1,800` | `PDF page 300–600`
`grep 5–15` | `find 5–20` | `full skill 500–1,000` | Bash scouts. Read loads. Never reverse.

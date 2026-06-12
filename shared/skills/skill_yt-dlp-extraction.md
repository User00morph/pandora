# SKILL — YOUTUBE EXTRACTION
**Loadable by: D.R.D, D.I.I, D.S.S, D.C.E, D.S.E. Load whenever processing YouTube videos or playlists.**

---

## WHAT THIS SKILL IS

The protocol for extracting timestamped transcripts and metadata from YouTube videos, with minimum token cost. Two tools are used in combination:
- **`youtube-transcript-api`** — primary tool for transcript extraction (bypasses PO token restriction)
- **`yt-dlp`** — used for playlist metadata mapping and video info only

Long-form video content (lectures, audiobooks, talks) can run 2–10+ hours. This skill prevents loading full transcripts blindly and ensures extracted content enters the D.R.D refinement pipeline before integration into any department file.

> **Known limitation:** Some uploaders disable subtitles entirely. If a video returns "Subtitles are disabled," no transcript is recoverable without downloading the audio and running a local speech-to-text model.

---

## WHEN TO LOAD

- A YouTube URL (video or playlist) is provided for research
- Audio or video content needs to be converted to searchable text
- A department requests data from a YouTube source

---

## PRE-FLIGHT CHECK

Verify both tools are installed:

```bash
python3 -m yt_dlp --version
python3 -c "from youtube_transcript_api import YouTubeTranscriptApi; print('ok')"
```

If not installed:
```bash
pip3 install yt-dlp youtube-transcript-api
```

---

## THE YT-DLP EXTRACTION PROTOCOL

### STEP 1 — ASSESS THE SOURCE

```
IDENTIFY:   Single video or playlist?
            Video URL:    https://www.youtube.com/watch?v=[ID]
            Playlist URL: https://www.youtube.com/playlist?list=[ID]

REGISTER:   Before extracting, note in the active research file:
            SOURCE: [Video/Playlist title]
            URL:    [URL]
            TIER:   [1–5 per D.R.D tier system]
            PURPOSE: [What question this video answers]
```

---

### STEP 2 — PULL PLAYLIST METADATA FIRST (playlists only)

Never extract transcripts blindly from a playlist. Map it first:

```bash
python3 -m yt_dlp --flat-playlist \
  --print "%(playlist_index)s. %(title)s [%(duration_string)s]" \
  "[PLAYLIST_URL]" 2>/dev/null
```

Output: numbered list of all videos with duration.

```
REVIEW:
  - How many videos? Total runtime?
  - Which are relevant to the active research question?
  - Flag any out-of-scope videos (do not extract those)
  - Proceed only with relevant videos
```

---

### STEP 3 — EXTRACT TRANSCRIPT (per video)

Use `youtube-transcript-api` — this bypasses YouTube's PO token restriction that blocks `yt-dlp` caption downloads.

```python
from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()

def seconds_to_timestamp(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

transcript = api.fetch('[VIDEO_ID]')  # ID only, not full URL
lines = []
for snippet in transcript:
    ts = seconds_to_timestamp(snippet.start)
    text = snippet.text.strip().replace('\n', ' ')
    lines.append(f"[{ts}] {text}")

transcript_text = '\n'.join(lines)
```

**If transcript fails with "Subtitles are disabled":**
- The uploader has turned off captions — no workaround without downloading audio
- Note the video as `TRANSCRIPT_UNAVAILABLE` in the raw extract index
- Flag for potential future audio transcription via Whisper if content is critical

**To extract multiple videos in one pass:** loop over a list of video IDs, catch exceptions per video, and continue — never let one failure block the rest.

---

### STEP 4 — CLEAN THE VTT TRANSCRIPT

Raw `.vtt` files contain timestamp headers and duplicate lines. Clean them:

```bash
python3 -c "
import re, sys

with open('[file].vtt', 'r') as f:
    content = f.read()

# Remove VTT header and timestamp lines
lines = content.split('\n')
cleaned = []
seen = set()
for line in lines:
    line = line.strip()
    if not line or line.startswith('WEBVTT') or '-->' in line or re.match(r'^\d+$', line):
        continue
    if line not in seen:
        cleaned.append(line)
        seen.add(line)

print('\n'.join(cleaned))
" > "[output].txt"
```

Or clean all `.vtt` files in a directory at once:
```bash
for f in /path/to/research/domain/*.vtt; do
  python3 -c "
import re, sys
with open('$f') as f: content = f.read()
lines = content.split('\n')
cleaned = []
seen = set()
for line in lines:
    line = line.strip()
    if not line or line.startswith('WEBVTT') or '-->' in line or re.match(r'^\d+$', line): continue
    if line not in seen: cleaned.append(line); seen.add(line)
print('\n'.join(cleaned))
" > "${f%.vtt}_clean.txt"
done
```

---

### STEP 5 — BUILD THE RAW EXTRACT FILE

For each video, create a D.R.D raw extract file:

```
FILE:     D.R.D/research/[domain]/drd_research_[topic]_raw-extract.md
NAMING:   Follow Pandora OS naming convention
CONTAINS: Metadata block + cleaned timestamped transcript
```

**Raw extract file structure:**

```markdown
# RAW EXTRACT — [Video Title]

## Source Metadata
- **Title:** [title]
- **Channel:** [channel name]
- **Published:** [date]
- **Duration:** [duration]
- **URL:** [url]
- **Tier:** [1–5]
- **Extracted:** [YYYY-MM-DD]
- **Domain:** [consciousness / suppressed-science / pre-western-knowledge / etc.]

## Transcript (timestamped)
[cleaned transcript content]

---
*RAW — not yet passed through D.R.D deconstruction. Do not integrate into department files.*
```

---

### STEP 6 — ROUTE TO D.R.D PIPELINE

Extracted video content is **raw data**. Per the Data Refinement Protocol:

```
FILE in:   D.R.D/research/[domain]/drd_research_[topic]_raw-extract.md
DO NOT use directly in:
  - Department context files
  - Workflow files
  - Skill files
  - Agent definitions
  Until it has passed through D.R.D Stages 3–5
```

---

## TOKEN COST RULES

```
NEVER load a full transcript into context unless necessary.
For long videos (1h+):
  - Load metadata block first
  - Use grep to locate relevant sections before reading
  - Read targeted timestamp ranges, not full transcript

UNOPTIMIZED:                    OPTIMIZED:
Load 10h transcript fully       Grep for keywords first
= context destroyed             Read 20-min relevant window
= research quality degrades     = targeted, clean extraction

SAVINGS: Hours of irrelevant transcript context
```

**Grepping a transcript for keywords:**
```bash
grep -n "keyword" drd_research_[topic]_raw-extract.md
```
Then use `offset` + `limit` on the Read tool to load only the relevant lines.

---

## REGISTERED SINGLE VIDEO SOURCES

```
Brian Scott — The Money Simulation: Currency Behaves Like Code
URL:      https://youtu.be/irfXyWX9jTk
Domain:   systemic-analysis, consciousness, simulation-hypothesis
Added:    2026-06-02
Status:   Raw extract filed — drd_research_brian-scott-money-simulation_raw-extract.md (~6,293 words)
```

---

## REGISTERED PLAYLIST SOURCES

```
Professor Jiang — Game Theory Series
URL:      https://youtube.com/playlist?list=PLWKcfqsabTLVQ0W6b99OM_aH_Fkxs1ywL
Domain:   systemic-analysis, geopolitics, power-mechanics
Added:    2026-05-05
Status:   Partially extracted — see below

EXTRACTED (raw extract files exist in D.R.D/research/systemic-analysis/):
  Full playlist:  Secret History series — 28 episodes, ~346,286 words  → DECODED (drd_decode_jiang-secret-history_decoded.md)
  GT#7:           America's Game — ~7,773 words                         → DECODED (drd_decode_jiang-game-theory-7-americas-game_v1.md)

---

Rev. Saaja — Divine Feminine / Narcissistic System Framework
URL:      (individual videos, no single playlist)
Domain:   divine-feminine, consciousness, nervous-system
Added:    2026-05-05
Status:   7 videos extracted + full decode complete

EXTRACTED (raw extract files exist in D.R.D/research/divine-feminine/):
  1. Nervous System as Cosmic Battlefield               → ~5,675 words  → DECODED
  2. Origin of Narcissistic Abuse                       → ~6,326 words  → DECODED
  3. War on Love — Patriarchy Spell                     → ~6,631 words  → DECODED
  4. Only True Sin — Forgetting Your Magic              → ~6,180 words  → DECODED
  5. Masculine Energy Reframe                           → ~8,441 words  → DECODED
  6. Narcissism and Creative Thinking                   → ~4,728 words  → DECODED
  7. Healing from Narcissism — Inner Child Reality      → ~6,320 words  → DECODED
Decode filed: drd_decode_rev-saaja_narcissistic-system-framework_v1.md

---

Hermetic / Egyptian / Occult / Consciousness Studies
URL:      https://www.youtube.com/playlist?list=PLWKcfqsabTLUlFcf6ec4C5Vn5yf9Dm36Y
Domain:   consciousness, pre-western-knowledge
Added:    2026-04-29
Status:   Partially extracted — see below

EXTRACTED (raw extract files exist in D.R.D/research/):
  1. The Hermetica — Freke & Gandy               → pre-western-knowledge | ~21,294 words
  2. Iamblichus — Mysteries of Egyptians          → pre-western-knowledge | ~71,267 words
  3. Nervous System — Earth New Year              → consciousness         | ~7,254 words
  5. Carl Jung — Archetypes Collective Unconscious → consciousness        | ~107,774 words
  6. Egyptian Book of the Dead — Budge pt1        → pre-western-knowledge | ~85,211 words
  7. Egyptian Book of the Dead — Budge pt2        → pre-western-knowledge | ~93,936 words

TRANSCRIPT_UNAVAILABLE (subtitles disabled by uploader):
  4. Alchemy and Hermeticism — Occult Lecture     → candidate for Whisper transcription
  8. Do You Use Illusions?                        → candidate for Whisper transcription

RESERVED:
  9. How To Connect Claude to TradingView         → D.I.I / D.S.E Trading System (not yet initiated)

---

Quant / Options Flow / AI Trading Stack
URL:      https://youtube.com/playlist?list=PLWKcfqsabTLVlzJSqJCr3deYDRCG195zK
Domain:   trading-systems, quant-methodology, options-mechanics, ai-agentic-trading
Added:    2026-05-20
Status:   Fully extracted + decoded

EXTRACTED (raw extract + decode in D.R.D/research/trading-systems/):
  Full playlist: 7 videos, ~2h 50m → DECODED (drd_decode_quant-options-ai-trading-stack_v1.md)
  
OUTPUTS GENERATED:
  drd_research_quant-options-ai-trading-stack_raw-extract.md   → raw transcripts + structured notes
  drd_decode_quant-options-ai-trading-stack_v1.md              → full D.R.D decode + STIS integration map
  dse_framework_gex-options-mechanics.md                       → new L1 fundamental framework (GEX + Greeks)
  tools/pine-scripts/markov_state_matrix.pine                  → Markov State Matrix Pine Script v1
```

---

Pandora Tech Playlist — Agentic Systems / AI Infrastructure
URL:      https://youtube.com/playlist?list=PLWKcfqsabTLUxfC7OFs7UZ8EIJ6hjY_M8
Domain:   tech-decentralization / agentic-systems / local-ai-infrastructure
Added:    2026-06-09
Status:   Tier 1 (5 videos) fully extracted + decoded

EXTRACTED (raw extracts in D.R.D/research/tech-decentralization/):
  CLI vs MCP: How AI Agents Choose the Right Tool      → ~2,008 words
  Context Engineering in 29 Minutes                    → ~6,782 words
  Running LLMs Locally (Ollama + MCP)                  → ~5,995 words
  Claude Architect: Multi-Agent Orchestration           → ~23,499 words
  Build Agentic GraphRAG (MCP + Knowledge Graph)        → ~10,551 words
  TOTAL TIER 1: ~48,835 words across 5 videos

DECODED: drd_decode_tech-playlist-tier1-agentic-systems_v1.md
KEY OUTPUTS: CLI/MCP decision rule, 4 context strategies (WSCI), local model stack
  (Ollama + OLLMCP + Zapier MCP), Hub+Spoke orchestration, Graph RAG architecture

REMAINING (Tier 2-4 — not yet extracted, 30 videos):
  Tier 2: Sell Claude Code to Businesses, Senior Engineers + AI, $5K in 7 Days,
           System Design (APIs/DBs/CDNs), LM Studio
  Tier 3: DACM/Akash (decentralized AI compute), Linux, Origin Pilot Quantum OS
  Tier 4: Alex Gladstein (decentralized tech freedom), DeFi animated, Privacy

---

Don Killam — Sovereign Entity / Business Structure Series
URL:      https://youtube.com/playlist?list=PLWKcfqsabTLUDzfteFe3THpM5656piXR5
Domain:   sovereign-entity
Added:    2026-06-04
Status:   Fully extracted + decoded (14/14 videos — 0 TRANSCRIPT_UNAVAILABLE)

EXTRACTED (raw extract files in D.R.D/research/sovereign-entity/):
  14 videos, ~244K words → DECODED (drd_decode_don-killam-sovereign-entity-stack_v1.md)

OUTPUTS GENERATED:
  drd_research_don-killam-[01-14]-[slug]_raw-extract.md  → 14 raw transcript files
  drd_decode_don-killam-sovereign-entity-stack_v1.md      → full D.R.D Stage 3–4 decode
  drd_brief_dse_don-killam-sovereign-entity-extensions_v1.md → D.S.E integration brief

KEY TOPICS: status correction, name as LLC, ministry trust (unincorporated association),
  non-grantor irrevocable spendthrift trust, GAAP/FASB framework, 1099-OID (HELD),
  TDA/Treasury Direct (HELD), manufacturing spend, private banking posture,
  admin process ladder (SEC/FINRA/FTC), baby land deeds, patent of nativity,
  ULC ordination, baptismal certificate, 1041 vs 1040, Form 3115, Form 3949-A

---

Rashad Jamal — Full Lectures Collection
URL:      https://youtube.com/playlist?list=PLWKcfqsabTLVikPa593Nl3pn9cEPrF-dY
Domain:   kemetic, consciousness, pre-western-knowledge, suppressed-science, human-history, D.O.M, D.B.S
Added:    2026-05-28
Status:   Fully extracted (44/48 videos — 4 TRANSCRIPT_UNAVAILABLE)

EXTRACTED:
  Group C (11 videos — medium lectures):    kemetic/drd_research_rashad-jamal-group-c_raw-extract.md           → ~128,230 words
  Group B (9 videos — The Spells series):   kemetic/drd_research_rashad-jamal-group-b-spells_raw-extract.md    → ~246,588 words
  Group A (11 videos — shorts/clips):       kemetic/drd_research_rashad-jamal-group-a-shorts_raw-extract.md    → ~24,014 words
  Group E (10/12 videos — consciousness):   consciousness/drd_research_rashad-jamal-playlist-group-e_raw-extract.md → ~167,441 words
  Group D (3/5 videos — indigenous/hist):   human-history/drd_research_rashad-jamal-playlist-group-d-indigenous_raw-extract.md → ~48,080 words

TRANSCRIPT_UNAVAILABLE (subtitles disabled — candidates for Whisper):
  E: Understanding The Brain, Consciousness and Kemetic Science (Kemetic YogaSkills)
  E: Do you use illusions?
  D: Why Ancient Egypt Worshiped The Sun (It wasn't a God, it was a Technology)
  D: Unlocking Tartarian Mysteries: Dr. Ali Muhammad on America's Secret Indigenous Blueprint

TOTAL: ~614,353 words across 44 videos

```

---

D.O.M Magik Playlist
URL:      https://youtube.com/playlist?list=PLWKcfqsabTLXDVusrLKN0XFMR73bxkStG
Domain:   magik / spell-craft / elemental-work / servitor-craft / deity-work / protection / kemetic-symbology
Added:    2026-06-11
Status:   17/18 extracted (0 TRANSCRIPT_UNAVAILABLE) — #04 Seth/Jane Roberts audiobook HELD (11h44m)

EXTRACTED (raw extract files in D.R.D/research/magik/):
  01. Spells and Getting What You Want              → ~13,379 words  | spell-craft
  02. Earth, Air, Water & Fire — The Elementals     → ~15,036 words  | elemental-work
  03. Creating Servitors in Esoteric Traditions      → ~7,633 words   | servitor-craft
  05. This Will Find You When Funds Are Deposited   → ~4,953 words   | manifestation
  06. Protect Energy From Dark Cults & Occult       → ~6,047 words   | protection
  07. Charge Everyday Items to Attract What You Want→ ~24,726 words  | enchantment
  08. Create Your Life — Cosmic People Create       → ~22,490 words  | sovereign-creation
  09. Magic Practices and Manifesting               → ~34,156 words  | practice
  10. Sex Magick                                    → ~2,466 words   | sex-magick
  11. Be Careful with Baneful Magick                → ~2,876 words   | baneful-magick
  12. How To Work with Deities The Way I Do         → ~2,855 words   | deity-work
  13. How to Create a Servitor                      → ~2,096 words   | servitor-craft
  14. How to Build Relationships with your Spirits  → ~3,037 words   | spirit-work
  15. Dark Energy Workers                           → ~4,440 words   | dark-energy
  16. The Real Meaning of The Ankh                  → ~4,791 words   | kemetic-symbology
  17. Writing Spells — Powerful                     → ~2,625 words   | spell-craft
  18. Protection Spell Against All Lower Entities   → ~2,521 words   | protection
  TOTAL: ~156,127 words across 17 videos

HELD:
  04. The Nature of Personal Reality — Seth/Jane Roberts Audiobook Pt.1 (11:44:15) → extract separately

```

---

*SKILL_YT_DLP_EXTRACTION | Pandora OS | D.R.D refinement required before integration*

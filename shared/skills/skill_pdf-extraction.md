# SKILL — PDF EXTRACTION
**Loadable by: D.R.D, D.I.I, D.S.S, D.B.S, D.R.A. Load whenever processing PDF documents.**

---

## WHAT THIS SKILL IS

The protocol for extracting usable, refined knowledge from PDF documents with minimum token cost. PDFs are dense. Most pages in any given PDF are not relevant to the active research question. This skill prevents full-document loading and ensures extracted content enters the D.R.D refinement pipeline — never directly into output files.

---

## WHEN TO LOAD

- Any PDF document is referenced in the active session
- Research requires pulling from a book, paper, or report in PDF format
- A department requests data from a stored PDF file

---

## THE PDF EXTRACTION PROTOCOL

### STEP 1 — IDENTIFY THE PDF
```
LOCATE:   Find the file path
          find /path -name "*.pdf"

ASSESS:   How large is it?
          Large PDFs (10+ pages) require the pages parameter
          Maximum 20 pages per read call

REGISTER: Before reading, note in the active research file:
          FILE: [name.pdf]
          SOURCE TIER: [1–5 per D.R.D tier system]
          PURPOSE: [what question this PDF answers]
```

---

### STEP 2 — READ THE INDEX PAGES FIRST (pages 1–3)
The first 1–3 pages of most PDFs contain:
- Title, author, publication date → confirms tier
- Table of contents → maps where content lives
- Abstract or introduction → confirms relevance to the question

```
Read: pages "1-3"
Extract:
  - Author credentials and affiliation → tier assignment
  - Publication source → tier adjustment
  - Table of contents → page numbers for relevant sections
  - Abstract → is this document worth extracting from?

IF IRRELEVANT → stop. Do not read further.
IF RELEVANT → proceed to Step 3 with page map in hand.
```

---

### STEP 3 — TARGETED PAGE EXTRACTION
Using the table of contents from Step 2, read only the pages that contain relevant content.

```
Read: pages "[start]-[end]"  (max 20 pages per call)
      e.g., pages "47-61" for a specific chapter

NEVER:
  Read pages "1-200" for a 200-page document
  Even if the content seems important —
  extract by section, not by volume

IF CONTENT SPANS MORE THAN 20 PAGES:
  Make multiple targeted reads, each on a specific sub-question
  from the D.R.D Stage 1 sub-question map
```

---

### STEP 4 — EXTRACT AND STRUCTURE
For each relevant section read, extract content in this format:

```
SOURCE: [PDF title, author, year, page range]
TIER:   [1–5]
CLAIM:  [Exact claim — precise, not paraphrase]
LIMITATION: [Sample size / date / methodology / author bias]
RELEVANT TO: [Which D.R.D sub-question this addresses]
CONTRADICTION: [Does this conflict with another source? Y/N]
```

Never write "the document says..." — extract the specific claim at the specific page.

---

### STEP 5 — ROUTE TO D.R.D PIPELINE
Extracted PDF content is **raw data**. Per the Data Refinement Protocol:

```
FILE the extraction in: research/[domain]/drd_research_[topic]_raw-extract.md
DO NOT use PDF content directly in:
  - Department context files
  - Workflow files
  - Skill files
  - Agent definitions
  Until it has passed through D.R.D Stages 3–5
```

---

## EXISTING PANDORA OS PDFS

```
celestial archetypes.pdf    → D.P.S.A / D.O.M / D.S.S domain
                               Tier assessment: pending
                               Location: /Users/emoefedorgu/Desktop/Pandora/
```

For any new PDF added to the OS — register it here with tier and domain before extracting.

---

## TOKEN COST COMPARISON

```
UNOPTIMIZED:                      OPTIMIZED:
Read full 200-page PDF            Index pages 1-3: 3 pages
= context window destroyed        Targeted section: 15 pages
= research quality degrades       = 18 pages total

SAVINGS: 182 pages of irrelevant context
```

---

*SKILL_PDF_EXTRACTION | Pandora OS | D.R.D refinement required before integration*

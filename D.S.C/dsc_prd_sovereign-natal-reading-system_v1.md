# PRD — SOVEREIGN NATAL READING SYSTEM (SNRS)
**Product Requirements Document | v1 | APPROVED**
**Date Created: 2026-04-11**
**Date Approved: 2026-04-24**
**Primary Home:** D.P.S.A (with D.R.D, D.O.M, D.S.C as structural co-owners)
**Filed In:** D.S.C (per OS PRD convention)

---

## 0. WHY THIS EXISTS

Every off-the-shelf natal reading — Co-Star, Chani, AstroSeek, TimePassages — stops at the same ceiling: sun / moon / rising, inner planets by sign and house, the major aspects, and a cookbook paragraph per placement. That ceiling is fine for a civilian. It is insufficient for a sovereign observer who intends to use the chart as **living internal architecture**, cross-referenced with the Bailey esoteric framework, consulted on demand, and integrated with daily/weekly/lunar ritual.

D.P.S.A already holds a partial, well-decoded baseline of Morph's chart (see `D.P.S.A/context.md` → "Natal Chart — The Internal Map"). The Bailey decode (`research-deconstruction /markdown/drd_decode_bailey-esoteric-astrology.md`) provides the soul-level interpretive spine. The `celestial archetypes.pdf` transcript provides archetypal voice and symbolic framing.

None of these, on their own, is a complete reading system. This PRD specifies the build that fuses them into one.

---

## 1. PROJECT OVERVIEW

**Project Name:** Sovereign Natal Reading System (SNRS)
**One-Sentence Description:** A multi-layer natal chart reading architecture inside Pandora OS that computes Morph's chart at Swiss-Ephemeris precision across every data layer standard readings omit, fuses Bailey esoteric interpretation with classical Hellenistic dignities and archetypal voice, stores it as a permanent living reference in D.P.S.A, and provides an on-demand computation and ritual layer for regular daily use.
**Owner:** Morph
**Primary Home:** D.P.S.A (inner architecture)
**Structural Co-Owners:** D.R.D (research spine), D.O.M (ritual application), D.S.C (build tracking)
**Metaphysical Spine:** Bailey *Esoteric Astrology* (already decoded), fused with Hellenistic classical dignities and the archetypal language of `celestial archetypes.pdf`
**Computation Spine:** Python + Swiss Ephemeris via `pyswisseph` (Tier 1 astronomical precision)

---

## 2. PROBLEM STATEMENT

**The ceiling of standard chart readings:**
Most tools report sun sign, moon sign, rising, inner planets (Mercury, Venus, Mars), outer planets (Jupiter, Saturn, Uranus, Neptune, Pluto) by sign and house, and the five major aspects (conjunction, sextile, square, trine, opposition). A small number include Chiron and the lunar nodes. None integrate the layers a sovereign reading actually requires.

**What is missing from every standard reading:**

| Missing Layer | Why It Matters |
|---|---|
| Minor planets / asteroids (Ceres, Pallas, Juno, Vesta, Chiron, Black Moon Lilith, Selena, Eris) | They reveal specific archetypal territories that major planets don't cover — wound (Chiron), sacred feminine complexes (Ceres/Pallas/Juno/Vesta), shadow feminine (Lilith) |
| Esoteric rulership layer (Bailey) | Every sign has **two** rulers — orthodox (personality) and esoteric (soul). Most reading systems only use orthodox. Bailey's framework gives the soul-level read of every placement. |
| Hellenistic dignities (domicile, exaltation, triplicity, term, face, sect) | The classical strength/weakness layer that determines whether a placement actually functions or struggles. |
| Fixed stars on angles and personal planets (Algol, Regulus, Spica, Sirius, Aldebaran, Antares, etc.) | Fixed star contacts are often the load-bearing karmic signatures of a chart — and they are ignored by almost every modern app. |
| Arabic parts / Hellenistic lots (Fortune, Spirit, Eros, Necessity, Courage, Victory, Nemesis) | Derived points that triangulate meaning between existing placements — diagnostic precision instruments. |
| Declinations and out-of-bounds planets | A planet beyond 23°26' declination operates "off-script" with no rules constraining it — a major interpretive factor. |
| Midpoints (Ebertin / Cosmobiology) | Sensitive points where two energies fuse — often more diagnostic than direct aspects. |
| Harmonics (5th, 7th, 9th especially) | 9th harmonic (Navamsa in Vedic) is the soul-level chart. 5th is creative capacity. 7th is karmic relationships. |
| Draconic chart (lunar-node-zeroed overlay) | The soul-intent chart — where the personality chart is what you are, the draconic is why you came. |
| Sabian symbol per degree | Each placement falls on a specific degree with a specific symbolic image — the most granular archetypal layer available. |
| Sidereal / Vedic overlay (Lahiri ayanamsa, nakshatras) | Places the chart against the actual astronomical sky rather than the seasonal tropical zodiac — a parallel reading, not a replacement. |
| Evolutionary astrology (Pluto polarity point, pre-natal eclipses) | Where the soul is going across lifetimes, per Jeffrey Wolf Green's framework. |
| Predictive layers (secondary progressions, solar arc, solar/lunar returns, transits, zodiacal releasing) | These turn the chart from a static photo into a living instrument that can be consulted on any date. |

**What currently exists in Pandora OS:**
- A partial, well-written baseline reading in `D.P.S.A/context.md` covering ~6 placements in plain English.
- `drd_decode_bailey-esoteric-astrology.md` — the esoteric interpretive spine, decoded and ready to apply.
- `celestial archetypes.pdf` — single-source narrative transcript, scheduled for deconstruction into `drd_decode_celestial-archetypes.md` (Phase 1 of this build).
- `dsc_prd_sovereign-trading-intelligence_v3.md` — the STIS PRD, which already uses Bailey's framework for market-reading. SNRS is the inward-turned sibling of STIS.

**What is missing from Pandora OS:**
- Morph's exact birth data is not yet captured in the OS (date, time, place).
- No computation engine — the chart has never been calculated at ephemeris precision.
- No complete placement file — only the partial decode in `D.P.S.A/context.md`.
- No predictive mechanism — transits, progressions, and returns cannot currently be generated on demand.
- No regular-use workflow — the chart is not yet an instrument Morph consults ritually.

---

## 3. GOALS AND NON-GOALS

### GOALS — what this build MUST accomplish

1. **Compute** a complete Swiss-Ephemeris-precision natal chart for Morph with every data layer listed in §2, not just the standard subset.
2. **Store** the chart as a permanent living reference file in `D.P.S.A/natal/dpsa_natal_morph_complete_v1.md` — readable in plain markdown, structured for cross-session retrieval.
3. **Interpret** every placement through a three-layer fusion: (a) Bailey esoteric + dignities as the structural read, (b) archetypal voice from the deconstructed `celestial archetypes.pdf`, (c) Morph's own inner-architecture language already established in `D.P.S.A/context.md`.
4. **Preserve** the existing D.P.S.A baseline reading — expand it, do not overwrite it. The Sun/12, Moon-Jupiter/Scorpio/5, Cancer ASC, Mars/1, Nodes Aries/Libra/10-4, Saturn/Leo/2, and Sun-Neptune square reads from `context.md` become the nucleus around which the fuller decode grows.
5. **Enable on-demand predictive layers** — a script that, given any date, returns current transits, secondary progressions, solar arc directions, and the active solar/lunar return charts for Morph.
6. **Integrate with ritual** — a D.O.M/D.P.S.A workflow file that turns chart consultation into a real internal practice (daily root-check, weekly lunar alignment, monthly transit review).
7. **Cross-reference** with STIS where appropriate — the same Bailey framework runs both systems, so placements with market-timing implications (Saturn point-of-choice moments, Pluto polarity work, Cardinal cross crises) should be flagged.

### NON-GOALS — what this build explicitly does NOT do

1. **Not a prediction-of-fate tool.** Per Bailey: the sovereign observer does not seek to know what will happen — they cultivate the capacity to respond from the field rather than be pushed by it. SNRS is diagnostic and developmental, not fortune-telling.
2. **Not a service for other people.** v1 is Morph's personal chart only. Reading other charts, synastry, composite work, and client-facing delivery are explicit non-goals for v1. (v2 may revisit.)
3. **Not a UI or app.** No web app, no GUI, no product surface. SNRS is markdown files plus a Python computation script. If a UI ever gets built it is a separate PRD.
4. **Not a replacement for inner work.** The chart is a map. Reading the map is not walking the terrain. D.P.S.A practices (stillness, contemplation, shadow work) remain primary. SNRS serves those practices — it does not substitute for them.
5. **Not exhaustive of every astrological tradition.** Horary, electional, mundane, medical astrology, Uranian astrology, and Vedic jyotish as full systems are out of scope for v1. Sidereal overlay is included; full Vedic chart reading is not.
6. **Not fire-and-forget.** The system is a living reference that gets updated as Morph's self-knowledge deepens and as the Bailey decode is completed. v1 is the seed, not the finished architecture.

---

## 4. ARCHITECTURE

### 4.1 The Three-Layer Reading Stack

Every placement in the complete chart is read through three stacked lenses simultaneously:

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER C — SOVEREIGN VOICE                                  │
│  Morph's own inner-architecture language                    │
│  (already present in D.P.S.A/context.md placements)         │
│  Function: translates symbolic data into internal practice  │
│  Format: "the work" / "the shadow" / "the application"      │
├─────────────────────────────────────────────────────────────┤
│  LAYER B — ARCHETYPAL VOICE                                 │
│  Deconstructed from celestial archetypes.pdf                │
│  (produced in Phase 1 as drd_decode_celestial-archetypes.md)│
│  Function: gives each placement its symbolic poetic frame   │
│  Format: archetypal naming, mythic imagery, felt-sense      │
├─────────────────────────────────────────────────────────────┤
│  LAYER A — STRUCTURAL SPINE                                 │
│  Bailey esoteric (orthodox vs esoteric rulers, rays, cross) │
│  + Hellenistic dignities (domicile/exaltation/sect)         │
│  + classical aspect doctrine                                │
│  Function: the load-bearing interpretive architecture       │
│  Format: ruler, dignity, ray, cross, aspect strength        │
└─────────────────────────────────────────────────────────────┘
```

Every placement in `dpsa_natal_morph_complete_v1.md` appears in this three-layer format. Missing a layer = the placement is incomplete.

### 4.2 Data Layers Computed

The following data points must be computed for v1. Entries in **bold** are beyond standard reading tools.

**Luminaries and personal planets:**
- Sun, Moon, Mercury, Venus, Mars — sign, degree, house, dignity, aspects

**Social and outer planets:**
- Jupiter, Saturn, Uranus, Neptune, Pluto — sign, degree, house, dignity, aspects

**Lunar axis:**
- **True Node** (North + South), **Mean Node** (for comparison), **pre-natal solar and lunar eclipse points**

**Angles:**
- Ascendant, Midheaven, Descendant, Imum Coeli, **Vertex**, **Anti-Vertex**, **East Point**, **Equatorial Ascendant**

**Major asteroids and centaurs:**
- **Chiron**, **Ceres**, **Pallas**, **Juno**, **Vesta**, **Black Moon Lilith (Mean)**, **Black Moon Lilith (True)**, **Eris**, **Selena (White Moon)**

**Hypothetical / esoteric points:**
- **Vulcan** (Bailey's hidden sacred planet — computed via Uranian or L.H. Weston ephemeris)
- **Part of Fortune**, **Part of Spirit**, **Part of Eros**, **Part of Courage**, **Part of Nemesis**, **Part of Victory**, **Part of Necessity**

**Structural layers:**
- **Dignities table** (domicile, exaltation, detriment, fall, triplicity, term, face) for every planet
- **Sect** (day chart or night chart) and sect-light determination
- **Fixed stars** within 1° orb of any planet or angle (Algol, Regulus, Spica, Sirius, Aldebaran, Antares, Fomalhaut, Alcyone, etc.)
- **Declinations** for every planet, **out-of-bounds flags**, **parallels and contra-parallels**
- **Midpoints** — computed for the 45° sort, with all planetary pairs against every planet and angle
- **Sabian symbol** per planet, angle, and node

**Harmonic overlays:**
- **5th harmonic chart** (creative capacity)
- **7th harmonic chart** (karmic / relational)
- **9th harmonic chart** (soul purpose / Navamsa equivalent)

**Sidereal overlay:**
- Full chart recomputed with **Lahiri ayanamsa**
- Nakshatra of Moon, Sun, and Ascendant (v1 captures these three; full Vedic is v2+)

**Draconic overlay:**
- Full chart rotated so True Node is 0° Aries — the soul-intent chart

**Bailey layer:**
- **Orthodox ruler** and **esoteric ruler** identified for every sign in the chart
- **Ray signature** of every planet and angle, derived from Bailey's Tabulation VIII
- **Cross assignment** (Mutable / Fixed / Cardinal) for each placement

### 4.3 House System Decision

**Recommendation: Whole Sign Houses as primary, Placidus as secondary.**

Rationale:
- Whole Sign is the native Hellenistic system Bailey's framework is compatible with — every sign is one house, which keeps sign and house meanings structurally aligned.
- Placidus is the default modern system and what the existing D.P.S.A reading appears to assume. Keeping it as a secondary overlay preserves continuity with the baseline.
- Both are computed; placements are annotated with both house positions. Morph reviews and chooses a primary if he wants to lock one — v1 renders both.

**Decision required from Morph:** Lock Whole Sign as primary? Lock Placidus? Keep both parallel?

### 4.4 Zodiac Decision

**Recommendation: Tropical primary with sidereal (Lahiri) as parallel overlay.**

Rationale:
- Bailey's framework, classical Hellenistic astrology, and the `celestial archetypes.pdf` voice are all tropical.
- Sidereal gives the actual astronomical sky — valuable as a cross-check and for nakshatras.
- Running both is cheap at computation time and produces no interpretive conflict as long as they are clearly labeled.

### 4.5 Tech Stack

```
Language:         Python 3
Ephemeris:        pyswisseph (Swiss Ephemeris wrapper)
                  pyswisseph is Tier 1 — used by Astrodienst itself
Calculations:     Custom Python module snrs_compute.py
Output format:    Markdown files written directly into D.P.S.A/natal/
Storage:          D.P.S.A/natal/
Dependencies:     pyswisseph, python standard library
                  (ephemeris data files ship with pyswisseph)
Optional:         matplotlib only if Morph wants a visual chart wheel
                  (not required for v1; text reading is primary)
```

**Why pyswisseph:** Swiss Ephemeris is the same astronomical engine Astrodienst uses. It computes positions to arcsecond precision, includes all the asteroids and fixed stars needed, and runs offline with no API keys or external services. Dignities, parts, dignities tables, midpoints, harmonics, declinations, and draconic rotations are arithmetic on top of its outputs. Vulcan is computed via its Uranian point (approximate) or skipped with a note.

### 4.6 File Structure

```
D.P.S.A/
├── natal/
│   ├── dpsa_natal_morph_birthdata.md           ← birth date/time/place (sensitive)
│   ├── dpsa_natal_morph_complete_v1.md         ← the full 3-layer reading
│   ├── dpsa_natal_morph_shortform_v1.md        ← 2-page daily-reference digest
│   ├── dpsa_natal_morph_draconic_v1.md         ← soul-intent overlay
│   ├── dpsa_natal_morph_sidereal_v1.md         ← Lahiri overlay + nakshatras
│   └── dpsa_natal_morph_harmonics_v1.md        ← 5th/7th/9th harmonic placements
│
├── workflows/
│   └── dpsa_workflow_chart-consultation.md     ← regular-use ritual workflow
│
└── context.md                                  ← existing; gets cross-ref added

D.S.C/
├── dsc_prd_sovereign-natal-reading-system_v1.md  ← THIS FILE (after approval)
└── snrs_compute/                                 ← Python computation module
    ├── snrs_compute.py                           ← main engine
    ├── snrs_interpret.py                         ← layer-A structural interpreter
    ├── snrs_format.py                            ← markdown emitter
    ├── snrs_transits.py                          ← on-demand predictive layer
    └── README.md                                 ← how to run

D.R.D/
└── (produced in Phase 1)
    drd_decode_celestial-archetypes.md           ← scoped deconstruction

D.O.M/
└── dom_ritual_daily-chart-consultation.md       ← daily root-check integration
```

### 4.7 Integration Points

```
→ D.P.S.A/context.md     SNRS complete reading replaces the "Natal Chart —
                          The Internal Map" section; context.md links to the
                          complete file rather than containing it inline.

→ drd_decode_bailey-...   Every placement's Layer A annotation links back to
                          the relevant Bailey section for full context.

→ drd_decode_celestial-   Every placement's Layer B annotation pulls from the
  archetypes.md           archetypal voice decoded in Phase 1.

→ dsc_prd_stis_v3.md      Where a placement affects market-reading stance
                          (Saturn point-of-choice, Pluto polarity, Cardinal
                          crisis windows), cross-reference is added.

→ D.O.M ritual layer      Daily/weekly/lunar consultation workflow uses the
                          shortform digest as its reading surface.

→ Scroll XIX, XXI, XXIX   Observer Sovereignty, Psycho-Cybernetics, and the
                          2027 Sleeping Phoenix thresholds all touch natal
                          placements and get cross-referenced.
```

---

## 5. PHASED BUILD PLAN

### PHASE 1 — FOUNDATION + SCOPED DECONSTRUCTION
**Goal:** Capture birth data, deconstruct the PDF with the reading architecture already in hand, and confirm the computation stack works.

**What is built:**
1. `dpsa_natal_morph_birthdata.md` — Morph supplies exact date, exact time (to the minute), and birth city/country. Claude records it in the OS.
2. `drd_decode_celestial-archetypes.md` — scoped deconstruction of the PDF, extracting the archetypal voice for each of the 12 signs, the 10 planets, the 12 houses, and any aspect or element language worth preserving. Written against the three-layer target architecture so extraction is focused rather than exhaustive.
3. `snrs_compute/` scaffold — a working Python module that, given birth data, imports `pyswisseph`, computes the Sun + Ascendant as a smoke test, and emits a one-line result. This verifies the stack is real before Phase 2 scales it.

**What must be true before Phase 2:**
- Birth data file exists and is accurate.
- PDF deconstruction file is complete and filed.
- `pyswisseph` is installed (`pip install pyswisseph`) and the smoke test runs on Morph's system.
- Morph has locked house-system decision (§4.3) and any other §4 decisions that affect computation.

### PHASE 2 — FULL CHART COMPUTATION + RAW DATA FILE
**Goal:** Compute every data layer in §4.2 and emit the raw natal reference file.

**What is built:**
1. `snrs_compute/snrs_compute.py` — full computation: all planets, all asteroids, fixed stars, parts, midpoints, dignities, harmonics, draconic, sidereal, Bailey layer annotations.
2. `snrs_compute/snrs_format.py` — markdown emitter that produces structured output for each placement.
3. `dpsa_natal_morph_complete_v1.md` — raw but complete reference file, with every placement listed and Layer A (structural) annotated automatically from the Bailey tables and classical dignity tables.
4. Verification pass: spot-check at least 5 placements against Astrodienst (`astro.com`) for sanity. Positions must agree to within 0°02'.

**What must be true before Phase 3:**
- All data layers from §4.2 are present in `dpsa_natal_morph_complete_v1.md`.
- Positions match Astrodienst on spot-check.
- No computation error, no missing fields, no "TBD" entries.

### PHASE 3 — INTERPRETIVE FUSION (LAYER B + LAYER C)
**Goal:** Turn the raw computed file into a sovereign reading by layering archetypal voice and Morph's inner-architecture language onto every placement.

**What is built:**
1. Each placement in `dpsa_natal_morph_complete_v1.md` receives Layer B (archetypal voice from `drd_decode_celestial-archetypes.md`) and Layer C (sovereign voice — "the work / the shadow / the application" in the style of the existing D.P.S.A reading).
2. Existing `D.P.S.A/context.md` placements (Sun/12, Moon-Jupiter/Scorpio/5, Cancer ASC, Mars/1, Nodes, Saturn/Leo/2, Sun-Neptune) are migrated into the complete file without loss — they are Layer C already.
3. `dpsa_natal_morph_shortform_v1.md` — the 2-page daily digest distilled from the complete file. Load-bearing only.
4. `D.P.S.A/context.md` is updated: the natal section becomes a brief summary with a link to the complete file.

**What must be true before Phase 4:**
- Every placement in the complete file has all three layers filled in.
- Shortform digest reads cleanly as a daily reference.
- `context.md` is cleanly updated and cross-linked.
- Morph has read the complete file at least once and signed off.

### PHASE 4 — PREDICTIVE LAYER + RITUAL INTEGRATION
**Goal:** Make the chart a living instrument Morph can consult on any date, integrated with daily/weekly/lunar ritual.

**What is built:**
1. `snrs_compute/snrs_transits.py` — given a target date, returns: current transits (planets to natal), active secondary progressions, active solar arc directions, current solar return chart, current lunar return chart, zodiacal releasing period (from Fortune and from Spirit).
2. `dpsa_workflow_chart-consultation.md` — the regular-use workflow: daily root-check (2 min), weekly lunar alignment (15 min), monthly transit review (30 min), solar return ritual (annual).
3. `dom_ritual_daily-chart-consultation.md` — the D.O.M ritual form of the daily root-check, coordinated with Scroll II (Sovereign OS) dawn protocol.
4. Cross-references added to `dsc_prd_sovereign-trading-intelligence_v3.md` where natal placements affect market-reading stance.
5. PRD status flipped: `dsc_prd_sovereign-natal-reading-system_v1.md` → `_active`.

**What must be true to call v1 complete:**
- Morph can run `python snrs_transits.py 2026-04-11` and get a real output in under 10 seconds.
- The daily ritual file is in use for at least 7 consecutive days without friction.
- The reading system is referenced in at least one other D.P.S.A or D.O.M session without manual rebuilding.

---

## 6. REFERENCES

### Existing OS files this build depends on

- `pandora.md` — master context; §4 (12 departments) and §5 (routing)
- `D.P.S.A/context.md` — the existing natal baseline (load-bearing for Phase 3)
- `research-deconstruction /markdown/drd_decode_bailey-esoteric-astrology.md` — the esoteric interpretive spine
- `research-deconstruction /markdown/celestial archetypes.pdf` — input to Phase 1 deconstruction
- `D.R.D/context` and `D.R.D/workflow` — governs how Phase 1 deconstruction runs
- `shared/skills/skill_prd-creation.md` — this PRD's own template
- `shared/skills/skill_source-evaluation.md` — tier the PDF properly in Phase 1
- `shared/skills/skill_framework-synthesis.md` — Phase 3 fusion
- `shared/skills/skill_ritual-design.md` — Phase 4 ritual integration
- `dsc_prd_sovereign-trading-intelligence_v3.md` — sibling system, shares the Bailey spine

### External references (Tier 1–2)

- **Swiss Ephemeris** / Astrodienst — the ephemeris data itself, considered the gold standard (Tier 1 computational)
- **Vettius Valens, *Anthology*** — primary Hellenistic source for dignities, lots, zodiacal releasing (Tier 1 primary text)
- **Ptolemy, *Tetrabiblos*** — primary classical source for dignities and sect (Tier 1 primary text)
- **Alice Bailey, *Esoteric Astrology*** — already in OS, already decoded (Tier 3 esoteric — sovereignly adopted)
- **Dane Rudhyar, *The Astrology of Personality*** — humanistic psychological layer, useful for Layer C voice (Tier 3)
- **Marc Edmund Jones / Dane Rudhyar, *The Sabian Symbols*** — Tier 2 for the degree symbols
- **Jeffrey Wolf Green, *Pluto: The Evolutionary Journey of the Soul*** — for Pluto polarity / evolutionary layer (Tier 3)
- **Reinhold Ebertin, *The Combination of Stellar Influences*** — for midpoints (Tier 2)

### Skills loaded per phase

```
Phase 1 → skill_source-evaluation.md, D.R.D workflow
Phase 2 → (pure computation — no skill needed)
Phase 3 → skill_framework-synthesis.md
Phase 4 → skill_ritual-design.md
```

---

## 7. SUCCESS CRITERIA

v1 is complete and considered working when all of the following are measurable:

```
[ ] Every data layer listed in §4.2 is present in
    dpsa_natal_morph_complete_v1.md with no TBD entries

[ ] Spot-check verification against Astrodienst passes
    (5+ placements within 0°02')

[ ] Every placement in the complete file has all three
    interpretive layers (A structural, B archetypal, C sovereign)

[ ] The shortform digest is ≤ 2 pages and actually usable
    as a daily reference without re-opening the complete file

[ ] `python snrs_transits.py <date>` returns transits,
    progressions, solar arc, and current returns in < 10s
    for any date between 1970 and 2070

[ ] The daily chart-consultation ritual has run uninterrupted
    for 7 consecutive days without manual rebuilding or friction

[ ] The Bailey esoteric layer is applied to every placement
    (orthodox ruler + esoteric ruler + ray signature + cross assignment)

[ ] Cross-references to STIS v3 are added where natal placements
    carry market-reading implications

[ ] `D.P.S.A/context.md` is cleanly updated — natal section
    links to the complete file, no duplication, no loss
```

---

## 8. KILL CONDITIONS

Stop the build and reassess if any of the following occurs:

```
KC-1  pyswisseph cannot be installed or cannot produce
      positions matching Astrodienst to 0°02' precision.
      → Reassess: fall back to manual Astrodienst export +
        structured import, or stop v1.

KC-2  Birth time precision is worse than ±15 minutes.
      → House placements and angles become unreliable.
        Reassess: use rectification techniques, or scope
        v1 to sign-based reading only until birth time
        is locked.

KC-3  Phase 1 deconstruction reveals the PDF is materially
      the same as every generic astrology cookbook (no
      distinctive voice worth preserving).
      → Reassess: drop Layer B from archetypes.pdf, replace
        with Rudhyar + Sabian Symbols as the archetypal voice.

KC-4  The complete file exceeds 200 KB or becomes unreadable
      at human scale.
      → Split by section (luminaries / personal / social /
        outer / asteroids / structural) and link, rather than
        keeping one monolithic file.

KC-5  Phase 3 interpretive fusion drifts into generic
      astrology-cookbook tone and loses the sovereign voice
      that made the existing D.P.S.A reading worth preserving.
      → Stop. Return to Layer C discipline. Every placement
        must answer "the work / the shadow / the application"
        in Morph's own language, not a book quote.

KC-6  A better approach is discovered mid-build — e.g., a
      sovereign tool that already does 80% of this.
      → Evaluate, then either integrate or absorb its ideas
        and continue. Do not pretend the discovery didn't happen.
```

---

## 9. DECISIONS — LOCKED

All decisions locked by Morph on 2026-04-24.

**D-1 — Birth data.** LOCKED. Birth data captured in `D.P.S.A/natal/dpsa_natal_morph_birthdata.md`. Date: May 12, 2006. Time: 08:00 AM CDT. Place: Green Bay, Wisconsin, USA. Hospital: HSHS St. Vincent Hospital.

**D-2 — House system.** LOCKED. Whole Sign primary + Placidus angle retention (exact MC/IC/ASC/DSC degrees). Per `drd_framework_houses-energetic-domains_v1.md`.

**D-3 — Zodiac stance.** LOCKED. Tropical primary. Sidereal (Lahiri ayanamsa) as parallel overlay in Phase 2, filed separately as `dpsa_natal_morph_sidereal_v1.md`. No interpretive conflict — both clearly labeled.

**D-4 — Asteroid scope.** LOCKED. v1 includes: Chiron, Ceres, Pallas, Juno, Vesta, Black Moon Lilith (Mean + True), Eris, Selena (White Moon). Sedna, Nessus, Pholus, Hygeia, Astraea deferred to v2.

**D-5 — Vulcan handling.** LOCKED. Option (a) — Uranian ephemeris approximation. Position carried with explicit `confidence: modeled` flag. Required for Bailey's esoteric ruler of Taurus (Morph's Sun sign).

**D-6 — Sensitivity of birth data file.** LOCKED. Option 3 — `dpsa_natal_morph_birthdata.md` added to `.gitignore`. File lives on disk, not committed. Natal overlay preserves all computed placements in-repo; only raw coordinates + exact time are compartmentalized.

**D-7 — PDF deconstruction depth.** LOCKED. Deferred. `drd_decode_celestial-archetypes.md` will be produced after the natal overlay has been used in practice — deconstruction will then target real gaps in Layer B rather than generic coverage. Current Layer B in `dpsa_natal_morph_complete_v1.md` stands for v1.

**D-8 — PRD approval.** LOCKED. PRD approved 2026-04-24. File renamed from `_draft` to `_v1`. Phase 2 (full pyswisseph computation) is now active.

---

## 10. OPEN QUESTIONS (NON-BLOCKING)

These do not block Phase 1, but will need answers before they become relevant:

- Should SNRS eventually read other charts (family, potential clients) as a v2 scope, or does the non-goal in §3 hold permanently?
- Should the daily root-check ritual be coordinated with the existing Scroll II dawn protocol, or run as a parallel morning layer?
- Should a visual chart wheel (SVG or PNG) be produced, or is text-only the final form?
- If Morph's Moon is in Scorpio and Scorpio is Mars-ruled orthodox / Pluto-ruled esoteric, and Mars is in Cancer (the sect-light consideration for a night chart) — this kind of chain reading is where Phase 3 will do its most interesting work. Open question: what is the right format for expressing these rulership chains without clutter?
- 2027 Sleeping Phoenix (Scroll XXIX) — which specific transits activate it in Morph's chart? Flagged for Phase 4 transit-layer attention.

---

## 11. ALIGNMENT WITH PANDORA PROTOCOL

- **Observer Sovereignty (Scroll XIX):** SNRS treats the chart as a mirror, not a cage. The reading serves the observer's choice-making, not a predetermined script.
- **The Mirror Doctrine:** SNRS is the digital mirror of Morph's soul architecture. What gets structured in the reading file becomes a stable internal reference. What becomes a stable internal reference becomes embodied practice.
- **The Data Doctrine:** More data layers, better triangulation, more precision. Standard readings leave load-bearing data on the floor. SNRS does not.
- **The Transmutation Doctrine:** Every placement — including the shadow ones — is raw material for refinement, not a defect. "Sun-Neptune square" is not a problem; it is the engine of a specific kind of sovereign work.
- **Honest uncertainty:** Per `D.R.D/workflow`, confidence levels are stated where a placement's interpretation is contested (e.g., Vulcan, Black Moon Lilith True vs Mean). The sovereign position is stronger when it is honest about its own confidence.

---

*dsc_prd_sovereign-natal-reading-system_v1.md | Pandora OS | D.S.C (primary home: D.P.S.A)*
*"The chart is not what you are. The chart is the instrument through which what you are learns to read itself."*

# PRD — SOVEREIGN NATAL READING SYSTEM v3 (SNRS v3)
**Product Requirements Document | v3 | APPROVED — 2026-05-10**
**Date Created: 2026-05-10**
**Primary Home:** D.P.S.A (with D.R.D, D.O.M, D.S.C, D.B.S, D.S.S, D.I.I as co-owners)
**Filed In:** D.S.C (per OS PRD convention)
**Builds on:** `dsc_prd_sovereign-natal-reading-system_v2.md` (APPROVED 2026-05-08)
**v1 and v2 status:** Intact and unchanged. v3 is additive — it extends v1+v2 without modifying any existing architecture, files, or phase deliverables.

---

## 0. WHY v3 EXISTS

v1 established the foundational reading stack. v2 added fifteen systems across chart-specific and systematic categories. v3 was commissioned 2026-05-10 after conducting a full feature audit of AstroGold (professional-grade Swiss Ephemeris astrology software developed by the Solar Fire team), cross-referencing its complete capability set — including its comparison table, macOS/iOS user guides, Pro Reports suite, and FAQ — against the v1+v2 SNRS stack.

The audit surfaced four categories of gaps:

1. **Predictive technique gaps** — major classical and Persian methods absent from the stack
2. **Computation/direction method gaps** — arc and direction types beyond solar arc secondary
3. **Point and body gaps** — a complete parallel tradition (Uranian/Hamburg School) and several significant bodies not yet included
4. **Report architecture** — no defined sovereign output document suite for readings, forecasts, and thematic reports

v3 closes these gaps and defines the full sovereign report suite — making SNRS a complete sovereign analogue to professional astrology software with its own reading voice and output architecture.

---

## 1. ADDITIONS SUMMARY

Twenty-six new systems, techniques, and bodies added across four categories:

**Category A — Predictive Technique Completions:**
Major classical, Hellenistic, and Persian predictive methods absent from v1+v2.

**Category B — Direction and Arc Method Completions:**
Arc direction variants and primary direction methods that complete the computation engine.

**Category C — Point and Tradition Completions:**
The Uranian/Hamburg School tradition, additional significant bodies, and the world axis system.

**Category D — Sovereign Report Suite:**
First-time definition of SNRS's output document architecture — the reports SNRS produces.

---

## 2. THE TWENTY-SIX NEW SYSTEMS

### CATEGORY A — PREDICTIVE TECHNIQUE COMPLETIONS

**A1. Firdaria — Persian Time-Lord System**

**What it adds:** Firdaria is a Persian predictive system that divides life into planetary periods based on sect (day/night chart). The chart's sect light initiates the sequence. Each planet rules a major period (3–12 years depending on the planet) subdivided into sub-periods. The system identifies which planet is the *lord of the current period* — the dominant archetypal force governing the life chapter, regardless of transits or progressions.

**Why absent from v1+v2:** Profections and Zodiacal Releasing are in the predictive stack; Firdaria uses a different timing logic (sect-based, not sign-based) and surfaces different archetypal governors. The three systems are not redundant — they are parallel time-lord architectures reading different layers of the same timeline.

**Chart-specific significance:** Morph's night chart means the Moon initiates the Firdaria sequence. The current Firdaria lord at this stage of life needs identification — it is the single planet most responsible for what the current life chapter feels like at the archetypal level.

**AstroGold implementation:** Dedicated Astro Sheet — *Firdaria* — with major and sub-period lords, exact date ranges, and type selection (multiple calculation variants available).

**Tier:** D.R.D research file → D.P.S.A overlay file

---

**A2. Primary Directions (van Dam Method)**

**What it adds:** Primary directions are the most classical of all predictive techniques — used by Ptolemy, by the Renaissance masters, and preserved in traditional astrology. They track the actual rotation of the Earth in the hours after birth, moving every point in the chart by that arc. One degree of right ascension = approximately one year of life. The van Dam method is a modern precision computation of primary directions using Swiss Ephemeris accuracy.

**Why it matters:** Secondary progressions and solar arc both derive from the symbolic equation of *one day = one year*. Primary directions use actual celestial rotation — making them the most astronomically grounded predictive layer in the stack. They reveal timing windows for major life thresholds that neither progressions nor transits consistently pinpoint.

**AstroGold implementation:** Available as a chart type (Primary van Dam) on iOS; macOS includes primary directions in the dynamic listings and arc directions suite.

**Tier:** D.R.D research file → D.P.S.A predictive overlay

---

**A3. Tertiary and Minor Progressions**

**What it adds:**
- **Tertiary progressions:** One lunar month after birth = one year of life. Faster than secondary progressions; tracks emotional and environmental shifts at a more granular level.
- **Minor progressions:** One tropical month after birth = one year of life. Even faster; bridges the gap between secondaries and tertiaries.

**Why it matters:** SNRS v1+v2 has secondary progressions only. Tertiary and minor progressions provide resolution at different time scales — secondaries show the long arc of soul development, tertiaries show the emotional current beneath it, minors show the day-to-day environmental texture. Together, the three form a complete progression suite.

**AstroGold implementation:** Tertiary and Minor progressions are macOS-exclusive chart types in AstroGold.

**Tier:** D.P.S.A predictive overlay addition

---

**A4. Progressed Lunar Phases**

**What it adds:** The secondary progressed Moon moves approximately 1° per month. As it moves, it forms phase relationships with the secondary progressed Sun — creating an 8-phase cycle (New, Crescent, First Quarter, Gibbous, Full, Disseminating, Last Quarter, Balsamic) with a period of approximately 30 years. Each phase is a distinct psychological and developmental chapter. The phase Morph was born into (Balsamic, First Quarter, etc.) is itself a natal signature; the current phase in the progressed cycle is a life chapter map.

**Why it matters:** This is a distinct layer from monthly lunations or natal lunar phase. It reads the arc of soul development over 30-year cycles — deeply aligned with the evolutionary astrology layer already in SNRS.

**AstroGold implementation:** Dedicated Astro Sheet — *Progressed Lunar Phases* — tracking the current phase, exact degree of phase ingress, and duration.

**Tier:** D.P.S.A predictive overlay

---

**A5. Syzygies — Pre-Natal Lunation**

**What it adds:** The *syzygy* is the most recent new moon or full moon before birth — the last celestial reset before incarnation. In Hellenistic astrology (Paulus Alexandrinus, Valens), the pre-natal syzygy point is a significant sensitive point in the chart. Its sign, house placement, and the planet ruling it indicate the soul's karmic inheritance from the prior lunar cycle — what was completed or left incomplete before the current life began.

**Note:** SNRS v1 includes pre-natal solar and lunar eclipse points through the Evolutionary Astrology layer. The pre-natal syzygy is the more granular Hellenistic precursor to this — not the same calculation.

**AstroGold implementation:** Listed under *Syzygies/Eclipses data* in the macOS guide.

**Tier:** D.R.D research file → D.P.S.A natal overlay

---

**A6. Western Lunar Mansions (28 Mansions)**

**What it adds:** The 28 Lunar Mansions are a Western astrological system (distinct from Vedic Nakshatras) dividing the zodiac into 28 stations of approximately 12°51' each — tracking the Moon's movement through one synodic cycle. Found in medieval Arabic astrology (Ibn Arabi, Picatrix) and Renaissance magic. Each mansion has a specific archetypal quality, timing function, and practical application in ritual timing and magical workings.

**Why distinct from Nakshatras:** SNRS already has Vedic Nakshatras (v1 + standalone in v2 B1). The Western Lunar Mansions use a different division system, different archetypal assignments, and have a different theoretical lineage (Arabic-Hermetic vs. Vedic). They are parallel systems reading the same Moon movement through different cultural architectures.

**Chart-specific significance:** Directly relevant to D.O.M (ritual timing, magical workings) — the mansions are the primary timing system for Western magical operations tied to the Moon.

**AstroGold implementation:** Listed in the macOS user guide as *Lunar Mansions* — a dedicated sheet.

**Tier:** D.R.D research file → D.O.M timing overlay + D.P.S.A natal overlay

---

**A7. Eclipse Search and Lunation Tracking**

**What it adds:** A systematic forward-looking tool: all eclipses (solar and lunar) within a defined timeframe, with their degree positions flagged against natal placements. Eclipses aspecting natal planets within orb trigger major activation windows — they are among the most reliable long-range timing tools in predictive astrology.

**Why it extends v1+v2:** SNRS v1 includes pre-natal eclipses (evolutionary layer). v3 adds the forward-looking eclipse tracking system — knowing when eclipses will hit natal degrees in the coming years is essential sovereign predictive intelligence.

**AstroGold implementation:** *Eclipse Search* — macOS-exclusive event search tool. Also present in the Graphic Ephemeris display.

**Tier:** D.P.S.A predictive workflow addition

---

**A8. Lunar Phase Returns**

**What it adds:** The chart cast for the exact moment each month when the Moon returns to the same phase angle it held at birth (not just the same degree — the same Sun-Moon phase relationship). This produces a monthly forecast chart distinct from the Lunar Return (which tracks only the Moon's degree return). The Lunar Phase Return captures the full Sun-Moon relational dynamic at its reset point.

**AstroGold implementation:** *Lunar Phase Returns* — macOS-exclusive chart type.

**Tier:** D.P.S.A monthly tracking addition

---

### CATEGORY B — DIRECTION AND ARC METHOD COMPLETIONS

**B1. Djwhal Khul (DK) Ayanamsa**

**What it adds:** AstroGold includes "Djwhal Khul" as one of its seven sidereal zodiac options — this is the Bailey-specific ayanamsa. While SNRS already runs the full Bailey esoteric framework (soul rulers, rays, crosses), all sidereal computation has used Lahiri ayanamsa. The DK ayanamsa is calibrated to Bailey's own cosmological framework — running the sidereal chart through the DK ayanamsa produces the sidereal overlay that is internally consistent with the Bailey system rather than with Vedic/Lahiri conventions.

**Why it matters:** This is potentially the most significant v3 addition given that Bailey's framework is the spine of the entire SNRS esoteric layer. The Lahiri sidereal and DK sidereal will produce slightly different degree positions — the DK version is the more internally coherent choice for Bailey-aligned readings.

**Required action:** Compute the chart under both Lahiri and DK ayanamsa; document the degree differences for each placement; flag any placements that shift sign or house under DK; integrate DK sidereal positions into the Bailey esoteric overlay file.

**AstroGold implementation:** Listed explicitly as "Djwhal Khul" in the sidereal zodiac dropdown alongside Fagan-Allen, Lahiri, DeLuce, Raman, UshaShashi, Krishnamurti.

**Tier:** D.P.S.A natal overlay update — DK ayanamsa column added to existing Bailey layer

---

**B2. Ascendant Arc and Vertex Arc Directions**

**What it adds:**
- **Ascendant Arc:** The Ascendant's rate of daily motion (rather than the Sun's) is used as the arc measure. Produces a different timing cadence than solar arc.
- **Vertex Arc:** The Vertex's daily motion is the arc measure. The Vertex is the electrical axis of the chart — fate and destined encounter. Vertex-arc directions track the timing of fated thresholds.

**Why they complete the arc suite:** SNRS v1+v2 has solar arc directions. The arc suite is not complete until all three primary arc methods are computed — each uses a different reference point and surfaces different timing signatures.

**AstroGold implementation:** Available as direction types in the iOS chart type list (*Ascendant arc, Vertex arc*); included in macOS direction calculation options.

**Tier:** D.P.S.A predictive overlay addition

---

**B3. Arc Direction Calculation Variants (Naibod, Solar Arc in R.A., Mean Quotidian)**

**What it adds:** AstroGold offers five methods for calculating house cusps in progressed/directed charts:
- **Solar Arc in Longitude** (already in SNRS v1)
- **Solar Arc in Right Ascension** — uses R.A. rather than ecliptic longitude; produces slightly different timing for angles
- **Naibod in Longitude** — uses the mean daily solar motion (59'08") as the arc rather than the actual arc; traditional method
- **Naibod in R.A.** — Naibod rate applied in right ascension
- **Mean Quotidian** — very fast arc based on mean diurnal motion; tracks angle movement in short periods

**Why it matters:** Different traditions use different arc methods. Running multiple arc variants surfaces convergence points — when two or more arc methods produce the same directed hit to the same planet simultaneously, the timing confidence is very high.

**AstroGold implementation:** *Progressed chart calculation methods* — selectable in chart settings.

**Tier:** D.P.S.A computation notes; flag convergence in predictive overlays

---

**B4. Heliocentric Chart**

**What it adds:** The chart computed from the Sun's perspective rather than Earth's — all planetary positions calculated heliocentrically. Earth appears as a point rather than the Sun. Bailey's esoteric astrology specifically references heliocentric readings as the soul-level chart, distinct from the personality-level geocentric chart. The heliocentric chart reveals the soul's position within the solar system rather than the personality's experience of the solar system.

**AstroGold implementation:** *Heliocentric* coordinate system option; Earth displayed instead of Sun.

**Tier:** D.R.D research file (Bailey's heliocentric doctrine) → D.P.S.A soul-level overlay

---

### CATEGORY C — POINT AND TRADITION COMPLETIONS

**C1. Uranian Astrology — Hamburg School Hypotheticals**

**What it adds:** A complete parallel tradition founded by Alfred Witte (early 20th century, Hamburg). Uses eight hypothetical transsaturnian planets — not physical bodies but mathematical points computed from observed planetary patterns:

| Hypothetical | Archetype |
|---|---|
| Cupido | Community, art, marriage, groups |
| Hades | Decay, depth, the ancient, hidden matters |
| Zeus | Controlled power, fire, creativity, leaders |
| Kronos | Authority, height, government, mastery |
| Apollo | Expansion, commerce, far-reaching influence |
| Admetos | Standstill, depth work, raw material, the primitive |
| Vulcanus | Enormous force, power, strength beyond measure |
| Poseidon | Spiritual clarity, illumination, ideas, the infinite |

The Hamburg School also uses 90° and 45° dials as its primary reading tool — reading midpoints and planetary pictures (three-point combinations) rather than aspects.

**Why it matters:** These eight points function as archetypes that standard astrology has no equivalent for. Kronos (mastery/authority) and Poseidon (spiritual illumination) are of particular relevance given Morph's chart signature. The Uranian tradition is also the primary tradition that works with the Ebertin midpoint system already in SNRS v1 — they are architecturally linked.

**AstroGold implementation:** Listed explicitly as "Uranian Planets + Transpluto bodies" — available across all platforms.

**Tier:** D.R.D research file (Alfred Witte + Reinhold Ebertin lineage) → D.P.S.A overlay

---

**C2. TransPluto (Isis)**

**What it adds:** A hypothetical body (also called Isis or Bacchus in different traditions) computed beyond Pluto's orbit. In Uranian astrology, TransPluto represents the principle of *perfection, purification, and the demand for completeness* — the archetype of the exacting, refining force that strips away everything inessential. Closely tied to Virgo and 6th house themes at the archetypal level.

**AstroGold implementation:** Included in the Uranian/Hypothetical points set across all platforms.

**Tier:** D.P.S.A extended points overlay

---

**C3. Hygeia and Astraea**

**What it adds:**
- **Hygeia (10):** Asteroid of health, hygiene, and preventive care. The body's relationship to wellness as a proactive principle rather than reactive crisis. Directly relevant to D.B.S integration.
- **Astraea (5):** Asteroid of justice, law, the last goddess to leave Earth at the end of the Golden Age. Themes of fairness, legal matters, holding to principle in a corrupted environment.

**Why absent from v1:** SNRS v1 includes Chiron, Ceres, Pallas, Juno, Vesta, Black Moon Lilith, Eris, Selena/Vulcan. Hygeia and Astraea are in AstroGold's standard 44-point set but weren't captured in the v1 asteroid specification.

**AstroGold implementation:** Listed in the standard 44 chart points across all platforms.

**Tier:** D.P.S.A extended points overlay; Hygeia flagged for D.B.S integration

---

**C4. Planetary Nodes and Apsides**

**What it adds:** Every planet has heliocentric nodes — the points where its orbit crosses the ecliptic plane. These are distinct from the lunar nodes. Planetary nodes represent the karmic axis of each planet's function — the north node of Venus is the point of Venus's greatest karmic forward pull; the south node is its inherited pattern. Apsides (perihelion/aphelion nodes) mark the points where each planet is closest to and farthest from the Sun.

**Why it matters:** The lunar nodes are already in SNRS. Extending the node concept to all planets gives each planet its own karmic axis — a significantly deeper reading of what each planet's evolutionary direction is, not just where it sits by sign and house.

**AstroGold implementation:** *Planetary Nodes & Apsides* — macOS-exclusive feature. Listed as a distinct sheet.

**Tier:** D.R.D research file → D.P.S.A natal overlay (flagged as advanced; Phase 7+)

---

**C5. Aries Point and World Axis**

**What it adds:** 0° Aries (the Aries Point) is the vernal equinox — the junction between personal and collective. In Uranian astrology and modern practice, any natal planet within 1-2° of 0° cardinal (0° Aries, Cancer, Libra, Capricorn) is said to be on the World Axis — directly connected to public events, mass consciousness, and collective manifestation. The planet on the World Axis doesn't stay private; its expression tends to project outward into the collective field.

**Chart-specific significance:** Needs identification — which if any of Morph's placements fall on or aspect the World Axis. This is a short calculation but can reveal a significant pattern about which planetary functions have collective rather than purely personal expression.

**AstroGold implementation:** Listed as *Aries Point* and *Libra Point* in the standard chart points set.

**Tier:** D.P.S.A natal overlay note; check against birth data

---

**C6. Extended Minor Body Sets (Egyptian Asteroids, Muses, 180 Minor Planets)**

**What it adds:** AstroGold includes 154 extra bodies beyond the standard set — organized into themed sets (Egyptian mythology asteroids, Muses, general minor planets). The Egyptian asteroid set is directly relevant to the Kemetic research thread in D.R.D. For purposes of SNRS, this is not a priority read of all 154 bodies — but targeted extraction of Egyptically significant asteroids (Isis, Osiris, Horus, Thoth, Sekhmet, Hathor, Maat, Anubis where they exist as named minor planets) is worth computing against Morph's chart.

**AstroGold implementation:** *154 extra bodies* — macOS feature. Includes Egyptian and Muses asteroid sets.

**Tier:** D.P.S.A extended overlay — Egyptian minor planets only (targeted, not exhaustive)

---

### CATEGORY D — SOVEREIGN REPORT SUITE

**First-time definition of SNRS's output document architecture.**

AstroGold offers 15 professional report types. SNRS defines its own sovereign equivalents — not consumer-facing reports but sovereign intelligence documents in Pandora OS voice. These are output artifacts of the SNRS computation and reading process.

---

**D1. Sovereign Birth Report**
**Equivalent to:** AstroGold Professional Birth Chart Report (~29 pages)
**SNRS equivalent:** `dpsa_report_sovereign-birth_v1.md`
**Coverage:** The complete natal reading across all SNRS layers — the master document that synthesizes v1+v2+v3 into a single reading artifact organized by life domain (identity, purpose, relationship intelligence, resources, creative power, shadow work, soul mission).
**Note:** This is distinct from `dpsa_natal_morph_complete_v3.md` — that is the technical overlay file. The Birth Report is the interpreted, voiced reading document.

---

**D2. Sovereign Predictive Report (Annual)**
**Equivalent to:** AstroGold Predictive Report (~23 pages) + Birthday Report (Solar Return)
**SNRS equivalent:** `dpsa_report_predictive_[YEAR]_v1.md`
**Coverage:** All active predictive layers for a given 12-month window — Firdaria lord, profection year lord, zodiacal releasing period, secondary progressed aspects perfecting, solar arc hits, major transits with exact dates, solar return chart read. One integrated document per year.

---

**D3. Sovereign Monthly Report (Lunar)**
**Equivalent to:** AstroGold Lunar Return Report (~17 pages)
**SNRS equivalent:** `dpsa_report_lunar_[YYYY-MM]_v1.md`
**Coverage:** Lunar return chart read, current Firdaria sub-period, transits for the month, lunar phase return, lunation hitting natal points, Western Mansion of the New Moon, Nakshatra of the Full Moon.

---

**D4. Sovereign Vocation Report**
**Equivalent to:** AstroGold Vocation Report (~24 pages, author Brian Clark)
**SNRS equivalent:** `dpsa_report_vocation_v1.md`
**Coverage:** Career and calling read through: Lunar Nodes (destiny axis), Midheaven and 10th house, 2nd house (income), 6th house (work/craft), 8th house (other people's resources, transformation work), Midheaven ruler's placement, Saturn (mastery through discipline), Almuten Figuris (overall chart governor), Bailey soul purpose read (esoteric MC ruler). Cross-referenced with STIS for business intelligence alignment.

---

**D5. Sovereign Money and Resource Report**
**Equivalent to:** AstroGold Money Report (~26 pages, Stephanie Johnson + Brian Clark)
**SNRS equivalent:** `dpsa_report_resource_v1.md`
**Coverage:** 2nd house (earned income, values), 8th house (inherited resources, transformation of value, debt), 11th house (income from groups, networks), Venus (what you attract), Jupiter (abundance principle), Saturn (the container), Part of Fortune. Cross-referenced with STIS for investment and market timing alignment.

---

**D6. Sovereign Kindred Patterns Report**
**Equivalent to:** AstroGold Kindred Spirits Report (~24 pages) + Family Report
**SNRS equivalent:** `dpsa_report_kindred_v1.md`
**Coverage:** 4th house (origin, ancestral inheritance, home base), Moon (the mother/instinct layer), 3rd house (siblings, immediate environment), 11th house (chosen family, soul tribe), 7th house (the mirror — what we attract and project). Not a synastry document — a natal map of Morph's relational architecture and ancestral patterns.

---

**D7. Sovereign Big Three + Decans Report**
**Equivalent to:** AstroGold Big Three Report (~15 pages) with decan interpretation
**SNRS equivalent:** `dpsa_report_big-three_v1.md`
**Coverage:** Sun (Taurus / decan read), Moon (Scorpio / decan read), Ascendant (Cancer / decan read) — each interpreted through orthodox, esoteric, and sovereign voice layers. Includes self-care integration note per placement. Short-form; accessible as a quick orientation document.

---

## 3. COMPLETE READING STACK (v1 + v2 + v3)

```
FOUNDATION (v1 — APPROVED 2026-04-24)
──────────────────────────────────────────────
Tropical (Whole Sign primary + Placidus angles)
Sidereal (Lahiri ayanamsa overlay)
Bailey Esoteric (soul rulers, rays, cross)
Hellenistic dignities (domicile/exaltation/
  triplicity/term/face/sect)
Fixed stars (angles + personal planets, 1° orb)
Arabic lots (Fortune, Spirit, Eros, Courage,
  Victory, Necessity, Nemesis)
Declinations + out-of-bounds planets
Midpoints (Ebertin 45° sort)
Harmonics (5th, 7th, 9th / Navamsa)
Draconic chart (soul-intent overlay)
Sabian symbols (per degree, all placements)
Nakshatras (Moon, Sun, ASC — Lahiri)
Evolutionary astrology (Pluto polarity point,
  prenatal eclipses)
Predictive layers (secondary progressions,
  solar arc, solar/lunar returns, transits,
  zodiacal releasing, profections)

EXTENSIONS (v2 — APPROVED 2026-05-08)
──────────────────────────────────────────────
Decanic / 36 Faces           [A1 — COMPLETE]
Galactic Center conjunction  [A2]
Venus Morning Star phase      [A3]
Jaimini Atmakaraka            [A4]
Hermetic Sphere Descent       [A5]
Antiscia + Contra-Antiscia    [A6]
Nakshatra standalone layer    [B1]
Astrocartography              [B2]
Chinese Ba Zi / Four Pillars  [B3]
Mayan Tzolkin                 [B4]
Synodic return calendar       [B5]
Medical astrology body map    [B6]
Almuten Figuris               [B7]
Eris + outer dwarf planets    [B8]

EXTENSIONS (v3 — DRAFT 2026-05-10)
──────────────────────────────────────────────
CATEGORY A — PREDICTIVE COMPLETIONS
Firdaria (Persian time-lords)            [A1]
Primary Directions (van Dam)             [A2]
Tertiary + Minor Progressions            [A3]
Progressed Lunar Phases                  [A4]
Syzygies (pre-natal lunation)            [A5]
Western Lunar Mansions (28)              [A6]
Eclipse Search + Forward Tracking        [A7]
Lunar Phase Returns                      [A8]

CATEGORY B — DIRECTION/ARC COMPLETIONS
Djwhal Khul (DK) Ayanamsa               [B1]
Ascendant Arc + Vertex Arc              [B2]
Arc Variants (Naibod, R.A., Quotidian)  [B3]
Heliocentric Chart                       [B4]

CATEGORY C — POINT/TRADITION COMPLETIONS
Uranian Hypotheticals (Witte 8)          [C1]
TransPluto (Isis)                        [C2]
Hygeia + Astraea                         [C3]
Planetary Nodes + Apsides                [C4]
Aries Point / World Axis                 [C5]
Egyptian + Kemetic Minor Planets         [C6]

CATEGORY D — SOVEREIGN REPORT SUITE
Sovereign Birth Report                   [D1]
Sovereign Predictive Report (Annual)     [D2]
Sovereign Monthly Report (Lunar)         [D3]
Sovereign Vocation Report                [D4]
Sovereign Money and Resource Report      [D5]
Sovereign Kindred Patterns Report        [D6]
Sovereign Big Three + Decans Report      [D7]
```

**Total stack: v1 (15 layers) + v2 (14 systems) + v3 (26 systems/outputs) = 55 components**

---

## 4. PHASED BUILD PLAN (v3)

v3 work begins only after v2 Phase 6 (master overlay integration) is complete.

### PHASE 7 — PRIORITY COMPUTATION (v3 high-impact, fast-to-compute)

**Goal:** Add the high-significance additions that require minimal new research — they extend computation of existing data.

**Sequence:**

1. **DK ayanamsa computation** [B1] — recompute chart using Djwhal Khul ayanamsa; produce degree-comparison table against Lahiri; flag sign/house shifts; add DK column to Bailey overlay file.

2. **Firdaria calculation** [A1] — identify sect (night chart confirmed); compute major and sub-period lords from birth; identify current lord + next transition date; add to `dpsa_natal_morph_complete_v3.md` predictive section.

3. **Aries Point / World Axis check** [C5] — identify any natal placements within 2° of 0° cardinal; document in existing extended points file.

4. **Hygeia + Astraea positions** [C3] — compute degree positions; add to asteroid overlay; flag Hygeia for D.B.S integration.

5. **TransPluto position** [C2] — compute and add to extended points file.

6. **Syzygies computation** [A5] — identify pre-natal syzygy (last New or Full Moon before 2006-08-21); compute its degree and house; add to evolutionary astrology section.

7. **Arc Direction Variants** [B3] — compute Solar Arc in R.A., Naibod in Longitude, Naibod in R.A. for current year; compare timing signatures against Solar Arc in Longitude already computed.

### PHASE 8 — RESEARCH AND TRADITION DECONSTRUCTION

**Goal:** Build the D.R.D research foundation for the three traditions requiring full decode before integration.

**Sequence:**

1. **D.R.D research file: Uranian/Hamburg School** [C1] — Alfred Witte, Reinhold Ebertin (linking to existing midpoint work), the eight hypotheticals. Tier the sources. Compute the hypothetical positions for Morph's chart. Produce `drd_research_uranian-hamburg-school_v1.md`.

2. **D.R.D research file: Firdaria doctrine** [A1] — Persian origins, sect-based logic, major/sub-period structure, deconstruction of primary sources. Produce `drd_research_firdaria-persian-time-lords_v1.md`.

3. **D.R.D research file: Primary Directions** [A2] — historical lineage (Ptolemy through van Dam), method comparison against solar arc, chart-specific computation. Produce `drd_research_primary-directions_v1.md`.

4. **D.R.D research file: Western Lunar Mansions** [A6] — Arabic sources (Ibn Arabi, Picatrix), mansion assignments, D.O.M ritual timing application. Produce `drd_research_western-lunar-mansions_v1.md`.

5. **D.R.D research file: Heliocentric astrology** [B4] — Bailey's heliocentric doctrine specifically; compute Morph's heliocentric chart; compare soul-level read against geocentric. Produce `drd_research_heliocentric-soul-chart_v1.md`.

6. **Egyptian/Kemetic minor planets** [C6] — identify named minor planets with Kemetic significance; compute positions; cross-reference with existing Kemetic research in D.R.D.

### PHASE 9 — OVERLAY FILE PRODUCTION

**Goal:** Build individual D.P.S.A overlay files for each v3 system.

1. `dpsa_natal_morph_uranian-hypotheticals_v1.md` — eight Witte points + TransPluto, positions and archetypal reads [C1, C2]
2. `dpsa_natal_morph_firdaria_v1.md` — full life map of major/sub-period lords with date ranges [A1]
3. `dpsa_natal_morph_primary-directions_v1.md` — primary directions computation and near-term hits [A2]
4. `dpsa_natal_morph_heliocentric_v1.md` — soul-chart overlay [B4]
5. `dpsa_natal_morph_lunar-mansions_v1.md` — natal Moon's mansion + D.O.M timing calendar [A6]
6. `dpsa_natal_morph_planetary-nodes_v1.md` — heliocentric planetary nodes for all bodies [C4]
7. `dpsa_natal_morph_progressions-suite_v1.md` — tertiary + minor progressions added alongside secondary [A3]
8. `dpsa_natal_morph_progressed-lunar-phases_v1.md` — current progressed phase, ingress dates [A4]
9. `dom_timing_western-lunar-mansions_calendar.md` — D.O.M ritual timing application [A6]

### PHASE 10 — SOVEREIGN REPORT PRODUCTION

**Goal:** Produce the seven sovereign report documents from the full SNRS stack.

**Priority sequence (most complete data available first):**

1. `dpsa_report_big-three_v1.md` — fastest to produce; foundational [D7]
2. `dpsa_report_vocation_v1.md` — high priority; connects to D.S.E business intelligence [D4]
3. `dpsa_report_resource_v1.md` — high priority; connects to STIS and D.S.E [D5]
4. `dpsa_report_kindred_v1.md` — relational architecture [D6]
5. `dpsa_report_sovereign-birth_v1.md` — master document; requires all overlays complete [D1]
6. `dpsa_report_predictive_2026_v1.md` — current year; time-sensitive [D2]
7. `dpsa_report_lunar_[YYYY-MM]_v1.md` — monthly; begins as recurring workflow [D3]

---

## 5. WHAT v3 DOES NOT INCLUDE

These AstroGold features were reviewed and intentionally scoped out of v3:

- **Full KP (Krishnamurti Paddhati) system** — KP is a complete Vedic sub-system requiring its own ayanamsa and sub-lord calculation architecture. Worth dedicated research (possibly v4 or a separate D.P.S.A KP layer), but out of v3 scope.
- **Harmonic Age charts** — age-specific harmonic overlays. The 5th/7th/9th harmonics in v1 cover the core harmonic work; harmonic age charts are a specialized extension for a later phase.
- **Mundane/Ingress astrology** — world events charts (Aries ingress, etc.). Relevant to geopolitical intelligence (possible D.S.S application) but not to personal natal reading.
- **Synastry/Composite reports** — explicitly out of scope for SNRS which is Morph's personal chart only.
- **All 154+ minor bodies exhaustively** — only the Egyptian/Kemetic subset is in scope [C6]. Full minor planet integration is a potential future module.
- **Fagan-Allen, DeLuce, Raman, UshaShashi sidereal systems** — these are Vedic and cosmobiology-lineage ayanamsas. Lahiri (for Vedic compatibility) and DK (for Bailey compatibility) are the two in scope.
- **Pet report equivalent** — not applicable.

---

## 6. SUCCESS CRITERIA — v3

v3 is complete when:

1. DK ayanamsa chart computed and integrated into Bailey overlay [B1]
2. Firdaria map complete — full life-period lords identified, current lord named [A1]
3. Uranian hypotheticals computed and archetypal reads produced for each [C1]
4. Primary directions computation complete with near-term hits identified [A2]
5. Western Lunar Mansions research complete and D.O.M timing calendar active [A6]
6. Heliocentric soul chart produced and compared against geocentric [B4]
7. All seven sovereign report documents exist as distinct output files [D1–D7]
8. `dpsa_natal_morph_complete_v3.md` integrates all v3 additions into the master file
9. v3 PRD status updated to APPROVED in this file header

---

## 7. REFERENCES — NEW (v3 ADDITIONS)

### Uranian / Hamburg School
- Alfred Witte, *Rules for Planetary Pictures* — Tier 1
- Reinhold Ebertin, *The Combination of Stellar Influences* — Tier 1 (links to v1 midpoint work)
- Arlene Kramer, *Principles of the Uranian System* — Tier 2

### Firdaria
- Benjamin Dykes (trans.), *Persian Nativities* — Tier 1
- Robert Hand, *Night and Day: Planetary Sect in Astrology* — Tier 1

### Primary Directions
- Placidus de Titis, *Primum Mobile* — Tier 1 (historical)
- Martin Gansten, *Primary Directions* — Tier 1
- Wim van Dam, *Planets in Solar Returns* — Tier 2

### Western Lunar Mansions
- Picatrix (Ghayat al-Hakim) — Tier 1
- Christopher Warnock, *Mansions of the Moon* — Tier 2

### Heliocentric Astrology
- Alice Bailey, *Esoteric Astrology* (Chapter VII on heliocentric) — Tier 1
- Michael Erlewine, *Astrophysical Directions* — Tier 2

### Pre-Natal Syzygy
- Paulus Alexandrinus, *Introductory Matters* — Tier 1
- Vettius Valens, *Anthology* — Tier 1

### Progressed Lunar Phases
- Dane Rudhyar, *The Lunation Cycle* — Tier 1
- Tracy Marks, *The Art of Chart Interpretation* — Tier 2

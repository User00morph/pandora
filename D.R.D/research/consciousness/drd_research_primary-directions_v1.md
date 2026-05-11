# D.R.D RESEARCH — PRIMARY DIRECTIONS
**Type:** raw-extract → research
**Domain:** Pre-Western Knowledge / Consciousness
**Confidence:** Established (within tradition)
**Destination:** D.P.S.A (natal predictive overlay)
**Filed:** 2026-05-10
**Source tier:** See below

---

## SOURCE TIER ASSESSMENT

| Source | Tier | Notes |
|---|---|---|
| Claudius Ptolemy, *Tetrabiblos* (2nd c. CE) | Tier 1 | Foundational primary source; established the doctrine of primary directions as the premier predictive method |
| Placidus de Titis, *Primum Mobile* (1657) | Tier 1 | The definitive Baroque-era systematization; the "Placidean" method is named for him |
| Martin Gansten, *Primary Directions: Astrology's Old Master Technique* (2009) | Tier 1 | Best modern critical reconstruction; translates and systematizes the historical literature |
| Wim van Dam, *Astrological Techniques*, various | Tier 2 | The van Dam method referenced in AstroGold and modern computational systems |
| Robert Hand, *Planets in Transit* | Tier 2 | Contextualizes primary directions within the broader predictive tradition |

---

## 1. DOCTRINE

Primary directions are the most historically prestigious predictive technique in Western astrology — used by Ptolemy, Abu Mashar, Lilly, and every major traditional astrologer from antiquity through the 17th century. They fell from mainstream practice during the 18th–19th centuries as secondary progressions and transits rose to dominance, but have been systematically revived in the late-20th century reconstructionist movement.

**Core principle:** After birth, the heavens continue their diurnal rotation (the Earth's daily rotation causing all celestial bodies to appear to move westward across the sky). The arc traveled by a significator (a natal planet or angle) in this continuing rotation corresponds to time in the native's life. **Specifically: 1° of diurnal arc = 1 year of life.**

This is a *real, astronomical motion* — not the symbolic "day for a year" equation of secondary progressions, which is an analogy. Primary directions use the actual celestial mechanics of the post-birth sky.

---

## 2. HOW THEY WORK

### The Symbolic Key
- The Earth rotates 360° in 24 hours
- Therefore: 1 hour of time = 15° of arc
- Therefore: 4 minutes of time = 1° of arc
- Therefore: 4 minutes post-birth ≈ 1 year of life

**Practical meaning:** Looking at what celestial points move into exact aspect with natal planets in the hours after birth reveals the timing of major life events for corresponding years.

### What is directed
In classical primary directions, the usual significators are the Ascendant, Midheaven, and the luminaries (Sun and Moon). The *promittors* (the points they are directed toward) are natal planets and sensitive points.

In modern computational approaches (including AstroGold), all natal planets and angles can be directed, producing a much larger set of hits.

### The arc of direction
The arc of direction is computed in *right ascension* (RA) — the equatorial coordinate system — not ecliptic longitude. This is what makes primary directions computationally distinct from secondary progressions (which work in ecliptic longitude).

**Example:** If the Ascendant needs to travel 35° of RA to conjunct the natal position of Saturn, this direction perfects at age 35.

---

## 3. METHODS

### Placidean Method (Placidus de Titis)
Uses the *under-the-pole* method for computing house positions, consistent with the Placidus house system. Directions are computed in the Placidean semi-arc system. This is the most historically prevalent Western method and is what most traditional sources describe.

### Regiomontanus Method
Uses the Regiomontanus house system's mathematical framework for computing directions. Preferred by some traditional astrologers as more geometrically rigorous.

### Van Dam Method
Wim van Dam's refinement uses modern computational precision (Swiss Ephemeris quality) to compute primary directions. The van Dam method is essentially the Placidean method with high-precision astronomical data — what AstroGold and other modern software implement.

### In Mundo vs. In Zodiaco
- **In Mundo:** The direction is measured in terms of the planet's actual movement through the houses — a three-dimensional spatial calculation
- **In Zodiaco:** The direction is measured along the ecliptic, using longitude alone — a two-dimensional calculation

Traditional literature uses both; modern software computes both. They produce different timing for the same directions.

---

## 4. THE ARC VARIANTS (SNRS v3 B3)

The "arc" used in solar arc directions, ascendant arc directions, and vertex arc directions are all derived from the primary direction concept. The difference is which celestial body's daily motion provides the arc measure:

| Method | Arc unit | Traditional key |
|---|---|---|
| Primary directions | Right ascension of the significator's actual motion | 1° RA = 1 year |
| Solar arc (longitude) | Sun's ecliptic longitude daily motion | 1° ecliptic = 1 year |
| Solar arc (RA) | Sun's RA daily motion | ~1° RA = 1 year |
| Naibod arc (longitude) | Mean daily solar motion: 0°59'08" | 0.986° = 1 year |
| Naibod arc (RA) | Mean RA equivalent | ~0.986° RA = 1 year |
| Ascendant arc | Ascendant's daily RA motion | Variable (ASC moves faster near equator) |
| Vertex arc | Vertex's daily RA motion | Variable |
| Mean Quotidian | Mean daily motion of MC | Very fast; used for angle positions in short periods |

**The key insight:** Different arc methods measure different things. When two or more arc methods produce a hit to the same natal planet within the same year, confidence in that year's significance is high. **Convergence is the signal; divergence is the norm.**

---

## 5. INTERPRETATION

### What primary directions time
Primary directions are traditionally associated with *major life thresholds* — events of structural significance that alter the life course. They are not suited to day-to-day timing (transits handle that) but to decade-scale and year-scale watershed events.

Classical uses:
- Directions to the Ascendant: changes in the body, circumstances, physical beginnings
- Directions to the Midheaven: career, public life, reputation changes
- Directions to Sun: life force, father, authority figures, health of the vital principle
- Directions to Moon: mother, emotional security, domestic circumstances, public standing
- Hard aspects (conjunction, opposition, square) → crisis or confrontation with the directed archetype
- Soft aspects (trine, sextile) → facilitated expression, assistance from the directed archetype

### Orb for primary directions
Traditional: 1° orb (= 1 year of approach + 1 year of departure = effective 2-year window)
Modern practice: sometimes extended to 1.5° but rarely beyond

### Priority hits for Morph's chart (to be computed)
The highest-priority primary directions to compute for Morph's chart are:
1. Directions to/from the Ascendant (00° Cancer) — the incarnational threshold
2. Directions to/from the Midheaven (03° Pisces)
3. Directions involving Saturn (05° Leo) — the just-completed Firdaria lord
4. Directions involving Jupiter (12° Scorpio) — the incoming Firdaria lord
5. Directions involving Pluto (26° Sagittarius) — soul-level transformation axis

**Computation required:** pyswisseph or AstroGold primary directions module for birth data: May 12, 2006, 13:07 UT, 44.5133°N / 88.0158°W.

---

## 6. RELATIONSHIP TO SECONDARY PROGRESSIONS AND SOLAR ARC

| Feature | Primary Directions | Secondary Progressions | Solar Arc |
|---|---|---|---|
| Basis | Actual celestial rotation post-birth | Day-for-year symbolic analogy | Sun's actual motion as symbolic arc |
| Coordinate | Right ascension (equatorial) | Ecliptic longitude | Ecliptic longitude (or RA variant) |
| Historical prestige | Highest (classical period) | 18th–20th c. dominant | 20th c. dominant |
| Events timed | Major life thresholds | Soul development arc | Major outer-planet transits to progressed positions |
| Speed | Same as arc methods (~1°/year) | Progressed Moon: ~1°/month | Same as primary (~1°/year) |

**Together, all three form a complete predictive triangle** — each reads a different dimension of time.

---

*drd_research_primary-directions_v1.md | D.R.D | Pandora OS*

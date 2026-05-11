# D.R.D RESEARCH — HELIOCENTRIC ASTROLOGY / SOUL-CHART
**Type:** raw-extract → research
**Domain:** Consciousness / Pre-Western Knowledge
**Confidence:** Established (within Bailey tradition); Investigating (cross-tradition)
**Destination:** D.P.S.A (heliocentric soul-chart overlay)
**Filed:** 2026-05-10
**Source tier:** See below

---

## SOURCE TIER ASSESSMENT

| Source | Tier | Notes |
|---|---|---|
| Alice Bailey (via Djwhal Khul), *Esoteric Astrology* (1951) — specifically Chapter VII | Tier 1 | Primary Bailey source on heliocentric; the soul-chart doctrine originates here within the esoteric framework |
| Michael Erlewine, *Astrophysical Directions* (1977) | Tier 2 | First systematic modern computation of heliocentric charts for astrological use; establishes the practical framework |
| Eon Parai & David Cochrane, various publications on heliocentric astrology | Tier 2 | Modern computational approaches |
| AstroGold documentation (accessed 2026-05-10) | Tier 3 | Confirms heliocentric as a standard chart computation option |

---

## 1. DOCTRINE

### The Geocentric vs. Heliocentric Distinction

**Geocentric astrology** (standard): Charts computed from Earth's perspective — the observer is at the center, and all planets are positioned relative to Earth's location.

**Heliocentric astrology**: Charts computed from the Sun's perspective — the observer is at the center of the solar system, and all planets (including Earth) are positioned relative to the Sun.

**Key differences:**
- In heliocentric charts, there is **no Sun placement** — the Sun is the center from which all positions are measured
- **Earth** appears as a chart point (approximately opposite the geocentric Sun's position)
- The Moon is **not included** in heliocentric charts (the Moon orbits Earth, not the Sun)
- All planetary positions shift slightly from their geocentric positions due to the change in perspective
- **Retrogrades disappear** — from the Sun's perspective, all planets orbit in direct motion; retrogrades are a geocentric optical effect
- For slower planets (Jupiter outward), the difference between geocentric and heliocentric position is relatively small (often under 5°). For faster planets (Mercury, Venus), the difference can be significant.

---

## 2. BAILEY'S ESOTERIC RATIONALE

In *Esoteric Astrology* (Chapter VII), the Tibetan Master Djwhal Khul presents heliocentric astrology as the **soul-level chart** — the chart of the solar angel (the higher self / soul) rather than the personality's experience of incarnation.

**The doctrine:**
- The **geocentric chart** = the personality chart — how the outer, incarnated self experiences the energies
- The **heliocentric chart** = the soul chart — the soul's direct relationship to the solar system's forces, unmediated by Earth's filtering perspective

**Rationale:** Earth (matter, incarnation) is the central reference point of the geocentric chart. The soul is not Earth-bound — it is identified with the Sun (the solar logos, the spiritual will). From the soul's perspective, the Sun is the center — hence heliocentric positioning is the more accurate map of the soul's celestial relationships.

**Bailey's specific use:** DK does not extensively interpret individual heliocentric charts in the published works, but establishes the theoretical framework: heliocentric positions of the outer planets (Pluto especially) reveal the soul's evolutionary agenda with greater clarity than the geocentric position.

---

## 3. KEY HELIOCENTRIC PRINCIPLES

### Earth as a Chart Point
In the heliocentric chart, **Earth appears at the degree opposite the geocentric Sun's position** (approximately — there is a slight parallax adjustment for precise computation).

Morph's geocentric Sun: 21° Taurus 40'
**Approximate heliocentric Earth: ~21° Scorpio 40'** (directly opposite)

The Earth degree in the heliocentric chart carries a different meaning than the geocentric Sun: it represents the *point of incarnation* — where the soul entered the Earth plane. In Bailey's framework, the Earth degree is the soul's chosen entry point into matter.

### Planetary Positions
The outer planets (Saturn, Uranus, Neptune, Pluto) have minimal difference between geocentric and heliocentric positions (typically under 1°). The inner planets (Mercury, Venus, Mars) can have significant differences.

For Morph's chart (requires precise pyswisseph computation with `SEFLG_HELCTR` flag):
- Mercury geocentric: 14° Taurus 14' → heliocentric: requires computation (can be significantly different)
- Venus geocentric: 10° Aries 21' → heliocentric: requires computation
- Mars geocentric: 16° Cancer 41' → heliocentric: requires computation
- Jupiter geocentric: 12° Scorpio 59' R → heliocentric: approximately same (less than 1° difference; retrograde disappears)
- Saturn geocentric: 05° Leo 34' → heliocentric: approximately same
- Uranus geocentric: 14° Pisces 09' → heliocentric: approximately same
- Neptune geocentric: 19° Aquarius 47' → heliocentric: approximately same
- Pluto geocentric: 26° Sagittarius 16' R → heliocentric: approximately same (retrograde disappears)

**The significant differences will be in Mercury, Venus, and Mars.** These personal planet positions in the heliocentric chart reveal the soul's direct relationship to the mental principle (Mercury), the aesthetic/value principle (Venus), and the action/desire principle (Mars) — unfiltered by Earth's perspective.

### No Retrogrades in Heliocentric
**Jupiter, Pluto, Saturn are retrograde in Morph's geocentric chart.** In the heliocentric chart, all retrogrades disappear — what appeared to be inward-turned energy from Earth's perspective is revealed as forward-moving from the soul's perspective. This is a significant reframe: the retrograde quality of these planets is not a soul-level condition but a personality-level *experience* of those planets' forward motion from an Earth-bound perspective.

---

## 4. DJWHAL KHUL AYANAMSA — COMPUTATIONAL NOTE

### The DK Ayanamsa Defined
The Swiss Ephemeris documentation references the DK ayanamsa as: "Pole of true galactic plane, calculated by DK." This ayanamsa is distinct from the Galactic Center (GC)-anchoring ayanamsa.

**Two different DK-related ayanamsa concepts exist in the literature:**

1. **GC-anchoring ayanamsa:** Places the Galactic Center at 0° Sagittarius in the sidereal zodiac. The GC is at approximately 26°56' Sagittarius tropical (2006), so this ayanamsa ≈ 26°56'. This produces a dramatically different sidereal zodiac from Lahiri.

2. **Swiss Ephemeris DK ayanamsa (SIDM_TRUE_CITRA or DK_D86):** The Swiss Ephemeris uses a specific calculation based on the galactic plane pole, which produces a different value. The exact numerical value for 2006 requires reading the pyswisseph constant `swe.SIDM_DK_D86` or equivalent.

**Action required:** Compute the DK ayanamsa value for May 12, 2006 via:
```python
import swisseph as swe
jd = swe.julday(2006, 5, 12, 13.117)  # 13:07 UT
swe.set_sid_mode(swe.SIDM_TRUE_CITRA)  # or SIDM_DK_D86 if available
ayanamsa = swe.get_ayanamsa_ut(jd)
print(f"DK ayanamsa value: {ayanamsa:.4f}°")
```

**Working assumption until computed:** The DK ayanamsa is likely in the range of 22°–27°, probably closer to the Lahiri value (23°51') than the extreme GC-anchoring value (26°56'). The operational difference from Lahiri will shift sidereal positions by the delta between the two ayanamsa values.

**Most significant impact:** Pluto at 26° Sagittarius 16' is only 40' from the GC under tropical calculation. Under the DK ayanamsa, the question is whether Pluto and the GC maintain their near-conjunction or separate. **This must be precisely computed.**

---

## 5. INTEGRATION WITH SNRS BAILEY LAYER

The heliocentric chart is the *soul's chart* in Bailey's framework. The Bailey esoteric layer (soul rulers, rays, esoteric crosses) is already the soul-level interpretation layer of SNRS — the heliocentric chart adds the soul's *positional* data to complement the soul's *interpretive* data.

**Integration principle:**
- Geocentric chart + Bailey esoteric interpretation = personality-through-soul-lens
- Heliocentric positions = soul's direct celestial coordinates

For each natal planet, the complete Bailey-integrated read would include:
1. Geocentric position (personality's experience)
2. Bailey esoteric ruler (soul's governance layer)
3. Heliocentric position (soul's direct positional coordinate)

---

## 6. COMPUTATION COMMAND (PYSWISSEPH)

```python
import swisseph as swe

swe.set_ephe_path('/path/to/ephemeris')
jd = swe.julday(2006, 5, 12, 13 + 7/60)  # 13:07 UT

print("=== HELIOCENTRIC CHART ===")
bodies = {
    swe.SUN: "Sun (not applicable — center)",
    swe.MOON: "Moon (not applicable — geocentric body)",
    swe.MERCURY: "Mercury",
    swe.VENUS: "Venus",
    swe.MARS: "Mars",
    swe.JUPITER: "Jupiter",
    swe.SATURN: "Saturn",
    swe.URANUS: "Uranus",
    swe.NEPTUNE: "Neptune",
    swe.PLUTO: "Pluto",
    swe.EARTH: "Earth",
}

for body, name in bodies.items():
    if body in [swe.SUN, swe.MOON]:
        continue
    result = swe.calc_ut(jd, body, swe.FLG_SWIEPH | swe.FLG_HELCTR)
    lon = result[0][0]
    sign = int(lon / 30)
    deg = lon % 30
    signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
             "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
    print(f"{name}: {deg:.2f}° {signs[sign]}")
```

---

*drd_research_heliocentric-soul-chart_v1.md | D.R.D | Pandora OS*

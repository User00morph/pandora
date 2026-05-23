#!/usr/bin/env python3
"""
PANDORA — ASPECT SCANNER
Finds tight planetary aspects and calculates when ASC/MC will trigger them.
Earik Beann intraday methodology.

Usage:
  python3 aspect_scanner.py                    # Today, New York
  python3 aspect_scanner.py --date 2026-06-04  # Specific date
  python3 aspect_scanner.py --location london  # London session
  python3 aspect_scanner.py --orb 2.0          # Tighter orb filter
"""

import ephem
import math
import argparse
from datetime import date, datetime, timedelta, timezone


# ── Aspect definitions ────────────────────────────────────────────────────────
ASPECTS = {
    'Conjunction':  {'angle': 0,   'division': 1, 'power': 5},
    'Opposition':   {'angle': 180, 'division': 2, 'power': 5},
    'Trine':        {'angle': 120, 'division': 3, 'power': 4},
    'Square':       {'angle': 90,  'division': 4, 'power': 4},
    'Sextile':      {'angle': 60,  'division': 6, 'power': 3},
    'Quincunx':     {'angle': 150, 'division': 0, 'power': 2},
    'SemiSquare':   {'angle': 45,  'division': 8, 'power': 2},
}

# Planets to scan
PLANET_OBJECTS = {
    'Moon':    ephem.Moon,
    'Mercury': ephem.Mercury,
    'Venus':   ephem.Venus,
    'Sun':     ephem.Sun,
    'Mars':    ephem.Mars,
    'Jupiter': ephem.Jupiter,
    'Saturn':  ephem.Saturn,
    'Uranus':  ephem.Uranus,
    'Neptune': ephem.Neptune,
}

# Planet power weights for aspect scoring
PLANET_POWER = {
    'Moon': 5, 'Sun': 5, 'Mercury': 4, 'Venus': 4,
    'Mars': 3, 'Jupiter': 3, 'Saturn': 3,
    'Uranus': 2, 'Neptune': 2, 'Pluto': 1,
}

# Observer locations
LOCATIONS = {
    'new_york': {'lat': '40.7128', 'lon': '-74.0060', 'tz_offset': -4, 'label': 'New York (EDT)'},
    'london':   {'lat': '51.5074', 'lon': '-0.1278',  'tz_offset': 1,  'label': 'London (BST)'},
    'chicago':  {'lat': '41.8781', 'lon': '-87.6298', 'tz_offset': -5, 'label': 'Chicago (CDT)'},
    'tokyo':    {'lat': '35.6762', 'lon': '139.6503', 'tz_offset': 9,  'label': 'Tokyo (JST)'},
}

RAD_TO_DEG = 180.0 / math.pi
SID_DAY_MIN = 23 * 60 + 56.07  # minutes in a sidereal day


def get_planet_ra(planet_name: str, obs: ephem.Observer) -> float:
    """Get planet's Right Ascension in degrees."""
    obj = PLANET_OBJECTS[planet_name]()
    obj.compute(obs)
    return float(obj.ra) * RAD_TO_DEG


def get_ecliptic_lon(planet_name: str, obs: ephem.Observer) -> float:
    """Get planet's ecliptic longitude in degrees (for aspect calculation)."""
    obj = PLANET_OBJECTS[planet_name]()
    obj.compute(obs)
    ecl = ephem.Ecliptic(obj)
    return float(ecl.lon) * RAD_TO_DEG


def angular_difference(a: float, b: float) -> float:
    """Smallest angular difference between two ecliptic positions."""
    diff = abs(a - b) % 360
    return min(diff, 360 - diff)


def is_applying(planet1: str, planet2: str, obs: ephem.Observer, aspect_angle: float) -> bool:
    """
    Returns True if the aspect between planet1 and planet2 is APPLYING
    (planets moving toward exact), False if separating.
    Uses a tiny time step to determine direction.
    """
    dt = 0.5 / 24  # 30 minutes ahead
    obs2 = ephem.Observer()
    obs2.lat = obs.lat
    obs2.lon = obs.lon
    obs2.date = ephem.Date(float(obs.date) + dt)

    lon1_now = get_ecliptic_lon(planet1, obs)
    lon2_now = get_ecliptic_lon(planet2, obs)
    lon1_later = get_ecliptic_lon(planet1, obs2)
    lon2_later = get_ecliptic_lon(planet2, obs2)

    diff_now   = angular_difference(lon1_now, lon2_now)
    diff_later = angular_difference(lon1_later, lon2_later)

    # Applying: the gap to the nearest aspect angle is shrinking
    def gap_to_nearest_aspect(diff):
        gaps = [abs(diff - a) for a in [0, 60, 90, 120, 150, 180]]
        return min(gaps)

    return gap_to_nearest_aspect(diff_later) < gap_to_nearest_aspect(diff_now)


def find_aspects(obs: ephem.Observer, orb: float = 2.0) -> list:
    """
    Find all planetary aspects within the given orb.
    Returns sorted list of aspect dicts.
    """
    planets = list(PLANET_OBJECTS.keys())
    found = []

    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            p1, p2 = planets[i], planets[j]
            lon1 = get_ecliptic_lon(p1, obs)
            lon2 = get_ecliptic_lon(p2, obs)
            diff = angular_difference(lon1, lon2)

            for asp_name, asp in ASPECTS.items():
                angle = asp['angle']
                # Check the aspect and its supplement (for trine: 120 and 240)
                for target in [angle, 360 - angle]:
                    actual_diff = abs(lon1 - lon2) % 360
                    check_diff = min(abs(actual_diff - target), 360 - abs(actual_diff - target))

                    if check_diff <= orb:
                        applying = is_applying(p1, p2, obs, angle)
                        exactness = orb - check_diff  # higher = tighter
                        power = asp['power'] * PLANET_POWER.get(p1, 2) * PLANET_POWER.get(p2, 2)

                        found.append({
                            'planet1':   p1,
                            'planet2':   p2,
                            'aspect':    asp_name,
                            'angle':     angle,
                            'orb':       round(check_diff, 3),
                            'applying':  applying,
                            'power':     power,
                            'lon1':      round(lon1, 2),
                            'lon2':      round(lon2, 2),
                            'ra1':       round(get_planet_ra(p1, obs), 2),
                            'ra2':       round(get_planet_ra(p2, obs), 2),
                        })
                        break  # found this aspect, no need to check 360-angle

    # Sort: applying first, then by tightness (orb ascending)
    found.sort(key=lambda x: (not x['applying'], x['orb']))
    return found


def mc_at_time(obs: ephem.Observer) -> float:
    """Return current MC (Midheaven) in degrees RA."""
    return float(obs.sidereal_time()) * RAD_TO_DEG


def time_until_mc_reaches(target_ra: float, obs: ephem.Observer, tz_offset: int) -> dict:
    """
    Calculate when MC and ASC will transit a given RA degree today.
    Returns dict with UTC and local times.
    """
    current_mc = mc_at_time(obs)
    deg_to_go = (target_ra - current_mc) % 360
    minutes_ahead = deg_to_go * (SID_DAY_MIN / 360)

    # Convert ephem.Date float to datetime
    base_dt = ephem.Date(obs.date).datetime()
    mc_utc = base_dt + timedelta(minutes=minutes_ahead)
    mc_local = mc_utc + timedelta(hours=tz_offset)

    # ASC transits same RA ~6 hours (90°) before MC
    asc_utc = mc_utc - timedelta(minutes=SID_DAY_MIN / 4)
    asc_local = asc_utc + timedelta(hours=tz_offset)

    # DSC = 6h after MC
    dsc_utc = mc_utc + timedelta(minutes=SID_DAY_MIN / 4)
    dsc_local = dsc_utc + timedelta(hours=tz_offset)

    return {
        'mc_utc':   mc_utc,
        'mc_local': mc_local,
        'asc_utc':  asc_utc,
        'asc_local': asc_local,
        'dsc_utc':  dsc_utc,
        'dsc_local': dsc_local,
        'deg_to_go': round(deg_to_go, 2),
        'min_ahead': round(minutes_ahead, 1),
    }


def build_trigger_schedule(aspects: list, obs: ephem.Observer, tz_offset: int,
                            location_label: str) -> list:
    """
    For each aspect, calculate when ASC and MC trigger each planet's RA.
    Returns sorted list of trigger events for the day.
    """
    triggers = []
    seen_times = set()

    for asp in aspects:
        for planet_key, ra_key in [('planet1', 'ra1'), ('planet2', 'ra2')]:
            planet = asp[planet_key]
            ra = asp[ra_key]
            timing = time_until_mc_reaches(ra, obs, tz_offset)

            for trigger_type, utc_t, local_t in [
                ('MC',  timing['mc_utc'],  timing['mc_local']),
                ('ASC', timing['asc_utc'], timing['asc_local']),
                ('DSC', timing['dsc_utc'], timing['dsc_local']),
            ]:
                # Only include times within today's trading window
                hour = local_t.hour
                if 7 <= hour <= 17:  # 7am-5pm local time
                    # Deduplicate times within 5-minute windows
                    time_bucket = (trigger_type, local_t.hour, local_t.minute // 5)
                    if time_bucket not in seen_times:
                        seen_times.add(time_bucket)
                        triggers.append({
                            'local_time':   local_t.strftime('%H:%M'),
                            'utc_time':     utc_t.strftime('%H:%M UTC'),
                            'trigger':      trigger_type,
                            'planet':       planet,
                            'aspect':       asp['aspect'],
                            'partners':     asp['planet1'] if planet == asp['planet2'] else asp['planet2'],
                            'orb':          asp['orb'],
                            'applying':     asp['applying'],
                            'power':        asp['power'],
                            'sort_key':     local_t,
                        })

    triggers.sort(key=lambda x: x['sort_key'])
    return triggers


def power_bar(power: int, max_power: int = 100) -> str:
    pct = min(power / max_power, 1.0)
    filled = int(pct * 10)
    return '█' * filled + '░' * (10 - filled)


def print_report(aspects: list, triggers: list, location_label: str, scan_date: str):
    print()
    print('═' * 68)
    print('  PANDORA — ASPECT SCANNER')
    print(f'  Date: {scan_date}   Location: {location_label}')
    print('═' * 68)

    # Aspects found
    applying = [a for a in aspects if a['applying']]
    separating = [a for a in aspects if not a['applying']]

    print(f'\n  APPLYING ASPECTS ({len(applying)}) — Energy BUILDING:')
    if applying:
        print(f'  {"Planets":22s} {"Aspect":12s} {"Orb":>6s}  {"Power":12s}  Status')
        print(f'  {"─"*22}  {"─"*12}  {"─"*6}  {"─"*12}  {"─"*10}')
        for a in applying:
            pair = f'{a["planet1"]} / {a["planet2"]}'
            bar = power_bar(a['power'])
            print(f'  {pair:22s}  {a["aspect"]:12s}  {a["orb"]:5.2f}°  {bar}  ◆ APPLYING')
    else:
        print('  None within orb.')

    if separating:
        print(f'\n  SEPARATING ASPECTS ({len(separating)}) — Energy dissipating:')
        for a in separating[:5]:
            pair = f'{a["planet1"]} / {a["planet2"]}'
            print(f'  {pair:22s}  {a["aspect"]:12s}  {a["orb"]:5.2f}°  (separating)')

    # Trigger schedule
    print(f'\n  TRIGGER SCHEDULE — Watch times today:')
    print(f'  {"Time":8s}  {"Trig":5s}  {"Planet":10s}  {"Aspect w/":12s}  {"Orb":>5s}  {"Signal"}')
    print(f'  {"─"*8}  {"─"*5}  {"─"*10}  {"─"*12}  {"─"*5}  {"─"*20}')

    if triggers:
        for t in triggers:
            quality = '◆◆ HIGH' if t['applying'] and t['orb'] < 0.5 else \
                      '◆ MED'  if t['applying'] and t['orb'] < 1.5 else \
                      '  low'
            print(f'  {t["local_time"]:8s}  {t["trigger"]:5s}  {t["planet"]:10s}  '
                  f'{t["partners"]:12s}  {t["orb"]:4.2f}°  {quality}')
    else:
        print('  No triggers in trading window.')

    # T-Square detection
    t_squares = find_t_squares(aspects)
    if t_squares:
        print(f'\n  T-SQUARES DETECTED ({len(t_squares)}) — Highest power configurations:')
        for ts in t_squares:
            print(f'  {ts["p1"]} – {ts["p2"]} – {ts["p3"]}')
            print(f'    Empty corner triggers at: {ts["empty_corner"]:.1f}° RA')

    print()
    print('  HOW TO USE:')
    print('  1. Applying aspects = energy is building (prioritize these)')
    print('  2. At each trigger time → watch for price reversal')
    print('  3. Price levels: map planet RA to price via the price wheel')
    print('  4. T-squares = highest probability reversal configurations')
    print('  5. Tighter orb (<0.5°) = more precise timing')
    print()
    print('═' * 68)


def find_t_squares(aspects: list) -> list:
    """Detect T-square configurations (three planets in square/opposition pattern)."""
    t_squares = []
    squares_opps = [a for a in aspects if a['aspect'] in ('Square', 'Opposition')]

    for i in range(len(squares_opps)):
        for j in range(i + 1, len(squares_opps)):
            a1, a2 = squares_opps[i], squares_opps[j]
            # Find shared planet
            shared = set([a1['planet1'], a1['planet2']]) & set([a2['planet1'], a2['planet2']])
            if shared:
                focal = list(shared)[0]
                others = [p for p in [a1['planet1'], a1['planet2'],
                                       a2['planet1'], a2['planet2']] if p != focal]
                if len(others) >= 2:
                    # Empty corner = opposite the focal planet
                    focal_ra = a1['ra1'] if a1['planet1'] == focal else a1['ra2']
                    empty_ra = (focal_ra + 180) % 360
                    t_squares.append({
                        'p1': focal, 'p2': others[0], 'p3': others[1],
                        'empty_corner': empty_ra,
                    })
    return t_squares


def main():
    parser = argparse.ArgumentParser(description='Pandora Aspect Scanner')
    parser.add_argument('--date',     help='Date YYYY-MM-DD (default: today)')
    parser.add_argument('--location', default='new_york',
                        choices=list(LOCATIONS.keys()), help='Trading location')
    parser.add_argument('--orb',      type=float, default=2.0, help='Aspect orb in degrees')
    parser.add_argument('--time',     default='13:30',
                        help='Start time UTC for MC calc (default: 13:30 = NYSE open)')
    args = parser.parse_args()

    scan_date = args.date or date.today().isoformat()
    loc = LOCATIONS[args.location]

    # Build observer
    obs = ephem.Observer()
    obs.lat = loc['lat']
    obs.lon = loc['lon']
    obs.elevation = 10
    obs.date = ephem.Date(f"{scan_date.replace('-', '/')} {args.time}:00")

    print(f'\n  Scanning aspects for {scan_date} at {args.time} UTC...')

    aspects  = find_aspects(obs, orb=args.orb)
    triggers = build_trigger_schedule(aspects, obs, loc['tz_offset'], loc['label'])

    print_report(aspects, triggers, loc['label'], scan_date)


if __name__ == '__main__':
    main()

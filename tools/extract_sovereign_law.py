#!/usr/bin/env python3
"""
Pandora OS — Sovereign Law / Entity Stack Extraction
Extracts transcripts via youtube_transcript_api (no audio download).
Videos: credit union, AI contracting, treasury direct, inalienable rights,
        lex mercatori, frivolous firewall, economic mastery (retry).
"""

import os
import sys
import time
from pathlib import Path

OUTPUT_DIR = Path("/Users/emoefedorgu/Desktop/Pandora/D.R.D/research/systemic-analysis")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

VIDEOS = [
    ("H6ZoFwwiqHY", "This Credit Union Gives ANYONE $50,000 With a 580 FICO Score", "sovereign-finance"),
    ("I-enT6szVQQ", "I Used AI to Fix Government Contracting", "tech-sovereign"),
    ("VrqEMO3-nps", "Treasury Direct Trust Forms: A List of Forms to Research", "sovereign-entity"),
    ("9d6rlqSvXuA", "Your Inalienable Rights: Denoting Privilege", "sovereign-law"),
    ("YeckVwrzUwU", "Lex Mercatori: The Law Merchant and SECURED TRANSACTIONS", "sovereign-law"),
    ("Imtp_y5TlpU", "Frivolous: A Firewall Protocol", "sovereign-law"),
    ("NwaIhcs2XV0", "Economic Mastery Class — Credit Business Credit Exemptions", "sovereign-finance"),
]

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("ERROR: youtube_transcript_api not installed")
    sys.exit(1)

api = YouTubeTranscriptApi()

def fetch_transcript(video_id):
    try:
        return list(api.fetch(video_id))
    except Exception as e:
        print(f"  ERROR: {e}")
        return None

def format_transcript(entries):
    lines = []
    for entry in entries:
        start = getattr(entry, 'start', 0)
        minutes = int(start // 60)
        seconds = int(start % 60)
        text = getattr(entry, 'text', '').replace('\n', ' ').strip()
        if text:
            lines.append(f"[{minutes:02d}:{seconds:02d}] {text}")
    return '\n'.join(lines)

results = []
for video_id, title, domain in VIDEOS:
    print(f"\nExtracting: {title}")
    print(f"  ID: {video_id}")

    entries = fetch_transcript(video_id)
    if not entries:
        print(f"  FAILED — no transcript available")
        results.append((video_id, title, domain, False, 0))
        continue

    formatted = format_transcript(entries)
    word_count = len(formatted.split())

    # Build output filename
    slug = title.lower().replace(' ', '-').replace(':', '').replace("'", '').replace('"', '').replace('/', '-').replace(',', '')[:60]
    outfile = OUTPUT_DIR / f"drd_research_{slug}_raw-extract.md"

    content = f"""---
title: {title}
video_id: {video_id}
url: https://www.youtube.com/watch?v={video_id}
domain: {domain}
words: {word_count}
extracted: 2026-06-06
stage: raw-extract
pipeline: sovereign-law-entity-stack
---

# RAW EXTRACT — {title}

## Source Metadata
- **Title:** {title}
- **Video ID:** {video_id}
- **URL:** https://www.youtube.com/watch?v={video_id}
- **Domain:** {domain}
- **Word Count:** {word_count}
- **Extracted:** 2026-06-06
- **Pipeline:** Sovereign Law / Entity Stack

---

## Transcript

{formatted}
"""

    outfile.write_text(content)
    print(f"  OK — {word_count} words → {outfile.name}")
    results.append((video_id, title, domain, True, word_count))
    time.sleep(1)

print("\n\n=== SOVEREIGN LAW EXTRACTION SUMMARY ===")
for vid_id, title, domain, success, words in results:
    status = f"OK ({words:,} words)" if success else "FAILED"
    print(f"  [{status}] {title}")

print("\nDone.")

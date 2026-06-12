#!/usr/bin/env python3
"""
Pandora OS — Consciousness / Natural Law Extraction
Extracts transcripts via youtube_transcript_api (no audio download).
Videos: Self Actualization, Mark Passio Natural Law Full + Part 1.
"""

import os
import sys
import time
from pathlib import Path

OUTPUT_DIR = Path("/Users/emoefedorgu/Desktop/Pandora/D.R.D/research/pre-western-knowledge")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

VIDEOS = [
    ("laJzABwqi3U", "Self Actualization: The reality of the governing forces against your TRUE SELF", "consciousness"),
    ("ChgCh2Gui5M", "Mark Passio Natural Law Seminar FULL version", "natural-law"),
    ("ASUHN3gNxWo", "Mark Passio - Natural Law Seminar - New Haven CT - Part 1 of 3", "natural-law"),
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
    print(f"\nExtracting: {title[:60]}...")
    print(f"  ID: {video_id}")

    entries = fetch_transcript(video_id)
    if not entries:
        print(f"  FAILED — no transcript available")
        results.append((video_id, title, domain, False, 0))
        continue

    formatted = format_transcript(entries)
    word_count = len(formatted.split())

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
pipeline: natural-law-consciousness
---

# RAW EXTRACT — {title}

## Source Metadata
- **Title:** {title}
- **Video ID:** {video_id}
- **URL:** https://www.youtube.com/watch?v={video_id}
- **Domain:** {domain}
- **Word Count:** {word_count}
- **Extracted:** 2026-06-06
- **Pipeline:** Consciousness / Natural Law

---

## Transcript

{formatted}
"""

    outfile.write_text(content)
    print(f"  OK — {word_count} words → {outfile.name}")
    results.append((video_id, title, domain, True, word_count))
    time.sleep(1)

print("\n\n=== NATURAL LAW EXTRACTION SUMMARY ===")
for vid_id, title, domain, success, words in results:
    status = f"OK ({words:,} words)" if success else "FAILED"
    print(f"  [{status}] {title[:70]}")

print("\nDone.")

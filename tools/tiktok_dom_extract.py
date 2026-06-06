#!/usr/bin/env python3
"""
Pandora OS — TikTok Collection Extractor (D.O.M)
Downloads videos from TikTok collection URLs, transcribes with Whisper,
and outputs structured transcripts for D.R.D intake.

Usage: python3 tiktok_dom_extract.py
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path

# --- CONFIG ---
COLLECTIONS = {
    "rootwurk": "https://www.tiktok.com/@user00morph/collection/rootwurk-7642094010722470669",
    "magik":    "https://www.tiktok.com/@user00morph/collection/magik-7637397325959465741",
}
OUTPUT_DIR = Path("/Users/emoefedorgu/Desktop/Pandora/research-deconstruction /dom-magik-rootwurk-raw")
VIDEO_DIR  = OUTPUT_DIR / "videos"
MODEL_SIZE = "small"   # small gives better accuracy for short-form content
DEVICE     = "cpu"
# --- END CONFIG ---


def setup_ffmpeg():
    try:
        import static_ffmpeg
        static_ffmpeg.add_paths()
        print("[ffmpeg] static-ffmpeg paths registered")
    except Exception as e:
        print(f"[ffmpeg] WARNING: {e} — will try system ffmpeg")


def load_model():
    from faster_whisper import WhisperModel
    print(f"[model] Loading faster-whisper '{MODEL_SIZE}' on {DEVICE} ...")
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="int8")
    print("[model] Ready.")
    return model


def list_collection(url: str, label: str) -> list[dict]:
    """Return list of {title, url} dicts from a TikTok collection."""
    print(f"\n[list] Fetching {label} collection index...")
    result = subprocess.run(
        [
            sys.executable, "-m", "yt_dlp",
            "--flat-playlist",
            "--print", "%(title)s|||%(url)s",
            "--no-warnings",
            url,
        ],
        capture_output=True, text=True, timeout=120
    )
    videos = []
    for line in result.stdout.strip().splitlines():
        if "|||" in line:
            title, video_url = line.split("|||", 1)
            videos.append({"title": title.strip(), "url": video_url.strip()})
    print(f"[list] {len(videos)} videos found in '{label}'")
    return videos


def download_video(video_url: str, out_dir: Path, label: str, idx: int) -> Path | None:
    """Download a single TikTok video. Returns path to downloaded file."""
    out_dir.mkdir(parents=True, exist_ok=True)
    output_template = str(out_dir / f"{label}_{idx:02d}_%(id)s.%(ext)s")

    # Check if already downloaded
    existing = list(out_dir.glob(f"{label}_{idx:02d}_*.mp4"))
    if existing:
        print(f"  [skip] {label}_{idx:02d} already downloaded")
        return existing[0]

    result = subprocess.run(
        [
            sys.executable, "-m", "yt_dlp",
            "--format", "mp4/best[ext=mp4]/best",
            "--output", output_template,
            "--no-warnings",
            "--quiet",
            video_url,
        ],
        capture_output=True, text=True, timeout=120
    )

    found = list(out_dir.glob(f"{label}_{idx:02d}_*.mp4"))
    if found:
        return found[0]

    # Try with .mp4 extension directly
    found = list(out_dir.glob(f"{label}_{idx:02d}_*"))
    if found:
        return found[0]

    print(f"  [error] Download failed: {result.stderr[:200] if result.stderr else 'no output'}")
    return None


def transcribe_file(model, video_path: Path, collection: str) -> dict:
    """Transcribe a video. Returns metadata dict with transcript text."""
    txt_path = video_path.with_suffix(".txt")

    if txt_path.exists():
        print(f"  [skip] {video_path.name} — transcript exists")
        return {"file": video_path.name, "status": "skipped", "transcript": txt_path.read_text()}

    print(f"  [transcribing] {video_path.name}")
    try:
        segments, info = model.transcribe(str(video_path), beam_size=5)
        full_text = " ".join(seg.text.strip() for seg in segments)
        word_count = len(full_text.split())
        duration = info.duration or 0

        txt_path.write_text(full_text)
        print(f"  [done] {word_count} words | {duration:.0f}s")
        return {
            "file": video_path.name,
            "status": "transcribed",
            "words": word_count,
            "duration_s": round(duration),
            "transcript": full_text,
        }
    except Exception as e:
        print(f"  [error] {e}")
        return {"file": video_path.name, "status": f"error: {e}", "transcript": ""}


def build_raw_extract(all_results: dict[str, list[dict]], output_dir: Path):
    """Write the combined raw extract markdown file for D.R.D intake."""
    out_path = output_dir / "drd_research_dom-magik-rootwurk_raw-extract.md"

    total_words = sum(
        r.get("words", 0)
        for entries in all_results.values()
        for r in entries
    )
    total_videos = sum(len(v) for v in all_results.values())

    lines = [
        "# D.R.D RAW EXTRACT — D.O.M Magik & Rootwurk TikTok Collections",
        f"**Source:** Morph's TikTok collections — `rootwurk` + `magik`",
        f"**Total videos:** {total_videos} | **Total words:** ~{total_words:,}",
        f"**Extracted:** 2026-06-02",
        f"**Stage:** 1 (Raw Extract) — ready for Stage 3 decode",
        f"**Department routing:** D.O.M (primary) | D.R.D (decode) | D.P.S.A (practices) | D.B.S (herbs/body)",
        "",
        "---",
        "",
    ]

    for collection_label, entries in all_results.items():
        lines.append(f"## COLLECTION: {collection_label.upper()}")
        lines.append("")
        success = [e for e in entries if e.get("status") in ("transcribed", "skipped") and e.get("transcript")]
        errors  = [e for e in entries if "error" in e.get("status", "")]
        lines.append(f"**{len(success)} transcribed | {len(errors)} errors**")
        lines.append("")

        for i, entry in enumerate(entries, 1):
            title = entry.get("title", "untitled")
            creator = entry.get("creator", "unknown")
            words = entry.get("words", 0)
            duration = entry.get("duration_s", 0)
            transcript = entry.get("transcript", "").strip()
            status = entry.get("status", "")

            lines.append(f"### {collection_label.upper()}-{i:02d} | {title[:80]}")
            lines.append(f"**Creator:** @{creator} | **Words:** {words} | **Duration:** {duration}s | **Status:** {status}")
            lines.append("")
            if transcript:
                lines.append(transcript)
            else:
                lines.append(f"[{status}]")
            lines.append("")
            lines.append("---")
            lines.append("")

    out_path.write_text("\n".join(lines))
    print(f"\n[extract] Raw extract saved → {out_path}")
    return out_path


def main():
    setup_ffmpeg()
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1 — list all collections
    collection_index: dict[str, list[dict]] = {}
    for label, url in COLLECTIONS.items():
        collection_index[label] = list_collection(url, label)

    # Step 2 — download all videos
    print("\n[download] Downloading videos...")
    for label, videos in collection_index.items():
        coll_dir = VIDEO_DIR / label
        coll_dir.mkdir(parents=True, exist_ok=True)
        for i, video in enumerate(videos, 1):
            print(f"  [{label} {i}/{len(videos)}] {video['title'][:60]}")
            path = download_video(video["url"], coll_dir, label, i)
            video["local_path"] = str(path) if path else None
            video["creator"] = video["url"].split("/@")[1].split("/")[0] if "/@" in video["url"] else "unknown"

    # Step 3 — transcribe
    print("\n[transcribe] Loading Whisper model...")
    model = load_model()

    all_results: dict[str, list[dict]] = {}
    for label, videos in collection_index.items():
        results = []
        print(f"\n[transcribe] Collection: {label}")
        for video in videos:
            if not video.get("local_path"):
                results.append({
                    "title": video["title"],
                    "creator": video.get("creator", "unknown"),
                    "status": "download_failed",
                    "transcript": "",
                    "words": 0,
                    "duration_s": 0,
                })
                continue
            meta = transcribe_file(model, Path(video["local_path"]), label)
            meta["title"] = video["title"]
            meta["creator"] = video.get("creator", "unknown")
            results.append(meta)
        all_results[label] = results

    # Step 4 — build raw extract
    extract_path = build_raw_extract(all_results, OUTPUT_DIR)

    # Summary
    total = sum(len(v) for v in all_results.values())
    done  = sum(1 for entries in all_results.values() for e in entries if e.get("status") in ("transcribed", "skipped"))
    failed = total - done
    print(f"\n[COMPLETE] {done}/{total} transcribed | {failed} failed")
    print(f"[OUTPUT]   {extract_path}")


if __name__ == "__main__":
    main()

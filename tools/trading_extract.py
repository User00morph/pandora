#!/usr/bin/env python3
"""
Pandora OS — Trading Videos Whisper Extraction
Transcribes MP4 files from iCloud trading directory.
Output → research-deconstruction /trading-raw/

Usage: python3 trading_extract.py
"""

import os
import sys
import time
import json
from pathlib import Path

# --- CONFIG ---
VIDEO_DIR = Path("/Users/emoefedorgu/Library/Mobile Documents/com~apple~CloudDocs/trading ")
OUTPUT_DIR = Path("/Users/emoefedorgu/Desktop/Pandora/research-deconstruction /trading-raw")
MODEL_SIZE = "small"   # small for better accuracy on financial/technical content
DEVICE = "cpu"
EXTENSIONS = {".mp4", ".mov", ".MP4", ".MOV"}
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


def transcribe_file(model, video_path: Path, output_dir: Path, index: int) -> dict:
    label = f"TRADE-{index:02d}"
    safe_stem = video_path.stem.replace(" ", "_").replace("/", "-")
    txt_path = output_dir / f"{label}_{safe_stem}.txt"
    meta_path = output_dir / f"{label}_{safe_stem}.meta.json"

    if txt_path.exists():
        print(f"  [skip] {video_path.name} — transcript exists")
        return {"label": label, "file": video_path.name, "status": "skipped"}

    start = time.time()
    print(f"  [transcribing] {label} | {video_path.name}")

    try:
        segments, info = model.transcribe(
            str(video_path),
            beam_size=5,
            language=None,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500),
        )

        text_parts = []
        segment_list = []
        for seg in segments:
            text_parts.append(seg.text.strip())
            segment_list.append({
                "start": round(seg.start, 2),
                "end": round(seg.end, 2),
                "text": seg.text.strip(),
            })

        full_text = " ".join(text_parts)
        elapsed = round(time.time() - start, 1)

        txt_path.write_text(
            f"LABEL: {label}\n"
            f"FILE: {video_path.name}\n"
            f"SIZE: {round(video_path.stat().st_size / 1_000_000, 1)}MB\n"
            f"LANGUAGE: {info.language} (confidence: {round(info.language_probability, 2)})\n"
            f"DURATION: {round(info.duration, 1)}s\n"
            f"TRANSCRIBED: {elapsed}s processing\n"
            f"{'='*60}\n\n"
            f"{full_text}\n",
            encoding="utf-8"
        )

        meta = {
            "label": label,
            "file": video_path.name,
            "size_mb": round(video_path.stat().st_size / 1_000_000, 1),
            "language": info.language,
            "language_confidence": round(info.language_probability, 3),
            "duration_seconds": round(info.duration, 1),
            "processing_seconds": elapsed,
            "word_count": len(full_text.split()),
            "status": "ok",
        }
        meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

        print(f"    -> {label} | {info.language} | {round(info.duration/60, 1)}min | {len(full_text.split())} words | {elapsed}s")
        return meta

    except Exception as e:
        print(f"    -> ERROR: {e}")
        txt_path.write_text(f"LABEL: {label}\nFILE: {video_path.name}\nERROR: {e}\n", encoding="utf-8")
        return {"label": label, "file": video_path.name, "status": "error", "error": str(e)}


def run():
    setup_ffmpeg()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not VIDEO_DIR.exists():
        print(f"[ERROR] Video directory not found: {VIDEO_DIR}")
        sys.exit(1)

    videos = sorted([f for f in VIDEO_DIR.iterdir() if f.suffix in EXTENSIONS])
    print(f"[scan] {VIDEO_DIR.name.strip()}: {len(videos)} video files")

    if not videos:
        print("No video files found.")
        sys.exit(1)

    print(f"[output] Transcripts → {OUTPUT_DIR}\n")

    model = load_model()

    results = []
    for i, vpath in enumerate(videos, 1):
        print(f"\n[{i}/{len(videos)}]", end=" ")
        result = transcribe_file(model, vpath, OUTPUT_DIR, i)
        results.append(result)

    ok = sum(1 for r in results if r.get("status") == "ok")
    skipped = sum(1 for r in results if r.get("status") == "skipped")
    errors = sum(1 for r in results if r.get("status") == "error")

    print(f"\n{'='*60}")
    print(f"COMPLETE: {ok} transcribed | {skipped} skipped | {errors} errors")
    print(f"Transcripts saved to: {OUTPUT_DIR}")

    index_path = OUTPUT_DIR / "_INDEX.json"
    index_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Index written: {index_path}")


if __name__ == "__main__":
    run()

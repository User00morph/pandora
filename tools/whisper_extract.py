#!/usr/bin/env python3
"""
Pandora OS — Whisper Video Extraction Tool
Batch transcribes MP4/MOV files from a source directory.
Saves transcripts as .txt files for D.R.D intake.

Usage: python3 whisper_extract.py
"""

import os
import sys
import time
import json
from pathlib import Path

# --- CONFIG ---
VIDEO_DIRS = [
    Path("/Users/emoefedorgu/Downloads/pandora vids"),
    Path("/Users/emoefedorgu/Desktop/Pandora"),
]
OUTPUT_DIR = Path("/Users/emoefedorgu/Desktop/Pandora/research-deconstruction /pandora-vids-raw")
MODEL_SIZE = "tiny"   # tiny / base / small / medium / large
DEVICE = "cpu"
EXTENSIONS = {".mp4", ".mov", ".MP4", ".MOV"}
# --- END CONFIG ---


def setup_ffmpeg():
    """Register static-ffmpeg binary so faster-whisper can find it."""
    try:
        import static_ffmpeg
        static_ffmpeg.add_paths()
        print("[ffmpeg] static-ffmpeg paths registered")
    except Exception as e:
        print(f"[ffmpeg] WARNING: {e} — will try system ffmpeg")


def load_model():
    from faster_whisper import WhisperModel
    print(f"[model] Loading faster-whisper '{MODEL_SIZE}' on {DEVICE} ...")
    print("[model] First run downloads the model (~145MB for base) — one-time only.")
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="int8")
    print("[model] Ready.")
    return model


def transcribe_file(model, video_path: Path, output_dir: Path) -> dict:
    """Transcribe a single video file. Returns metadata dict."""
    safe_stem = video_path.stem.replace(" ", "_").replace("/", "-")
    txt_path = output_dir / f"{safe_stem}.txt"
    meta_path = output_dir / f"{safe_stem}.meta.json"

    if txt_path.exists():
        print(f"  [skip] {video_path.name} — transcript exists")
        return {"file": video_path.name, "status": "skipped"}

    start = time.time()
    print(f"  [transcribing] {video_path.name}")

    try:
        segments, info = model.transcribe(
            str(video_path),
            beam_size=5,
            language=None,         # auto-detect
            vad_filter=True,       # skip silence
            vad_parameters=dict(min_silence_duration_ms=500),
        )

        # Collect segments
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

        # Write transcript
        txt_path.write_text(
            f"FILE: {video_path.name}\n"
            f"LANGUAGE: {info.language} (confidence: {round(info.language_probability, 2)})\n"
            f"DURATION: {round(info.duration, 1)}s\n"
            f"TRANSCRIBED: {elapsed}s processing\n"
            f"{'='*60}\n\n"
            f"{full_text}\n",
            encoding="utf-8"
        )

        # Write metadata
        meta = {
            "file": video_path.name,
            "language": info.language,
            "language_confidence": round(info.language_probability, 3),
            "duration_seconds": round(info.duration, 1),
            "processing_seconds": elapsed,
            "word_count": len(full_text.split()),
            "segments": segment_list,
            "status": "ok",
        }
        meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

        print(f"    -> {info.language} | {round(info.duration, 0)}s | {len(full_text.split())} words | done in {elapsed}s")
        return meta

    except Exception as e:
        print(f"    -> ERROR: {e}")
        txt_path.write_text(f"FILE: {video_path.name}\nERROR: {e}\n", encoding="utf-8")
        return {"file": video_path.name, "status": "error", "error": str(e)}


def run():
    setup_ffmpeg()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    videos = []
    for vdir in VIDEO_DIRS:
        found = sorted([f for f in vdir.iterdir() if f.suffix in EXTENSIONS])
        videos.extend(found)
        print(f"[scan] {vdir.name}: {len(found)} video files")

    if not videos:
        print("No video files found in any source directory")
        sys.exit(1)

    print(f"\n[scan] Total: {len(videos)} videos across {len(VIDEO_DIRS)} directories")
    print(f"[output] Transcripts → {OUTPUT_DIR}\n")

    model = load_model()

    results = []
    for i, vpath in enumerate(videos, 1):
        print(f"\n[{i}/{len(videos)}]", end=" ")
        result = transcribe_file(model, vpath, OUTPUT_DIR)
        results.append(result)

    # Summary
    ok = sum(1 for r in results if r.get("status") == "ok")
    skipped = sum(1 for r in results if r.get("status") == "skipped")
    errors = sum(1 for r in results if r.get("status") == "error")

    print(f"\n{'='*60}")
    print(f"COMPLETE: {ok} transcribed | {skipped} skipped | {errors} errors")
    print(f"Transcripts saved to: {OUTPUT_DIR}")

    # Write index
    index_path = OUTPUT_DIR / "_INDEX.json"
    index_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Index written: {index_path}")


if __name__ == "__main__":
    run()

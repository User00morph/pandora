#!/usr/bin/env python3
"""
One-shot runner: transcribe 6 MP4s from 🦦🦦 iCloud folder.
Output → research-deconstruction /otter-stack/
"""

import os, sys, time, json
from pathlib import Path

SOURCE_DIR = Path("/Users/emoefedorgu/Library/Mobile Documents/com~apple~CloudDocs/🦦🦦")
OUTPUT_DIR = Path("/Users/emoefedorgu/Desktop/Pandora/research-deconstruction /otter-stack")
MODEL_SIZE = "small"
DEVICE = "cpu"
EXTENSIONS = {".mp4", ".mov", ".MP4", ".MOV"}


def setup_ffmpeg():
    try:
        import static_ffmpeg
        static_ffmpeg.add_paths()
        print("[ffmpeg] ready")
    except Exception as e:
        print(f"[ffmpeg] WARNING: {e}")


def run():
    setup_ffmpeg()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    videos = sorted([f for f in SOURCE_DIR.iterdir() if f.suffix in EXTENSIONS])
    if not videos:
        print("No videos found.")
        sys.exit(1)

    print(f"[scan] {len(videos)} videos found in 🦦🦦")
    print(f"[output] → {OUTPUT_DIR}\n")

    from faster_whisper import WhisperModel
    print(f"[model] Loading faster-whisper '{MODEL_SIZE}' ...")
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="int8")
    print("[model] Ready.\n")

    results = []
    for i, vpath in enumerate(videos, 1):
        safe_stem = vpath.stem.replace(" ", "_").replace("/", "-")
        txt_path = OUTPUT_DIR / f"{safe_stem}.txt"
        meta_path = OUTPUT_DIR / f"{safe_stem}.meta.json"

        if txt_path.exists():
            print(f"[{i}/{len(videos)}] SKIP {vpath.name} — exists")
            results.append({"file": vpath.name, "status": "skipped"})
            continue

        print(f"[{i}/{len(videos)}] {vpath.name}")
        start = time.time()

        try:
            segments, info = model.transcribe(
                str(vpath), beam_size=5, language=None,
                vad_filter=True, vad_parameters=dict(min_silence_duration_ms=500),
            )
            parts, seg_list = [], []
            for seg in segments:
                parts.append(seg.text.strip())
                seg_list.append({"start": round(seg.start,2), "end": round(seg.end,2), "text": seg.text.strip()})

            full_text = " ".join(parts)
            elapsed = round(time.time() - start, 1)

            txt_path.write_text(
                f"FILE: {vpath.name}\nLANGUAGE: {info.language} ({round(info.language_probability,2)})\n"
                f"DURATION: {round(info.duration,1)}s\nPROCESSED: {elapsed}s\n{'='*60}\n\n{full_text}\n",
                encoding="utf-8"
            )
            meta_path.write_text(json.dumps({
                "file": vpath.name, "language": info.language,
                "language_confidence": round(info.language_probability,3),
                "duration_seconds": round(info.duration,1),
                "processing_seconds": elapsed,
                "word_count": len(full_text.split()),
                "segments": seg_list, "status": "ok"
            }, indent=2), encoding="utf-8")

            print(f"    {info.language} | {round(info.duration,0)}s | {len(full_text.split())} words | {elapsed}s\n")
            results.append({"file": vpath.name, "status": "ok", "words": len(full_text.split()), "duration": round(info.duration,1)})

        except Exception as e:
            print(f"    ERROR: {e}\n")
            txt_path.write_text(f"FILE: {vpath.name}\nERROR: {e}\n", encoding="utf-8")
            results.append({"file": vpath.name, "status": "error", "error": str(e)})

    ok = sum(1 for r in results if r["status"] == "ok")
    skipped = sum(1 for r in results if r["status"] == "skipped")
    errors = sum(1 for r in results if r["status"] == "error")

    print(f"{'='*60}")
    print(f"DONE: {ok} transcribed | {skipped} skipped | {errors} errors")
    (OUTPUT_DIR / "_INDEX.json").write_text(json.dumps(results, indent=2), encoding="utf-8")


if __name__ == "__main__":
    run()

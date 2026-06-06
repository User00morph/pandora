#!/usr/bin/env python3
"""
Pandora OS — Travis Woo Playlist Extraction Tool
Downloads audio-only from YouTube → transcribes with Whisper → deletes audio.
Saves transcripts to research-deconstruction /travis-woo-raw/

Usage: python3 traviswoo_extract.py
"""

import os
import sys
import time
import json
import subprocess
import tempfile
from pathlib import Path

OUTPUT_DIR = Path("/Users/emoefedorgu/Desktop/Pandora/research-deconstruction /travis-woo-raw")
MODEL_SIZE = "tiny"
DEVICE = "cpu"
SLEEP_BETWEEN = 2

VIDEOS = [
    ("X5QcNyYRMqQ", "How to handle Regime Changes (by ex HFT quant trader)", 2228),
    ("GE4JISxYuXY", "Options Flow: The Edge You've Been Looking For", 803),
    ("XfUAMnLPUUk", "GEX Daily Model: The Only Trading Strategy You Will Ever Need!", 797),
    ("ZVMTeDBmSrI", "I Re-Created A Quant Trading Strategy With Claude Code", 1635),
    ("4vZZReXFKkQ", "Claude Code Just Got a Trading Agent Dashboard", 225),
    ("hXENLAwmc7k", "AI Just Killed the $300 Volume Profile Market", 1458),
    ("T6jdfZ317Vw", "How To Create A Personal Zero Human Trading Firm", 3079),
    ("SSygS-Oubi8", "WEEKLY ASTROLOGY FORECAST - Major Shifts Happening Worldwide", 1389),
    ("-l9qSLAG3dM", "The Wheel Options Strategy I Will Use For Life", 2655),
    ("q2q26X3Dwzc", "BUY Signals on the Market - Going in HEAVY", 265),
    ("Z10zBXL4Lkw", "How I'm Trading the Stock Market Crash", 687),
    ("17JD1mClsuY", "How I Made $40k Trading the Japanese Stock Market This Year in 5 Minutes", 483),
    ("9ODMAYCirq0", "Giving You a Full Trading Education for Free", 6975),
    ("op6Nqg3ZvDU", "My Instagram Got Banned for Revealing this Broker Statement", 592),
    ("0ptg3gu-RhI", "Up $473k on my TRX Trade - Deep Dive into Fundamentals and Chart Analytics", 1118),
    ("y9nhEo_U-H0", "New MTP Backtesting Tool is Cooking", 811),
    ("-B3veSrnjGA", "MTP Backtesting Software Tutorial", 1256),
    ("lpqt1iQ6Txc", "Crypto Edge Pro System Updates and Results - Crypto Bots are COOKING", 687),
    ("PgwctmzVUCI", "This Claude Code Trick Saves You $1000s on TradingView", 1416),
]


def setup_ffmpeg():
    try:
        import static_ffmpeg
        static_ffmpeg.add_paths()
        print("[ffmpeg] static-ffmpeg registered")
    except Exception as e:
        print(f"[ffmpeg] WARNING: {e}")


def load_model():
    from faster_whisper import WhisperModel
    print(f"[model] Loading faster-whisper '{MODEL_SIZE}' ...")
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type="int8")
    print("[model] Ready.")
    return model


def download_audio(video_id: str, out_dir: Path) -> Path | None:
    url = f"https://www.youtube.com/watch?v={video_id}"
    out_template = str(out_dir / f"{video_id}.%(ext)s")

    cmd = [
        "python3", "-m", "yt_dlp",
        "--format", "bestaudio[ext=m4a]/bestaudio",
        "--output", out_template,
        "--no-playlist",
        "--quiet",
        "--no-warnings",
        url,
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        for ext in ["m4a", "webm", "opus", "mp3"]:
            candidate = out_dir / f"{video_id}.{ext}"
            if candidate.exists():
                return candidate
        for f in out_dir.iterdir():
            if f.stem == video_id:
                return f
        print(f"    [download] No audio file found. stderr: {result.stderr[:200]}")
        return None
    except subprocess.TimeoutExpired:
        print(f"    [download] TIMEOUT")
        return None
    except Exception as e:
        print(f"    [download] ERROR: {e}")
        return None


def transcribe_audio(model, audio_path: Path, video_id: str, title: str, output_dir: Path) -> dict:
    txt_path = output_dir / f"{video_id}.txt"
    meta_path = output_dir / f"{video_id}.meta.json"

    start = time.time()
    try:
        segments, info = model.transcribe(
            str(audio_path),
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
            f"VIDEO_ID: {video_id}\n"
            f"TITLE: {title}\n"
            f"LANGUAGE: {info.language} (confidence: {round(info.language_probability, 2)})\n"
            f"DURATION: {round(info.duration, 1)}s\n"
            f"TRANSCRIBED: {elapsed}s processing\n"
            f"{'='*60}\n\n"
            f"{full_text}\n",
            encoding="utf-8"
        )

        meta = {
            "video_id": video_id,
            "title": title,
            "language": info.language,
            "language_confidence": round(info.language_probability, 3),
            "duration_seconds": round(info.duration, 1),
            "processing_seconds": elapsed,
            "word_count": len(full_text.split()),
            "status": "ok",
            "segments": segment_list,
        }
        meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
        return meta

    except Exception as e:
        txt_path.write_text(f"VIDEO_ID: {video_id}\nTITLE: {title}\nERROR: {e}\n", encoding="utf-8")
        return {"video_id": video_id, "title": title, "status": "error", "error": str(e)}


def run():
    setup_ffmpeg()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    todo = [(vid, title, dur) for vid, title, dur in VIDEOS
            if not (OUTPUT_DIR / f"{vid}.txt").exists()]

    total_dur = sum(d for _, _, d in todo)
    print(f"\n[plan] {len(todo)} videos to extract ({round(total_dur/3600, 1)}h total audio)")
    print(f"[plan] Estimated Whisper time: ~{round(total_dur/3600*0.7, 1)}h on CPU")
    print(f"[output] → {OUTPUT_DIR}\n")

    model = load_model()
    results = []

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        for i, (video_id, title, dur) in enumerate(todo, 1):
            print(f"\n[{i}/{len(todo)}] {title[:65]} ({round(dur/60, 1)}min)")
            print(f"  [download] {video_id} ...")
            audio_path = download_audio(video_id, tmp)

            if audio_path is None:
                results.append({"video_id": video_id, "title": title, "status": "download_failed"})
                continue

            print(f"  [transcribe] ...")
            meta = transcribe_audio(model, audio_path, video_id, title, OUTPUT_DIR)

            if meta.get("status") == "ok":
                print(f"  -> {meta['word_count']} words | {meta['processing_seconds']}s")
            else:
                print(f"  -> ERROR: {meta.get('error', 'unknown')}")

            try:
                audio_path.unlink()
            except Exception:
                pass

            results.append(meta)
            if i < len(todo):
                time.sleep(SLEEP_BETWEEN)

    ok = sum(1 for r in results if r.get("status") == "ok")
    failed = len(results) - ok
    total_words = sum(r.get("word_count", 0) for r in results)

    print(f"\n{'='*60}")
    print(f"COMPLETE: {ok} transcribed | {failed} failed | ~{total_words:,} words")
    print(f"Transcripts → {OUTPUT_DIR}")

    index_path = OUTPUT_DIR / "_INDEX.json"
    index_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Index written: {index_path}")


if __name__ == "__main__":
    run()

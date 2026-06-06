#!/usr/bin/env python3
"""Transcribe MP4s in a folder using Whisper small model."""

import os
import subprocess
import sys
import tempfile
import whisper

FFMPEG_BIN = "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-x86_64-v7.1"
# Whisper calls `ffmpeg` by name — create a symlink in /tmp so it's on PATH
_ffmpeg_link = "/tmp/ffmpeg"
if not os.path.exists(_ffmpeg_link):
    os.symlink(FFMPEG_BIN, _ffmpeg_link)
os.environ["PATH"] = "/tmp:" + os.environ.get("PATH", "")
INPUT_DIR = "/Users/emoefedorgu/Downloads/private sector and bihness"
OUTPUT_DIR = "/Users/emoefedorgu/Desktop/Pandora/research-deconstruction /private-sector-bihness"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading Whisper small model...")
model = whisper.load_model("small")
print("Model loaded.\n")

mp4_files = sorted([f for f in os.listdir(INPUT_DIR) if f.upper().endswith(".MP4")])
total = len(mp4_files)

for i, fname in enumerate(mp4_files, 1):
    mp4_path = os.path.join(INPUT_DIR, fname)
    base = os.path.splitext(fname)[0]
    out_path = os.path.join(OUTPUT_DIR, f"{base}.txt")

    if os.path.exists(out_path):
        print(f"[{i}/{total}] SKIP (already transcribed): {fname}")
        continue

    print(f"[{i}/{total}] Extracting audio: {fname}")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp_audio = tmp.name

    subprocess.run(
        [FFMPEG, "-y", "-i", mp4_path, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", tmp_audio],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    print(f"[{i}/{total}] Transcribing: {fname}")
    result = model.transcribe(tmp_audio, language="en", fp16=False)
    os.unlink(tmp_audio)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    word_count = len(result["text"].split())
    print(f"[{i}/{total}] Done — {word_count:,} words → {out_path}\n")

print("All transcriptions complete.")

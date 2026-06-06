#!/usr/bin/env python3
"""Transcribe trading MP4s from iCloud using Whisper small model."""

import os
import subprocess
import sys
import tempfile
import whisper

FFMPEG_BIN = "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-x86_64-v7.1"
_ffmpeg_link = "/tmp/ffmpeg"
if not os.path.exists(_ffmpeg_link):
    os.symlink(FFMPEG_BIN, _ffmpeg_link)
os.environ["PATH"] = "/tmp:" + os.environ.get("PATH", "")

INPUT_DIR  = "/Users/emoefedorgu/Library/Mobile Documents/com~apple~CloudDocs/trading "
OUTPUT_DIR = "/Users/emoefedorgu/Desktop/Pandora/D.R.D/research/trading-systems/icloud-trading-raw"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading Whisper small model...")
model = whisper.load_model("base")
print("Model loaded.\n")

mp4_files = sorted([f for f in os.listdir(INPUT_DIR) if f.upper().endswith(".MP4")])
total = len(mp4_files)
print(f"Found {total} MP4 files.\n")

for i, fname in enumerate(mp4_files, 1):
    mp4_path = os.path.join(INPUT_DIR, fname)
    base = os.path.splitext(fname)[0]
    out_path = os.path.join(OUTPUT_DIR, f"{base}.txt")

    if os.path.exists(out_path):
        print(f"[{i}/{total}] SKIP (exists): {fname}")
        continue

    print(f"[{i}/{total}] Extracting audio: {fname}")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp_audio = tmp.name

    subprocess.run(
        ["/tmp/ffmpeg", "-y", "-i", mp4_path, "-ar", "16000", "-ac", "1",
         "-c:a", "pcm_s16le", tmp_audio],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    print(f"[{i}/{total}] Transcribing: {fname}")
    result = model.transcribe(tmp_audio, language="en", fp16=False)
    os.unlink(tmp_audio)

    with open(out_path, "w") as f:
        f.write(result["text"].strip())

    print(f"[{i}/{total}] Done: {base}.txt\n")

print("All transcriptions complete.")
print(f"Output: {OUTPUT_DIR}")

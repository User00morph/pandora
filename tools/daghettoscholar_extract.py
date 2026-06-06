#!/usr/bin/env python3
"""
Pandora OS — DaGhettoScholar YouTube Extraction Tool
Downloads audio-only from YouTube → transcribes with Whisper → deletes audio.
Saves transcripts to research-deconstruction /daghettoscholar-raw/

Usage: python3 daghettoscholar_extract.py
"""

import os
import sys
import time
import json
import subprocess
import tempfile
from pathlib import Path

# --- CONFIG ---
OUTPUT_DIR = Path("/Users/emoefedorgu/Desktop/Pandora/research-deconstruction /daghettoscholar-raw")
MODEL_SIZE = "tiny"
DEVICE = "cpu"
SLEEP_BETWEEN = 2  # seconds between downloads to avoid rate limit

# Already extracted in Rashad Jamal playlist — skip these
ALREADY_EXTRACTED = {
    "m3wtYLW6VH4",  # America is NOT named After Amerigos Vespucci
    "oKP-zcASboc",  # Black American indigenous Culture
    "B59mCHbtwmI",  # Cairo & Babylon were the SAME CITY
    "FiPmnKrgZAU",  # The Real New Year
    "7id9I1C8tbc",  # Pseudo Killa
    "a34AjumeUcQ",  # We R Indigenous Documentary Series Part 1
    "ZXUtRrACNJ8",  # We are Indigenous Documentary Series Part 2
    "KPcQDPXwouk",  # Global Genealogy
}

# Full channel video list — ID | Title | Duration(s)
VIDEOS = [
    ("W6NMwze2jtQ", "The Rh Factor Myth Debunked", 7987),
    ("KPHJQZZM29E", "DNA Testing Bias #CopperColored", 390),
    ("GyrYVppfbBI", "How to FIX your Aging Face #fasciaHealth", 312),
    ("oRotZaCQi30", "Fruit Only Diets Cause Atrophy", 599),
    ("Ih5tLJEHi4k", "Coconut Milk from Scratch Coconut Everything", 38),
    ("CYflIi6NB3M", "Who is the Agent Dr Sebi Lied Part 2", 504),
    ("B_Y_wEVA1Qs", "The # 1 Exercise for Total Body Health", 792),
    ("9uk84LceRjQ", "Dr Sebi Lied", 372),
    ("PwCPTkhvi4g", "Why you MUST Sleep on your Left Side for Optimal Health", 408),
    ("txGEcjp8z7Q", "Fascia Kinetic Therapy Certification", 321),
    ("fKLmxyP5Rm0", "The Science of Calming Your Nervous System via 1 Exercise", 594),
    ("pJvzv42LXkQ", "Aboriginal University Courses", 9),
    ("sc6I6QZbGrQ", "Who R the Oldest & Original Americans - The DNA Speaks", 601),
    ("nRai8jhZ5yo", "ARNA Official Orientation Class OVERVIEW", 3118),
    ("WtEH7HL3_Ts", "Part 2 Who was in the Caves - The Bible is an Academic Walmart", 601),
    ("ECNNMtqgGGg", "How to Actually Get Reparations for REAL", 601),
    ("82weMjZ1RIc", "Who Was in the Caves Part 1", 601),
    ("Nb2NiRhIU5A", "How Excessive Sitting Causes Major Health issues with the Spine and pelvic muscles", 474),
    ("S3lqa981dBQ", "Flow Breathing Technique for Total Body Health", 188),
    ("ejywpgpJNvY", "A Pressure Point that can bring Total Body Healing", 579),
    ("O-trhZV05SE", "The Science of Weight Loss is via the Breath - Fat Burning = Breathing to Eating Ratio", 489),
    ("YCsXnx_mxjM", "Part 2 Haiti was not the 1st Liberated Jurisdiction of Black People post Colonization", 570),
    ("yHWRz3A6RmA", "Addressing the Pseudo Claims of a Haiti Empire in the American South", 369),
    ("Xtsr-eVxTM4", "Brigido Lara & 40k Fake Indigenous Artifacts", 280),
    ("7R0sQzm9CfI", "Deep in Da Bag Series - What do cells actually use for Energy", 598),
    ("ItXlQG_rroI", "Bible Crack on sale to Indigenous Americans", 549),
    ("7aNJfrrMWi4", "Indigenous Americans Ain't Muurs", 299),
    ("IDEOlO5miRU", "Who Really Built Tartarian Buildings in America", 589),
    ("zT881jomVPE", "They Lied About The Royal African Company & The Slave Trade", 321),
    ("oSc0Qwc8pWk", "The Lost Pages of Religion (Islam Christianity & Judaism)", 570),
    ("CR7j7IPQ1kQ", "How to Get Super Strong & Super Healthy via Training your Fascia", 274),
    ("4FC8QCUkk50", "Indigenous Medicine @ Ancient Indigenous Sites", 311),
    ("MnFTV9g35Ls", "Prostate Disease & Heaux Culture", 601),
    ("wsv2z-iF7iA", "Deep in da Bag Series - How Powerful is the Human Body Actually", 191),
    ("WOcBihURVwo", "Deep in da Bag Series Science - Trees are from Heaven not Earth - Tree Hugging Technique", 282),
    ("drloND__8xk", "Fascia Fitness - Your Walk Tells your Health", 341),
    ("XHueWytT4ZA", "Follow my New Instagram Page @godbodyhealth", 301),
    ("NwaIhcs2XV0", "Economic Mastery Class Credit Business Credit Exemptions", 261),
    ("KiRkAHAKNvM", "The Genetic Science of Lactose Intolerance in Indigenous Peoples Animal Milk Toxicity", 3134),
    ("umGgBJZRwhI", "ShuShu Carrington KO", 23),
    ("TfLIbgCuiqE", "The Bible is stolen Heritage - American Indians are not Israelites", 597),
    ("0Y_h5ETuPoM", "Indigenous Americans were NOT Hebrews or Lost Tribes of Israel", 601),
    ("cTkXqWJmUo8", "Ancient America is not Egypt (TaMeri)", 302),
    ("UC4WRCXjtlU", "Black Americans Built all American Cities - Aboriginal American Renaissance", 601),
    ("KUvLkQQfS20", "Addressing Scientific Racism", 507),
    ("Q-QPUffyvfk", "WHY are they Hated", 331),
    ("MrnfDZVSnnk", "The 1 Health Tool - Breathing", 391),
    ("FtocUqHVq9Q", "Who is Really a Culture Vulture Original Americans vs Eurasian Implants", 657),
    ("IKFjOpiYPyg", "Heavy Metal Detox Guide w/Formulas", 91),
    ("3ZvZ4VczRJw", "Crawford is the GOAT - He Stepped on Canelo", 345),
    ("gfiOoHJ3LuA", "Purpose is Everything - Methodology to Developing Purpose", 1085),
    ("X7ACCx5bBjE", "AMA Doctors Class 4 Mutation Sciences & BioCosmology", 5520),
    ("9Hy893hK8GI", "Health Debunking Series We need Protein & Why Dr Ali vs Yahki & Sebi", 10335),
    ("cdR-IqqZifo", "AMA Health Class Level1 Physics & Chemistry Laws of Biology Real Body Building Concepts", 6380),
    ("t2FOCcOamlY", "Indigenous Psychology Class 3 Cartomancy & AstroStudies", 4354),
    ("iiAu0lX1MCI", "Juneteenth is Disrespect to US - Here is the History U Need", 518),
    ("ioammi2FDfs", "Yamasee Guale Ogeechee vs The Fiction of Gullah Geechee", 586),
    ("g99fzZ8SIFo", "The Worldwide White Slave Trade", 598),
    ("2WT_JfdbkWs", "Gullah Geechee is NOT African - We are Indigenous American", 320),
    ("-fCh_gOji08", "508c1a Business vs 501c3", 305),
    ("DAcbZqz91HE", "South America was Africa - Indigenous Scholarship", 489),
    ("nifiaE_YLgU", "Trump from an Indigenous Perspective - Civics Tariffs Prophecy", 1161),
    ("MSzianp7SKs", "Indigenous Governance vs DEI & Civil Rights", 1055),
    ("e5b0D04vtwE", "Grow Your Hair Back #HairGrowthScience", 311),
    ("LNT0pfNnRDk", "How to Fix Family", 289),
    ("Fcb_RDXdr9Q", "The Tank Davis Jake Paul Curse", 360),
    ("t1c_os3FqL4", "Pre Sparring Workout GodBodyOG", 267),
    ("IDniBbWtOF0", "White Lion Lies - Proper History of Point Comfort Virginia", 259),
    ("Zil8jeeH9Lo", "Documentary - Indigenous Insurrection - The Black Rebellion - Untold Causes of the Civil War", 534),
    ("51SrTAdrkSU", "Food Science vs Food Fads - Why we should eat High Carbon Meats", 186),
    ("1jB5aznW_h4", "The Real Dr Sebi - A Documentary on the World renowned Alfredo Bowman", 6768),
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
    """Download audio-only for a YouTube video. Returns path to audio file."""
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
        # Find the downloaded file
        for ext in ["m4a", "webm", "opus", "mp3"]:
            candidate = out_dir / f"{video_id}.{ext}"
            if candidate.exists():
                return candidate
        # Fallback: search for any file with the video_id stem
        for f in out_dir.iterdir():
            if f.stem == video_id:
                return f
        print(f"    [download] No audio file found for {video_id}")
        print(f"    stderr: {result.stderr[:200]}")
        return None
    except subprocess.TimeoutExpired:
        print(f"    [download] TIMEOUT for {video_id}")
        return None
    except Exception as e:
        print(f"    [download] ERROR: {e}")
        return None


def transcribe_audio(model, audio_path: Path, video_id: str, title: str, output_dir: Path) -> dict:
    """Transcribe audio file. Returns metadata dict."""
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

    # Filter out already-extracted videos
    todo = [(vid, title, dur) for vid, title, dur in VIDEOS if vid not in ALREADY_EXTRACTED]
    # Skip already-transcribed
    todo = [(vid, title, dur) for vid, title, dur in todo
            if not (OUTPUT_DIR / f"{vid}.txt").exists()]

    total_dur = sum(d for _, _, d in todo)
    print(f"\n[plan] {len(todo)} videos to extract ({round(total_dur/3600, 1)}h total audio)")
    print(f"[plan] Estimated Whisper time ({MODEL_SIZE}): ~{round(total_dur/3600 * 0.7, 1)}h on CPU")
    print(f"[output] → {OUTPUT_DIR}\n")

    model = load_model()

    results = []
    with tempfile.TemporaryDirectory(dir="/tmp") as tmpdir:
        tmp = Path(tmpdir)

        for i, (video_id, title, dur) in enumerate(todo, 1):
            print(f"\n[{i}/{len(todo)}] {title[:60]} ({round(dur/60, 1)}min)")

            # Download audio
            print(f"  [download] {video_id} ...")
            audio_path = download_audio(video_id, tmp)

            if audio_path is None:
                print(f"  [skip] download failed")
                results.append({"video_id": video_id, "title": title, "status": "download_failed"})
                continue

            print(f"  [transcribe] {audio_path.name} ...")
            meta = transcribe_audio(model, audio_path, video_id, title, OUTPUT_DIR)

            if meta.get("status") == "ok":
                print(f"  -> {meta['word_count']} words | {meta['processing_seconds']}s")
            else:
                print(f"  -> ERROR: {meta.get('error', 'unknown')}")

            # Delete audio immediately to free space
            try:
                audio_path.unlink()
            except Exception:
                pass

            results.append(meta)

            if i < len(todo):
                time.sleep(SLEEP_BETWEEN)

    # Summary
    ok = sum(1 for r in results if r.get("status") == "ok")
    failed = len(results) - ok
    total_words = sum(r.get("word_count", 0) for r in results)

    print(f"\n{'='*60}")
    print(f"COMPLETE: {ok} transcribed | {failed} failed | ~{total_words:,} words")
    print(f"Transcripts → {OUTPUT_DIR}")

    index_path = OUTPUT_DIR / "_INDEX.json"
    # Merge with existing index if it exists
    existing = []
    if index_path.exists():
        try:
            existing = json.loads(index_path.read_text())
        except Exception:
            pass
    index_path.write_text(json.dumps(existing + results, indent=2), encoding="utf-8")
    print(f"Index updated: {index_path}")


if __name__ == "__main__":
    run()

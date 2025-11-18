# models/orpheus_client.py

import os
import time
from pathlib import Path
from agent_tts.orpheus.inference import generate_speech_from_api, DEFAULT_VOICE

OUTPUT_DIR = os.getenv("ORPHEUS_OUTPUT_DIR", "orpheus_out")


def ensure_dir() -> Path:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    return out


def tts_to_wav(text: str, voice: str | None = None, filename_prefix="orpheus"):
    out_dir = ensure_dir()
    ts = int(time.time() * 1000)
    fname = f"{filename_prefix}_{ts}.wav"
    output_path = out_dir / fname

    generate_speech_from_api(
        prompt=text,
        voice=voice or DEFAULT_VOICE,
        output_file=str(output_path),
    )

    print(f"[Orpheus] Saved WAV → {output_path}")
    return str(output_path)

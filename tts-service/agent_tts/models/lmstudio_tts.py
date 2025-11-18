# models/lmstudio_tts.py

from agent_tts.models.orpheus_client import tts_to_wav as orpheus_tts


def tts_to_wav(text: str) -> str:
    """
    GPU TTS via LM Studio using Orpheus under the hood.
    """
    return orpheus_tts(text, filename_prefix="lm_orpheus")

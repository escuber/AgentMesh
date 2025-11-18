# queues.py
from queue import Queue

# Queue for TTS tasks (chunks)
tts_queue = Queue()

# Queue for playback-ordered WAVs
playback_queue = Queue()

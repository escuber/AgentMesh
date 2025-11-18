# workers/tts_worker.py

import threading
from agent_tts.queues import tts_queue, playback_queue
from agent_tts.models.lmstudio_tts import tts_to_wav as gpu_tts
from agent_tts.models.orpheus_client import tts_to_wav as cpu_tts


class TTSWorker(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)

    def run(self):
        print("[TTSWorker] Ready")

        while True:
            item = tts_queue.get()
            engine = item["engine"]
            seq    = item["seq"]
            text   = item["text"]

            try:
                if engine == "lmstudio":
                    wav = gpu_tts(text)
                else:
                    wav = cpu_tts(text)

                playback_queue.put({"seq": seq, "wav_path": wav})

            except Exception as e:
                print("[TTSWorker] ERROR:", e)

            tts_queue.task_done()

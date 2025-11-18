# workers/playback_worker.py

import threading
import simpleaudio as sa
import traceback
import time
from agent_tts.queues import playback_queue


class PlaybackWorker(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.expected_seq = 0
        self.buffer = {}

    def play(self, path: str):
        wave = sa.WaveObject.from_wave_file(path)
        obj = wave.play()
        obj.wait_done()

    def run(self):
        print("[PlaybackWorker] Ready")

        while True:
            try:
                item = playback_queue.get()
                seq = item["seq"]
                wav = item["wav_path"]

                self.buffer[seq] = wav

                while self.expected_seq in self.buffer:
                    try:
                        print(f"[PlaybackWorker] seq={self.expected_seq}")
                        self.play(self.buffer.pop(self.expected_seq))
                    except Exception as e:
                        print("[PlaybackWorker] Playback error:", e)
                        traceback.print_exc()

                    self.expected_seq += 1

                playback_queue.task_done()

            except Exception as e:
                print("[PlaybackWorker] Worker recovered:", e)
                traceback.print_exc()
                time.sleep(0.1)

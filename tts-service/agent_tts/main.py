# main.py

import json
from agent_tts.models.qwen_client import chat
from agent_tts.tools import tools, execute_tool
from agent_tts.workers.tts_worker import TTSWorker
from agent_tts.workers.playback import PlaybackWorker


def start_workers():
    for _ in range(3):
        TTSWorker().start()
    PlaybackWorker().start()


SYSTEM_PROMPT = """
You are a tool-calling assistant.
Never output plain text.
Never generate JSON.
Only produce tool calls.

Workflow:
• First call split_text(text).
• Then call enqueue_lmstudio_tts(seq, text) for each chunk.
• If user asks for CPU/local, call enqueue_local_tts.
"""


def agent_step(user_text):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": user_text},
    ]

    print("\n" + "=" * 70)
    print(" AGENT STEP")
    print("=" * 70)

    # STEP 1 → split_text
    response = chat(messages, tools=tools)
    choice = response.choices[0].message

    if not choice.tool_calls:
        print("[ERROR] No tool call (split_text)")
        return

    tc = choice.tool_calls[0]
    args = json.loads(tc.function.arguments)
    result_msg = execute_tool(tc.function.name, args)
    messages.append(result_msg)

    # STEP 2 → enqueue TTS chunks
    follow = chat(messages, tools=tools)
    fc = follow.choices[0].message

    if not fc.tool_calls:
        print("[ERROR] No TTS tool calls")
        return

    for call in fc.tool_calls:
        args = json.loads(call.function.arguments)
        execute_tool(call.function.name, args)


def main():
    start_workers()
    print("\nWorkers ready.\n")

    text = "Hello world.\n\nThis is test two.\n\nThird line."

    while True:
        agent_step(text)
        text = input("> ").strip()
        if not text:
            continue


if __name__ == "__main__":
    main()

# tools.py

import json
from agent_tts.queues import tts_queue


tools = [
    {
        "type": "function",
        "function": {
            "name": "split_text",
            "description": "Split text into ordered chunks.",
            "parameters": {
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "enqueue_lmstudio_tts",
            "description": "Queue a text chunk for LM Studio TTS.",
            "parameters": {
                "type": "object",
                "properties": {
                    "seq": {"type": "integer"},
                    "text": {"type": "string"}
                },
                "required": ["seq", "text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "enqueue_local_tts",
            "description": "Queue a text chunk for CPU/Local TTS.",
            "parameters": {
                "type": "object",
                "properties": {
                    "seq": {"type": "integer"},
                    "text": {"type": "string"}
                },
                "required": ["seq", "text"],
            },
        },
    },
]


def split_text(text: str):
    parts = [p.strip() for p in text.split("\n") if p.strip()]
    chunks = [{"seq": i, "text": chunk} for i, chunk in enumerate(parts)]
    return {"role": "tool", "content": json.dumps({"chunks": chunks})}


def enqueue_lmstudio_tts(seq: int, text: str):
    tts_queue.put({"engine": "lmstudio", "seq": seq, "text": text})
    return {"role": "tool", "content": json.dumps({"seq": seq, "engine": "lmstudio"})}


def enqueue_local_tts(seq: int, text: str):
    tts_queue.put({"engine": "local", "seq": seq, "text": text})
    return {"role": "tool", "content": json.dumps({"seq": seq, "engine": "local"})}


def execute_tool(name: str, args: dict, tool_call_id=None):
    if name == "split_text":
        return split_text(args["text"])

    if name == "enqueue_lmstudio_tts":
        return enqueue_lmstudio_tts(args["seq"], args["text"])

    if name == "enqueue_local_tts":
        return enqueue_local_tts(args["seq"], args["text"])

    return {"role": "tool", "content": json.dumps({"error": "unknown tool"})}

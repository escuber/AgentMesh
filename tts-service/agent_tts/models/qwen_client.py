# models/qwen_client.py

import copy
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

LMSTUDIO_URL = os.getenv("LMSTUDIO_URL")
LMSTUDIO_MODEL = os.getenv("LMSTUDIO_MODEL")

client = OpenAI(base_url=LMSTUDIO_URL, api_key="not-needed-for-local")


def chat(messages, tools=None, tool_choice="auto"):
    """
    Wrapper around LM Studio chat completions.
    Supports optional tool definitions.
    """
    payload = {
        "model": LMSTUDIO_MODEL,
        "messages": messages,
    }

    if tools:
        payload["tools"] = copy.deepcopy(tools)
        payload["tool_choice"] = tool_choice

    return client.chat.completions.create(**payload)

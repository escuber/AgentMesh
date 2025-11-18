from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

LMSTUDIO_URL = os.getenv("LMSTUDIO_URL")
MODEL_NAME = os.getenv("LMSTUDIO_MODEL")

client = OpenAI(
    base_url=LMSTUDIO_URL,
    api_key="not-needed-for-local"
)
tools = [
    {
        "type": "function",
        "function": {
            "name": "split_text",
            "description": "Splits text into non-empty trimmed sections separated by CRLF.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    }
]



def split_text(text: str):
    # Matches your exact C# behavior
    parts = text.split("\r\n")
    sections = [p.strip() for p in parts if p.strip()]
    return sections

def split_text_tool(args):
    text = args.get("text", "")
    return split_text(text)

def enqueue_tts(args):
    text = args["text"]
    tts_queue.put(text)
    return {"status": "queued"}
def main():
    print("Testing LM Studio connection...\n")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "When asked to split text, call the split_text tool."},
            {"role": "user", "content": "Split this:\r\nLine one\r\n\r\nLine two\r\nLine three"}
        ],
        tools=tools,
        tool_choice="required"
    )
    print(response)
    choice = response.choices[0]

# Check for tool call
    if choice.finish_reason == "tool_calls":
        tool_call = choice.message.tool_calls[0]
        tool_name = tool_call.function.name
        tool_args = tool_call.function.arguments

        import json
        args = json.loads(tool_args)

        if tool_name == "split_text":
            result = split_text(args["text"])
            print("Tool result:", result)
    else:
        print("Model text response:", choice.message.content)
    

    # response = client.chat.completions.create(
    #     model=MODEL_NAME,
    #     messages=[
    #         {"role": "user", "content": "Hello from Python! Can you hear me?"}
    #     ]
    # )

    # print("Model response:")
    
    # print(response.choices[0].message.content)
        

if __name__ == "__main__":
    main()
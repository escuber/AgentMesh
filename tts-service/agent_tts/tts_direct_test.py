from agent_tts.orpheus.inference import generate_speech_from_api

print("Generating speech…")
audio = generate_speech_from_api(
    prompt="Hello Jimmy, this is Orpheus speaking.",
    voice="tara",
    output_file="out.wav"
)

print("Saved to out.wav")

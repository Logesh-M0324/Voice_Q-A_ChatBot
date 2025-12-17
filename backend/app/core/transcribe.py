from faster_whisper import WhisperModel

# Load model once (global)
model = WhisperModel(
    "base",
    device="cpu",        # use "cuda" if GPU available
    compute_type="int8"  # fast + low memory for CPU
)

def transcribe_audio(audio_path: str) -> str:
    segments, info = model.transcribe(audio_path)
    print(segments)
    transcript = ""
    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()
    
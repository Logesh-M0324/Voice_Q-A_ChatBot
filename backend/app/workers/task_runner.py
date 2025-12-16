from app.core.transcribe import transcribe_audio
from app.workers.translate import translate_text
from app.workers.generate_pdf import generate_pdf
from app.core.memory import redis_client

def run_task(task_id: str, audio_path: str):
    redis_client.hset(task_id, "status", "processing")

    text = transcribe_audio(audio_path)
    translated = translate_text(text, "English")

    output_path = f"outputs/{task_id}.pdf"
    generate_pdf(translated, output_path)

    redis_client.hset(task_id, mapping={
        "status": "completed",
        "result_path": output_path
    })

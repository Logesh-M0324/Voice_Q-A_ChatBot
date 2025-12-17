# from app.core.transcribe import transcribe_audio
# from app.workers.translate import translate_text
# from app.workers.generate_pdf import generate_pdf
# from app.core.memory import redis_client

# def run_task(task_id: str, audio_path: str):
#     redis_client.hset(task_id, "status", "processing")

#     text = transcribe_audio(audio_path)
#     translated = translate_text(text, "English")

#     output_path = f"outputs/{task_id}.pdf"
#     generate_pdf(translated, output_path)

#     redis_client.hset(task_id, mapping={
#         "status": "completed",
#         "result_path": output_path
#     })

from app.core.transcribe import transcribe_audio
from app.core.embeddings import add_transcript_to_vector_db
from app.workers.generate_pdf import generate_pdf
from app.core.memory import redis_client
import os

def run_task(task_id: str, audio_path: str, conversation_id: str):
    try:
        # Mark task as running
        redis_client.hset(task_id, "status", "running")

        # 1️⃣ Transcribe audio
        transcript = transcribe_audio(audio_path)

        # 2️⃣ Add transcript to vector DB
        add_transcript_to_vector_db(conversation_id, transcript)

        # 3️⃣ Generate PDF from transcript
        pdf_path = f"outputs/{task_id}.pdf"
        generate_pdf(transcript, pdf_path)

        # 4️⃣ Task completed, store paths in Redis
        redis_client.hset(task_id, mapping={
            "status": "completed",
            "conversation_id": conversation_id,
            "pdf_path": pdf_path,
            "audio_path": audio_path
        })

    except Exception as e:
        # Task failed
        redis_client.hset(task_id, mapping={
            "status": "failed",
            "error": str(e)
        })

    # We **keep audio in uploads/** as requested
    # PDF is saved in outputs/

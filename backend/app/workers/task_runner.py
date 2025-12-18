from app.core.transcribe import transcribe_audio
from app.core.embeddings import add_transcript_to_vector_db
from app.workers.generate_pdf import generate_pdf
from app.core.memory import redis_client
import os

def run_task(task_id: str, audio_path: str, conversation_id: str):
    try:
        # Mark task as running
        redis_client.hset(task_id, mapping={
            "status": "running",
            "progress": 5
        })

        # 1️⃣ Transcribe audio
        redis_client.hset(task_id, mapping={
            "status": "transcribing",
            "progress": 20
        })
        transcript = transcribe_audio(audio_path)

        # 2️⃣ Add transcript to vector DB
        redis_client.hset(task_id, mapping={
            "status": "embedding",
            "progress": 50
        })
        add_transcript_to_vector_db(conversation_id, transcript)

        # 3️⃣ Generate PDF from transcript
        redis_client.hset(task_id, mapping={
            "status": "generating_pdf",
            "progress": 80
        })
        
        pdf_path = f"outputs/{task_id}.pdf"
        generate_pdf(transcript, pdf_path)

        # 4️⃣ Task completed
        redis_client.hset(task_id, mapping={
            "status": "completed",
            "progress": 100,
            "conversation_id": conversation_id,
            "pdf_path": pdf_path,
            "audio_path": audio_path
        })

    except Exception as e:
        redis_client.hset(task_id, mapping={
            "status": "failed",
            "error": str(e)
        })

    # Audio remains in uploads/
    # PDF remains in outputs/

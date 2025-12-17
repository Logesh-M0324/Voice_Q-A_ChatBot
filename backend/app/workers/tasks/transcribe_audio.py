from core.transcribe import transcribe_audio
from core.chunking import chunk_text
from core.embeddings import add_documents
from redis import Redis

redis = Redis(decode_responses=True)

def process_audio_task(task_id: str, api_key: str, filename: str):
    redis.set(task_id, "processing", ex=86400)

    text = transcribe_audio(filename)
    chunks = chunk_text(text)

    add_documents(
        texts=chunks,
        namespace=api_key  # per-user isolation
    )

    redis.set(task_id, "completed", ex=86400)

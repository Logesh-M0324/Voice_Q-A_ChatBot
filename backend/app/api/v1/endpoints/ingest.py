from fastapi import APIRouter
from app.models.schemas import TranscriptUploadRequest
from app.core.embeddings import add_transcript_to_vector_db

router = APIRouter()

# Phase-1 temporary in-memory store (still needed for chat)
TRANSCRIPTS = {}

@router.post("/upload")
def upload_transcript(payload: TranscriptUploadRequest):
    # Store transcript in Phase-1 memory
    TRANSCRIPTS[payload.conversation_id] = payload.text

    # Phase-2: chunk + embed + save in Chroma
    add_transcript_to_vector_db(payload.conversation_id, payload.text)

    print("TRANSCRIPTS:")
    print(TRANSCRIPTS)

    return {"status": "uploaded and embedded"}

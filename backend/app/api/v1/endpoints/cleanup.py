from fastapi import APIRouter
from app.core.embeddings import delete_conversation

router = APIRouter()

@router.delete("/cleanup/{conversation_id}")
def cleanup_conversation(conversation_id: str):
    delete_conversation(conversation_id)
    return {"status": "conversation deleted"}

from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.core.llm_client import generate_reply
from app.api.v1.endpoints.ingest import TRANSCRIPTS

router = APIRouter()

# Phase-1 session memory
CONVERSATIONS = {}

@router.post("/", response_model=ChatResponse)
def chat(payload: ChatRequest):
    transcript = TRANSCRIPTS.get(payload.conversation_id, "")
    history = "\n".join(CONVERSATIONS.get(payload.conversation_id, []))

    reply = generate_reply(transcript, history, payload.message)

    CONVERSATIONS.setdefault(payload.conversation_id, [])
    CONVERSATIONS[payload.conversation_id].append(f"User: {payload.message}")
    CONVERSATIONS[payload.conversation_id].append(f"Assistant: {reply}")

    return {"reply": reply}

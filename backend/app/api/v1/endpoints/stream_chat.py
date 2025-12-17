from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from app.core.llm_client import generate_reply
from app.core.embeddings import query_vector_db
from app.core.memory import get_memory, save_message
from app.core.auth import verify_api_key
from app.core.session import get_or_create_session
from app.core.stream import stream_chunks
from app.api.v1.endpoints.rate_limit import rate_limit

router = APIRouter()

@router.post("/chat/rag/stream")
def chat_rag_stream(
    request: Request,
    payload: dict,
    api_key: str = Depends(verify_api_key)
):  
    conversation_id = payload["conversation_id"]
    message = payload["message"]

    session_id = get_or_create_session(api_key)
    rate_limit(api_key, session_id)

    memory = get_memory(conversation_id)
    history = "\n".join([f"{m.type}: {m.content}" for m in memory.messages])

    retrieved = query_vector_db(message)
    context = "\n".join(retrieved)

    full_reply = generate_reply(context, history, message)

    save_message(conversation_id, "human", message)
    save_message(conversation_id, "ai", full_reply)

    def event_stream():
        for chunk in stream_chunks(full_reply):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

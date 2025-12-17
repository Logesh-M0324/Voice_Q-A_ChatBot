from fastapi import APIRouter, Depends  
from pydantic import BaseModel
from app.core.llm_client import generate_reply
from app.core.embeddings import query_vector_db
from app.core.memory import get_memory, save_message
from app.core.auth import verify_api_key
from app.core.session import get_or_create_session


router = APIRouter()

class ChatRAGRequest(BaseModel):
    conversation_id: str
    message: str

class ChatRAGResponse(BaseModel):
    reply: str

@router.post("", response_model=ChatRAGResponse)
def chat_rag(payload: ChatRAGRequest, api_key: str = Depends(verify_api_key)):
    # Load memory
    memory = get_memory(payload.conversation_id)
    history = "\n".join(
        [f"{m.type}: {m.content}" for m in memory.messages]
    )
    user_session = get_or_create_session(api_key)
    query = payload.message

    # RAG retrieval
    retrieved_chunks = query_vector_db(payload.message, top_k=5)
    transcript_context = "\n".join(retrieved_chunks)


    reply = generate_reply(
        transcript_context,
        history,
        payload.message
    )

    # Save memory
    save_message(payload.conversation_id, "human", payload.message)
    save_message(payload.conversation_id, "ai", reply)

    return {"reply": reply}
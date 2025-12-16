from fastapi import FastAPI
from app.api.v1.endpoints import ingest, chat, chat_rag
from app.api.v1.endpoints import memory
from app.api.v1.endpoints import tasks

app = FastAPI(title="Transcript Chatbot")

app.include_router(ingest.router, prefix="/api/v1/ingest", tags=["Ingest"])
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(chat_rag.router, prefix="/api/v1/chat/rag", tags=["Chat-RAG"])
app.include_router(memory.router, prefix="/api/v1/memory", tags=["Memory"])
app.include_router(tasks.router,prefix="/api/v1/createTask",tags=["tasks"])
#app.include_router(tasks.router,prefix="/api/v1/getTask",tags=["tasks"])


@app.get("/")
def health():
    return {"status": "ok"}

from fastapi import FastAPI
from app.api.v1.endpoints import ingest, chat, chat_rag
from app.api.v1.endpoints import memory
from app.api.v1.endpoints import tasks
from app.api.v1.endpoints import tasks_status
from app.api.v1.endpoints import stream_chat
from app.api.v1.endpoints import cleanup, health
from app.api.v1.endpoints import downloadPdf
from app.api.v1.endpoints import task_stream
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
import os


app = FastAPI(title="Transcript Chatbot")

# used to load the header authorization
security = HTTPBearer() 


# ✅ CORS MUST COME FIRST (before include_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ingest.router, prefix="/api/v1/ingest", tags=["Ingest"]) 
app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
app.include_router(chat_rag.router, prefix="/api/v1/chat/rag", tags=["Chat-RAG"])
app.include_router(memory.router, prefix="/api/v1/memory", tags=["Memory"])
app.include_router(tasks.router,prefix="/api/v1/createTask",tags=["tasks"])
app.include_router(tasks_status.router,prefix="/api/v1/tasks/status",tags=["tasks"])
app.include_router(cleanup.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")
app.include_router(stream_chat.router, prefix="/api/v1")
app.include_router(downloadPdf.router, prefix="/api/v1/download", tags=["download"])
app.include_router(task_stream.router, prefix="/api/v1", tags=["task_stream"])

@app.get("/")
def health():
    return {"status": "ok"}

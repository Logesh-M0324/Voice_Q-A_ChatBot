from pydantic import BaseModel
from typing import List

class TranscriptUploadRequest(BaseModel):
    conversation_id: str
    text: str

class ChatRequest(BaseModel):
    conversation_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
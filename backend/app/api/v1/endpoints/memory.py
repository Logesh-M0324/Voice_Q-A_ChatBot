# Optional Memory API (Inspect / Clear)
    
from fastapi import APIRouter
import redis

router = APIRouter()

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

@router.get("/{conversation_id}")
def get_memory(conversation_id: str):
    return redis_client.lrange(conversation_id, 0, -1)

@router.delete("/{conversation_id}")
def clear_memory(conversation_id: str):
    redis_client.delete(conversation_id)
    return {"status": "memory cleared"}

from fastapi import APIRouter
from app.core.memory import redis_client

router = APIRouter()

@router.get("/health")
def health_check():
    redis_status = redis_client.ping()
    return {
        "status": "ok",
        "redis": redis_status
    }

from fastapi import APIRouter
from app.core.memory import redis_client

router = APIRouter()

@router.get("/{task_id}")
def get_task_status(task_id: str):
    data = redis_client.hgetall(task_id)
    print(data)
    if not data:
        return {"status": "not_found"}

    # Redis returns bytes
    return {k : v for k, v in data.items()}

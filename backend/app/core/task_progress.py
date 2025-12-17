from app.core.memory import redis_client

def update_progress(task_id: str, status: str, percent: int):
    redis_client.hset(task_id, mapping={
        "status": status,
        "progress": percent
    })

def get_progress(task_id: str):
    data = redis_client.hgetall(task_id)
    return {
        "status": data.get("status", ""),
        "progress": int(data.get("progress", 0))
    }

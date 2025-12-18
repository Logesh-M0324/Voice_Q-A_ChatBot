from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import time
import json

from app.core.memory import redis_client

router = APIRouter()

@router.get("/tasks/stream/{task_id}")
def stream_task(task_id: str):

    def event_generator():
        last_status = None
        last_progress = None

        while True:
            data = redis_client.hgetall(task_id)

            if not data:
                yield "event: error\ndata: Task not found\n\n"
                break

            status = data.get("status", "queued")
            progress = int(data.get("progress", 0))

            if status != last_status or progress != last_progress:
                payload = {
                    "status": status,
                    "progress": progress
                }

                yield f"data: {json.dumps(payload)}\n\n"

                last_status = status
                last_progress = progress

            if status in ("completed", "failed"):
                break

            # Heartbeat every 1s
            time.sleep(1)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )

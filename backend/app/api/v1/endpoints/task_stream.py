from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import time
from app.core.task_progress import get_progress

router = APIRouter()

@router.get("/tasks/stream/{task_id}")
def stream_task(task_id: str):

    def event_generator():
        last_progress = -1
        while True:
            progress = get_progress(task_id)
            if progress["progress"] != last_progress:
                yield f"data: {progress}\n\n"
                last_progress = progress["progress"]

            if progress["status"] == "completed":
                break

            time.sleep(1)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

from fastapi import APIRouter, UploadFile, BackgroundTasks, Form
import uuid
import shutil
from app.workers.task_runner import run_task
from app.core.memory import redis_client

router = APIRouter()

@router.post("/tasks/create")
async def create_task(
    file: UploadFile,
    background_tasks: BackgroundTasks,
    conversation_id: str = Form(...)
):
    task_id = str(uuid.uuid4())
    audio_path = f"uploads/{task_id}.wav"

    with open(audio_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    redis_client.hset(task_id, mapping={
        "status": "queued",
        "conversation_id": conversation_id
    })

    # TTL: auto-delete after X days (example: 7 days)
    redis_client.expire(task_id, 60 * 60 * 24 * 7)

    background_tasks.add_task(
        run_task,
        task_id,
        audio_path,
        conversation_id
    )

    return {"task_id": task_id}

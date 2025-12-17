from fastapi import APIRouter, UploadFile, BackgroundTasks
import uuid
import shutil
from app.workers.task_runner import run_task
from app.core.memory import redis_client

router = APIRouter()

@router.post("/tasks/create")
async def create_task(
    file: UploadFile,
    background_tasks: BackgroundTasks
):
    task_id = str(uuid.uuid4())
    audio_path = f"uploads/{task_id}.wav"

    with open(audio_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    redis_client.hset(task_id, "status", "queued")
    background_tasks.add_task(run_task, task_id, audio_path)

    return {"task_id": task_id}

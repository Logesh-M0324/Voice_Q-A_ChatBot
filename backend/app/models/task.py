from pydantic import BaseModel
from typing import Optional

class TaskStatus(BaseModel):
    task_id: str
    status: str
    result_path: Optional[str] = None

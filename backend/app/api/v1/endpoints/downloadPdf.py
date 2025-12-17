from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

# Path to outputs folder (adjust based on your project structure)
outputs_path = os.path.join(os.path.dirname(__file__), "../../../../outputs")

@router.get("/{task_id}")
def download_pdf(task_id: str):

    file_path = os.path.join(outputs_path, f"{task_id}.pdf")

    if os.path.exists(file_path):
        return FileResponse(
            file_path,
            media_type="application/pdf",
            filename=f"{task_id}.pdf",
            headers={
                "Content-Disposition": f'inline; filename="{task_id}.pdf"'
            }   
        )

    return {"detail": "Not Found"}
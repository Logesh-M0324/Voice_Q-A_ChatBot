from fastapi import Depends, Request
from app.core.auth import verify_api_key

def get_current_user(request: Request = Depends(verify_api_key)):
    return request.state.user

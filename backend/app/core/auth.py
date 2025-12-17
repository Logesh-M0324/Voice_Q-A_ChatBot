from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()  # ⬅️ used for the Authorization of API key ,able to see in FASTAPI SWAGGER UI RIGHT TOP

VALID_API_KEYS = {
    "test123",
    "demo-key-456",
}

def verify_api_key(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    if credentials.credentials not in VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )

    return credentials.credentials

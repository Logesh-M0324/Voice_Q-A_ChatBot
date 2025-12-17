from fastapi import Depends, HTTPException
from app.core.memory import redis_client
from app.core.auth import verify_api_key

RATE_LIMIT = 50  # per minute

def rate_limit(api_key: str, session_id: str):
    key = f"rl:{api_key}:{session_id}"
    count = redis_client.incr(key)

    if count == 1:
        redis_client.expire(key, 60)

    if count > RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

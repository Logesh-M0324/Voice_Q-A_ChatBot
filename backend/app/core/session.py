import uuid
import redis

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_or_create_session(api_key: str) -> str:
    session_key = f"session:{api_key}"
    session_id = redis_client.get(session_key)

    if not session_id:
        session_id = str(uuid.uuid4())
        redis_client.set(session_key, session_id)

    return session_id

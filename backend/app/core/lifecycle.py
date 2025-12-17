from app.core.memory import redis_client

REDIS_TTL_SECONDS = 7 * 24 * 60 * 60  # 7 days

def set_ttl(key: str):
    redis_client.expire(key, REDIS_TTL_SECONDS)

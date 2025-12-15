import redis
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage, AIMessage

# Redis client (local)
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def get_memory(conversation_id: str) -> ConversationBufferMemory:
    memory = ConversationBufferMemory(return_messages=True)

    stored = redis_client.lrange(conversation_id, 0, -1)
    for msg in stored:
        role, content = msg.split("::", 1)
        if role == "human":
            memory.chat_memory.add_message(HumanMessage(content=content))
        else:
            memory.chat_memory.add_message(AIMessage(content=content))

    return memory

def save_message(conversation_id: str, role: str, content: str):
    redis_client.rpush(conversation_id, f"{role}::{content}")

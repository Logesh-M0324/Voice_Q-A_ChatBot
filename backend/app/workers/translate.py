from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

def translate_text(text: str, target_lang: str) -> str:
    prompt = f"Translate this text to {target_lang}:\n{text}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

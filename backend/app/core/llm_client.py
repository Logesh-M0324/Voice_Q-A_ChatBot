from langchain_groq import ChatGroq
from langchain.messages import HumanMessage
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

def generate_reply(transcript: str, history: str, question: str) -> str:
    prompt = f"""
            You are an AI assistant.
            Answer ONLY using the transcript.

            Transcript:
            {transcript}

            Conversation so far:
            {history}

            User question:
            {question}
        """

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
TRANSCRIPTS = {}

def save_transcript(conversation_id: str, text: str):
    TRANSCRIPTS[conversation_id] = text

def get_transcript(conversation_id: str) -> str:
    return TRANSCRIPTS.get(conversation_id, "")

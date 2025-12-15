// Phase-1 chat (original endpoint)
export async function sendMessage(conversationId: string, message: string) {
  const res = await fetch("http://localhost:8000/api/v1/chat/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ conversation_id: conversationId, message })
  });
  return res.json();
}

// Phase-2 RAG chat
export async function sendMessageRAG(conversationId: string, message: string) {
  const res = await fetch("http://localhost:8000/api/v1/chat/rag/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ conversation_id: conversationId, message })
  });
  return res.json();
}

// Upload transcript (automatically embeds in vector DB)
export async function uploadTranscript(conversationId: string, text: string) {
  const res = await fetch("http://localhost:8000/api/v1/ingest/upload", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ conversation_id: conversationId, text })
  });
  return res.json();
}




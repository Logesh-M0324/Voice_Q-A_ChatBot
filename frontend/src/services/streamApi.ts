export async function streamChat(
  apiKey: string,
  conversationId: string,
  message: string,
  onChunk: (chunk: string) => void
) {
  const res = await fetch("http://127.0.0.1:8000/api/v1/chat/rag/stream", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": apiKey,
    },
    body: JSON.stringify({
      conversation_id: conversationId,
      message,
    }),
  });

  const reader = res.body?.getReader();
  if (!reader) return;

  const decoder = new TextDecoder();

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    onChunk(decoder.decode(value));
  }
}

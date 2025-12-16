const BASE_URL = "http://127.0.0.1:8000/api/v1";

export async function sendChatMessage(
  conversation_id: string,
  message: string
) {
  const res = await fetch(`${BASE_URL}/chat/rag`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      conversation_id: conversation_id,
      message: message,
    }),
  });

  return res.json();
}

export async function uploadAudio(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BASE_URL}/createTask/tasks/create`, {
    method: "POST",
    body: formData,
  });

  return res.json();
}

export async function getTaskStatus(taskId: string) {
  const res = await fetch(`${BASE_URL}/createTask/tasks/status/${taskId}`);
  return res.json();
}

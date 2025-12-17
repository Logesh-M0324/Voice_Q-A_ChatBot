const BASE_URL = "http://127.0.0.1:8000/api/v1";
import { getApiKey } from "../utils/apiKey";


export async function sendChatMessage(
  conversation_Id: string,
  message: string
) {
  const apiKey = getApiKey();

  if (!apiKey) {
    throw new Error("API key missing. Please set API key.");
  }

  console.log(apiKey)

  const res = await fetch(`${BASE_URL}/chat/rag`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${apiKey}`, // ✅ DEFAULT API KEY USED HERE or "x-api-key": apiKey
    },
    body: JSON.stringify({
      conversation_id: conversation_Id,
      message:message,
    }),
  });

  console.log(res)

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
  const res = await fetch(
    `${BASE_URL}/tasks/status/${taskId}`
  );
  return res.json();
}
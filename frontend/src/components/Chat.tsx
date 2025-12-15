import { useState } from "react";
import { sendMessage } from "../services/api";

export default function Chat() {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState("");
  const conversationId = "demo-session";

  async function handleSend() {
    const res = await sendMessage(input, conversationId);
    setMessages([...messages, "You: " + input, "Bot: " + res.reply]);
    setInput("");
  }

  return (
    <div>
      <div>
        {messages.map((m, i) => <p key={i}>{m}</p>)}
      </div>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

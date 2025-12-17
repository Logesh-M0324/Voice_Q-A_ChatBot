import { useState } from "react";
import { sendChatMessage } from "../../services/api";

export default function ChatWindow() {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState("");

  const sessionId = "default-session";

  const handleSend = async () => {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, "You: " + input]);

    const res = await sendChatMessage(sessionId, input);

    setMessages((prev) => [...prev, "Bot: " + res.reply]);

    setInput("");
  };

  return (
    <div>
      {messages.map((m, i) => (
        <p key={i}>{m}</p>
      ))}

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <button onClick={handleSend}>Send</button>
    </div>
  );
}
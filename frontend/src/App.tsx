import { useState } from "react";
import ChatWindow from "./components/ChatWindow/ChatWindow";
import VoiceRecorder from "./components/VoiceRecorder/VoiceRecorder";
import ApiKeyModal from "./components/ApiKeyModal/ApiKeyModal";
import { getApiKey } from "./utils/apiKey";

export default function App() {
  const [hasKey, setHasKey] = useState(!!getApiKey());

  if (!hasKey) {
    return <ApiKeyModal onSaved={() => setHasKey(true)} />;
  }

  return (
    <center>
      <ChatWindow />
      <VoiceRecorder />
    </center>
  );
}

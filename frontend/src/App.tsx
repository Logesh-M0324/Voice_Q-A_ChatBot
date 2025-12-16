import './index.css'
import ChatWindow from "./components/ChatWindow/ChatWindow";
import VoiceRecorder from "./components/VoiceRecorder/VoiceRecorder";

function App() {
  return (
    <center>
      <div>
        <h2>EchoRAG Demo</h2>

        <h3>Chat</h3>
        <ChatWindow />

        <hr />

        <h3>Voice to PDF</h3>
        <VoiceRecorder />
      </div>
    </center>
  );
}

export default App;

import { useState } from "react";
import { uploadAudio, getTaskStatus } from "../../services/api";

export default function VoiceRecorder() {
  const [taskId, setTaskId] = useState<string | null>(null);
  const [status, setStatus] = useState("");

  const handleUpload = async (file: File) => {
    const res = await uploadAudio(file);
    setTaskId(res.task_id);
  };

  const checkStatus = async () => {
    if (!taskId) return;
    const res = await getTaskStatus(taskId);
    setStatus(res.status);
  };

  return (
    <div>
      <input
        type="file"
        accept=".wav"
        onChange={(e) =>
          e.target.files && handleUpload(e.target.files[0])
        }
      />
      <button onClick={checkStatus}>Check Status</button>
      <p>Status: {status}</p>
    </div>
  );
}

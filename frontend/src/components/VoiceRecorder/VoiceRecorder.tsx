// // import { useState } from "react";
// // import { uploadAudio, getTaskStatus } from "../../services/api";

// // export default function VoiceRecorder() {
// //   const [taskId, setTaskId] = useState<string | null>(null);
// //   const [status, setStatus] = useState("");

// //   const handleUpload = async (file: File) => {
// //     const res = await uploadAudio(file);
// //     setTaskId(res.task_id);
// //   };

// //   const checkStatus = async () => {
// //     if (!taskId) return;
// //     const res = await getTaskStatus(taskId);
// //     setStatus(res.status);
// //   };

// //   return (
// //     <div>
// //       <input
// //         type="file"
// //         accept=".wav"
// //         onChange={(e) =>
// //           e.target.files && handleUpload(e.target.files[0])
// //         }
// //       />
// //       <button onClick={checkStatus}>Check Status</button>
// //       <p>Status: {status}</p>
// //     </div>
// //   );
// // }

// import { useState } from "react";
// import { uploadAudio } from "../../services/api";
// import TaskStatus from "../TaskStatus";

// export default function VoiceRecorder() {
//   const [taskId, setTaskId] = useState<string | null>(null);

//   const handleUpload = async (file: File) => {
//     const res = await uploadAudio(file);
//     setTaskId(res.task_id);
//   };

//   return (
//     <div>
//       <input
//         type="file"
//         accept=".wav"
//         onChange={(e) =>
//           e.target.files && handleUpload(e.target.files[0])
//         }
//       />

//       {taskId && <TaskStatus taskId={taskId} />}
//     </div>
//   );
// }


import { useState } from "react";
import { uploadAudio } from "../../services/api";
import TaskStatus from "../TaskStatus/TaskStatus";

export default function VoiceRecorder() {
  const [taskId, setTaskId] = useState<string | null>(null);
  const [conversationId, setConversationId] = useState<string>("");

  const handleUpload = async (file: File) => {
    if (!conversationId) {
      alert("Please enter a conversation ID!");
      return;
    }

    const res = await uploadAudio(file, conversationId);
    setTaskId(res.task_id);
  };

  return (
    <div>
      <div style={{ marginBottom: "10px" }}>
        <label>
          Conversation ID:{" "}
          <input
            type="text"
            value={conversationId}
            onChange={(e) => setConversationId(e.target.value)}
            placeholder="Enter conversation ID"
          />
        </label>
      </div>

      <input
        type="file"
        accept=".wav"
        onChange={(e) =>
          e.target.files && handleUpload(e.target.files[0])
        }
      />

      {taskId && <TaskStatus taskId={taskId} />}
    </div>
  );
}

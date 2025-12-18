// import { useEffect, useState } from "react";
// import { getTaskStatus } from "../../services/api";

// export default function TaskStatus({ taskId }: { taskId: string }) {
//   const [status, setStatus] = useState("queued");
//   const [progress, setProgress] = useState<number | null>(null);
//   const [downloadUrl, setDownloadUrl] = useState<string | null>(null);
  
//   useEffect(() => {
//     if (!taskId) return;

//     const interval = setInterval(async () => {
//       const res = await getTaskStatus(taskId);

//       setStatus(res.status);
//       if (res.progress !== undefined) {
//         setProgress(res.progress);
//       }

//       if (res.status === "completed") {
//         const fileName = res.pdf_path.split("/").pop();
//         const extractedTaskId = fileName.replace(".pdf", "");

//         setDownloadUrl(
//           `http://127.0.0.1:8000/api/v1/download/${extractedTaskId}`
//         );

//         clearInterval(interval);
//       }
//     }, 2000);

//     return () => clearInterval(interval);
//   }, [taskId]);

//   return (
//     <div>
//       <p>Status: {status}</p>

//       {progress !== null && <p>Progress: {progress}%</p>}

//       {downloadUrl && (
//         <a href={downloadUrl} target="_blank" rel="noopener noreferrer">
//           Download PDF
//         </a>
//       )}
//     </div>
//   );
// }

import { useEffect, useState } from "react";
import { getTaskStatus } from "../../services/api";
import { useTaskStream } from "../../hooks/useTaskStream";

export default function TaskStatus({ taskId }: { taskId: string }) {
  // 🔹 SSE state
  const {
    status: sseStatus,
    progress: sseProgress,
  } = useTaskStream(taskId);

  // 🔹 Polling state (fallback)
  const [status, setStatus] = useState("queued");
  const [progress, setProgress] = useState<number | null>(null);
  const [downloadUrl, setDownloadUrl] = useState<string | null>(null);

  // 🔹 Decide source of truth
  const finalStatus = sseStatus || status;
  const finalProgress =
    sseProgress !== undefined ? sseProgress : progress;

  // 🔹 Polling fallback (only if SSE not active)
  useEffect(() => {
    if (!taskId) return;
    if (sseStatus) return; // ⛔ SSE active → skip polling

    const interval = setInterval(async () => {
      const res = await getTaskStatus(taskId);

      setStatus(res.status);
      if (res.progress !== undefined) {
        setProgress(res.progress);
      }

      if (res.status === "completed") {
        const fileName = res.pdf_path.split("/").pop();
        const extractedTaskId = fileName.replace(".pdf", "");

        setDownloadUrl(
          `http://127.0.0.1:8000/api/v1/download/${extractedTaskId}`
        );

        clearInterval(interval);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [taskId, sseStatus]);

  // 🔹 Handle download when SSE completes
  useEffect(() => {
    if (sseStatus === "completed" && !downloadUrl) {
      setDownloadUrl(
        `http://127.0.0.1:8000/api/v1/download/${taskId}`
      );
    }
  }, [sseStatus, taskId, downloadUrl]);

  return (
    <div>
      <p>Status: {finalStatus}</p>

      {finalProgress !== null && (
        <p>Progress: {finalProgress}%</p>
      )}

      {downloadUrl && (
        <a
          href={downloadUrl}
          target="_blank"
          rel="noopener noreferrer"
        >
          Download PDF
        </a>
      )}
    </div>
  );
}

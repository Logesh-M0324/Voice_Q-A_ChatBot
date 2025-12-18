import { useEffect, useState } from "react";

export function useTaskStream(taskId: string | null) {
  const [status, setStatus] = useState("queued");
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    if (!taskId) return;

    const eventSource = new EventSource(
      `http://127.0.0.1:8000/api/v1/tasks/stream/${taskId}`
    );

    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setStatus(data.status);
      setProgress(data.progress);

      if (data.status === "completed" || data.status === "failed") {
        eventSource.close();
      }
    };

    eventSource.onerror = () => {
      eventSource.close(); // fallback to polling
    };

    return () => eventSource.close();
  }, [taskId]);

  return { status, progress };
}

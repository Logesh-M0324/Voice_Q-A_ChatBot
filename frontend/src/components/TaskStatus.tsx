import { useEffect, useState } from "react";
import { getTaskStatus } from "../services/api";

export default function TaskStatus({ taskId }: { taskId: string }) {
  const [status, setStatus] = useState("queued");
  const [pdf, setPdf] = useState<string | null>(null);

  useEffect(() => {
    if (!taskId) return;

    const interval = setInterval(async () => {
      const res = await getTaskStatus(taskId);
      setStatus(res.status);

      if (res.status === "completed") {
        setPdf(res.pdf_path);
        clearInterval(interval);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [taskId]);

  return (
    <div>
      <p>Status: {status}</p>

      {pdf && (
        <a
          href={`http://127.0.0.1:8000/${pdf}`}
          target="_blank"
        >
          Download PDF
        </a>
      )}
    </div>
  );
}

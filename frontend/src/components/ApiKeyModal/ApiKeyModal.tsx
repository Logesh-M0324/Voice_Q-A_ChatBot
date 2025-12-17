import { useState } from "react";
import { setApiKey } from "../../utils/apiKey";

type Props = {
  onSaved: () => void;
};


export default function ApiKeyModal({ onSaved }: Props) {
  const [key, setKey] = useState("");

  const handleSave = () => {
    if (!key.trim()) return;
    setApiKey(key.trim());
    onSaved();
  };

  return (
    <div>
      <h3>Enter API Key</h3>

      <input type="password" value={key} onChange={(e) => setKey(e.target.value)}/>
      
      <button onClick={handleSave}>Save</button>
    </div>
  );
}

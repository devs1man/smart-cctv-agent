import { useState } from "react";
import { uploadVideo, processVideo } from "../api";

export default function VideoUpload({ setJobId, setResults }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select a video");

    setLoading(true);

    try {
      const uploadRes = await uploadVideo(file);
      const jobId = uploadRes.data.job_id;
      setJobId(jobId);

      const processRes = await processVideo(jobId);
      setResults(processRes.data);
    } catch (err) {
      alert("Error processing video");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input
        type="file"
        accept="video/*"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <br />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Processing..." : "Upload & Process"}
      </button>
    </div>
  );
}

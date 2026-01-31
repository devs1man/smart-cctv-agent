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
    <div className="flex flex-col items-center border-2 border-dashed border-gray-300 rounded-xl p-8 mb-8 bg-gray-50">
      <p className="text-gray-600 mb-4 text-sm">
        Supported formats: MP4, AVI, MOV
      </p>

      <input
        type="file"
        accept="video/*"
        className="mb-4 block w-full max-w-sm text-sm text-gray-700
                 file:mr-4 file:py-2 file:px-4
                 file:rounded-md file:border-0
                 file:text-sm file:font-semibold
                 file:bg-blue-50 file:text-blue-700
                 hover:file:bg-blue-100"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="mt-4 bg-blue-600 text-white px-6 py-2 rounded-lg
                 hover:bg-blue-700 disabled:opacity-50
                 transition-all"
      >
        {loading ? "Processing video..." : "Upload & Process"}
      </button>
    </div>
  );
}

import { useState } from "react";
import VideoUpload from "./components/VideoUpload";
import Results from "./components/Results";

export default function App() {
  const [jobId, setJobId] = useState(null);
  const [results, setResults] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 flex items-start justify-center pt-24 px-6">
      <div className="bg-white w-full max-w-2xl rounded-3xl shadow-xl p-10">
        <h1
          className="text-4xl font-extrabold text-center mb-3
               bg-gradient-to-r from-blue-600 to-indigo-600
               bg-clip-text text-transparent"
        >
          Smart CCTV Agent
        </h1>

        <p className="text-gray-500 text-center mb-10">
          Upload a CCTV video to detect, track, and summarize activities
        </p>

        <VideoUpload setJobId={setJobId} setResults={setResults} />

        {results && <Results jobId={jobId} results={results} />}
      </div>
    </div>
  );
}

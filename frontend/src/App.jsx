import { useState } from "react";
import VideoUpload from "./components/VideoUpload";
import Results from "./components/Results";
import "./App.css";

function App() {
  const [jobId, setJobId] = useState(null);
  const [results, setResults] = useState(null);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Smart CCTV Agent</h1>

      <VideoUpload setJobId={setJobId} setResults={setResults} />

      {results && <Results jobId={jobId} results={results} />}
    </div>
  );
}

export default App;

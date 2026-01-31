import { downloadVideoUrl } from "../api";

export default function Results({ jobId, results }) {
  return (
    <div style={{ marginTop: "2rem" }}>
      <h2>Summary</h2>
      <pre>{results.summary}</pre>

      <h2>Events</h2>
      <ul>
        {results.events.map((e, idx) => (
          <li key={idx}>
            [{e.event}] {e.class} (ID{e.track_id}) at {e.time_sec}s
          </li>
        ))}
      </ul>
      <a href={downloadVideoUrl(jobId)}>
        <button>Download Tracked Video</button>
      </a>
    </div>
  );
}

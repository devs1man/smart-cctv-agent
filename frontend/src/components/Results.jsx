import { downloadVideoUrl } from "../api";

export default function Results({ jobId, results }) {
  return (
    <div className="mt-8">
      <hr className="my-6" />
      <h2 className="text-xl font-semibold mb-3 text-gray-800">
        📄 AI Summary
      </h2>

      <pre
        className="bg-gray-900 text-green-400 p-4 rounded-xl
                text-sm mb-8 whitespace-pre-wrap font-mono"
      >
        {results.summary}
      </pre>

      <h2 className="text-xl font-semibold mb-3 text-gray-800">
        📊 Detected Events
      </h2>

      <ul className="space-y-3 mb-8">
        {results.events.map((e, idx) => (
          <li
            key={idx}
            className="flex justify-between items-center
                 bg-gray-50 border rounded-lg p-3
                 hover:bg-blue-50 transition"
          >
            <span className="font-medium text-gray-700">
              {e.event.toUpperCase()} — {e.class}
            </span>

            <span className="text-sm text-gray-400">
              ID {e.track_id} · {e.time_sec}s
            </span>
          </li>
        ))}
      </ul>

      <a
        href={downloadVideoUrl(jobId)}
        className="inline-flex items-center gap-2
             bg-green-600 text-white px-6 py-3 rounded-xl
             hover:bg-green-700 hover:shadow-lg
             transition-all"
      >
        ⬇️ Download Tracked Video
      </a>
    </div>
  );
}

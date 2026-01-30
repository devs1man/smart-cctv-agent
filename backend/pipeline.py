from pathlib import Path
import json

from tracking_module import run_tracking
from events_module import generate_events
from summary_module import generate_summary

def run_pipeline(
        input_video_path: str,
        job_dir: str,
        conf_threshold: float = 0.5,
):
    
    job_dir = Path(job_dir)
    job_dir.mkdir(parents=True, exist_ok=True)

    tracked_video_path = job_dir / "output_tracked.mp4"
    tracking_log_path = job_dir / "tracking_log.json"
    events_path = job_dir / "events.json"
    summary_path = job_dir / "summary.txt"

    run_tracking(
        input_video_path=input_video_path,
        output_video_path=str(tracked_video_path),
        output_json_path=str(tracking_log_path),
        conf_threshold=conf_threshold,
    )

    generate_events(
        tracking_log_path= str(tracking_log_path),
        events_output_path=str(events_path),
        exit_missing_frames=30,
        move_threshold_pixels=30
    )

    generate_summary(
        events_path=str(events_path),
        summary_output_path=str(summary_path),
    )

    summary_text = summary_path.read_text(encoding="utf-8") 
    events_json = json.loads(events_path.read_text(encoding="utf-8"))

    return{
        "tracked_video_path":str(tracked_video_path),
        "tracking_log_path": str(tracking_log_path),
        "events_path": str(events_path),
        "summary_path": str(summary_path),
        "summary_text": summary_text,
        "events_json": events_json,
    }
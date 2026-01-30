from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
import uuid

from pipeline import run_pipeline

app = FastAPI(title="Smart CCTV Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
UPLOADS_DIR = BASE_DIR / "uploads"
UPLOADS_DIR.mkdir(exist_ok=True)


@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    if not file.filename.endswith((".mp4", ".avi", ".mov")):
        raise HTTPException(status_code=400, detail="Unsupported file format")

    job_id = str(uuid.uuid4())
    job_dir = UPLOADS_DIR / job_id
    job_dir.mkdir()

    input_video_path = job_dir / "input.mp4"
    with open(input_video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "Upload successful", "job_id": job_id}


@app.post("/process/{job_id}")
def process_video(job_id: str):
    job_dir = UPLOADS_DIR / job_id
    input_video_path = job_dir / "input.mp4"

    if not input_video_path.exists():
        raise HTTPException(status_code=404, detail="Video not found")

    try:
        result = run_pipeline(
            input_video_path=str(input_video_path),
            job_dir=str(job_dir),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return JSONResponse({
        "message": "Processing completed",
        "summary": result["summary_text"],
        "events": result["events_json"],
        "job_id": job_id
    })


@app.get("/download/{job_id}/video")
def download_tracked_video(job_id: str):
    video_path = UPLOADS_DIR / job_id / "output_tracked.mp4"

    if not video_path.exists():
        raise HTTPException(status_code=404, detail="Tracked video not found")

    return FileResponse(
        path=video_path,
        filename="tracked_video.mp4",
        media_type="video/mp4"
    )


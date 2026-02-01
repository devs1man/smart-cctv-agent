# Smart CCTV Agent

### Full-Stack AI System for Intelligent Video Surveillance

An end-to-end **Machine Learning + Web Application** that analyzes CCTV footage to detect, track, and interpret object behavior using Computer Vision and a REST API backend.

---

## Project Highlights

- End-to-end AI pipeline from raw video to human-readable insights
- YOLO-based object detection and multi-object tracking
- Behavioral event inference (entry, exit, movement)
- Modular, production-style ML architecture
- FastAPI backend exposing ML pipeline via REST APIs
- Designed for extension with a React frontend

---

## System Capabilities

### Computer Vision & ML

- Object detection using YOLOv8
- Persistent multi-object tracking with ByteTrack
- Frame-level tracking logs
- Event detection:
  - Entry
  - Exit
  - Movement

### Intelligence Layer

- Converts tracking data into meaningful behavioral events
- Generates human-readable summaries from detected events

### Backend API

- Video upload via REST API
- Job-based processing pipeline
- Result retrieval endpoints
- Tracked video download support

---

## Architecture Overview

Video Input (CCTV / Uploaded File)
↓
YOLO Object Detection + ByteTrack Tracking
↓
Frame-Level Tracking Logs (JSON)
↓
Event Inference Layer
• Entry Detection
• Exit Detection
• Movement Detection
↓
Human-Readable Summary Generation
↓
FastAPI Backend (REST APIs)
↓
Frontend Client (React – Planned)

### Project overview

## 📁 Project Structure

smart-cctv-agent/
├── backend/
│ ├── main.py # FastAPI application entry point
│ ├── pipeline.py # ML pipeline orchestrator
│ ├── tracking_module.py # YOLO detection + ByteTrack tracking
│ ├── events_module.py # Behavioral event inference
│ ├── summary_module.py # Human-readable summary generation
│ ├── uploads/ # Runtime video data (gitignored)
│ └── requirements.txt # Backend dependencies
│
├── frontend/ # React + Tailwind frontend
│
├── legacy/ # Early experimental scripts
├── .gitignore
└── README.md

## Live Demo

**Frontend (UI):**  
🔗 https://smart-cctv-agent.vercel.app

> **Note:**  
> The backend performs real-time video processing using YOLO and runs locally due to compute limitations on free cloud tiers.  
> To experience full functionality, please run the backend locally and then use the deployed frontend UI.

## Run Backend Locally

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


```

### Deployment Notes

Due to the computational cost of video inference and object tracking, the backend is designed to run locally. The system architecture supports cloud deployment on paid tiers or GPU-enabled services.

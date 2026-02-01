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

1. **Video Input**
   - CCTV footage or user-uploaded video file

2. **Object Detection**
   - YOLO-based object detection on each frame

3. **Object Tracking**
   - ByteTrack for assigning persistent IDs across frames

4. **Frame-Level Logging**
   - Per-frame detection and tracking data stored as structured JSON

5. **Event Inference Layer**
   - Entry detection
   - Exit detection
   - Movement detection based on spatial displacement

6. **Summary Generation**
   - Converts low-level events into human-readable descriptions

7. **Backend API**
   - FastAPI-based REST APIs for upload, processing, and results

8. **Frontend Client**
   - React + Tailwind UI for interaction and visualization

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

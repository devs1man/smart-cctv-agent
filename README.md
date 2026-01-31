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

import cv2
import json
from ultralytics import YOLO

def run_tracking(
        input_video_path :str,
        output_video_path :str,
        output_json_path: str,
        conf_threshold: float = 0.5,
):
    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {input_video_path}")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    tracking_log = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        time_sec = frame_count/fps

        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf = conf_threshold,
        )
        r = results[0]

        frame_tracks = []

        if r.boxes is not None and len(r.boxes) >0:
            ids = r.boxes.id

            for i in range(len(r.boxes)):
                box = r.boxes[i]

                track_id = None
                if ids is not None:
                    track_id = int(ids[i].item())

                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]
                conf = float(box.conf[0])

                x1, y1, x2, y2 = box.xyxy[0].tolist()
                bbox = [int(x1), int(y1), int(x2), int(y2)]

                frame_tracks.append({
                    "track_id": track_id,
                    "class": class_name,
                    "conf": round(conf, 3),
                    "bbox": bbox
                })
        
        tracking_log.append({
            "frame" : frame_count,
            "time_sec":round(time_sec, 3),
            "tracks" : frame_tracks
        })

        tracked_frame = r.plot()
        out.write(tracked_frame)

    cap.release()
    out.release()

    with open(output_json_path, "w") as f:
        json.dump(tracking_log, f, indent=2)

    print("Tracking finished")
    print("Video saved to: ", output_video_path)
    print("Tracking log saved to : ",output_json_path)


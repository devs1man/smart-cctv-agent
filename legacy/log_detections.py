import cv2
import json
import numpy as np
from ultralytics import YOLO

INPUT_VIDEO_PATH = "input.mp4"
OUTPUT_VIDEO_PATH = "output_detected_step2.mp4"
OUTPUT_JSON_PATH = "detections_log.json"

MODEL_NAME = "yolov8n.pt"
CONF_THRESHOLD = 0.5

model = YOLO(MODEL_NAME)

cap = cv2.VideoCapture(INPUT_VIDEO_PATH)

if not cap.isOpened():
    print("Error could not open the video folder")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Video opened successfully")
print(f"FPS: {fps}, width:{width}, height: {height}")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (width, height))

log_data = []
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count+= 1

    time_sec = frame_count / fps

    results = model(frame)
    r = results[0]

    frame_detections = []

    for box in r.boxes:
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])

        if conf < CONF_THRESHOLD:
            continue

        class_name = model.names[cls_id]

        x1, y1, x2, y2 = box.xyxy[0].tolist()
        bbox = [int(x1), int(y1), int(x2), int(y2)]

        frame_detections.append({
            "class" : class_name,
            "conf" : round(conf, 3),
            "bbox": bbox
        })

    log_data.append({
        "frame" : frame_count,
        "time_sec" : round(time_sec, 3),
        "detections" : frame_detections
    })

    detected_frame = results[0].plot()
    detected_frame =  np.asarray(detected_frame, dtype=np.uint8)
    detected_frame = np.ascontiguousarray(detected_frame)
    out.write(detected_frame)

    cv2.imshow("STEP-2 -YOLO Detection + Logging", detected_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if frame_count % 30 == 0:
        print(f"processed {frame_count} frames")

cap.release()
out.release()
cv2.destroyAllWindows()

with open(OUTPUT_JSON_PATH, "w") as f:
    json.dump(log_data, f, indent=2)

print("All done")
print("saved video:", OUTPUT_JSON_PATH)
print("saved json log: ", OUTPUT_JSON_PATH)
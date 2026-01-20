import cv2
from ultralytics import YOLO

INPUT_VIDEO_PATH = "input.mp4"
OUTPUT_VIDEO_PATH = "output_detected.mp4"
MODEL_NAME = "yolov8n.pt"

model = YOLO(MODEL_NAME)

cap = cv2.VideoCapture(INPUT_VIDEO_PATH)

if not cap.isOpened():
    print("ERROR : COULD NOT OPEN THE VIDEO FILE")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Video opened successfully!")
print(f"FPS: {fps}, Width: {width}, Height: {height}")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (width, height))

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    results = model(frame)
    detected_frame = results[0].plot()

    out.write(detected_frame)

    cv2.imshow("YOLO CCTV Detection", detected_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if frame_count % 30 == 0:
        print(f"Processed {frame_count}frame...")

cap.release()
out.release()
cv2.destroyAllWindows()

print("Done ! Saved output video as :", OUTPUT_VIDEO_PATH)
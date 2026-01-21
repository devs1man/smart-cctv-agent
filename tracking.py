import argparse
import cv2
import json
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=str, required=True, help="Path to input video file")
    parser.add_argument("--conf", type=float, default=0.5, help="Confidence threshold")
    args = parser.parse_args()

    INPUT_VIDEO_PATH = args.video
    CONF_THRESHOLD = args.conf

    OUTPUT_VIDEO_PATH = "output_tracked.mp4"
    OUTPUT_JSON_PATH = "tracking_log.json"
    MODEL_NAME = "yolov8n.pt"

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

    track_log = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count+= 1

        time_sec = frame_count / fps

        results = model.track(frame, persist=True, tracker = "bytetrack.yaml", conf = CONF_THRESHOLD)
        r = results[0]

        frame_tracks = [0]

        if r.boxes is not None and len(r.boxes)>0:
            ids = r.boxes.id

            for i in range(len(r.boxes)):
                box = r.boxes[i]

                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]

                x1, y1, x2, y2 = box.xyxy[0].tolist()
                bbox = [int(x1), int(y1), int(x2), int(y2)]

                track_id = None     
                if ids is not None:
                    track_id = int(ids[i].item())    

                frame_tracks.append({
                "track_id" : track_id,
                "class" : class_name,
                "conf" : round(conf,3),
                "bbox" : bbox
            }) 
        
            track_log.append({
            "frame" : frame_count,
            "time_sec": round(time_sec, 3),
            "tracks" : frame_tracks
        })

            tracked_frame = r.plot()
            out.write(tracked_frame)

            cv2.imshow("Step 3- YOLO tracking", tracked_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            if frame_count % 30 == 0:
                print(f"Processed {frame_count} frames...")

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    with open(OUTPUT_JSON_PATH, "w") as f:
        json.dump(track_log,f, indent=2)

    print("DONE SUCCESSFULLY!")
    print("saved tracked video: ",OUTPUT_VIDEO_PATH)
    print("saved tracked logs: ", OUTPUT_JSON_PATH)

if __name__ == "__main__":
    main()

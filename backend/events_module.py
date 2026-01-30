import json
import math

def  bbox_center(bbox):
    x1, y1, x2, y2 = bbox
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    return cx, cy

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def generate_events(
        tracking_log_path:str,
        events_output_path:str,
        exit_missing_frames: int = 30,
        move_threshold_pixels: int = 30,
):
    
    with open(tracking_log_path, "r") as f:
        tracking_data = json.load(f)

    events = []
    active = {}

    for frame_info in tracking_data:
        frame_no = frame_info["frame"]
        time_sec = frame_info["time_sec"]
        tracks = frame_info["tracks"]

        seen_this_frame = set()

        for t in tracks:
            if isinstance(t, dict):
                track_id = t.get("track_id")
                cls = t.get("class", "unknown")
                bbox = t.get("bbox")

            else:
                continue

            if track_id is None:
                continue

            seen_this_frame.add(track_id)

            if track_id not in active:
                active[track_id] = {
                    "class" : cls,
                    "last_seen_frame" : frame_no,
                    "last_seen_time" : time_sec,
                    "last_center": None
                }

                events.append({
                    "time_sec": time_sec,
                    "frame": frame_no,
                    "event": "entry",
                    "track_id": track_id,
                    "class": cls
                })
            else:
                if bbox is not None:
                    center = bbox_center(bbox)
                    prev_center = active[track_id]["last_center"]

                    if prev_center is not None:
                        d = dist(prev_center, center)
                        if d >= move_threshold_pixels:
                            events.append({
                                "time_sec": time_sec,
                                "frame": frame_no,
                                "event": "movement",
                                "track_id": track_id,
                                "class": cls,
                                "distance_px": round(d, 2)
                            })

                    active[track_id]["last_center"] = center

                active[track_id]["last_seen_frame"] = frame_no
                active[track_id]["last_seen_time"] = time_sec

        to_remove = []
        for track_id, info in active.items():
            last_seen = info["last_seen_frame"]
            missing_for = frame_no - last_seen

            if missing_for >= exit_missing_frames and track_id not in seen_this_frame:
                events.append({
                   "time_sec": time_sec,
                    "frame": frame_no,
                    "event": "exit",
                    "track_id": track_id,
                    "class": info["class"] 
                })

                to_remove.append(track_id)

        for tid in to_remove:
            del active[tid]

    with open(events_output_path, "w") as f:
        json.dump(events, f, indent=2)

    print("Events generated")
    print("Events saved to:", events_output_path)
    print("Total events:", len(events))
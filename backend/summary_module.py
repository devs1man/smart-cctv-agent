import json
from collections import defaultdict

def format_time(seconds: float) -> str:
    minute = int(seconds // 60)
    secs = int(seconds % 60)

    return f"{minute: 02d}:{secs:02d}"

def generate_summary(
        events_path: str,
        summary_output_path: str,
):
    
    with open(events_path, "r") as f:
        events = json.load(f)

    events_by_id = defaultdict(list)
    for e in events:
        events_by_id[e["track_id"]].append(e)

    lines = []
    lines.append("SMART CCTV SUMMARY REPORT\n")

    total_entries = 0
    total_exits = 0
    total_movements = 0

    for track_id, evs in events_by_id.items():
        evs.sort(key=lambda x:x["time_sec"])

        obj_class = evs[0].get("class", "unknown")

        lines.append(f"Object: {obj_class} (ID{track_id})")

        for e in evs:
            t = format_time(e["time_sec"])

            if e["event"] == "entry":
                total_entries += 1
                lines.append(f"[{t}]ENTERED")

            elif e["event"] == "exit":
                total_exits += 1
                lines.append(f"  [{t}]EXITED")

            elif e["event"] == "movement":
                total_movements += 1
                dist_px = e.get("distance_px")
                if dist_px is not None:
                    lines.append(f"  [{t}] MOVED ({dist_px}px)")
                else:
                    lines.append(f"  [{t}] MOVED")

        lines.append("")

    lines.append("OVERALL STATISTICS")
    lines.append(f"Total entry events: {total_entries}")
    lines.append(f"Total exit events: {total_exits}")
    lines.append(f"Total movement events: {total_movements}")

    with open(summary_output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(" Summary generated")
    print(" Summary saved to:", summary_output_path)
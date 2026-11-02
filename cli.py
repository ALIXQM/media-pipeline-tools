import os
import json
import argparse
from pathlib import Path

def generate_video_config(title: str, duration_sec: int, fps: int = 30):
    total_frames = duration_sec * fps
    config = {
        "projectTitle": title,
        "fps": fps,
        "durationInSeconds": duration_sec,
        "totalFrames": total_frames,
        "dimensions": {
            "width": 1920,
            "height": 1080
        },
        "audio": {
            "sampleRate": 44100,
            "channels": 2
        }
    }
    return config

def export_srt_template(output_path: str, lines: list):
    with open(output_path, "w", encoding="utf-8") as f:
        for idx, text in enumerate(lines, start=1):
            start_sec = (idx - 1) * 3
            end_sec = idx * 3
            f.write(f"{idx}\n")
            f.write(f"00:00:{start_sec:02d},000 --> 00:00:{end_sec:02d},000\n")
            f.write(f"{text}\n\n")

def main():
    parser = argparse.ArgumentParser(
        description="Media Pipeline Tools: Automation utilities for programmatic video rendering workflows."
    )
    parser.add_argument("--title", type=str, default="Demo Project", help="Title of the media project")
    parser.add_argument("--duration", type=int, default=60, help="Duration in seconds")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second")
    parser.add_argument("--out", type=str, default="dist", help="Output directory")

    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    config_path = out_dir / "render-config.json"
    srt_path = out_dir / "subtitles-template.srt"

    config_data = generate_video_config(args.title, args.duration, args.fps)
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=2)

    sample_subtitles = [
        "Welcome to the video",
        "This is an automated media pipeline segment",
        "Generated via media-pipeline-tools"
    ]
    export_srt_template(str(srt_path), sample_subtitles)

    print(f"Pipeline assets initialized in: {out_dir}/")

if __name__ == "__main__":
    main()

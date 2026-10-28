"""Example YOLO object detector with a live camera view.

Set up with ``uv sync``. Example:
	uv run yolotest.py
	uv run yolotest.py photo.jpg --model yolov8n.pt --output detections
"""

import argparse
from pathlib import Path


def main() -> None:
	parser = argparse.ArgumentParser(description="Run YOLO object detection on an image, video, or webcam.")
	parser.add_argument("source", nargs="?", default="0", help="Input path or webcam index (default: 0).")
	parser.add_argument("--model", default="yolov8n.pt", help="Weights file (default: yolov8n.pt).")
	parser.add_argument("--output", default="runs/detect/predict", help="Directory for saved results.")
	parser.add_argument("--confidence", type=float, default=0.5, help="Minimum detection confidence.")
	parser.add_argument("--device", default="0", help="Device to run on: 0 or cuda:0 (NVIDIA/AMD), mps (Apple Silicon), cpu (default: 0).")
	args = parser.parse_args()

	try:
		from ultralytics import YOLO
	except ImportError:
		parser.error("Install the dependency first: uv sync")

	source = int(args.source) if args.source.isdigit() else args.source
	output = Path(args.output)
	model = YOLO(args.model)
	results = model.predict(
		source=source,
		conf=args.confidence,
		save=True,
		stream=True,
		project=str(output.parent),
		name=output.name,
		exist_ok=True,
		show=True,
		device=args.device
	)

	print("Live detection started. Press Q in the video window to stop.")
	for _ in results:
		pass
	print(f"Results saved under {output}")


if __name__ == "__main__":
	main()

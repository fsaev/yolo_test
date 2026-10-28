# yolo_test

Run [Ultralytics YOLO](https://docs.ultralytics.com/) object detection on an image, a video, or a live webcam feed. Results are shown in a window and saved to disk.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- A Mac with Apple Silicon. The script uses `device="mps"`; change it in `yolotest.py` to run on CUDA or CPU.

## Setup

Create the `.venv` virtual environment and install the locked dependencies:

```sh
uv sync
```

`uv run` uses this environment automatically. To activate it in a shell instead:

```sh
source .venv/bin/activate        # bash/zsh
source .venv/bin/activate.fish   # fish
```

## Usage

```sh
uv run yolotest.py [source] [--model MODEL] [--output DIR] [--confidence CONF]
```

| Argument       | Default                | Description                                  |
| -------------- | ---------------------- | -------------------------------------------- |
| `source`       | `0`                    | Image/video path, or webcam index            |
| `--model`      | `yolov8n.pt`           | Weights file                                 |
| `--output`     | `runs/detect/predict`  | Directory for saved results                  |
| `--confidence` | `0.5`                  | Minimum detection confidence                 |

Examples:

```sh
uv run yolotest.py                                    # default webcam
uv run yolotest.py 1 --model yolo26x-seg.pt           # second camera, segmentation model
uv run yolotest.py photo.png --output detections      # single image
```

Press `Q` in the video window to stop a live session.

Weights missing from the project directory are downloaded by Ultralytics on first use.

## Managing dependencies

```sh
uv add <package>      # add a dependency
uv remove <package>   # remove one
uv lock --upgrade     # upgrade locked versions
```

Dependencies are declared in `pyproject.toml` and pinned in `uv.lock`.

## Files

- `yolotest.py`: the detection script
- `*.pt`: model weights
- `runs/`: saved detection output
- `.vscode/launch.json`: debug configuration for the webcam run

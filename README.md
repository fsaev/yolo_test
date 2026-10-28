# yolo_test

Run [Ultralytics YOLO](https://docs.ultralytics.com/) object detection on an image, a video, or a live webcam feed. Results are shown in a window and saved to disk.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- A camera, or an image/video file, as input
- Optionally a GPU; see [Choosing a device](#choosing-a-device). The default device is `0`, the first NVIDIA/AMD GPU. On a Mac, pass `--device mps`.

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
uv run yolotest.py [source] [--model MODEL] [--output DIR] [--confidence CONF] [--device DEVICE]
```

| Argument       | Default                | Description                                  |
| -------------- | ---------------------- | -------------------------------------------- |
| `source`       | `0`                    | Image/video path, or webcam index            |
| `--model`      | `yolov8n.pt`           | Weights file                                 |
| `--output`     | `runs/detect/predict`  | Directory for saved results                  |
| `--confidence` | `0.5`                  | Minimum detection confidence                 |
| `--device`     | `0`                    | Device to run on, see [below](#choosing-a-device) |

Examples:

```sh
uv run yolotest.py --device mps                       # default webcam on a Mac
uv run yolotest.py 1 --model yolo26x-seg.pt           # second camera, segmentation model, first GPU
uv run yolotest.py photo.png --device cpu             # single image on the CPU
```

Press `Q` in the video window to stop a live session.

Weights missing from the project directory are downloaded by Ultralytics on first use.

## Choosing a device

Pick the device with `--device`. The default is `0`, which is the first NVIDIA or AMD GPU and fails on a Mac without a CUDA GPU, so Mac users need `--device mps`.

| Hardware                | `--device` value         | Notes                                                                 |
| ----------------------- | ------------------------ | --------------------------------------------------------------------- |
| Mac (Apple Silicon)     | `mps`                    | Metal Performance Shaders. Works with the default `uv sync` install.  |
| NVIDIA GPU              | `0` (or `cuda:0`)        | Needs an NVIDIA driver. `0,1` uses multiple GPUs.                     |
| AMD GPU                 | `0` (or `cuda:0`)        | Linux only, via ROCm. Needs a ROCm build of PyTorch (see below).      |
| CPU                     | `cpu`                    | Works everywhere, but is slow with the larger models.                 |

PyTorch exposes ROCm devices through the same `cuda` API, so AMD GPUs use the same values as NVIDIA.

### PyTorch builds

`uv sync` installs the default PyTorch wheel from PyPI for your platform. That wheel supports `mps` on macOS and CUDA on Linux and Windows, but not ROCm. For AMD, install the ROCm build from the PyTorch package index; the [PyTorch install selector](https://pytorch.org/get-started/locally/) shows the matching index URL. See the [uv PyTorch guide](https://docs.astral.sh/uv/guides/integration/pytorch/) for how to configure that index in `pyproject.toml`.

To check which devices PyTorch can see:

```sh
uv run python -c "import torch; print('mps:', torch.backends.mps.is_available(), '| cuda/rocm:', torch.cuda.is_available())"
```

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

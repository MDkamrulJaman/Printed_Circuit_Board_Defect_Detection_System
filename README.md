
# PCB Defect Detection System

A deep learning-based system for detecting defects in printed circuit boards (PCBs) using computer vision and YOLO-based object detection. The project includes a FastAPI backend for inference, dataset handling, training pipeline support, and Docker deployment configuration.

## Overview

This project is designed to:

- detect PCB defects from uploaded images
- support real-time or near-real-time inference through a REST API
- provide a clean backend for integration with web or desktop interfaces
- support model training and artifact persistence under the `runs/` directory
- run in a containerized environment using Docker

## Features

- PCB image upload through API
- YOLOv8-based inference
- FastAPI backend for prediction and health checks
- CORS-enabled API service for frontend integration
- Docker support for deployment
- Training artifacts stored in `runs/`
- Optional frontend image assets for demo and visualization

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- OpenCV
- Pillow
- NumPy
- PyTorch
- Ultralytics YOLO
- Docker

## Project Structure

```text
Printed_Circuit_Board_Defect_Detection_System/
├── api/
│   └── main.py
├── docker/
│   └── dockerfile
├── notebook/
│   └── frontend_images/
├── runs/
│   └── detection/
├── .dockerignore
├── .gitignore
├── requirements-docker.txt
├── README.md
└── pcb-defect-dataset/   # ignored in Git, if used locally
```

## Requirements

Before running the project, ensure the following are available:

- Python 3.11+
- pip
- Docker (optional, for containerized deployment)
- GPU or CPU environment for inference
- Pretrained model weights for the detection task

Important:
The API is configured to load a model from:

```text
runs/detection/train/weights/pcbdefect02yolo26n.onnx
```

Make sure this file exists before starting the application.

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd Printed_Circuit_Board_Defect_Detection_System
```

2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

If using the Docker-specific environment:

```bash
pip install -r requirements-docker.txt
```

## Running the API Locally

From the project root:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

Then open:

- Swagger UI: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

## API Endpoints

### GET /

Returns the API root information.

### GET /health

Checks whether the service is running.

### POST /predict

Uploads an image for defect detection.

Request:

- multipart form-data
- field: `file`
- optional: `confidence_threshold`

Example using curl:

```bash
curl -X POST "http://localhost:8000/predict" \
  -F "file=@sample_pcb.jpg" \
  -F "confidence_threshold=0.5"
```

## Docker Deployment

Build the Docker image:

```bash
docker build -f docker\dockerfile -t pcb-defect-detector .
```

Run the container:

```bash
docker run --rm -p 8000:8000 pcb-defect-detector
```

The API will be available at:

```text
http://localhost:8000
```

## Environment Notes

The project uses:

- `api/` for the FastAPI backend
- `runs/` for model artifact storage
- `notebook/frontend_images/` for visuals and demo assets

These folders should be kept organized and should not be committed if they contain large datasets or model weights.

## Model Management

Place trained weights and model artifacts in the appropriate `runs/` folder structure. If using different model names, update the path in `api/main.py`:

```python
MODEL_PATH = "runs/detection/train/weights/pcbdefect02yolo26n.onnx"
```

## Git Ignore

The repository includes a `.gitignore` file to prevent committing:

- local datasets
- model weights
- virtual environments
- logs
- editor metadata

## License

This project is intended for academic, research, or internal industrial use unless otherwise specified by the project owner.

## Contact

For project-related questions, model updates, or deployment support, contact the project maintainer or repository owner.

## Future Improvements

- Add frontend dashboard
- Add batch inference support
- Add defect classification summaries
- Add training scripts for custom datasets
- Add metrics visualization and reporting
- Add authentication and request limits for production deployment

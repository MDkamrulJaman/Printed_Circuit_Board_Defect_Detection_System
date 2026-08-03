from ultralytics import YOLO


def train_yolo_model(
    model_path: str = "yolo26n.pt",
    data_path: str = "pcb-defect-dataset/data.yaml",
    epochs: int = 50,
    batch: int = 8,
    imgsz: int = 640,
    project: str = "C:/Users/HP/OneDrive/Desktop/object-detection-yolo/src/runs",
    optimizer: str = "AdamW",
    learning_rate: float = 0.001,
    patience: int = 20,
    workers: int = 2,
) -> None:
    """Train a YOLO model with the provided dataset and configuration.

    Args:
        model_path: Path to the YOLO model, weights, or checkpoint.
        data_path: Path to the dataset YAML file.
        epochs: Number of training epochs.
        batch: Batch size for training.
        imgsz: Input image size.
        project: Directory where training results are saved.
        optimizer: Optimizer to use for training.
        learning_rate: Initial learning rate.
        patience: Number of epochs to wait for improvement before stopping training.
        workers: Number of worker threads to use for training.
    """
    model = YOLO(model_path)
    model.train(
        data=data_path,
        epochs=epochs,
        batch=batch,
        imgsz=imgsz,
        project=project,
        optimizer=optimizer,
        lr0=learning_rate,
        patience=patience,
        workers=workers,

    )

if __name__ == "__main__":
    # Example usage
    train_yolo_model()          
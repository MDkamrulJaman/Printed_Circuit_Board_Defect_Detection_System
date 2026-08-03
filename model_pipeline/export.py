from ultralytics import YOLO

# Load a model
model = YOLO("runs/detection/train/weights/pcbdefect02yolo26n.onnx")  # load a custom model

# Export the model
model.export(format="onnx")
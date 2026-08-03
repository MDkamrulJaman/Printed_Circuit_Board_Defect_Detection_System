from ultralytics import YOLO

model = YOLO("runs/detection/train/weights/pcbdefect02yolo26n.onnx")


image_paths = [
    "pcb-defect-dataset-samples/test/images/l_light_01_missing_hole_04_2_600.jpg",
]

model.predict(
    source  = image_paths,
    imgsz   = 640,
    conf    = 0.25,
    save    = True,
    name    = "prediction",
)





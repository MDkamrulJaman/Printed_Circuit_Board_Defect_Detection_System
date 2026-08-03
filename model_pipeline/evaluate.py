from pathlib import Path
import pandas as pd
from ultralytics import YOLO

# SETTINGS
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL = str(PROJECT_ROOT / "runs" / "detection" / "train" / "weights" / "pcbdefect02yolo26n.onnx")
DATA = str(PROJECT_ROOT / "pcb-defect-dataset" / "data.yaml")
IMGSZ = 640
OUTPUT_CSV = PROJECT_ROOT / "evaluation_results.csv"

# Load trained model
model = YOLO(MODEL)

# Run evaluation on val set
metrics = model.val(
    data=DATA,
    imgsz=IMGSZ,
    task="detect",
)

# Export the full summary and per-class metrics to CSV
summary = {
    "model": MODEL,
    "dataset": DATA,
    "imgsz": IMGSZ,
}
summary.update(metrics.results_dict)

summary_df = pd.DataFrame([summary])
summary_df.to_csv(OUTPUT_CSV, index=False)

# Also include the class-wise table if available
try:
    class_df = metrics.to_df()
    if class_df is not None and not class_df.empty:
        class_df.to_csv(PROJECT_ROOT / "evaluation_results_per_class.csv", index=False)
except Exception:
    pass

print(f"Saved evaluation summary to {OUTPUT_CSV}")
print(f"Saved per-class evaluation results to {PROJECT_ROOT / 'evaluation_results_per_class.csv'}")


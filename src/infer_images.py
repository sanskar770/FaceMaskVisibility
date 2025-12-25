from ultralytics import YOLO

MODEL_PATH = "runs/detect/mask_detector/weights/best.pt"

model = YOLO(MODEL_PATH)

results = model.predict(
    source="dataset/images/val", 
    conf=0.25,
    imgsz=416,
    save=True,
    line_thickness=1,   
    show_labels=True,           
    show_conf=False   
)

print("Saved outputs in runs/detect/predict/")
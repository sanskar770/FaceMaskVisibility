import os
import random
import shutil

IMG_DIR = "dataset/images"
LBL_DIR = "dataset/yolo_labels"   # 🔥 FIX HERE

TRAIN_IMG = "dataset/images/train"
VAL_IMG = "dataset/images/val"
TRAIN_LBL = "dataset/labels/train"
VAL_LBL = "dataset/labels/val"

os.makedirs(TRAIN_IMG, exist_ok=True)
os.makedirs(VAL_IMG, exist_ok=True)
os.makedirs(TRAIN_LBL, exist_ok=True)
os.makedirs(VAL_LBL, exist_ok=True)

images = [f for f in os.listdir(IMG_DIR) if f.endswith((".jpg", ".png"))]

random.shuffle(images)

split = int(0.8 * len(images))
train_files = images[:split]
val_files = images[split:]

def safe_move(src, dst):
    if os.path.exists(src):
        shutil.move(src, dst)
    else:
        print(f"⚠️ Label missing for {os.path.basename(src)} — skipped")

for f in train_files:
    base = os.path.splitext(f)[0]

    shutil.move(
        os.path.join(IMG_DIR, f),
        os.path.join(TRAIN_IMG, f)
    )

    safe_move(
        os.path.join(LBL_DIR, base + ".txt"),
        os.path.join(TRAIN_LBL, base + ".txt")
    )

for f in val_files:
    base = os.path.splitext(f)[0]

    shutil.move(
        os.path.join(IMG_DIR, f),
        os.path.join(VAL_IMG, f)
    )

    safe_move(
        os.path.join(LBL_DIR, base + ".txt"),
        os.path.join(VAL_LBL, base + ".txt")
    )

print("Dataset split completed successfully")

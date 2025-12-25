 # Face Mask Detection using YOLO (YOLO-Lite)
 An end-to-end real-time face mask detection system built using **YOLO (You Only Look Once)**.  
The system detects multiple faces in an image/video stream and classifies them as:
-  with_mask  
-  without_mask  
-  mask_weared_incorrect  

This project is suitable for **smart surveillance systems**, **public safety monitoring**, and **real-time compliance checking**.
## Project Highlights

- YOLO-Lite (YOLOv5 Nano) for fast & accurate detection
- Supports **multiple faces per image**
-  Correct bounding box placement
-  Real-time inference using OpenCV
-  Automatic evaluation using mAP & IoU
-  Ready for deployment and extension
  face-mask-yolo/
│
├── dataset/
│ ├── images/
│ │ ├── train/
│ │ └── val/
│ │
│ ├── labels/
│ │ ├── train/
│ │ └── val/
│
├── src/
│ ├── xml_to_yolo.py # Convert Pascal VOC XML → YOLO format
│ ├── split_dataset.py # Train/Validation split
│ ├── train_yolo.py # Train YOLO model
│ └── detect.py # Inference & visualization
│
├── data.yaml # YOLO dataset configuration
├── requirements.txt
├── .gitignore
└── README.md

## 🛠️ Setup & Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/face-mask-yolo.git
cd face-mask-yolo
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🔄 Dataset Preparation
Convert XML → YOLO format
bash
Copy code
python src/xml_to_yolo.py
Split dataset into train & validation
bash
Copy code
python src/split_dataset.py
🚀 Training YOLO Model
bash
Copy code
python src/train_yolo.py
Training outputs are saved inside:

bash
Copy code
runs/detect/train/
Inference & Visualization

Run detection on an image:

python src/detect.py


🧪 Technologies Used
Python

YOLOv5 (Ultralytics)

OpenCV

NumPy

PyYAML




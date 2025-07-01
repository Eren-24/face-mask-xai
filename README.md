# 😷 Face Mask Detection with Explainable AI (xAI)

🧠 **Goal:**  
Build a lightweight computer vision model to detect if a person is wearing a face mask, and explain *how* the model makes its decisions using Grad-CAM and saliency maps.

📅 **Deadline:** *20 July 2025*  
👥 **Team:** Group of 4 students (beginner project)

---

## 📌 Project Overview
- **Task:** Classify images as *masked* or *unmasked*
- **Dataset:** RMFD (Real-World Masked Face Dataset) or similar
- **Model:** Lightweight CNN or MobileNetV2
- **Explainability:** Grad-CAM and saliency maps to visualize important regions
- **Error Analysis:** Analyze incorrect predictions to understand failure cases

---

## 📂 Folder Structure
face-mask-xai/
├── data/                       
│   ├── data_loader.py              # scripts to load data (not actual data)
│   └── preprocessing.py           # optional: resize, clean, augment
│
├── notebooks/                    
│   ├── 01_data_exploration.ipynb  # dataset EDA & visualization
│   ├── 02_train_model.ipynb       # model training notebook
│   ├── 03_xai_gradcam.ipynb       # Grad-CAM / saliency maps notebook
│   └── 04_error_analysis.ipynb    # analyze misclassifications
│
├── explainability/                
│   ├── gradcam.py                 # script for Grad-CAM as reusable function
│   └── saliency.py                # optional: saliency map script
│
├── models/                        
│   └── best_model.h5              # saved trained model (DO NOT commit large files; add to .gitignore)
│
├── reports/                       
│   ├── final_report.md / .pdf     # final written report
│   └── presentation.pptx          # slides
│
├── requirements.txt               # list of Python packages
├── .gitignore                     # tells git to ignore e.g., large files, checkpoints
├── README.md                      # project description, instructions, team info
└── LICENSE                        # (optional) add license if sharing publicly

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
├── data/                  # data loader & preprocessing scripts
├── notebooks/             # Jupyter/Colab notebooks
├── explainability/        # Grad-CAM, saliency map scripts
├── models/                # trained models (do not commit large files)
├── reports/               # final report, slides
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md              # this file

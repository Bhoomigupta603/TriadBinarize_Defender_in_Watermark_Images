# 🛡️ **TriadBinarize Defender**
### **Watermark Detection & Text Binarization System**

**TriadBinarize Defender** is an end-to-end **watermark text detection and extraction prototype** that combines **YOLOv8 object detection** with **background removal and advanced binarization techniques** to enhance watermark text visibility.

This project demonstrates how **deep learning** and **classical image processing** can be integrated into a single interactive system.

---

##  **Key Features**

-  Watermark detection using **YOLOv8s**
-  Accurate **cropping of detected watermark region**
-  Background removal using **rembg**
-  **OTSU thresholding** for binary text extraction
-  **Wavelet transform binarization** (bior1.3)
-  **Streamlit-based GUI** for interactive visualization

---

##  **Project Pipeline**

Input Image  
⬇  
**YOLOv8 Watermark Detection**  
⬇  
**Cropped Watermark Region**  
⬇  
**Background Removal (rembg)**  
⬇  
**OTSU Binarization**  
⬇  
**Wavelet Transform Binarization (bior1.3)**  

---

##  Model Details

- **Model**: YOLOv8s (Ultralytics)  
- **Task**: Text Watermark Detection  
- **Dataset**: Custom watermark image dataset  
- **Image Size**: 640 × 640  
- **Epochs**: 100  

*Trained model weights (`best.pt`) are not included due to GitHub’s 100 MB file size limit.*

---

##  Project Structure

```text
TriadBinarize-Defender/
│
├── app.py # Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files & folders
│
├── models/
│ └── best.pt # Trained YOLOv8 model (not included)
│
├── training/
│ └── training_commands.txt # Training & validation commands
│
└── outputs/ # Generated outputs (ignored via .gitignore)
```

---

##  Installation & Usage

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

2️⃣ Run the Application
streamlit run app.py

Training Commands (Summary)
Training

yolo task=detect mode=train model=yolov8s.pt data=data.yaml epochs=100 imgsz=640

**Validation**
yolo task=detect mode=val model=best.pt data=data.yaml

**Results & Observations**

- YOLOv8 accurately localizes watermark text even in complex backgrounds

- rembg significantly improves text clarity before binarization

- OTSU provides fast global thresholding

- Wavelet Transform preserves fine stroke details better than OTSU

- Final outputs closely match classical watermark binarization results (2023 standard)
---


##  **Graphical User Interface (GUI)**

The project is implemented as an **interactive Streamlit web application** that allows users to:

- Upload an image
- Visualize watermark detection
- View cropped watermark text
- Compare **OTSU** and **Wavelet** binarization outputs

---

##  **Results & Output Samples**

<img width="1917" height="946" alt="watermark_GUI_img1" src="https://github.com/user-attachments/assets/9f987d37-50b2-4f73-887f-fe93abb8d58a" />

<img width="1918" height="935" alt="watermark_GUI_img2" src="https://github.com/user-attachments/assets/4c2e5205-c32f-4675-a677-aca4d8a8871e" />

<img width="1216" height="915" alt="watermark_GUI_img3" src="https://github.com/user-attachments/assets/ee23b756-ead4-4f2b-a2ad-cd5f7b102539" />

<img width="1216" height="915" alt="watermark_GUI_img4" src="https://github.com/user-attachments/assets/b8c439bc-aa90-42d1-b401-06c20d50351c" />

>  *Output quality may vary depending on watermark transparency, font thickness, and background complexity.*

---
**Technologies Used**

- Python

- YOLOv8 (Ultralytics)

- OpenCV

- rembg

- PyWavelets

- Streamlit

- NumPy

---

**Use Cases** 

- Digital watermark analysis

- Copyright & ownership verification

- Image forensics

- Document security research

- Academic and research demonstrations

---

**Author**

Bhoomi Gupta
MCA (AI/ML) Student
Email: bhoomigupta603@gmail.com

GitHub: https://github.com/Bhoomigupta603
---

**Acknowledgements**

- Ultralytics YOLOv8

- OpenCV Community

- rembg Contributors

- PyWavelets Library

⭐ If you find this project useful, feel free to star the repository!




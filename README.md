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

##  **Project Structure**

```text
TriadBinarize-Defender/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── best.pt   (not included due to size limit)
│
├── training/
│   └── training_commands.txt
│
└── outputs/   (ignored via .gitignore)

##  **Installation & Usage**

pip install -r requirements.txt
streamlit run app.py

Model Training (Summary)

Model: YOLOv8s (Ultralytics)

Dataset: Custom watermark image dataset

Training performed using YOLOv8 detection pipeline

Final trained weights: best.pt

 Due to GitHub file size limits, trained model weights are not included in this repository.

 Pretrained Model Download

Download the trained YOLOv8 model from the link below and place it inside the models/ folder:

models/best.pt


## Project Status

This project is a research and academic prototype.

Designed to demonstrate pipeline integration

Not intended for production deployment

Suitable for major projects, internships, and research demos

## Author

Bhoomi Gupta
MCA (AI/ML)
Major Project – Image Processing & Deep Learning

## License

This project is shared for educational and research purposes only.


---


# 🛡️ TriadBinarize Defender

**TriadBinarize Defender** is a prototype system for detecting and extracting **text-based watermarks** from images using **YOLOv8 object detection** and **advanced binarization techniques**.

This project demonstrates how deep learning and classical image processing can be combined to analyze watermark patterns.

---

## Features

- YOLOv8-based watermark detection
- Precise watermark region cropping
- Background removal using rembg
- OTSU binarization
- Wavelet-based binarization
- Interactive Streamlit GUI

---

## Project Pipeline

```md

Input Image  
⬇  
YOLOv8 Watermark Detection  
⬇  
Cropped Watermark Region  
⬇  
Background Removal (rembg)  
⬇  
OTSU Binarization  
⬇  
Wavelet Transform Binarization (bior1.3)

---

## **Project Structure**

```text
TriadBinarize-Defender/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── models/
│   └── best.pt
│
├── uploads/
│
├── outputs/
│   ├── detected/
│   ├── bg_removed/
│   ├── otsu/
│   └── wavelet/
│
├── training/
    └── training_commands.txt
  
---

## Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/TriadBinarize-Defender.git
cd TriadBinarize-Defender
2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Application
streamlit run app.py

Sample Results
Stage	Output
Original Image	✔️
YOLO Detection	✔️
Background Removed	✔️
OTSU Binarization	✔️
Wavelet Binarization	✔️

(See sample_images/ folder)

**Project Status**

This project is a research prototype.

Output quality may vary depending on:

watermark transparency

font thickness

background complexity

The goal is to demonstrate feasibility, not production-level perfection.

Future Enhancements

Text-aware segmentation models

Morphological post-processing

OCR-based watermark reconstruction

Improved alpha-matting techniques

**Author**

Bhoomi Gupta
MCA (AI/ML)
Major Project – Image Processing & Deep Learning

**License**

This project is for academic and research purposes only.


---

## **Model Training**
The YOLOv8 watermark detection model was trained on a custom dataset.

Training details and commands are available here:
`training_commands.txt`

# WatermarkText_Binarization_project
This project combines multiple techniques to detect, remove background, and binarize watermark text from images. It utilizes YOLOv8 for watermark text detection, followed by background removal using image processing techniques, and finally, text binarization using OTSU and wavelet transform methods.

Features
Watermark Text Detection: Utilizes YOLOv8 to accurately detect watermark text in images.
Background Removal: Removes the background from the detected watermark text region to isolate it.
Text Binarization: Applies OTSU and wavelet transform techniques to binarize the watermark text, enhancing its visibility and usability.


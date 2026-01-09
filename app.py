import streamlit as st
import cv2
import numpy as np
import os
from ultralytics import YOLO
from PIL import Image
from rembg import remove
import pywt

# ---------------- CONFIG ----------------
st.set_page_config(page_title="TriadBinarize Defender", layout="wide")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

model = YOLO("models/best.pt")

# ---------------- FUNCTIONS ----------------

def get_largest_box(boxes):
    areas = []
    for b in boxes:
        x1, y1, x2, y2 = map(int, b.xyxy[0])
        areas.append((x2 - x1) * (y2 - y1))
    return boxes[np.argmax(areas)]

def crop_from_original(original, box):
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    return original[y1:y2, x1:x2]

def rembg_remove_background(cropped_bgr):
    rgb = cv2.cvtColor(cropped_bgr, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb)
    removed = remove(pil_img)
    removed = removed.convert("RGB")
    return cv2.cvtColor(np.array(removed), cv2.COLOR_RGB2GRAY)

def otsu_binarization(gray):
    _, binary = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    return binary

def wavelet_binarization(gray):
    coeffs = pywt.dwt2(gray, 'bior1.3')
    cA, (cH, cV, cD) = coeffs

    threshold = 30
    cA = pywt.threshold(cA, threshold, mode='soft')
    cH = pywt.threshold(cH, threshold, mode='soft')
    cV = pywt.threshold(cV, threshold, mode='soft')
    cD = pywt.threshold(cD, threshold, mode='soft')

    reconstructed = pywt.idwt2((cA, (cH, cV, cD)), 'bior1.3')
    reconstructed = np.clip(reconstructed, 0, 255).astype(np.uint8)

    _, binary = cv2.threshold(reconstructed, 128, 255, cv2.THRESH_BINARY)
    return binary

# ---------------- UI ----------------

st.title("🛡️ TriadBinarize Defender")
st.subheader("YOLO → rembg → OTSU & Wavelet (End-to-End Pipeline)")

uploaded = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
run = st.button("▶ Run Detection")

if uploaded and run:

    img_path = os.path.join(UPLOAD_DIR, uploaded.name)
    with open(img_path, "wb") as f:
        f.write(uploaded.read())

    original = cv2.imread(img_path)

    # -------- YOLO DETECTION (NO PLOT USED) --------
    results = model(img_path, conf=0.25)
    boxes = results[0].boxes

    if boxes is None or len(boxes) == 0:
        st.error("❌ No watermark detected")
        st.stop()

    best_box = get_largest_box(boxes)

    # -------- CROP FROM ORIGINAL IMAGE --------
    cropped = crop_from_original(original, best_box)

    # -------- BACKGROUND REMOVAL (CLEAN) --------
    gray_extracted = rembg_remove_background(cropped)

    # -------- BINARIZATION --------
    otsu_img = otsu_binarization(gray_extracted)
    wavelet_img = wavelet_binarization(gray_extracted)

    # -------- DISPLAY --------
    st.markdown("## Results")

    c1, c2, c3 = st.columns(3)
    c4, c5 = st.columns(2)

    c1.image(Image.open(img_path),
             caption="Original Image",
             use_container_width=True)

    c2.image(results[0].plot(),
             caption="YOLO Detection (Visualization)",
             use_container_width=True)

    c3.image(cropped,
             caption="YOLO Cropped Watermark (Clean)",
             use_container_width=True)

    c4.image(otsu_img,
             caption="OTSU Binarization",
             use_container_width=True)

    c5.image(wavelet_img,
             caption="Wavelet Binarization (bior1.3)",
             use_container_width=True)

    st.success("Watermark text successfully extracted and binarized")

else:
    st.info("Upload an image and click Run Detection")
 
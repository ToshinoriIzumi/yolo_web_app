import cv2
import os
import streamlit as st
from ultralytics import YOLO

TMP_DIR_PATH = "/opt/app/tmp"
MODEL_DIR_PATH = "/opt/app/src/models"
if not os.path.exists(TMP_DIR_PATH):
    os.makedirs(TMP_DIR_PATH)

st.title("Yolo WEB App")

img_file = st.file_uploader("Upload an image",
                            type=["png", "jpg", "jpeg"])

if img_file is not None:
    file_path = os.path.join(TMP_DIR_PATH, img_file.name)
    with open(file_path, "wb") as f:
        f.write(img_file.getvalue())
    analysis_img_path = os.path.join(TMP_DIR_PATH,
                                     f"analysis_{img_file.name}")

    model = YOLO(os.path.join(MODEL_DIR_PATH, "yolov8n.pt"))
    results = model.predict(file_path, save=True)
    img = cv2.imread(file_path)
    for point in results[0].boxes.xyxy:
        cv2.rectangle(img,
                      (int(point[0]), int(point[1])),
                      (int(point[2]), int(point[3])),
                      (0, 0, 255),
                      thickness=5)
    cv2.imwrite(analysis_img_path, img)
    st.image(analysis_img_path,
             caption="Uploaded Image.",
             use_column_width=True)

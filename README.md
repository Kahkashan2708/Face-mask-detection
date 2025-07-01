# Face Mask Detection 🛡️😷

This project focuses on building a **Face Mask Detection** system using image classification. The model is trained on a dataset of images containing people with and without face masks and can distinguish between the two classes effectively.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Kahkashan2708/Face-mask-detection/blob/main/Face_mask_detection.ipynb)

---

## 📁 Dataset

- **Source**: [Kaggle - Face Mask Dataset](https://www.kaggle.com/datasets/omkargurav/face-mask-dataset)
- **Classes**: 
  - `with_mask` → Label 1
  - `without_mask` → Label 0
- **Preprocessing**:
  - Resized all images to 128×128 pixels
  - Converted images to RGB format
  - Converted to NumPy arrays and normalized

---

## 🧠 Model Overview

- Used a **Convolutional Neural Network (CNN)** for classification.
- Built using **TensorFlow/Keras**.
- Architecture includes:
  - Multiple Conv2D and MaxPooling2D layers
  - Flatten → Dense → Dropout
  - Final Dense layer with sigmoid activation (binary classification)

---

## 🧪 Training & Evaluation

- Data split into **80% training** and **20% testing**
- Loss Function: `binary_crossentropy`
- Optimizer: `adam`
- Evaluation Metrics: `accuracy`

---

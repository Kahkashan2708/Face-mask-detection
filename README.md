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
## 📊 Results

- Achieved strong accuracy on the test set
- Confusion Matrix and Accuracy Curve were plotted for performance visualization

---


## 📈 Model Performance

The model was trained for **10 epochs** and achieved the following results:

| Epoch | Train Accuracy | Train Loss | Val Accuracy | Val Loss |
|-------|----------------|------------|--------------|----------|
| 1     | 68.99%         | 0.6699     | 86.94%       | 0.2853   |
| 2     | 87.85%         | 0.3130     | 89.26%       | 0.2304   |
| 3     | 89.32%         | 0.2649     | 91.24%       | 0.2206   |
| 4     | 92.54%         | 0.1740     | 90.25%       | 0.2397   |
| 5     | 93.77%         | 0.1699     | 91.07%       | 0.1953   |
| 6     | 93.95%         | 0.1597     | 92.23%       | 0.1996   |


✨ **Peak validation accuracy**: **92.23%*  

---


## 🛠️ Requirements

- Python
- NumPy
- Matplotlib
- OpenCV
- PIL
- TensorFlow / Keras
- scikit-learn
- Kaggle API

Install dependencies in Colab:
```bash
!pip install kaggle

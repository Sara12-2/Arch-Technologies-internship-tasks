# 🧠 ML Projects — Arch Technologies Internship

This repository contains two interactive machine learning applications built during the **Arch Technologies Internship**:

---

## 📧 Project 1: Email/SMS Spam Classifier

> A real-time classifier that detects whether a message is **SPAM** or **NOT SPAM**, using traditional ML techniques.

### 🚀 Overview

This project demonstrates how to build and deploy a **spam detection system** using machine learning and natural language processing (NLP). The model is trained on the [UCI SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection), and the user interface is built using **Streamlit**.

### 🧠 How It Works

1. 🧹 **Preprocessing**  
   Text messages are cleaned and vectorized using **TF-IDF** to transform text into numerical features.

2. 🤖 **Model**  
   A **Multinomial Naive Bayes** classifier is trained on thousands of labeled SMS messages.

3. 🖥️ **Web App**  
   Users enter a message, click "Check Spam", and get instant feedback with visual labels.

### 💻 Tech Stack

| Tool           | Description                                 |
|----------------|---------------------------------------------|
| `Python`       | Core programming language                   |
| `scikit-learn` | For training the spam detection model       |
| `Streamlit`    | Interactive web interface                   |
| `Joblib`       | To save/load the ML model                   |
| `UCI Dataset`  | Public dataset with spam/ham labels         |

### ✉️ Example Predictions

| Message                                               | Prediction  |
|-------------------------------------------------------|-------------|
| "Congratulations! You’ve won a free cruise!"          | 🚨 SPAM     |
| "Hi, are you free this weekend to catch up?"          | ✅ NOT SPAM |
| "Urgent! Your account is at risk. Click the link now" | 🚨 SPAM     |
| "Reminder: Your appointment is at 4:30 PM tomorrow."  | ✅ NOT SPAM |

---

## 🔢 Project 2: Handwritten Digit Classifier (CNN-based)

> A real-time digit recognition system using **Convolutional Neural Networks** trained on the MNIST dataset.

### 🚀 Overview

This project uses deep learning to classify handwritten digits (0–9) from images. It is trained on the **MNIST** dataset and deployed via **Streamlit** with an interactive UI that lets users draw a digit or upload an image for prediction.

### 🧠 How It Works

1. 🖼️ **Image Input**  
   Users can draw a digit on the canvas or upload a 28x28 pixel grayscale image.

2. 🔄 **Preprocessing**  
   The image is reshaped and normalized before being fed to the model.

3. 🧠 **Model Architecture**  
   A CNN with multiple layers:
   - Conv2D + ReLU + MaxPooling
   - Dense (Fully Connected)
   - Softmax output layer for 10-class classification

4. ⚡ **Prediction**  
   The model predicts the digit with high accuracy, and displays the result instantly.

### 💻 Tech Stack

| Tool            | Description                              |
|-----------------|------------------------------------------|
| `Python`        | Core programming language                |
| `TensorFlow/Keras` | For building and training the CNN    |
| `Streamlit`     | User-friendly web app interface          |
| `NumPy` | For image handling and preprocessing     |
| `MNIST`         | Benchmark dataset for handwritten digits |

### 🔍 Example Predictions

| Input Image        | Predicted Digit |
|--------------------|-----------------|
| (Drawn "5")        | 5 ✅             |
| (Uploaded "3.png") | 3 ✅             |

---

> ✅ **Both projects are deployable and fully interactive**, showcasing skills in both classical ML and deep learning.


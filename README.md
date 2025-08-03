# 📧 Email/SMS Spam Classifier

A simple and interactive machine learning web app that detects whether a given email or SMS message is **Spam** or **Not Spam** using a trained model — built during my internship at **Arch Technologies**.

## 🚀 Project Overview

This application allows users to paste or type a message, and it will instantly classify it using a **machine learning model** trained on the [UCI SMS Spam Collection dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection).

It was built using:
- **Python**
- **scikit-learn** for training the model
- **Streamlit** for deploying the user-friendly web interface

---

## 🧠 How It Works

1. **Data Preprocessing**  
   Text data is cleaned and transformed using `TfidfVectorizer`.

2. **Model Training**  
   A classification model (like Naive Bayes or Logistic Regression) is trained on spam vs non-spam data.

3. **Web Interface**  
   A user can input any message via the text box, and with one click, get a spam prediction instantly.


## 💻 Technologies Used

| Tool/Library      | Purpose                       |
|-------------------|-------------------------------|
| Python            | Programming language          |
| Streamlit         | Web interface (GUI)           |
| scikit-learn      | ML model & preprocessing      |
| Joblib            | Saving/loading model          |
| UCI Dataset       | Spam/ham labeled data         |





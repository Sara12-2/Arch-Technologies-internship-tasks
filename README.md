# 📧 Email/SMS Spam Classifier

> **Internship Task — Arch Technologies**

An interactive machine learning web app that classifies a given email or SMS message as **SPAM** or **NOT SPAM** in real-time — built with 💙 using Python, Streamlit, and scikit-learn.

---

## 🚀 Project Overview

This project demonstrates how to build and deploy a **spam detection system** using machine learning and natural language processing (NLP). The model is trained on the well-known [UCI SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection), and the user interface is built with **Streamlit** for simplicity and speed.

---

## 🧠 How It Works

📌 **Step-by-step Process:**

1. 🧹 **Preprocessing**  
   Input text is cleaned and transformed using **TF-IDF Vectorization** to convert it into a numerical form.

2. 🧠 **Model Training**  
   A machine learning model (e.g., **Multinomial Naive Bayes**) is trained on thousands of spam and ham messages.

3. 💻 **Web Interface**  
   The user enters a message → clicks the **Check Spam** button → gets an instant prediction with visual feedback.

---

## 💻 Tech Stack

| 🔧 Tool           | 🧾 Description                                  |
|------------------|------------------------------------------------|
| `Python`         | Core language used for development             |
| `scikit-learn`   | Machine learning library for model training    |
| `Streamlit`      | Web-based GUI framework                        |
| `Joblib`         | For saving and loading the trained model       |
| `UCI Dataset`    | Public dataset with labeled spam/ham messages  |

---

## ✉️ Sample Message Predictions

| Message                                               | Prediction  |
|-------------------------------------------------------|-------------|
| "Congratulations! You’ve won a free cruise!"          | 🚨 SPAM     |
| "Hi, are you free this weekend to catch up?"          | ✅ NOT SPAM |
| "Urgent! Your account is at risk. Click the link now" | 🚨 SPAM     |
| "Reminder: Your appointment is at 4:30 PM tomorrow."  | ✅ NOT SPAM |

---


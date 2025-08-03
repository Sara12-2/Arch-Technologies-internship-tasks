📧 Email/SMS Spam Classifier
An interactive and lightweight machine learning web application that classifies any given email or SMS message as SPAM or NOT SPAM in real time.

📍 Developed during my internship at Arch Technologies.

🚀 Project Overview
This project showcases how machine learning can be effectively used to filter out spam content from messages using natural language processing techniques. It provides a clean and responsive web-based interface for end users to interact with the model.

🧾 The model is trained on the popular UCI SMS Spam Collection dataset, which contains 5,574 real-world labeled messages.

✨ Key Features
Real-time spam prediction via a simple text input

User-friendly interface built with Streamlit

Fast predictions with a pre-trained ML model

Lightweight, portable, and easy to use

🧠 How It Works
Text Preprocessing
Input text is vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) to convert messages into numerical format.

Model Training
A classifier (such as Multinomial Naive Bayes or Logistic Regression) is trained to distinguish between spam and ham messages.

Prediction
The trained model predicts whether the input is spam based on its learned patterns.

Streamlit UI
The app provides an instant classification result (with emoji-based feedback) once the message is submitted.

💻 Tech Stack
Tool/Library	Description
Python	Core programming language
scikit-learn	Machine learning model + preprocessing
Streamlit	Frontend web interface
Joblib	Model saving/loading utility
UCI Dataset	Real-world SMS spam dataset

🧪 Sample Predictions
Sample Message	Prediction
“Congratulations! You've won a free iPhone!”	SPAM
“Hey, are we still on for the meeting tomorrow?”	NOT SPAM
“You've been selected for a cash reward! Click now”	SPAM
“Don’t forget to pick up groceries on your way!”	NOT SPAM

🔧 Installation & Usage
📦 Install Dependencies
bash
Copy
Edit
pip install streamlit scikit-learn joblib
▶️ Run the App
bash
Copy
Edit
streamlit run streamlit_app.py
🙌 Acknowledgements
This project was completed as part of my internship at Arch Technologies.
It helped me ato enhance my skills.

✍️ Author
[sara manzoor]
Machine learning Intern


# save this as train_model.py and run it once to create the model file

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load the dataset (UCI SMS Spam Collection format)
df = pd.read_csv("SMSSpamCollection", sep="\t", header=None, names=["label", "message"])

# Convert labels: 'ham' → 0, 'spam' → 1
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})

# Split the data
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label_num'], test_size=0.2, random_state=42)

# Create a pipeline: vectorizer + Naive Bayes classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, "spam_classifier.pkl")

print("Model trained and saved successfully.")

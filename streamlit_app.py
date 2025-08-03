import streamlit as st
import joblib

# Load trained model
model = joblib.load("spam_classifier.pkl")

# Page setup
st.set_page_config(page_title="Spam Classifier", page_icon="📧")

# Title and description
st.title("📧 Email/SMS Spam Classifier")
st.write("Paste or write your message below to check whether it's spam or not.")

# Text input area
message = st.text_area("✉️ Enter your message:")

# Single prediction button
if st.button("✅ Check Spam"):
    if message.strip():
        prediction = model.predict([message])[0]
        if prediction == 1:
            st.error("❌ This message is **SPAM**.")
        else:
            st.success("✅ This message is **NOT SPAM**.")
    else:
        st.warning("⚠️ Please enter a message.")

# -----------------------
# ✅ Polished Footer
# -----------------------
st.markdown("---")  # Horizontal line

st.markdown(
    """
    ### 🙌 Thank You for Using the Spam Classifier App!

    - 🔍 Built with **Python + Streamlit**
    - 📦 Model trained using **Scikit-learn**
    - 💻 Developed during internship at **Arch Technologies**
    
    > *This tool helps classify messages as SPAM or NOT SPAM using machine learning.*
    """
)

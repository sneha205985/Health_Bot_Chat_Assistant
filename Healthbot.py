import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")


# Fixed top-left red title 
st.markdown(
    """
    <style>
        .top-left {
            position: fixed;
            top: 15px;
            left: 15px;
            font-size: 40px;
            font-weight: bold;
            color: red;
            font-family: Arial;
            z-index: 9999;
        }
    </style>
    <div class="top-left">HealthBot Chat Assistant</div>
    """,
    unsafe_allow_html=True
)

# Center-aligned welcome and intro
st.markdown(
    """
    <div style='text-align: center;'>
        <div style='font-size: 37px; font-weight: bold; font-family: Arial; margin-top: 60px;'>
            WELCOME! HOPE YOU ARE DOING WELL.
        </div>
        <p style='font-size: 16px; font-family: Arial; margin-top: 20px;'>
            This HealthBot will help you identify diseases based on symptoms.<br>
            Just enter your symptoms below, and then ask health-related follow-up questions.<br><br>
            <strong>Note:</strong> This is for informational use only. Always consult a real doctor.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Session state setup ---
if "symptoms" not in st.session_state:
    st.session_state.symptoms = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Step 1: Enter Patient Symptoms ---
with st.expander("📝 Enter Patient's Symptoms"):
    symptoms_input = st.text_input("Example: fever, sore throat, fatigue", key="symptom_input")
    if st.button("Submit Symptoms"):
        if symptoms_input.strip() != "":
            st.session_state.symptoms = symptoms_input.strip()
            st.success("Symptoms submitted successfully.")
        else:
            st.warning("Please enter some symptoms.")

# Show message to proceed
if st.session_state.symptoms:
    st.markdown("**✅ Symptoms received. Now you can ask your health-related question below:**")
else:
    st.warning("⚠️ Please enter patient’s symptoms to begin diagnosis.")

# --- Step 2: Follow-up Chat Input ---
user_query = st.chat_input("Ask your health-related question...")

# --- Step 3: Handle Input & Response ---
if user_query:
    if st.session_state.symptoms == "":
        bot_reply = "⚠️ Please enter the patient's symptoms first."
    else:
        # Prepare structured context prompt
        context = f"""
You are a medical assistant AI that analyzes symptoms and suggests possible diseases.

Symptoms: {st.session_state.symptoms}
User question: {user_query}

Please reply in the following structured format:
**Possible Disease**: ...
**Likely Symptoms**: ...
**Cause**: ...
**Suggested Remedies**: ...
**Doctor Consultation Advice**: ...

Avoid giving prescriptions or dosage instructions. Keep it informative and friendly.
"""
        response = model.generate_content(context)
        bot_reply = response.text

    # Save to history
    st.session_state.chat_history.append(("user", user_query))
    st.session_state.chat_history.append(("assistant", bot_reply))

# --- Display Chat History ---
for role, message in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").markdown(message)

# --- Reset Button ---
if st.button("🔄 Reset Conversation"):
    st.session_state.symptoms = ""
    st.session_state.chat_history = []
    st.success("Chat reset successfully.")

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from typing import Optional

# Page configuration
st.set_page_config(
    page_title="HealthBot Chat Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load API key from .env file
load_dotenv()
# Support both GOOGLE_API_KEY and GEMINI_API_KEY for flexibility
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

# Initialize Gemini model with error handling
model = None
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash")
    except Exception as e:
        st.error(f"Error initializing AI model: {str(e)}")
        model = None
else:
    st.error("⚠️ API key not found. Please set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file or environment variables.")

# Custom CSS styling
st.markdown(
    """
    <style>
        .top-left {
            position: fixed;
            top: 15px;
            left: 15px;
            font-size: 18px;
            font-weight: bold;
            color: #FF4444;
            font-family: Arial, sans-serif;
            z-index: 9999;
            background-color: rgba(255, 255, 255, 0.9);
            padding: 8px 12px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .main-header {
            text-align: center;
            font-size: 37px;
            font-weight: bold;
            font-family: Arial, sans-serif;
            margin-top: 60px;
            color: #2C3E50;
        }
        .intro-text {
            font-size: 16px;
            font-family: Arial, sans-serif;
            margin-top: 20px;
            color: #34495E;
            line-height: 1.6;
        }
        .disclaimer {
            background-color: #FFF3CD;
            border-left: 4px solid #FFC107;
            padding: 12px;
            margin: 20px 0;
            border-radius: 4px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 5px;
        }
    </style>
    <div class="top-left">🏥 HealthBot Chat Assistant</div>
    """,
    unsafe_allow_html=True
)

# Center-aligned welcome and intro
st.markdown(
    """
    <div style='text-align: center;'>
        <div class="main-header">
            WELCOME! HOPE YOU ARE DOING WELL.
        </div>
        <div class="intro-text">
            This HealthBot will help you identify diseases based on symptoms.<br>
            Just enter your symptoms below, and then ask health-related follow-up questions.<br><br>
        </div>
        <div class="disclaimer">
            <strong>⚠️ Important Disclaimer:</strong> This is for informational use only. 
            Always consult a qualified medical professional for proper diagnosis and treatment.
        </div>
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
st.markdown("---")
with st.expander("📝 Enter Patient's Symptoms", expanded=not st.session_state.symptoms):
    symptoms_input = st.text_input(
        "Enter symptoms (e.g., fever, sore throat, fatigue, headache)",
        key="symptom_input",
        value=st.session_state.symptoms if st.session_state.symptoms else "",
        placeholder="Example: fever, sore throat, fatigue"
    )
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("✅ Submit Symptoms", type="primary"):
            if symptoms_input.strip():
                st.session_state.symptoms = symptoms_input.strip()
                st.success("✅ Symptoms submitted successfully!")
                st.rerun()
            else:
                st.warning("⚠️ Please enter some symptoms.")
    with col2:
        if st.session_state.symptoms and st.button("🔄 Clear Symptoms"):
            st.session_state.symptoms = ""
            st.session_state.chat_history = []
            st.success("Symptoms cleared. You can enter new symptoms.")
            st.rerun()

# Show message to proceed
st.markdown("---")
if st.session_state.symptoms:
    st.info(f"✅ **Symptoms received:** {st.session_state.symptoms}\n\n**You can now ask your health-related questions below:**")
else:
    st.warning("⚠️ Please enter patient's symptoms above to begin diagnosis.")

# --- Step 2: Follow-up Chat Input ---
if model:  # Only show chat input if model is initialized
    user_query = st.chat_input("Ask your health-related question...")
    
    # === Step 3: Handle Input & Response ===
    if user_query:
        if not st.session_state.symptoms:
            bot_reply = "⚠️ Please enter the patient's symptoms first using the form above."
            st.session_state.chat_history.append(("user", user_query))
            st.session_state.chat_history.append(("assistant", bot_reply))
        else:
            # Show loading indicator
            with st.spinner("🤔 Analyzing your query..."):
                try:
                    user_query_lower = user_query.lower()
                    prompt = ""
                    
                    # Determine prompt based on query type
                    if "disease" in user_query_lower and not any(w in user_query_lower for w in ["cure", "remedy", "treatment"]):
                        prompt = f"""You are a professional medical assistant. Based on the symptoms below, ONLY predict the most likely disease(s) or condition(s).
DO NOT include causes, remedies, treatments, or any other information. Be concise and professional.

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide a clear, professional response about the possible disease(s)."""
                    
                    elif any(w in user_query_lower for w in ["cure", "remedy", "treatment"]):
                        prompt = f"""You are a professional medical assistant. Based on the symptoms below, ONLY provide remedies, treatments, or cures.
DO NOT mention disease names unless asked. Always remind the user to consult a doctor for serious conditions.

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide helpful treatment suggestions while emphasizing the importance of professional medical consultation."""
                    
                    elif "symptom" in user_query_lower:
                        prompt = f"""You are a professional medical assistant. Based on the symptoms below, ONLY explain the likely symptoms or how they relate to each other.
DO NOT include disease name, remedies, or causes.

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide a clear explanation of the symptoms."""
                    
                    elif "cause" in user_query_lower:
                        prompt = f"""You are a professional medical assistant. Based on the symptoms below, ONLY describe the possible causes of the condition.
DO NOT include symptoms, disease name, or remedies.

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide information about potential causes."""
                    
                    elif "doctor" in user_query_lower or "consult" in user_query_lower:
                        prompt = f"""You are a professional medical assistant. Based on the symptoms below, provide doctor consultation advice.
Explain when it's important to see a doctor and what type of specialist might be appropriate.

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide professional consultation advice."""
                    
                    elif "prevention" in user_query_lower:
                        prompt = f"""You are a professional medical assistant. Based on the symptoms below, ONLY suggest general prevention tips related to the suspected condition.
Do NOT include disease names or specific medications.

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide helpful prevention tips."""
                    
                    elif any(w in user_query_lower for w in ["diet", "nutrition", "food"]):
                        prompt = f"""You are a professional medical assistant. Based on the symptoms below, ONLY suggest healthy diet and nutritional habits 
that may help the user stay fit or recover better. Avoid giving any medicine names or diagnosis.

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide dietary and nutritional advice."""
                    
                    elif "medicine" in user_query_lower or "medication" in user_query_lower or "drug" in user_query_lower:
                        prompt = f"""You are a professional medical assistant. Based on the symptoms below, provide some basic over-the-counter medications 
that are commonly used, but ALWAYS include a strong warning: "**⚠️ IMPORTANT: If symptoms persist or worsen, consult a doctor immediately. Do not self-medicate for serious conditions.**"

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide medication information with appropriate warnings."""
                    
                    else:
                        prompt = f"""You are a professional medical assistant. Help the user based on the symptoms and their query.
Always remind them that this is for informational purposes only and they should consult a doctor for proper diagnosis.

Symptoms: {st.session_state.symptoms}
User Question: {user_query}

Provide a helpful, professional response."""
                    
                    # Generate response
                    response = model.generate_content(prompt)
                    bot_reply = response.text
                    
                    # Save to history
                    st.session_state.chat_history.append(("user", user_query))
                    st.session_state.chat_history.append(("assistant", bot_reply))
                    
                except Exception as e:
                    error_msg = f"❌ Error generating response: {str(e)}\n\nPlease try again or check your API key."
                    st.error(error_msg)
                    st.session_state.chat_history.append(("user", user_query))
                    st.session_state.chat_history.append(("assistant", error_msg))
    
    # --- Display Chat History ---
    if st.session_state.chat_history:
        st.markdown("### 💬 Conversation History")
        for role, message in st.session_state.chat_history:
            if role == "user":
                with st.chat_message("user"):
                    st.write(message)
            else:
                with st.chat_message("assistant"):
                    st.markdown(message)
    
    # --- Reset Button ---
    st.markdown("---")
    if st.button("🔄 Reset Conversation", type="secondary"):
        st.session_state.symptoms = ""
        st.session_state.chat_history = []
        st.success("✅ Chat reset successfully. You can enter new symptoms.")
        st.rerun()
else:
    st.error("**Cannot proceed:** AI model is not initialized. Please check your API key configuration.")
    st.info("""
    **To fix this:**
    1. Create a `.env` file in the project root
    2. Add your Google API key: `GEMINI_API_KEY=your_key_here` or `GOOGLE_API_KEY=your_key_here`
    3. Or set it as an environment variable
    4. Restart the Streamlit app
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #7F8C8D; font-size: 12px; padding: 20px;'>
        <p>HealthBot Chat Assistant | Built with Streamlit & Google Gemini AI</p>
        <p><strong>Remember:</strong> This tool is for informational purposes only. Always consult a qualified healthcare professional.</p>
    </div>
    """,
    unsafe_allow_html=True
)

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

# Load API key - try Streamlit secrets first (for Cloud), then .env file
api_key = None

# Try Streamlit secrets first (for deployed apps)
try:
    if hasattr(st, "secrets"):
        # Try direct access first
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
        except KeyError:
            try:
                api_key = st.secrets["GOOGLE_API_KEY"]
            except KeyError:
                pass
        
        # Also check if it's nested under [general] section
        if not api_key:
            try:
                api_key = st.secrets["general"]["GEMINI_API_KEY"]
            except (KeyError, TypeError):
                try:
                    api_key = st.secrets["general"]["GOOGLE_API_KEY"]
                except (KeyError, TypeError):
                    pass
except Exception:
    pass

# If not in secrets, try .env file
if not api_key:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

# Strip quotes and whitespace from API key if present (TOML format includes quotes)
if api_key:
    api_key = str(api_key).strip().strip('"').strip("'")

# Initialize Gemini model with error handling
model = None
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Try model names in order of preference (most compatible first)
        # Note: "gemini-pro" is the most widely available model
        model_names = ["gemini-pro", "gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.0-pro"]
        model = None
        last_error = None
        
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                # Try a simple test to verify the model works
                test_response = model.generate_content("test")
                # If we get here, the model works
                break
            except Exception as e:
                last_error = str(e)
                model = None
                continue
        
        if model is None:
            raise Exception(f"Could not initialize any Gemini model. Last error: {last_error}. Please check your API key and model availability.")
    except Exception as e:
        st.error(f"Error initializing AI model: {str(e)}")
        model = None
else:
    st.error("⚠️ API key not found. Please set GEMINI_API_KEY or GOOGLE_API_KEY in Streamlit Cloud Secrets or .env file.")

# Custom CSS styling for better visibility
st.markdown(
    """
    <style>
        /* Main container background */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Top left badge */
        .top-left {
            position: fixed;
            top: 15px;
            left: 15px;
            font-size: 18px;
            font-weight: bold;
            color: #FFFFFF;
            background: linear-gradient(135deg, #FF6B6B 0%, #EE5A6F 100%);
            font-family: Arial, sans-serif;
            z-index: 9999;
            padding: 10px 16px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        
        /* Main header - bright and visible */
        .main-header {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            font-family: 'Segoe UI', Arial, sans-serif;
            margin-top: 60px;
            margin-bottom: 20px;
            color: #FFFFFF;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
        }
        
        /* Intro text - high contrast */
        .intro-text {
            font-size: 18px;
            font-family: 'Segoe UI', Arial, sans-serif;
            margin-top: 20px;
            margin-bottom: 20px;
            color: #E0E0E0;
            line-height: 1.8;
            text-align: center;
        }
        
        /* Disclaimer box - bright and attention-grabbing */
        .disclaimer {
            background: linear-gradient(135deg, #FFD93D 0%, #FFB347 100%);
            border-left: 5px solid #FF6B00;
            padding: 16px 20px;
            margin: 25px auto;
            border-radius: 8px;
            max-width: 800px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            color: #1A1A1A;
            font-weight: 500;
        }
        
        .disclaimer strong {
            color: #D32F2F;
            font-size: 1.1em;
        }
        
        /* Buttons */
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        /* Text inputs */
        .stTextInput>div>div>input {
            background-color: #262730;
            color: #FAFAFA;
            border: 2px solid #3A3F4B;
        }
        
        .stTextInput>div>div>input:focus {
            border-color: #FF6B6B;
        }
        
        /* Chat messages */
        .stChatMessage {
            background-color: #1E1E2E;
        }
        
        /* Info and warning boxes */
        .stInfo {
            background-color: #1E3A5F;
            border-left: 4px solid #4A90E2;
            color: #E3F2FD;
        }
        
        .stWarning {
            background-color: #5D4037;
            border-left: 4px solid #FF9800;
            color: #FFF3E0;
        }
        
        .stSuccess {
            background-color: #1B5E20;
            border-left: 4px solid #4CAF50;
            color: #E8F5E9;
        }
        
        .stError {
            background-color: #B71C1C;
            border-left: 4px solid #F44336;
            color: #FFEBEE;
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            background-color: #262730;
            color: #FAFAFA;
            font-weight: 600;
        }
        
        /* Markdown text */
        .stMarkdown {
            color: #FAFAFA;
        }
        
        /* Footer */
        .footer-text {
            color: #B0B0B0 !important;
            font-size: 13px;
        }
        
        /* Improve overall text visibility */
        p, li, div {
            color: #E0E0E0;
        }
        
        h1, h2, h3 {
            color: #FFFFFF;
        }
        
        /* Code blocks */
        code {
            background-color: #1E1E2E;
            color: #A8E6CF;
            padding: 2px 6px;
            border-radius: 4px;
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
                    try:
                        response = model.generate_content(prompt)
                        bot_reply = response.text
                    except Exception as gen_error:
                        # If model fails, try to reinitialize with a different model
                        error_str = str(gen_error)
                        if "404" in error_str or "not found" in error_str.lower():
                            # Try to use gemini-pro as fallback
                            try:
                                fallback_model = genai.GenerativeModel("gemini-pro")
                                response = fallback_model.generate_content(prompt)
                                bot_reply = response.text
                            except:
                                raise gen_error
                        else:
                            raise gen_error
                    
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
    <div class="footer-text" style='text-align: center; font-size: 13px; padding: 20px;'>
        <p style='color: #B0B0B0;'>HealthBot Chat Assistant | Built with Streamlit & Google Gemini AI</p>
        <p style='color: #B0B0B0;'><strong style='color: #FF6B6B;'>Remember:</strong> This tool is for informational purposes only. Always consult a qualified healthcare professional.</p>
    </div>
    """,
    unsafe_allow_html=True
)

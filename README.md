# **🏥 HealthBot Chat Assistant**

A professional Streamlit-based AI chatbot that helps users identify potential health conditions by analyzing symptoms and answering health-related questions using Google's Gemini AI.

> **⚠️ Important Disclaimer:** This tool is intended for informational purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult a qualified medical professional for any health concerns.

## **🔗 Live Demo**

Try it here: [HealthBot Chat Assistant](https://healthbot-chat-assistant-tg.streamlit.app)

## **✨ Features**

- **Symptom Input**: Structured input field for entering patient symptoms
- **AI-Powered Analysis**: Uses Google Gemini 1.5 Flash for intelligent responses
- **Contextual Conversations**: Memory-aware chat that remembers entered symptoms
- **Comprehensive Responses**: Get information about:
  - Possible diseases/conditions
  - Symptoms and their relationships
  - Potential causes
  - Treatment suggestions and remedies
  - Over-the-counter medications (with safety warnings)
  - Prevention tips
  - Diet and nutrition advice
  - Doctor consultation recommendations
- **Chat History**: View complete conversation history
- **Professional UI**: Clean, modern interface with proper styling
- **Error Handling**: Robust error handling for API failures and missing configurations
- **Session Management**: Reset functionality to start new conversations

## **🛠️ Technologies Used**

- **Python 3.10+**
- **Streamlit** (>=1.30.0) - Web framework
- **Google Generative AI** (Gemini API) - AI model
- **python-dotenv** - Environment variable management

## **📋 Prerequisites**

- Python 3.10 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

## **🚀 Setup Instructions**

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/HealthBot-chatassistant.git
cd HealthBot-chatassistant
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.env` file in the project root directory:

```bash
# On Windows (PowerShell)
New-Item .env

# On macOS/Linux
touch .env
```

Add your Google Gemini API key to the `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

**To get your API key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it in your `.env` file

### 5. Run the application

```bash
streamlit run Healthbot.py
```

The app will open in your default web browser at `http://localhost:8501`

## **📁 Project Structure**

```
Health/
├── Healthbot.py          # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables (create this, not in repo)
├── .gitignore           # Git ignore file
└── venv/                 # Virtual environment (created locally)
```

## **🌐 Deployment on Streamlit Cloud**

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/HealthBot-chatassistant.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository
   - Set the main file path to `Healthbot.py`
   - Add your `GOOGLE_API_KEY` in the "Secrets" section:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```
   - Click "Deploy"

## **💡 Usage**

1. **Enter Symptoms**: Click on "📝 Enter Patient's Symptoms" and type in the symptoms (e.g., "fever, sore throat, fatigue")
2. **Submit**: Click "Submit Symptoms" button
3. **Ask Questions**: Use the chat input at the bottom to ask health-related questions such as:
   - "What disease could this be?"
   - "What are the treatments?"
   - "What are the causes?"
   - "Should I consult a doctor?"
   - "What prevention measures can I take?"
   - "What diet should I follow?"
4. **View History**: All conversations are displayed in the chat history
5. **Reset**: Click "Reset Conversation" to start fresh with new symptoms

## **🔒 Security Notes**

- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude sensitive files
- For production deployment, use Streamlit Cloud's secrets management

## **🐛 Troubleshooting**

### API Key Issues
- Ensure your `.env` file is in the project root
- Verify the API key format: `GOOGLE_API_KEY=your_key_here` (no quotes)
- Check that the API key is valid and has not expired

### Import Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using Python 3.10 or higher

### Streamlit Not Starting
- Check if Streamlit is installed: `pip install streamlit`
- Try running: `python -m streamlit run Healthbot.py`

## **📝 License**

This project is licensed under the MIT License.

## **👤 Author**

Developed by **SNEHA GUPTA**

## **🤝 Contributing**

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## **⭐ Acknowledgments**

- Google Gemini AI for the powerful language model
- Streamlit for the amazing web framework
- All contributors and users of this project

# HealthBot Chat Assistant

A web-based health assistant that helps you get information about potential health conditions based on symptoms you enter. Built with Streamlit and Google's Gemini AI.

**Live App:** [healthbot-chat-assistant-tg.streamlit.app](https://healthbot-chat-assistant-tg.streamlit.app)

> ⚠️ **Disclaimer:** This is for informational purposes only. Always consult a real doctor for medical advice.

## What it does

Enter your symptoms and ask questions about:
- Possible diseases or conditions
- Causes and symptoms
- Treatment options and remedies
- Prevention tips
- Diet and nutrition advice
- When to see a doctor

The chatbot remembers your symptoms throughout the conversation, so you can ask follow-up questions.

## Tech Stack

- Python 3.10+
- Streamlit
- Google Gemini AI
- python-dotenv

## Setup

1. Clone the repo:
```bash
git clone https://github.com/sneha205985/Health_Bot_Chat_Assistant.git
cd Health_Bot_Chat_Assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

4. Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

5. Run the app:
```bash
streamlit run Healthbot.py
```

## Project Files

- `Healthbot.py` - Main application
- `requirements.txt` - Dependencies
- `.env` - Your API key (not in repo)

## Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub account
3. Create a new app and select this repository
4. In the Secrets section, add:
   ```
   GEMINI_API_KEY = "your_api_key_here"
   ```
5. Deploy

## Usage

1. Enter symptoms in the input field
2. Click "Submit Symptoms"
3. Ask questions in the chat box at the bottom
4. View your conversation history
5. Click "Reset Conversation" to start over

## Author

SNEHA GUPTA

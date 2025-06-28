# **HealthBot Chat Assistant**

## Overview

**HealthBot Chat Assistant** is a Streamlit-based AI chatbot that helps users identify potential illnesses by analyzing entered symptoms and follow-up health-related questions. This project uses Google's Gemini Pro (Generative AI) to provide contextual and memory-aware responses.

> **Disclaimer:** This tool is intended for informational purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult a qualified medical professional for any health concerns.

## Features

- Enter symptoms through a structured input field
- Ask follow-up health-related questions with memory of previous input
- AI-generated structured responses that include:
  - Possible diseases
  - Likely symptoms
  - Causes
  - Suggested remedies
  - Doctor consultation advice
- Session history with user and assistant chat display
- Reset conversation functionality
- Customized UI with styled headings and expandable input sections

## Technologies Used

- **Python 3.10+**
- **Streamlit**
- **Google Generative AI (Gemini API)**
- **dotenv**

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/HealthBot-chatassistant.git
cd HealthBot-chatassistant
```

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Create a `.env` file and add:

```
GOOGLE_API_KEY=your_api_key_here
```

## Running the App

```bash
streamlit run Healthbot.py
```

## Folder Structure

```
healthbot-chat-assistant/
‚îú‚îÄ‚îÄ Healthbot.py              # Main application file
‚îú‚îÄ‚îÄ .env                      # Contains the Gemini API Key (excluded in .gitignore)
‚îú‚îÄ‚îÄ requirements.txt          # python dependencies
‚îî‚îÄ‚îÄ README.md                 # Project documentatiom 
```

## License

This project is licensed under the MIT License.

## Author 

Developed by SNEHA GUPTA
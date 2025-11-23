# HealthBot Chat Assistant

A web-based health assistant application that helps users get information about potential health conditions based on symptoms. Users can enter their symptoms and have a conversation with an AI-powered chatbot to learn about possible diseases, treatments, causes, and prevention methods.

**Live Demo:** [healthbot-chat-assistant-tg.streamlit.app](https://healthbot-chat-assistant-tg.streamlit.app)

## About the Project

HealthBot Chat Assistant is an interactive web application that uses artificial intelligence to provide health-related information. Users start by entering their symptoms, and then can ask various questions about their condition, including:

- Possible diseases or medical conditions
- Symptoms and how they relate to each other
- Potential causes
- Treatment options and home remedies
- Prevention strategies
- Dietary recommendations
- When to consult a healthcare professional

The chatbot maintains context throughout the conversation, remembering the symptoms you entered so you can ask follow-up questions naturally.

> ⚠️ **Important:** This tool is for informational purposes only and does not replace professional medical advice. Always consult a qualified healthcare provider for diagnosis and treatment.

## Technologies Used

- **Python 3.10+** - Programming language
- **Streamlit** - Web framework for building the user interface
- **Google Gemini AI** - AI model powering the chatbot responses
- **python-dotenv** - For managing environment variables and API keys

## Project Structure

```
Health_Bot_Chat_Assistant/
├── Healthbot.py          # Main application file
├── requirements.txt      # Python package dependencies
├── README.md            # Project documentation
├── .streamlit/          # Streamlit configuration
│   └── config.toml      # Theme and app settings
└── .gitignore           # Git ignore rules
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/sneha205985/Health_Bot_Chat_Assistant.git
cd Health_Bot_Chat_Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

You'll need a Google Gemini API key. Get one from [Google AI Studio](https://makersuite.google.com/app/apikey), then create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run Healthbot.py
```

## Key Features

- **Symptom-based Analysis** - Enter symptoms and get AI-powered insights
- **Conversational Interface** - Natural chat experience with context memory
- **Comprehensive Information** - Get answers about diseases, treatments, causes, and more
- **Modern UI** - Clean, user-friendly interface with dark theme
- **Session Management** - Reset conversations to start fresh

## Author

**SNEHA GUPTA**

---

*This project is part of my portfolio and demonstrates the use of AI in healthcare information applications.*

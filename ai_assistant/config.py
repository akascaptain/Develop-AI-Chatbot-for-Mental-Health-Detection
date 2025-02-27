# config.py

# OpenAI API Key (for ChatGPT responses)
OPENAI_API_KEY = "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"

# Wolfram Alpha API Key (for factual and computational queries)
WOLFRAMALPHA_APP_ID = "PR4KHV-48XQVYH3YH"

# Assistant settings
ASSISTANT_NAME = "Jarvis"
WAKE_WORDS = ["hey jarvis", "ok jarvis"]

# Speech settings
VOICE_SPEED = 150  # Adjust speech speed
VOICE_VOLUME = 1.0  # Set volume (0.0 to 1.0)

# Error messages
ERROR_MESSAGES = {
    "unrecognized_speech": "Sorry, I didn't catch that. Could you repeat?",
    "api_unavailable": "I'm having trouble connecting to the internet."
}

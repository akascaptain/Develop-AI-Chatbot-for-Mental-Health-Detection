# nlp.py

import openai
import wikipedia
import wolframalpha
from config import OPENAI_API_KEY, WOLFRAMALPHA_APP_ID

# Initialize APIs
openai.api_key = OPENAI_API_KEY
client = wolframalpha.Client(WOLFRAMALPHA_APP_ID)

def process_text(text):
    """Process user queries using AI, Wikipedia, or Wolfram Alpha."""
    
    if "wikipedia" in text:
        topic = text.replace("wikipedia", "").strip()
        try:
            return wikipedia.summary(topic, sentences=2)
        except wikipedia.exceptions.DisambiguationError:
            return "There are multiple results. Please be more specific."
        except wikipedia.exceptions.PageError:
            return "I couldn't find anything on Wikipedia for that."

    elif "calculate" in text or "what is" in text or "who is" in text:
        try:
            res = client.query(text)
            return next(res.results).text
        except:
            return "I couldn't compute that."

    else:
        # OpenAI (GPT) response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}]
        )
        return response["choices"][0]["message"]["content"]

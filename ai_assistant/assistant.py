import openai
import wikipedia
import wolframalpha
import os
import speech_recognition as sr
import pyttsx3
import time
import subprocess
from config import OPENAI_API_KEY, WOLFRAMALPHA_APP_ID

# Initialize APIs
openai.api_key = OPENAI_API_KEY
client = wolframalpha.Client(WOLFRAMALPHA_APP_ID)

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speed

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return "I couldn't understand you."
    except sr.RequestError:
        return "API unavailable."

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

    elif "open notepad" in text:
        subprocess.run("notepad.exe")
        return "Opening Notepad."

    elif "open browser" in text:
        subprocess.run("start chrome", shell=True)
        return "Opening browser."

    elif "time" in text:
        return f"The current time is {time.strftime('%I:%M %p')}"

    elif "date" in text:
        return f"Today's date is {time.strftime('%A, %B %d, %Y')}"

    else:
        # OpenAI (GPT) response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}]
        )
        return response["choices"][0]["message"]["content"]

def run_assistant():
    """Main function to run the AI assistant."""
    speak("Hello! I am your AI assistant. How can I help you?")
    
    while True:
        user_input = listen()
        if "exit" in user_input or "quit" in user_input or "stop" in user_input:
            speak("Goodbye!")
            break
        
        response = process_text(user_input)
        speak(response)

if __name__ == "__main__":
    run_assistant()

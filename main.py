import os   
import time 
from groq import Groq
from gtts import gTTS
import pygame
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Set GROQ_API_KEY in .env")

client = Groq(api_key=GROQ_API_KEY)
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
messages = [{"role": "system", "content": "You are a helpful AI assistant."}]

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
    
    # Windows-safe cleanup
    try:
        pygame.mixer.music.unload()
        os.remove("response.mp3")
    except:
        pass  # Ignore cleanup errors

print("✅ Config loaded successfully")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    
    messages.append({"role": "user", "content": user_input})
    chat_complete = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )
    
    reply = chat_complete.choices[0].message.content
    print("AI: " + reply)
    messages.append({"role": "assistant", "content": reply})
    text_to_speech(reply)

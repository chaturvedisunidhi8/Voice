import os
from dotenv import load_dotenv

# Load .env file from project root
load_dotenv()

# Get Groq API key securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Validate key exists and is valid format
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")
if not GROQ_API_KEY.startswith("gsk_"):
    raise ValueError("Invalid GROQ_API_KEY format - must start with gsk_")

print("✅ Config loaded successfully")

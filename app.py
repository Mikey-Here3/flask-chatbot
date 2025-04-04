import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()  # Load environment variables

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY:
    print("✅ API Key Loaded Successfully!")
else:
    print("❌ API Key Missing!")

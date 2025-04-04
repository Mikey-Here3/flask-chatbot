import os
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()  # Load environment variables

app = Flask(__name__)

# Load OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY:
    print("✅ API Key Loaded Successfully!")
else:
    print("❌ API Key Missing!")

# ✅ Add a Home Route to Prevent "Not Found" Error
@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask Chatbot API!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

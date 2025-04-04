import os
from dotenv import load_dotenv
from flask import Flask, jsonify

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask Chatbot API!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

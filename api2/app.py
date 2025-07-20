from flask import Flask, request, jsonify
import logging
import random
import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

RESPONSES = [
    "Hello from API2!",
    "API2 welcomes you!",
    "You've reached API2 successfully!",
    "Sending greetings from API2!",
    "Hello Hackathon from API2"
]

@app.route("/api")
def hello():
    user = request.args.get("user", "anonymous")
    message = random.choice(RESPONSES)
    timestamp = datetime.datetime.utcnow().isoformat()

    logging.info(f"[API2] Received request from API1. User: {user}")
    
    return jsonify({
        "source": "API2",
        "message": message,
        "timestamp": timestamp,
        "user": user
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

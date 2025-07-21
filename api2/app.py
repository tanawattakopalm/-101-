from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/api", methods=["GET", "POST"])
def hello():
    method = request.method
    user = "Unknown"

    if method == "POST":
        json_data = request.get_json() or {}
        user = json_data.get("user", "Unknown")
        logging.info(f"[API2] POST received with data: {json_data}")
    else:
        user = request.args.get("user", "Unknown")
        logging.info(f"[API2] GET received with user: {user}")

    return jsonify({
        "source": "API2",
        "message": "Hello Hackathon from API2",
        "timestamp": datetime.utcnow().isoformat(),
        "user": user
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

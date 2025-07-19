from flask import Flask, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/api")
def hello():
    logging.info("[API2] Received request from API1")
    return jsonify({"source": "API2", "message": "Hello Hackathon from API2"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
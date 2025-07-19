from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/API_1")
def call_api2():
    logging.info("[API1] Received request from User")
    response = requests.get("http://api2:5001/api")
    logging.info(f"[API1] Response from API2: {response.text}")
    return jsonify({"source": "API1", "message": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
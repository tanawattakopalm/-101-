from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/API_1")
def call_api2():
    user = request.args.get("user", "anonymous")
    logging.info(f"[API1] Received request from User: {user}")
    
    try:
        response = requests.get(f"http://api2:5001/api?user={user}")
        api2_data = response.json()
        logging.info(f"[API1] Response from API2: {api2_data}")
        return jsonify({
            "source": "API1",
            "received_from_api2": api2_data
        })
    except Exception as e:
        logging.error(f"[API1] Failed to connect to API2: {e}")
        return jsonify({"error": "Failed to connect to API2", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

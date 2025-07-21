from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/API_1", methods=["GET", "POST"])
def call_api2():
    user = request.args.get("user", "Unknown")
    method = request.method

    if method == "POST":
        json_data = request.get_json() or {}
        user = json_data.get("user", user)
        logging.info(f"[API1] POST request received with data: {json_data}")
        response = requests.post("http://api2:5001/api", json={"user": user})
    else:
        logging.info(f"[API1] GET request received with user: {user}")
        response = requests.get(f"http://api2:5001/api?user={user}")

    logging.info(f"[API1] Response from API2: {response.text}")
    return jsonify({
        "source": "API1",
        "method": method,
        "received_from_api2": response.json()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

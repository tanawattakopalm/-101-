# 🚀 Project: API Chaining with Docker Compose

## 📋 Description
This project demonstrates how to chain two Flask APIs using Docker Compose:
- **API1** (port 5000): Receives a `GET` or `POST` request from the user and forwards it to API2, then returns the combined JSON response.
- **API2** (port 5001): Responds with a message, timestamp, and optional username.
- Both APIs use Python's `logging` module for logging activity.

---

## ⚙️ Features
- 🔗 Chained communication: API1 calls API2 internally using HTTP.
- ✅ Methods Supported: `GET` (with query string) and `POST` (with JSON payload).
- 🕒 Adds current timestamp using `datetime`.
- 👤 Supports username passed via:
  - `GET`: `?user=YourName`
  - `POST`: JSON payload `{ "user": "YourName" }`
- 🔄 Full JSON Response with all info.
- 📄 Structured logging using Python `logging` module.
- 🐳 Containerized with **Docker Compose**.

---

## 📁 Folder Structure
```
├── api1
│   ├── app.py
│   └── Dockerfile
├── api2
│   ├── app.py
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚦 Deployment Steps
1. **Clone or download** this repository:
   ```
   git clone https://github.com/tanawattakopalm/-101-.git
   cd -101-
   ```
2. **Open a terminal** and navigate to the project root directory.
3. **Build and start** the containers:
   ```
   docker-compose up --build
   ```

## 🧪 How to Test
After the containers are running:
🔹 GET Request
  Use a web browser or curl to send a GET request:
    ```
    curl http://127.0.0.1:5000/API_1?user=Palm

    ```
  ✅ Response Example
    ```
    {
      "source": "API1",
      "method": "GET",
      "received_from_api2": {
        "source": "API2",
        "message": "Hello Hackathon from API2",
        "timestamp": "2025-07-20T15:28:17.229544",
        "user": "Palm"
      }
    }
    ```
🔸 POST Request
  Send a JSON body using curl or Postman:
    ```
    curl -X POST http://127.0.0.1:5000/API_1 \
     -H "Content-Type: application/json" \
     -d '{"user": "Palm"}'

    ```
  ✅ Response Example
    ```
    {
      "source": "API1",
      "method": "POST",
      "received_from_api2": {
        "source": "API2",
        "message": "Hello Hackathon from API2",
        "timestamp": "2025-07-20T15:28:17.229544",
        "user": "Palm"
      }
    }
    ```
📌 Tip: You can change "Palm" to any name to test dynamic input.


## 📝 Notes
- API1 and API2 run in separate containers and communicate using service names defined in docker-compose.yml.
- Ensure Docker is installed and running on your system.
- All source code and Dockerfiles are located inside their respective folders.
- Logs will appear in the terminal where you run docker-compose.
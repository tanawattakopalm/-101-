# 🚀 Project: API Chaining with Docker Compose

## 📋 Description
This project demonstrates how to chain two Flask APIs using Docker Compose:
- **API1** (port 5000): Receives a `GET` request from the user and forwards it to API2, then returns the combined JSON response.
- **API2** (port 5001): Responds with a message, timestamp, and optional username.
- Both APIs use Python's `logging` module for logging activity.

---

## ⚙️ Features
- 🔗 Chained communication: API1 calls API2 internally using HTTP.
- ✅ Method: `GET` with query parameters.
- 🕒 Adds current timestamp using `datetime`.
- 👤 Supports username passed via query string (`?user=YourName`).
- 🔄 Full JSON Response with all info.
- 🐳 Containerized with **Docker Compose**.

---

## 📁 Folder Structure
├── api1
│ ├── app.py # API1 Flask application
│ └── Dockerfile # Dockerfile for API1
├── api2
│ ├── app.py # API2 Flask application
│ └── Dockerfile # Dockerfile for API2
├── docker-compose.yml # Docker orchestration file
└── README.md # This file
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
- Open your browser or use `curl` to access API1:
  ```
  curl http://127.0.0.1:5000/API_1?user=Palm
  ```
- You should see a response like:
  ```
  {
  "received_from_api2": {
    "message": "Hello Hackathon from API2",
    "source": "API2",
    "timestamp": "2025-07-20T15:28:17.229544",
    "user": "Palm"
  },
  "source": "API1"
  }
  ✅ You can change Palm to any other name in the URL to test different inputs.
  ```

## 📝 Notes
- API1 and API2 run in separate containers and communicate using service names defined in `docker-compose.yml`.
- Ensure Docker is installed and running on your system.
- All source code and Dockerfiles are located inside their respective folders.
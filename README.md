# 🚀 Project: API Chaining with Docker Compose

## 📋 Description
This project demonstrates how to chain two Flask APIs using Docker Compose:
- **API1** (port 5000): Receives requests and forwards them to API2.
- **API2** (port 5001): Responds with `"Hello World from API2"`.
- Both APIs use Python's `logging` module for logging.

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
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Open a terminal** and navigate to the project root directory.
3. **Build and start** the containers:
   ```bash
   docker-compose up --build
   ```

## 🧪 How to Test
After the containers are running:
- Open your browser or use `curl` to access API1:
  ```bash
  curl http://localhost:5000/api
  ```
- You should see a response like:
  ```
  [API1] Received -> Hello Hackathon from API2
  ```



## 📝 Notes
- API1 and API2 run in separate containers and communicate using service names defined in `docker-compose.yml`.
- Ensure Docker is installed and running on your system.
- All source code and Dockerfiles are located inside their respective folders.
# Project: API Chaining with Docker Compose

## Description
This project sets up two APIs using Flask:
- API1 listens on port 5000 and forwards the request to API2
- API2 listens on port 5001 and returns "Hello World from API2"
- Logs are printed by both APIs using the logging module

## Folder Structure
```
├───api1
│   ├── app.py
│   └── Dockerfile
├───api2
│   ├── app.py
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## How to Deploy
1. Clone or download this repository
2. Navigate to the root project directory
3. Run the following command:
```bash
docker-compose up --build
```

## How to Test
Once the containers are up:
- Open your browser or use curl to access API1
```bash
curl http://localhost:5000/api
```
- You should see a response like:
```
[API1] Received -> Hello World from API2
```

## Notes
- API1 and API2 are separate containers and communicate via service names defined in docker-compose
- Make sure Docker is installed and running
- All source code and Dockerfiles are located inside their respective folders
@echo off
echo Building Docker image...
docker build -t fastapi_sqlite_app .

echo Running Docker container...
docker run -p 8000:8000 fastapi_sqlite_app

echo FastAPI is running at http://localhost:8000/users
pause

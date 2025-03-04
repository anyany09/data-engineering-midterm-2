#!/bin/bash

# Build Docker image
docker build -t fastapi_sqlite_app .

# Run the container
docker run -p 8000:8000 fastapi_sqlite_app
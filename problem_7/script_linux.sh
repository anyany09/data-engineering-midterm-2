#!/bin/bash
# Build the Docker container

echo "Building Docker image..."
docker build -t csv_processor . --no-cache

echo "Docker image built successfully."

# Set default values
INPUT_FILE="input.csv"
OUTPUT_FILE="output.csv"
COLUMN_NAME="category"
FILTER_VALUE="sports"

# Allow user to override default values
if [ ! -z "$1" ]; then INPUT_FILE="$1"; fi
if [ ! -z "$2" ]; then OUTPUT_FILE="$2"; fi
if [ ! -z "$3" ]; then COLUMN_NAME="$3"; fi
if [ ! -z "$4" ]; then FILTER_VALUE="$4"; fi

# Run the Docker container
echo "Running Docker container with input file: $INPUT_FILE"
docker run --rm -v "$(pwd):/app" csv_processor "$INPUT_FILE" "$OUTPUT_FILE" "$COLUMN_NAME" "$FILTER_VALUE"

echo "Processing completed. Output saved to $OUTPUT_FILE"
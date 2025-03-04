# Use the official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the necessary files
COPY requirements.txt .
COPY csv_processor.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entrypoint
ENTRYPOINT ["python", "csv_processor.py"]
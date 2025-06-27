# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app folder (code, templates, model, encoder)
COPY . .

# Expose port Flask runs on
EXPOSE 5005

# Command to run the Flask app
CMD ["python", "app.py"]

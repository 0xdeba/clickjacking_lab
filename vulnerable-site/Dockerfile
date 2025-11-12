# Use official lightweight Python image
FROM python:3.11-alpine

# Set working directory inside container
WORKDIR /app

# Copy requirements if you have any
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your app source code
COPY . .

# Expose port your Flask app runs on (default 5000)
EXPOSE 5000

# Set environment variable to tell Flask the app entrypoint
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start Flask app
CMD ["flask", "run"]

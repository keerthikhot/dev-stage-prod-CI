# Use lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Keep Python logs unbuffered and expose runtime host/port via env.
ENV PYTHONUNBUFFERED=1 \
    APP_HOST=0.0.0.0 \
    APP_PORT=5000

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose app port (based on your deployment.yaml: 5000)
EXPOSE 5000

# Run the application
CMD ["python", "src/app.py"]

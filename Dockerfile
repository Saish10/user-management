# Start from an official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy your application files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure uvicorn is installed
RUN pip install uvicorn

# Expose the port that Cloud Run expects
EXPOSE 8080

ENV PORT=8080

# Run FastAPI with uvicorn on the correct host and port
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

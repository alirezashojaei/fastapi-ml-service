# Use Python 3.11.4 as the base image
FROM python:3.11.4-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY app app
COPY tests tests

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run tests to validate the application setup
RUN pytest --disable-warnings

# Command to run the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

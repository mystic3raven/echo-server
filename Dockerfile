# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements and application code into the container
COPY server.py /app
COPY requirements.txt /app

# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "server.py"]

# Use the official Python image from the Docker Hub
FROM python:3.11.9-bullseye

# Set the working directory in the container
WORKDIR /app

COPY http_server.py .

# Create a virtual environment and install dependencies
RUN pip install --upgrade pip setuptools wheel

EXPOSE 3000
ENTRYPOINT [ "python", "http_server.py" ]
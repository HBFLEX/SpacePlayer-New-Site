# Use the official Python image as the base image

FROM python:3.11.4

# Set the working directory in the container

WORKDIR /app

# Copy the application files into the working directory

COPY . /app

# Install the application dependencies

RUN pip install -r requirements.txt

# Define the entry point for the container

CMD ["flask", "run", "--host=0.0.0.0"]

# The error "dockerfile must expose a tcp port" is because the Dockerfile is not exposing any ports.

# In order to fix this, I added the EXPOSE instruction to specify that the container will be listening on port 5000.flu
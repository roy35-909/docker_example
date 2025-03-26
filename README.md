# My Python App in Docker

## Description
This project demonstrates how to containerize a Python application using Docker.

## Prerequisites
- Docker installed

## Steps
1. Build the Docker image:
   ```sh
   docker build -t myapp .

2. Run The image:
   ```sh
    docker run -d -p 80:8080 myapp

3. Verify the running container:
   ```sh
    docker ps

4. Stop and remove the container
   ```sh
    docker stop <container_id>
    docker rm <container_id>
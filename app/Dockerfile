# 1. Use an official, lightweight Python image from Docker Hub as our base OS
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy our requirements file into the container
COPY requirements.txt .

# 4. Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our application code (server.py) into the container
COPY . .

# 6. Tell Docker that this container will listen on port 5000
EXPOSE 5000

# 7. The command to run when the container starts
CMD ["python", "server.py"]
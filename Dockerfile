# Use the official Python image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y 
    curl 
    git 
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy the project files
COPY . .

# Install dependencies including the nexus local package (if available in the context)
# Note: For production, we'd typically install nexus from a repo or wheels.
# For now, we assume the environment is set up.
RUN uv sync --frozen

# Expose the port for the ADK Web UI / API
EXPOSE 8080

# Command to run the agent
CMD ["uv", "run", "python", "main.py"]

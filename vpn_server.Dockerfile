# Use Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all the files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the server will listen on
EXPOSE 8000

# Set the default command to run the server script
CMD ["python", "vpn_server.py"]

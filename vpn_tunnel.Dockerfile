# Use Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all the files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the tunnel will listen on
EXPOSE 8080

# Set the default command to run the tunnel script
CMD ["python", "vpn_tunnel.py"]
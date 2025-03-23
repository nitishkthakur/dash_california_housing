# Base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Dash will use
EXPOSE 8050

# Run the app
CMD ["python", "app.py"]

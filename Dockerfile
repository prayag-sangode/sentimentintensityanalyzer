# Use Python image as base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data (vader_lexicon)
RUN python -m nltk.downloader vader_lexicon

# Copy the Flask application code
COPY . /app/

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]

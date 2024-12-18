
# Sentiment Analysis Flask API

This is a Flask-based API for analyzing the sentiment of text using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner). It provides sentiment analysis, liveness, and readiness probe endpoints.

## Features

- Analyze the sentiment of text as **positive** or **negative** with a compound score.
- Includes liveness and readiness endpoints for health monitoring.
- Simple and lightweight REST API.

## Requirements

- Python 3.7+
- Flask
- NLTK

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/sentiment-analysis-flask.git
   cd sentiment-analysis-flask
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK resources:**

   ```bash
   python -m nltk.downloader vader_lexicon
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

   The application will run at `http://127.0.0.1:5000`.

2. **Test the endpoints using `curl` or Postman.**

### Endpoints

#### 1. **Analyze Sentiment**

- **URL:** `/analyze_sentiment`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "text": "I love learning new things about AI and Flask!"
  }
  ```

- **Response:**

  ```json
  {
    "text": "I love learning new things about AI and Flask!",
    "sentiment": "positive",
    "score": 0.7
  }
  ```

#### 2. **Liveness Probe**

- **URL:** `/healthz`
- **Method:** `GET`
- **Response:**

  ```text
  OK
  ```

#### 3. **Readiness Probe**

- **URL:** `/readyz`
- **Method:** `GET`
- **Response:**

  ```text
  OK
  ```

## Deployment

### Using Docker

1. **Build the Docker image:**

   ```bash
   docker build -t sentiment-analysis-api .
   ```

2. **Run the container:**

   ```bash
   docker run -p 5000:5000 sentiment-analysis-api
   ```

### Kubernetes

Include readiness and liveness probes in your Kubernetes deployment:

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 5000
readinessProbe:
  httpGet:
    path: /readyz
    port: 5000
```

## Contact

For questions or support, contact **Prayag Sangode** at `prayag.rhce@gmail.com`.

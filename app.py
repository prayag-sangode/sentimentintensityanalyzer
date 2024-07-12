from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import os

# Get dataset path from environment variable
dataset_path = os.getenv('DATASET_PATH', '/home/prayag/data')
SentimentIntensityAnalyzer

# Ensure NLTK resources are downloaded
nltk.data.path.append(dataset_path)

app = Flask(__name__)

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Endpoint to analyze sentiment
@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data['text']

    # Perform sentiment analysis
    sentiment_scores = sid.polarity_scores(text)
    sentiment = 'positive' if sentiment_scores['compound'] >= 0 else 'negative'

    return jsonify({
        'text': text,
        'sentiment': sentiment,
        'score': sentiment_scores['compound']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

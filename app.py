from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure NLTK resources are downloaded
nltk.download('vader_lexicon')

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

# Liveness probe endpoint
@app.route('/healthz', methods=['GET'])
def healthz():
    return "OK", 200

# Readiness probe endpoint
@app.route('/readyz', methods=['GET'])
def readyz():
    # You can add more complex readiness checks here if needed
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

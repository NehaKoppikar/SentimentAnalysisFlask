from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize sentiment analysis pipeline
sentiment_analysis = pipeline('sentiment-analysis')

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    if request.method == 'POST':
        text = request.form['text']
        result = sentiment_analysis(text)
        return render_template('result.html', text=text, result=result[0])

if __name__ == '__main__':
    app.run(debug=True)

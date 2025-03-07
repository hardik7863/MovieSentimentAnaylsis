from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the IMDB dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load the pre-trained model with ReLU activation
model = load_model('simple_rnn_imdb.h5')

# Helper Functions
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

# Function to preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        user_input = request.form['review']
        
        if user_input:
            preprocessed_input = preprocess_text(user_input)
            prediction = model.predict(preprocessed_input)
            sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
            
            return jsonify({
                'sentiment': sentiment,
                'score': float(prediction[0][0])
            })
        else:
            return jsonify({'error': 'Please enter a movie review'})

if __name__ == '__main__':
    app.run(debug=True)
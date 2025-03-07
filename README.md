# IMDB Movie Review Sentiment Analysis

This project is a web application that classifies IMDB movie reviews as positive or negative using a pre-trained Recurrent Neural Network (RNN) model.

## Project Structure

```
.
├── app.py
├── embedding.ipynb
├── main.py
├── notes.ipynb
├── prediction.ipynb
├── requirements.txt
├── simple_rnn_imdb.h5
├── simplernn.ipynb
└── templates/
    └── index.html
```

- `app.py`: The main Flask application file.
- `embedding.ipynb`, `notes.ipynb`, `prediction.ipynb`, `simplernn.ipynb`: Jupyter notebooks for various stages of the project.
- `main.py`: A script to run the Streamlit app for sentiment analysis.
- `requirements.txt`: A file listing the dependencies required for the project.
- `simple_rnn_imdb.h5`: The pre-trained RNN model.
- `templates/index.html`: The HTML template for the web application.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/hardik7863/MovieSentimentAnaylsis.git
    cd RNNProject
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```sh
    python app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

1. Enter a movie review in the text area on the web page.
2. Click the "Classify" button to classify the review as positive or negative.
3. The result will be displayed on the web page.


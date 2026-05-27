# News Article Classification

## Project Overview

This is a complete news article classification application created and developed by Harshith. The project uses machine learning and NLP to classify news articles into categories like Business, Entertainment, Sports, Politics, Travel, and more.

## Features

- Text classification using a trained machine learning model
- Web interface for article submission and instant category prediction
- Clean and responsive HTML UI inside `templates/index2.html`
- Model training logic in `classifier.py`
- Local HTTP server implementation in `server.py`

## Installation

1. Open a terminal in the project folder.
2. Create and activate a Python virtual environment:
   - `python -m venv .venv`
   - `.
venv\Scripts\activate`
3. Install the required dependencies:
   - `pip install -r requirements.txt`

## Usage

1. Start the server:
   - `python server.py`
2. Open your browser and visit:
   - `http://localhost:8000/`
3. Paste a news article into the text area and click **Classify**.

## Project Structure

- `classifier.py` — model training and prediction code
- `server.py` — local HTTP server handling the web UI and classification requests
- `lemma_tokenizer.py` — custom tokenizer and lemmatization logic
- `NewsCategorizer.csv` — dataset used for training the model
- `templates/index2.html` — front-end page for the web app
- `requirements.txt` — Python dependencies
- `Models/` — additional model files used by the project

## Development Notes

- The classification model is built with scikit-learn and NLTK.
- Make sure NLTK resources like `stopwords`, `punkt`, `wordnet`, and `omw-1.4` are downloaded if training the model locally.
- If the web page does not appear, ensure `server.py` is still running and access `http://localhost:8000/` in your browser.

## License

This project is licensed under the MIT License.

## Author

- Harshith
- Developed as a personal project for news article classification using machine learning and NLP.

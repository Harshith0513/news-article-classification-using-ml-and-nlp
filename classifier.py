import pickle
import re
from collections import Counter

import pandas as pd
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import LinearSVC, SVC
from lemma_tokenizer import LemmaTokenizer

# Step 1: Load dataset
def load_data():
    data = pd.read_csv("NewsCategorizer.csv")
    return data['short_description'], data['category']

# Step 2: Train model
def train_model():
    texts, labels = load_data()

    texts_rt = texts.apply(remove_tags)
    texts_sc = texts_rt.apply(special_char)
    texts_cl = texts_sc.apply(convert_lower)
    texts_rs = texts_cl.apply(remove_stopwords)
    texts_lw = texts_rs.apply(lemmatize_word)
    vectorizer = TfidfVectorizer(stop_words='english', max_features=20000, token_pattern=r'\b[a-zA-Z0-9]+\b', min_df=2, max_df=0.8)
    X = vectorizer.fit_transform(texts_lw)
    print(vectorizer.get_feature_names_out()[:10])
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42, stratify=labels)

    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

    # Save the model and vectorizer
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

# Step 3: Predict
def predict(text):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)
    print(prediction)
    return prediction[0]

def remove_tags(text):
    remove = re.compile(r'<.*?>')
    return re.sub(remove, '', text)

def special_char(text):
    reviews = ''
    for x in text:
        if x.isalnum():
            reviews = reviews + x
        else:
            reviews = reviews + ' '
    return reviews

def convert_lower(text):
    return text.lower()

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    return [x for x in words if x not in stop_words]

def lemmatize_word(text):
    wordnet = WordNetLemmatizer()
    return " ".join([wordnet.lemmatize(word) for word in text])


if __name__ == "__main__":
    train_model()


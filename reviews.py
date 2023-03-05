import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load the dataset
with open('reviews.txt', 'r') as f:
    reviews = f.readlines()

# Preprocess the text data
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    return " ".join(words)

X = [preprocess_text(text) for text in reviews]

# Convert the text data into a numerical format
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Train a sentiment analysis model using logistic regression
model = LogisticRegression()
model.fit(X, y)

# Predict the sentiment of reviews
y_pred = model.predict(X)

# Write the predicted sentiment to a text file
with open('predicted_sentiment.txt', 'w') as f:
    for sentiment in y_pred:
        if sentiment == "positive":
            f.write("1\n")  # positive review
        else:
            f.write("0\n")  # negative review

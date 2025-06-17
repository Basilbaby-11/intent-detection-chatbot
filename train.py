import json
import random
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json", "r",encoding="utf-8") as f:
    data = json.load(f)

corpus = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        corpus.append(pattern)
        labels.append(intent["tag"])

# Vectorize the text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
y = np.array(labels)

# Train classifier
model = LogisticRegression()
model.fit(X, y)

# Save the model and vectorizer
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ Model trained and saved to chatbot_model.pkl")

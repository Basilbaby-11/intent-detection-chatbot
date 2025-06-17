import random
import json
import pickle

# Load trained model and vectorizer
with open("chatbot_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

# Load intents
with open("intents.json", "r") as f:
    intents = json.load(f)

# Function to get chatbot response
def get_response(user_input):
    X = vectorizer.transform([user_input])
    intent = model.predict(X)[0]
    
    for i in intents["intents"]:
        if i["tag"] == intent:
            return random.choice(i["responses"])

    return "Sorry, I didn't understand that."

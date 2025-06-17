from flask import Flask, render_template, request, jsonify
import json
import pickle

app = Flask(__name__)

# Load intents
with open("intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

# Load model and vectorizer
with open("chatbot_model.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    data = request.get_json()
    user_input = data.get("message")
    if not user_input:
        return jsonify({"reply": "Please enter a message."})

    X = vectorizer.transform([user_input])
    prediction = model.predict(X)[0]

    for intent in intents["intents"]:
        if intent["tag"] == prediction:
            return jsonify({"reply": intent["responses"][0]})
    return jsonify({"reply": "Sorry, I don't understand."})

if __name__ == "__main__":
    app.run(debug=True)

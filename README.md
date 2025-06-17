## 📁 Project Structure

```
intent-detection-chatbot/
├── static/
│   └── style.css              # Custom styles for the chat UI
├── templates/
│   └── index.html             # Frontend interface
├── intents.json               # Intents, patterns, and responses
├── chatbot_model.pkl          # Saved ML model and vectorizer
├── chatbot.py                 # Core logic for intent detection
├── train.py                   # Script to train the model
├── app.py                     # Flask app to serve chatbot
├── requirements.txt           # List of required Python packages
└── README.md                  # Documentation file
```

---

## 🔍 How It Works

1. `intents.json` contains patterns and their corresponding tags.
2. `train.py` loads the intents, vectorizes the text, and trains a Logistic Regression model.
3. The model and vectorizer are saved to `chatbot_model.pkl`.
4. `chatbot.py` contains the prediction logic that uses the model.
5. `app.py` sets up a Flask web server and routes user input to the model.
6. The user interacts with the chatbot through a web UI built in `index.html`.

---

## 🚀 Deployment Steps

### 🖥️ Run Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/intent-detection-chatbot.git
   cd intent-detection-chatbot
   ```

2. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Train the Model**

   ```bash
   python train.py
   ```

4. **Run the Web Server**

   ```bash
   python app.py
   ```

5. **Access in Browser**
   Open your browser and go to `http://127.0.0.1:5000`

---

## 🧠 Example Interaction

**User**: *"Hi there!"*
**Bot**: *"Hey! How can I assist you?"*

**User**: *"Thanks!"*
**Bot**: *"You're welcome!"*

---

## 💡 Customize It!

* Want to improve the chatbot? Add more patterns and responses to `intents.json`.
* Want smarter detection? Use a deep learning model instead of basic ML.
* Add a typing animation, voice input, or deploy it to the cloud!

---

## 📬 Contact

Made by Basil.
Feel free to fork, star ✩, or submit issues and improvements!

---

## 📄 License

This project is licensed under the **MIT License** – you can use it freely in personal or commercial projects.

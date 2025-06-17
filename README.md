# 🤖 Intent Detection Chatbot

This is a simple web-based chatbot that uses machine learning to detect user intent and respond accordingly. Built using Flask, HTML/CSS, and Python libraries like scikit-learn and NLTK.

---

## 🚀 Features

- Intent detection based on user input
- Predefined intents loaded from a JSON file
- Trained using basic ML (TF-IDF + Logistic Regression)
- Web interface with clean chat UI
- Responses are generated based on intent matching

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **ML Libraries**: scikit-learn, NLTK, pickle
- **Version Control**: Git + GitHub

---

## 📁 Project Structure

intent-detection-chatbot/
├── static/
│ └── style.css
├── templates/
│ └── index.html
├── intents.json
├── chatbot_model.pkl
├── chatbot.py # Bot logic
├── train.py # Model training
├── app.py # Flask web app
├── requirements.txt
└── README.md

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

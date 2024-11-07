from flask import Flask, render_template, request, jsonify
import threading
import pyttsx3
import speech_recognition as sr
import openai
from config import apikey
from responses import predefined_responses

app = Flask(__name__)

# Your existing functions go here (say, chat, takeCommand, etc.)
openai.api_key = apikey

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat(query):
    # Your chat function implementation
    if query in predefined_responses:
        response_text = predefined_responses[query]
        say(response_text)
        return response_text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Nova, an AI assistant created by Ashwani."},
                {"role": "user", "content": query},
            ],
            max_tokens=256,
            temperature=0.7,
        )
        response_text = response["choices"][0]["message"]["content"].strip()
        say(response_text)
        return response_text
    except Exception as e:
        return f"Error: {e}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_response():
    user_input = request.form["query"]
    response = chat(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

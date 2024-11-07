import re
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import openai
from config import apikey
from responses import predefined_responses
import os
from googleapiclient.discovery import build




GOOGLE_API_KEY = 'AIzaSyBLnLWePnIahg2Qhz1f2Pj2K2FH9UHzC9A'
GOOGLE_CSE_ID = '144a23a7e8a1c4653'

chatStr = ""
listening_mode = False
chat_mode = False

def chat(query):
    global chatStr
    query = query.lower()
    print(chatStr)
    
    if query in predefined_responses:
        response_text = predefined_responses[query]
        say(response_text)
        chatStr += f"Ashwani: {query}\nNova: {response_text}\n"
        return response_text

    openai.api_key = apikey
    chatStr += f"Ashwani: {query}\nNova: "
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
        print(response_text)
        say(response_text)
        chatStr += f"{response_text}\n"
        
        return response_text
    except Exception as e:
        print(f"Error: {e}")
        say("I am sorry, there was an error processing your request.")
        return None

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Nova, an AI assistant created by Ashwani."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=256,
            temperature=0.7,
        )
        response_text = response["choices"][0]["message"]["content"].strip()
        text += response_text
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        filename = f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt"
        with open(filename, "w") as f:
            f.write(text)
    except Exception as e:
        print(f"Error: {e}")
        say("I am sorry, there was an error processing your request.")

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            return "Sorry, I did not catch that."
        except sr.RequestError as e:
            return "Sorry, there was an error with the request."

def search_web(query):
    search_phrases = ["search", "find", "look up", "google", "what", "tell me about"]
    for phrase in search_phrases:
        if phrase in query:
            search_query = re.sub(r"(search|find|look up|google|what|tell me about)", "", query).strip()
            if search_query:
                service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
                response = service.cse().list(q=search_query, cx=GOOGLE_CSE_ID).execute()
                if 'items' in response and len(response['items']) > 0:
                    first_result = response['items'][0]
                    link = first_result.get('link')
                    say("Ok sir wait")
                    webbrowser.open(link)
                    return True

    return False

def listen_for_trigger():
    global listening_mode
    print("Listening for trigger...")
    while True:
        query = takeCommand().lower()
        if "nova listen" in query:
            say("Listening mode activated.")
            listening_mode = True
            break
        elif "nova chat" in query:
            say("Chat mode activated.")
            global chat_mode
            chat_mode = True
            break

def reset_modes():
    global listening_mode, chat_mode
    listening_mode = False
    chat_mode = False
    listen_for_trigger()


if __name__ == '__main__':
    print('Welcome to Nova A.I')
    say("Hello sir, I am Nova created by Ashwani. How may I assist you?")
    
   

    listen_for_trigger()  
    
    while True:
        if not listening_mode and not chat_mode:
            reset_modes()  

        if chat_mode:
            query = input("Type your message: ").lower()
            if "ok thank you" in query or "nova quit" in query:
                say("Goodbye!")
                break
            elif "reset chat" in query:
                chatStr = ""
                reset_modes()  
                continue
            else:
                print("Chatting...")
                chat(query)
                reset_modes() 
        elif listening_mode:
            print("Listening...")
            query = takeCommand().lower()
            
            if "ok thank you" in query:
                say("Goodbye!")
                break

            if search_web(query):
                reset_modes()  
                continue

            if "play my favourite music" in query:
                musicPath = "https://www.youtube.com/watch?v=gJLVTKhTnog"
                say("Ok sir, wait.")
                webbrowser.open(musicPath)
                reset_modes()  
                continue

            elif "the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"Sir, the time is {hour} hours and {min} minutes.")
                reset_modes()  
                continue

            elif "open facetime" in query:
                say("FaceTime is not available on Windows.")
                reset_modes()  
                continue

            elif "open pass" in query:
                say("Passkey is not available on Windows.")
                reset_modes()  
                continue

            elif "using artificial intelligence" in query:
                ai(prompt=query)
                reset_modes()  
                continue

            elif "nova quit" in query:
                say("Goodbye!")
                break

            elif "reset chat" in query:
                chatStr = ""
                reset_modes()  
                continue

            else:
                print("Chatting...")
                chat(query)
                reset_modes()  
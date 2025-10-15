import os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import smtplib
import requests
import json
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'chatbot' in command:
                command = command.replace('chatbot', '')
                print(command)
    except:
        pass
    return command


def run_chatbot():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'news' in command:
        try:
            news_api_key = os.getenv("NEWS_API_KEY")
            main_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
            news = requests.get(main_url).json()
            articles = news["articles"]
            news_headlines = []
            for ar in articles:
                news_headlines.append(ar["title"])
            for i in range(5):
                talk(news_headlines[i])
        except Exception as e:
            print(e)
            talk("Sorry, I couldn't fetch the news at the moment.")
    elif 'weather' in command:
        api_key = os.getenv("WEATHER_API_KEY")
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        talk("Of which city?")
        city_name = take_command()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talk(f'''
 Temperature (in kelvin unit) = {current_temperature}
 atmospheric pressure (in hPa unit) = {current_pressure}
 humidity (in percentage) = {current_humidiy}
 description = {weather_description}''')
        else:
            talk(" City Not Found ")
    elif 'send email' in command:
        talk("What should I say?")
        content = take_command()
        to = os.getenv("RECIPIENT_EMAIL")
        sendEmail(to, content)
        talk("Email has been sent!")
    elif 'control smart home devices' in command:
        talk("Which device you want to control?")
        device = take_command()
        if 'light' in device:
            talk("Turning on the light")
            # Code to control smart light
        elif 'thermostat' in device:
            talk("Setting the temperature")
            # Code to control thermostat
    elif 'open' in command:
        app = command.replace('open', '').strip()
        talk(f'Opening {app}')
        try:
            subprocess.Popen(app)
        except FileNotFoundError:
            talk(f"Sorry, I couldn't find the application {app}")
    elif 'what is' in command or 'who is' in command:
        question = command
        talk("Thinking...")
        response = model.generate_content(question)
        answer = response.text
        talk(answer)
    else:
        talk('Please say the command again.')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(os.getenv("SENDER_EMAIL"), os.getenv("EMAIL_PASSWORD"))
    server.sendmail(os.getenv("SENDER_EMAIL"), to, content)
    server.close()


while True:
    run_chatbot()

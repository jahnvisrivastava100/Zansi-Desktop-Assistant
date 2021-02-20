# My ZANSI project
import datetime
import os
import smtplib
import webbrowser as wb
from email.message import EmailMessage
import pyttsx3
import speech_recognition as sr

import wikipedia
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
app_id = 'ABC-123'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client('R2PP8Y-LXHL3PR8LT')


def listen():#Zansi recognizes your voice speech_recognition 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)#this recognized voice is converted in string

        try:
            print("Recognizing....")   #printing recognizing so that use comes to know that Zansi is Recognizing their voice
            query = r.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")
        except Exception as e:
            print("try speaking again..")
            return "null"
        return query


def speak(audio):#function for making Zansi speak string passed to the function
    engine.say(audio)
    engine.runAndWait()

#Function for chat mode of Zansi 
def chat():
    speak("Chat mode activated lets chat Hehe")

    while True:                infinite loop which terminates when You say deactivate
        i = listen().lower()
        if "hello" in i:
            speak("hello ji. lets chat")
        if "how are you" in i:
            speak("i am fine as always hopes same for you. cheers")

        elif "sad" in i:
            speak("oh! i dont like you like this lets chat and make things better")

        elif "happy" in i:
            speak("good to know.your happiness makes me happy too")

        elif "hungry" in i:
            speak("lets cook something tasty. firstly quiet chat mode. then speak open youtube hehe")

        elif "career" in i:
            speak("dont stress best things will happen to you")
        elif "your age" in i:
            date_1 = datetime.datetime(2021, 2, 5, 14, 30, 4)  # taking age when it was created
            date_2 = datetime.datetime.now()
            time_delta = (date_2 - date_1)  # difference between 2 dates
            total_seconds = time_delta.total_seconds()
            speak("when i am talking to you i am")
            speak(total_seconds)
            speak("seconds old")
        elif "deactivate" in i:
            speak("bye bye it was fun chatting hehe")
            return
        else:
            speak("sorry i didnt get")


def send_email(receiver, subject, message):#for sendig mail using smtp library
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('YourEmail@gmail.com', 'password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    #enter the email ids
}


def doubt():#doubt mode where zansii acesses data from Waphram Alpha
    speak("Doubt mode activated")
    str = "yes"
    while "yes" in str:
        dt = listen().lower()
        res = client.query(dt)
        ans = next(res.results).text
        print(ans)
        speak(ans)
        speak("do you want to ask more questions")
        str = listen().lower()


def greeting():
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr <= 12:
        speak(
            " Hello Janvi!! I hope your Morning is as bright as your Smile Good morning my gurl Zansi here to help you out")
    elif hr > 12 and hr <= 16:
        speak(
            " Hello Janvi!! I hope your Morning is as bright as your Smile Good morning my gurl Zansi here to help you out")
    else:
        speak(" Hello Janvi Still awake. Oh my girl you have so much work to do Zansi here to help you out ")

#main function
if __name__ == '__main__':

    print(sr.Microphone.list_microphone_names())
    greeting()
    while True:
        query = listen().lower()
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            print("Searching on Wikipedia")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "who are you" in query:
            speak(
                "I am Zansi. I was created by Janvi Srivastava in year 2020 during her Second year. I was written in python On pycharm")
        elif "open youtube" in query:

            wb.open('youtube.com', new=2)
        elif "open google" in query:
            wb.open('google.com', new=2)
        elif "open quora" in query:
            wb.open('quora.com', new=2)
        elif "play music" in query:
            music_dir = 'D:\my songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "c compiler" in query:
            dev = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(dev)
        elif "the time" in query:
            tim = datetime.datetime.now().strftime("%H:%M:%S")
            speak(tim)
            print(tim)

        elif "send email" in query:
            try:
                speak("To Whom you want to send email")
                name = listen().lower()
                receiver = email_list[name]
                print(receiver)
                speak("What is the subject of your email?")
                subject = listen().lower()
                speak("Tell me the text in your email")
                message = listen()
                send_email(receiver, subject, message)
                speak("Hey lazy ass. Your email is sent")

            except Exception as e:
                print(e)
                speak("Sorry janvi i am not able to send this email at this moment")


        elif "activate chat mode" in query:
            chat()
        elif "activate doubt mode" in query:
            doubt()
        elif "bye" in query:
            speak(
                "I’ll say goodbye, only if you promise to bring me expensive accessories when you return. hehe goodbye Janvi")
            exit(0)

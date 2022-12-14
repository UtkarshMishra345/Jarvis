os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING JARVIS BOT               ******")
print("*****      This tool was built by Utkarsh Mishra     ******")
print("*****       www.github.com/UtkarshMishra345         ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

from click import command
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyjokes
import pyaudio
import requests
import smtplib
import webbrowser
import time
import wikipedia
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
import pywhatkit as kit
import sys  
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from pytube import YouTube
from playsound import playsound
import keyboard
from googletrans import Translator
from keyboard import press
from keyboard import press_and_release
from keyboard import write 
from time import sleep
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 120)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source, timeout=100, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Lucky Said: {query}")

    except Exception as e:
        # speak("Say that again please...")
        return 'none'
    query = query.lower()
    return query


    # To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 16:
        speak("good afternoon")
    elif hour > 16 and hour < 19:
        speak("good evening")
    elif hour > 19 and hour < 0:
        speak("good night")

    else:
        speak("good evening")

    speak("hello sir I am Jarvis, tell me how can i help you")


# for news updates
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="
    #put API key....

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

#hindi class
def TakeHindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio,language='hi')
            print(f"You Said : {query}")

        except:
            return "none"

        return query.lower()

#translator
def Tran():
    speak("Tell Me The Line!")
    line = TakeHindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak(Text)

#open apps
def OpenApps():
    speak("Ok Sir , Wait A Second!")
        
    if 'code' in query:
        os.startfile("Put your path here")
        speak("Your Command Has Been Completed Sir!")
        #give your path here


    elif 'facebook' in query:
        webbrowser.open('https://www.facebook.com/')
        speak("Your Command Has Been Completed Sir!")
        #give your path here

    elif 'instagram' in query:
        webbrowser.open('https://www.instagram.com/')
        speak("Your Command Has Been Completed Sir!")

    elif 'open drive' in query:
        webbrowser.open('https://drive.google.com')
        speak("Your Command Has Been Completed Sir!")

    elif 'map' in query:
        webbrowser.open('https://www.google.com/maps/')
        speak("Your Command Has Been Completed Sir!")

    elif 'youtube' in query:
        webbrowser.open('https://www.youtube.com')
        speak("Your Command Has Been Completed Sir!")

    elif 'browser' in query:
        webbrowser.open('https://www.bing.com')
        speak("Your Command Has Been Completed Sir!")

#temprature
def Temp():
    search = input("Enter place here...")
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_="BNeawe").text
    speak(f"The Temperature Outside Is {temperature}")

    speak("Do I Have To Tell You Another Place Temperature ?")
    next = takecommand()

    if 'yes' in next:
        speak("Tell Me The Name Of tHE Place ")
        name = takecommand()
        search = f"temperature in {name}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_="BNeawe").text
        speak(f"The Temperature in {name} is {temperature}")

def phon():
    import phonenumbers

    # carrier: to know the name of
    # service provider of that phone number
    from phonenumbers import carrier

    number = input("Enter number here ...")


    service_provider = phonenumbers.parse(number)
    # Indian phone number example: +91**********
    # Nepali phone number example: +977**********

        
    # this will print the service provider name
    speak(carrier.name_for_number(service_provider,
                                'en'))

if __name__ == "__main__":
    #wish()
    while True:

        query = takecommand().lower()

        # Logic building for tasks

        if "open notepad" in query:
            npath = 'C:\\Windows\\System32\\notepad.exe'
            #give your path here
            os.startfile(npath)
            speak("opening")

        elif 'play music' in query:
            music_dir = 'Put Directory'
            #give your path here
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[128]))
            speak("playing music")

        # To Close any application
        elif 'close notepad' in query:
            speak("okay sir, closing")
            os.system("taskkill /f /im notepad.exe")

        # To find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 10")

        elif "restart the system" in query:
            os.system("shutdown /r /t 10")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(10)
            pyautogui.keyUp("alt")

        elif "tell me the news" in query:
            speak("please wait sir, while fetching the news for you")
            news()

        # to find my location using IPaddress
        elif "where i am" in query or "where we are" in query:
            speak('wait sir, let me check')
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country}")
            except Exception as e:
                speak("sorry sir,due to network issue i amnot able to find where we are.")
                pass

        # to hide files and folder
        elif "hide all files" in query or "hide this folder" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all files are now hidden")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir,all the files are now visible")

            elif "leave it" in condition:
                speak("ok sir")

        # how to do mode
        elif "activate how to do mode" in query:
            speak("how to do mode is activated")
            while True:
                speak("please tell me what do you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir,how to do mode is activated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)  # pip install pywikihow
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry, not able to find")

        # to know battery percentage
        elif "how much power " in query or "battery" in query:
            import psutil

            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage >= 75:
                speak("we have enough power, no need to charge")
            elif percentage >= 40 and percentage <= 75:
                speak("we should connect our system to the charging point")
            elif percentage >= 15 and percentage <= 30:
                speak("we don't have enough power,please connect to the charger")
            elif percentage <= 15:
                speak("we ahve very low power , please connect to the charger")

        # to play video and audio on yt
        elif "play songs on youtube" in query:
            try:
                speak("tell me the song name")
                name = input("please Enter the song name here")
                kit.playonyt(name)
            except Exception as e:
                speak("sorry sir i am unable to search")

        # SHUT UP
        elif "bye jarvis"  or " no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        #web search
        if "open google" in query:
            speak("what should i search")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening")
        
        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)


        # ip address
        elif "ip address" in query:
            from requests import get
            ip = get("https://api.ipify.org").text
            speak(f"your IP address is {ip}")

        # to download video

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            speak("Video Downloaded")

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')
            
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query: 
            keyboard.press_and_release('ctrl +h')

        elif 'home screen' in query:

            keyboard.press_and_release('windows + m')

        elif 'minimise the window' in query:

            keyboard.press_and_release('windows + m')

        elif 'show start' in query:

            keyboard.press('windows')

        elif 'open setting' in query:

            keyboard.press_and_release('windows + i')

        elif 'open search' in query:

            keyboard.press_and_release('windows + s')

        elif 'screen shot' in query:

            keyboard.press_and_release('windows + SHIFT + s')

        elif 'restore windows' in  query:

            keyboard.press_and_release('Windows + Shift + M')

        elif 'start the video' in query:
            keyboard.press('space bar')

        #website automation
        elif 'website' in query:
            speak("Ok Sir , Launching.....")
            query = query.replace("jerry","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched!")

        elif 'launch' in query:
            speak("Tell Me The Name Of The Website!")
            name = input("enter the website name: ")
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")

        # open apps
        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open map' in query:
            OpenApps()

        elif 'open drive' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'open browser' in query:
            OpenApps()


        elif "test network speed" in query:
            # internet speed

            import speedtest


            st = speedtest.Speedtest()

            option = int(input('''What speed do you want to test:

            1) Download Speed

            2) Upload Speed

            3) Ping

            Your Choice: '''))


            if option == 1:

                speak(st.download())

            elif option == 2:

                speak(st.upload())

            elif option == 3:

                servernames =[]

                st.get_servers(servernames)

                speak(st.results.ping)

            else:

                print("Please enter the correct choice !")

        elif "phone number info" in query:
            phon()

        #translator
        elif 'translator' in query:
            Tran()

        #temprature
        elif 'temperature' in query:
            Temp()

        #corona track
        elif 'coronavirus cases' in query:

            try:


                from Jarvis import CoronaVirus

                speak("Which Country's Information ?")

                cccc = takecommand()

                CoronaVirus(cccc)
        
            except:
                speak("No Data")

        elif 'activate answer bot' in query:
            # Python program to
            # demonstrate creation of an
            # assistant using wolf ram API

            import wolframalpha

            # Taking input from user
            question = input('Question: ')

            # App id obtained by the above steps
            app_id = "Put Your App Id by logging IN wolframalpha"

            # Instance of wolf ram alpha
            # client class
            client = wolframalpha.Client(app_id)

            # Stores the response from
            # wolf ram alpha
            res = client.query(question)

            # Includes only text from the response
            answer = next(res.results).text

            print(answer)
            
        elif "search google" in query:
            while True:
                try:
                    from googlesearch import search
                except ImportError:
                    print("No module named 'google' found")

                # to search
                query = input("Enter query...")

                if 'no' in query:
                    break

                for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                    print(j)

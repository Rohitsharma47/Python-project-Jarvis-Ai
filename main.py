import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import pyautogui
import platform
import os
from pygame import mixer
from plyer import notification



from intro import play_gif
play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....",end="",flush=True)
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("\r",end="",flush=True)
        print("Understanding..",end="",flush=True)
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def close_window():
    #  operating system
    if platform.system() == "Windows" :
        pyautogui.hotkey('alt', 'f4')  
   

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                    
                elif "google" in query:
                 from SearchNow import searchGoogle
                 searchGoogle(query)
                elif "youtube" in query:
                   from SearchNow import searchYoutube
                   searchYoutube(query)
                elif "wikipedia" in query:
                  from SearchNow import searchWikipedia
                  searchWikipedia(query) 
                  
                elif "schedule my day" in query:
                   tasks = [] #Empty list 
                   speak("Do you want to clear old tasks (Plz speak YES or NO)")
                   query = takeCommand().lower()
                   if "yes" in query:
                     file = open("tasks.txt","w")
                     file.write(f"")
                     file.close()
                     no_tasks = int(input("Enter the no. of tasks :- "))
                     i = 0
                     for i in range(no_tasks):
                      tasks.append(input("Enter the task :- "))
                      file = open("tasks.txt","a")
                      file.write(f"{i}. {tasks[i]}\n")
                      file.close()
                   elif "no" in query:
                    i = 0
                    no_tasks = int(input("Enter the no. of tasks :- "))
                    for i in range(no_tasks):
                     tasks.append(input("Enter the task :- "))
                     file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close() 
                
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                     )     
                  
                elif "temperature" in query:
                  search = "temperature in Ludhiana"
                  url = f"https://www.google.com/search?q={search}"
                  r  = requests.get(url)
                  data = BeautifulSoup(r.text,"html.parser")
                  temp = data.find("div", class_ = "BNeawe").text
                  speak(f"current{search} is {temp}")
                  
                elif "weather" in query:
                  search = "temperature in Ludhiana"
                  url = f"https://www.google.com/search?q={search}"
                  r  = requests.get(url)
                  data = BeautifulSoup(r.text,"html.parser")
                  temp = data.find("div", class_ = "BNeawe").text
                  speak(f"current{search} is {temp}")
                  
                elif "the time" in query:
                  strTime = datetime.datetime.now().strftime("%H:%M")    
                  speak(f"Sir, the time is {strTime}")
                  
                
                elif "remember that" in query:
                 rememberMessage = query.replace("remember that","")
                 rememberMessage = query.replace("jarvis","")
                 speak("You told me to "+rememberMessage)
                 remember = open("Remember.txt","a")
                 remember.write(rememberMessage)
                 remember.close()
                elif "what do you remember" in query:
                 remember = open("Remember.txt","r")
                 speak("You told me to " + remember.read())  
                 
                elif "open" in query:   
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  
                    
                    
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")    


                if "close window" in query:
                  close_window()
                  speak("I have closed the current window.")   
                
                elif "finally sleep" in query:
                 speak("Going to sleep,Boss")
                 exit()    
                 
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg") 
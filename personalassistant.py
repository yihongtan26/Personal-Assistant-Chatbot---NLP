import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyautogui 
import smtplib
import getpass
from playsound import playsound
import screen_brightness_control as sbc
import pywhatkit as pwt
import outputui
import sys
import random
import randfacts
import pyjokes
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import ctypes
import winshell


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning Boss")
        print("Hello,Good Morning Boss")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon Boss")
        print("Hello,Good Afternoon Boss")
    else:
        speak("Hello,Good Evening Boss")
        print("Hello,Good Evening Boss")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\n ꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷꟷ")
        print("Listening...\n")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"You said : {statement}\n")

        except Exception as e:
            Error = random.randint(1, 2)
            if Error == 1:
                speak("I don't understand', please say that again")
                print("I don't understand, please say that again")
            else:
                speak("Pardon me, please say that again")
                print("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading voice personal assistant")
wishMe()


if __name__=='__main__':
                    
    while True:
        startMsg = random.randint(1, 2)
        if startMsg == 1:
            speak("Tell me how can I help you now?")
            print("Tell me how can I help you now?")
        else:
            speak("What do you want me to do?")
            print("What do you want me to do?")
        statement = takeCommand().lower()
        if statement==0:
            continue

# wikipedia
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            try:
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                print("Sorry I can't find that")
                speak("Sorry I can't find that")

# open youtube
        elif 'open youtube' in statement or 'search youtube' in statement:
            if 'open youtube' in statement:
                statement = statement.replace("open youtube", "")
            elif 'search youtube' in statement:
                statement = statement.replace("search youtube", "")
            searchYT = "https://www.youtube.com/results?search_query=" + statement 
            webbrowser.open_new_tab(searchYT)
            speak("youtube is open now")
            time.sleep(3)
            
# play youtube
        elif 'play youtube' in statement:
            statement = statement.replace("play youtube", "")
            pwt.playonyt(statement)
            speak("Playing " + statement)
            print("Playing " + statement)
            time.sleep(3)

# open google 
        elif 'open google' in statement:
            webbrowser.open("https://www.google.com")
            speak("Google is open now")
            time.sleep(3)

# open gmail
        elif 'open gmail' in statement:
            webbrowser.open("https://mail.google.com/")
            speak("Google Mail is open now")
            time.sleep(3)

# weather
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Tell me the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"] - 274
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in degree celcius is " +
                      str(round(current_temperature, 2)) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in degree celcius is = " +
                      str(round(current_temperature,2)) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

# time now 
        elif 'time now' in statement or 'current time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time now is {strTime}")
            print("the time now is " + strTime)

# news
        elif 'news' in statement or 'headline' in statement:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            speak("Here are the Top Five news from the Google News")
            Num=1
            for news in news_list[:5]:
                print(str(Num) + " - " + news.title.text)
                speak(news.title.text)
                Num += 1

# camera
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

# google search 
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            pwt.search(statement)
            time.sleep(5)

# Wolfram
        elif 'ask' in statement or 'calculator' in statement:
            speak('You can try to ask me computational and geographical questions.')
            question=takeCommand()
            app_id="RYPL4G-YGGXE4JLWL"
            client = wolframalpha.Client('RYPL4G-YGGXE4JLWL')
            res = client.query(question)
            try:
                answer = next(res.results).text
                speak("The answer is " + answer)
                print("The answer is " + answer)
            except Exception:
                speak("Sorry I didn't know about that")
                print("Sorry I didn't know about that")
      
# calculation
        elif "calculate" in statement:
            app_id = "RYPL4G-YGGXE4JLWL"
            client = wolframalpha.Client(app_id)
            indx = statement.lower().split().index('calculate')
            query = statement.split()[indx + 1:]
            res = client.query(' '.join(query))
            try:
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except Exception:
                speak("Sorry I didn't know about that")
                print("Sorry I didn't know about that")
            
# Wolfram what is          
        elif "what is" in statement or "who is" in statement:
            client = wolframalpha.Client("RYPL4G-YGGXE4JLWL")
            res = client.query(statement)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                speak("Sorry, No result is found.")
                print("Sorry, No result is found.")
        
# volume  
        elif 'volume up' in statement:
            pyautogui.press('volumeup')

        elif 'volume down' in statement:
            pyautogui.press('volumedown')

        elif 'volume mute' in statement or 'mute' in statement:
            pyautogui.press('volumemute')
   
# screenshot         
        elif 'screenshot' in statement: 
            pyautogui.screenshot() 
            pyautogui.screenshot('ScreenShot.png')
            speak("Done, you can view the screenshot in your folder.")
      
# send email
        elif 'send an email' in statement:
            speak('Please enter your email')
            ownermail = input("Enter your email: ")
            pswd = getpass.getpass('Password:')
            speak('Who would you like to send to')  
            receivemail = input("Enter receiver email: ")   
            speak('What message would you like me to put')
            msg=takeCommand()
            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com",465)
                server.login(ownermail,pswd)
                server.sendmail(ownermail, 
                                receivemail, 
                                msg)
                server.quit()
                print("E-mail sent.")
                speak("E-mail sent.")
            except Exception:
                print("Sorry. Problems occured, Unable to send email.")
                speak("Sorry. Problems occured, Unable to send email.")
                
# set a timer            
        elif "set a timer" in statement or "set the timer" in statement:
            speak('Please tell me how many minutes you wish to countdown ')
            tm=takeCommand()
            try:
                if "minute" in tm:
                    tm=tm.replace("minute","")
                elif "minutes" in tm:
                    tm=tm.replace("minutes","")
                t = int (tm)
                scd = t*60
                print("Timer start now")
                speak("Timer start now")

                while scd:
                    mins = scd //60
                    secs = scd % 60
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    # sys.stdout.write("\r" + timer)
                    time.sleep(1)
                    scd -= 1 
                speak('Time is up')
                sys.stdout.write("\r" + 'Time is up')
                # playsound('alarm.mp3')
            except Exception:
                print("Sorry, Unable to start a timer")
                speak("Sorry, Unable to start a timer")

# brightness      
        elif "increase brightness" in statement or "brighter" in statement or "brightness up" in statement:
            current = sbc.get_brightness()
            if current==0:
                sbc.set_brightness(10)
            elif current==100:
                speak('Your brightness is the brightess already')
                print('Your brightness is the brightess already')
            else:
                bright = current+10 
                sbc.set_brightness(bright)

        elif "decrease brightness" in statement or "dimer" in statement or "brightness down" in statement:
            current = sbc.get_brightness() 
            if current==0:
                sbc.set_brightness(0)
                speak('Your brightness is the dimest already')
                print('Your brightness is the dimest already')
            else:
                dim = current-10 
                sbc.set_brightness(dim)
 
# launch app               
        elif 'launch' in statement or 'open' in statement:
            speak("What app do you want to launch?")
            app=takeCommand()
            os.system(app)
 
# facts           
        elif 'fact' in statement:
            fact=randfacts.get_fact()
            print("Fast facts : " + fact)
            speak("Fast facts : " + fact)

# jokes            
        elif 'joke' in statement:
            speak("No problem boss, let me tell you a joke.")
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
            speak("Funny right? Ha Ha Ha")

# notes            
        elif "write a note" in statement:
            speak("What should i write, Boss")
            note = takeCommand()
            file = open('NewNotes.txt', 'w')
            speak("Do you want to include date and time?")
            print("Do you want to include date and time?")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm or 'alright' in snfm:
                strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                file.write(note)
                file.write(" -:- ")
                file.write(strTime)
            else:
                file.write(note)
            speak("The Note is done.")
            print("The Note is done.")

        elif "show" and "note" in statement or "read" and "note" in statement:
            try:
                speak("No problem Boss. Reading Notes.")
                file = open("NewNotes.txt", "r")
                note=file.read(50)
                speak(note)
                print(note)
            except Exception:
                speak("Sorry, No notes was found.")
                print("Sorry, No notes was found.")
            
# empty bin
        elif "empty" and "recycle bin" in statement:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin had been cleared")
            print("Recycle Bin had been cleared")
  
# where is          
        elif "where is" in statement:
            statement = statement.replace("where is", "")
            location = statement
            speak(location + "will be search on Google Maps")
            print(location + "will be search on Google Maps")
            webbrowser.open("https://www.google.nl/maps/place/" + location)
            
# general question           
        elif "i love you" in statement:
            reply = random.randint(1, 2)
            if reply == 1:
                speak("You are such a sweet person")
                print("You are such a sweet person")
            else:
                speak("I will always here for you my lover")
                print("I will always here for you my lover")
                
# how are you  (general)              
        elif 'how are you' in statement:
            print("I am fine, Thank you")
            speak("I am fine, Thank you")
            print("How are you, Boss")
            speak("How are you, Boss")

        elif 'fine' in statement or "I" and "am good" in statement:
            print("It's good to know that you're fine")
            speak("It's good to know that you're fine")

# Self info
        elif 'who are you' in statement or 'what can you do' in statement or 'introduce yourself' in statement:
            print('I am your voice personal assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail, take a photo, search wikipedia, predict weather' 
                  'in different cities , get top headline news and you can ask me computational or geographical questions too!')
            speak('I am your voice personal assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail, take a photo, search wikipedia, predict weather' 
                  'in different cities , get top headline news and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            print("I was built by Two Bosses, Xin Ee and Yi Hong")
            speak("I was built by Two Bosses, Xin Ee and Yi Hong")
            
# lock windows               
        elif 'lock' and 'window' in statement:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
       
# restart
        elif "restart" in statement:
            speak("Your device will restart in a short while.")
            subprocess.call(["shutdown", "/r"])
			
# hibernate            
        elif "hibernate" in statement or "sleep" in statement:
            speak("Hibernating")
            subprocess.call(["shutdown", "/h"])
            
# Log off
        elif "log out" in statement or "sign out" in statement:
            speak("Ok , your pc will log out in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

# schedule shut down
        elif "schedule my pc to shut down" in statement:
            speak('After how long would you like to shut down')
            print('After how long would you like to shut down?')
            schedule=takeCommand()
            try:
                if 'minutes' in schedule:
                    s_time  = schedule.replace("minutes","")
                    s_time = int(s_time) * 60
                elif 'minute' in schedule:
                    s_time  = schedule.replace("minute","")
                    s_time = int(s_time) * 60
                elif 'seconds' in schedule:
                    s_time  = schedule.replace("seconds","")
                    s_time = int(s_time)
                elif 'second' in schedule:
                    s_time  = schedule.replace("second","")
                    s_time = int(s_time)
                speak('Your pc will be shut down after' + schedule + 'later')
                pwt.shutdown(s_time)
            except Exception:
                speak("Sorry, unable to schedule.")
                print("Sorry, unable to schedule.")

# cancel shut down
        elif "cancel shutdown schedule" in statement:
            pwt.cancel_shutdown()
            speak('Your scheduled shutdown has been cancel')
            print('Your scheduled shutdown has been cancel')

# send a message
        elif "Send" and "message" in statement:
            speak('What phone number would you like to send to')
            print('What phone number would you like to send to')
            telNo = input("Enter phone number: ")
            telNo = "+60" + telNo
            speak('what message would you like to send')
            print('what message would you like to send')
            msg=takeCommand()
            pwt.sendwhatmsg_instantly(telNo, msg)

# bye     
        if "bye" in statement or "goodbye" in statement or "stop" in statement:
            speak("Hope you have a nice day")
            print("Hope you have a nice day")
            speak('Voice Personal Assistant is shutting down, Good bye')
            print('Voice Personal Assistant is shutting down, Good bye')
            break

time.sleep(3)
                    
    

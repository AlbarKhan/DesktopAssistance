from asyncio import QueueEmpty
import imp
from logging import shutdown
from msvcrt import kbhit
from turtle import speed
from email.message import EmailMessage
from tkinter import Scale
import typing
from PyQt5.QtWidgets import QWidget
from numpy import safe_eval
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import cv2
import json
import numpy as np
import pyautogui as p
import pygame
import pywhatkit as kit
import requests
import sys
import pyjokes
import os.path
import smtplib
import webbrowser
import os
import smtplib

from PyQt5 import QtWidgets, QtCore ,QtGui
from PyQt5.QtCore import QTimer ,QTime , QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from albargui import Ui_albargui


hour_now = int(datetime.datetime.now().strftime("%H"))
minute_now =int(datetime.datetime.now().strftime("%M"))



'''recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cacadePath ="haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cacadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

id =2
names =['','sufiyan']
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret ,img = cam.read()

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW),int(minH)),
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),2)
        id,accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

        if (accuracy < 100):
            id = names[id]
            accuracy = "{0}%".format(round(100 - accuracy))
            #TaskExecution()
        else:
            id = "unknow"
            accuracy="{0}%".format(round(100 - accuracy))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)

    cv2.imshow('camera',img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    

print("Thanks for using this program.")
cam.release()
cv2.destroyAllWindows()'''


def TaskExecution():
    wishMe()
    if 1:

        p.press('esc')
        Speak("verification sucessful")
        Speak("Welcome to Sufiyan sir")
   
    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon")

    else:
        Speak("Good Evening!")


    #Speak("verification sucessful")
    Speak("Welcome to Sufiyan sir")
    Speak("Iam Javris maam. Please tell me how may help you")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()


    def takeCommand(self):
        # It Take microphone input from the user and return string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.8
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said:{query}\n")

        except Exception as e:
            # print(e)

            print("Say that again please...")
            return "None"
        return query


    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('shaikhsufiyan0045@gmail.com', 'Sufiyan@123')
        server.sendmail('shaikhsufiyan0045@gmail.com', to, content)
        server.close()


    def TaskExecution(self):
        wishMe()
        while True:
           
           self. query = self.takeCommand().lower()
        # login for executed taks
           if 'wikipedia' in self.query:
                Speak('Searching wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                Speak("According to wikipedia")
                print(results)
                Speak(results)
           elif 'how are you' in self.query:
                Speak("I am Fine sir,How can i help you")
           elif 'hello' in self.query:
                Speak("Hello sir")
           elif "What are you doing" in self.query:
                Speak("Iam a waiting for command")
           elif "open command" in self.query:
                os.system("start cmd")
           elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
                Speak("opening youtube")
           elif 'close youtube' in self.query:
                Speak('yes sir.closing youtube')
                os.system('taskkill /f /im msedge.exe')
           elif 'tell me joke' in self.query:
                joke = pyjokes.get_joke()
                Speak(joke)
            # elif 'open google' in query:
            #     webbrowser.open("google.com")
           elif 'open google' in self.query:
                Speak("sir .what should i open in google")
                cm=self.takeCommand().lower()
                webbrowser.open(cm)
           elif 'close google' in self.query:
                Speak('yes sir.closing google')
                os.system('taskkill /f /im msedge.exe')
            #below code is for sending message from whatsapp by using 'pywhatkit' and 'web browser module'
           elif 'send message shadab bhai' in self.query:
                Speak("what should i send")
                minute=minute_now+2
                speaking=self.takeCommand().lower()
                kit.sendwhatmsg("+919820038805",f"{speaking}",hour_now,minute)
           elif 'open stackoverflow' in self.query:
                webbrowser.open("open stackoverflow.com")
           elif 'open firefox' in self.query:
                webbrowser.open("open firefox")
           elif 'open visual studio' in self.query:
                codePath = "C:\\Program Files\Microsoft Visual Studio\\2022\Community\\Common7\\IDE\\devenv.exe"
                os.startfile(codePath)
           elif 'close visual studio' in self.query:
                Speak("okay sir . closing visual studio")
                os.system("taskkill /f /im visual studio.exe")
           elif 'open data' in self.query:
                codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\MySQL"
                os.startfile(codePath)
           elif "camera" in self.query or "take a photo" in self.query:
                os.capture(0, "Jarvis Camera ", "img.jpg")
           elif 'open idea' in self.query:
                idcode = "C:\\Users\\ADMIN\\Downloads"
                os.startfile(idcode)
           elif 'open Database' in self.query:
                ddpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
                os.startfile(ddpath)
            #elif "restart" in query:
                #subprocess.call(["shutdown", "/r"])
           elif 'open powerpoint' in self.query:
                pptpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
                os.startfile(pptpath)
           elif 'open microsoft' in self.query:
                wordpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
                os.startfile(wordpath)
           elif 'play music' in self.query:
                music_dir = 'E:\\Aiassitant'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
           elif 'what is time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                Speak(f"sir The time is:{strTime}")
           elif 'open studio' in self.query:
                codePath = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
           elif 'close studio' in self.query:
                Speak("okay sir Closing code")
                os.system("taskkill /f /im code.exe")
           elif 'set alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir = "E:\\music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))
           elif 'open Excel' in self.query:
                codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
                os.startfile(codePath)
           elif 'shut down the system' in self.query:
                os.system("shutdown /s /t 5")
           elif 'restart the system' in self.query:
                os.system("shutdown /s /t 5")
           elif 'sleep the system' in self.query:
                os.system("rundl132.exe powrprof.dil,SetSuspendState 0,1,0")
           elif 'close microsoft' in self.query:
                Speak("Thanks for using me sir, have a good day")
                os.system("taskkill /f /im microsoft.exe")
           elif 'you can sleep ' in self.query:
                Speak("Thank for using me sir, have good day")
                sys.exit()
           elif "shutdown system " in self.query:
                Speak("Are You sure want to shutdown")
                shutdown = input("Do you wish to shutdown your computer? (yes/no}")
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")
           elif 'Search on google' in self.query:
                    Speak('What do you want to search on Google, sir?')
           elif "send whatsapp message" in self.query:
                    Speak('On what number should I send the message sir? Please enter in the console: ')
                    number = input("Enter the number: ")
                    Speak("What is the message sir?")
                    # message = take_user_input().lower()
                    # send_whatsapp_message(number, message)
                    Speak("I've sent the message sir.")
            # elif "play a game" in query:cls
            #     from game import game_play
            #     game_play()
           elif 'ip address' in self.query:
                from requests import get
                ip = get('https://api.ipify.org').text
                Speak(f"your IP address is {ip}")
            # elif 'open' in query:
            #     query = query.replace("open","")
            #     query = query.replace("javis","")
            #     #pyautogui.press("super")
            #     pyautogui.typewrite(query)
            #     pyautogui.sleep(2)
            #     pyautogui.press("enter")
           elif 'screenshot' in self.query:
                import pyautogui
                im = pyautogui.screenshot()
                im.save("tt.jpg")
           elif 'click my photo' in self.query:
                pyautogui.press("enter")
                #pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                Speak("SMILE")
                pyautogui.press("enter")
           elif 'send to email' in self.query:
                try:
                    Speak("what should I say")
                    content = self.takeCommand()
                    to = "shaikhsufiyan0045@gmail.com"
                    self.sendEmail(to, content)
                    Speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    Speak("sorry my friend sufiyan bhai.Iam not able to send this email")



startExecution = MainThread()
class Main(QMainWindow):
    def __init__(self):
          super().__init__()
          self.ui = Ui_albargui()
          self.ui.setupUi(self)
          self.ui.pushButton.clicked.connect(self.startTask)
          self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
         self.ui.movie = QtGui.QMovie("C:/Users/ADMIN/Downloads/7LP8.gif")
         self.ui.label.setMovie(self.ui.movie)
         self.ui.movie.start()
         startExecution.start()
    


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
# akakakakakakaka
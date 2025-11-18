# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:51:13 2025

@author: HP
"""

import speech_recognition as sr
import webbrowser, os
speech = sr.Recognizer()

def voice_to_text():
    inp=''
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            inp = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return inp

def browse(inp):
    if "open" in inp:
        print("Open in your voice!!!")
        if "game" in inp:
            game = os.path.join(os.getcwd(),'game.html')
            webbrowser.open(f"file://{game}")
        elif "calculator" in inp:
            os.system('calc')
        elif 'labview' in inp:
            os.system(r"start C:\Program Files (x86)\National Instruments\LabVIEW 2020\LabVIEW.exe")
        else:
            inp = inp.replace('open ','')
            os.system(f"start {inp}") 
            
    if "search" in inp:
        search = inp.replace("search ",'')
        webbrowser.open(f"https://www.google.com/search?q={search}")
    if "browse" in inp:
        search = inp.replace("browse ",'')
        webbrowser.open(f"https://{search}.com")
    if "close" in inp:
        print("Closing as request!!!")
        app = inp.replace('close ','').strip()
        
        process_map={
            'calculator':'calc.exe',
            'notpad':'notepad.exe',
            'edge':'msedge.exe',
            'brave':'brave.exe',
            'matlab':'matlab.exe',
            'arduino':'arduino.exe',
            'labview':'labview.exe'
            }
        process_name = process_map.get(app.lower(),f'{app}.exe')
        try:
            os.system(f'taskkill /IM {process_name} /F')
            print(f"Closed app {app}")
        except Exception as e:
            print(f"Could not close {app}:{e}")


while True:
    print("Python is listening...")
    inp = voice_to_text().lower()
    print(f"You just said: {inp}",flush=True)
    if inp=='stop listening':
        print("Goodbye!!")
        break
    else:
        browse(inp)
        continue
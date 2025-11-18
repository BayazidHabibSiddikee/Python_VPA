# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 14:26:50 2025

@author: HP
"""

import speech_recognition as sr
import time, webbrowser, os

speech = sr.Recognizer()


print("Python is listening.......")
inp=""

with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    try:
        audio = speech.listen(source)
        inp = speech.recognize_google(audio)
        time.sleep(2)
        print(f"You just said {inp}")

        if "open" in inp:
            print("Open in your voice!!!")
            if "game" in inp:
                game = os.path.join(os.getcwd(),'game.html')
                browse = webbrowser.open(f"file://{game}")
            elif "calculator" in inp:
                os.system('calc')
            else:
                inp = inp.replace('open ','')
                os.system(f"start {inp}")
                
        if "search" in inp:
            search = inp.replace("search ",'')
            browse=webbrowser.open(f"https://www.google.com/search?q={search}")
            
    except Exception as e:
        print(f"Error {e}")
        
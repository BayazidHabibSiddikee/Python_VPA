# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 19:44:11 2025

@author: HP
"""

import os, platform, pathlib

import speech_recognition as sr

speech = sr.Recognizer() #Taking instances from sr speech as Recognizer class
directory = pathlib.Path.cwd()

def voice_to_text():
    voice = ''
    with sr.Microphone() as source: #opening microphone
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source,timeout=5)
            voice = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.WaitTimeoutError:
            pass
        except sr.RequestError:
            pass
    return voice.lower()

def open_file(filename):
    if platform.system()=='Windows':
        os.system(f"explorer {directory}\\files\\{filename}")
    elif platform.system()=='Darwin':
        os.system(f"open {directory}/files/{filename}")
    else:
        os.system(f"xdg-open {directory}/files/{filename}")


while True:
    print("Python is listening....",flush=True)
    inp = voice_to_text()
    print(f"You just said: {inp}")
    
    if inp=='stop listening':
        print("Good bye!!!")
        break
    elif "open pdf" in inp:
        inp = inp.replace("open pdf ",'')
        myfile = f'{inp}.pdf'
        open_file(myfile)
        continue 
    elif "open word" in inp :
         inp = inp.replace("open word ",'')
         myfile = f'{inp}.docx'
         open_file(myfile)
         continue
    elif "open excel" in inp:
        inp = inp.replace("open excel ",'').strip()
        myfile = f'{inp}.xlsx'
        open_file(myfile)
        continue  
    elif "open audio" in inp:
        inp = inp.replace("open audio ",'').strip()
        myfile = f'{inp}.opus'
        open_file(myfile)
        continue     
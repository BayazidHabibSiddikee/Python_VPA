# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:17:23 2025

@author: HP
"""

import speech_recognition as sr
import time

speech = sr.Recognizer()
while True:
    print("Python is listening...")
    inp = ''
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source,2)
        try:
            audio = speech.listen(source)
            inp = speech.recognize_google(audio,language='fr-FR')
            time.sleep(0.5)
            
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    print(f"You just said: {inp}",flush=True)
    if "stop listening" in inp:
        print("Thank u and goodbye!!!")
        break
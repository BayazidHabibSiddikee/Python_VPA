# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 13:03:29 2025

@author: HP
"""

from mysr import voice_to_text
import platform

if platform.system()=='Windows':
    import pyttsx3
    engine = pyttsx3.init()
else:
    import os
    
while True:
    print("Python is listening...")
    inp = voice_to_text()
    if inp=='stop listening':
        print("Good bye!!!!")
        if platform.system()=='Windows':
            engine.say(f"okkk  Good bye!")
            engine.runAndWait()
        else:
            os.system(f'gtts-cli --nocheck "Good bye!" | mpg123 -q -')
        break
    else:
        print(f"You just said {inp}")
        if platform.system()=='Windows':
            engine.say(inp)
            engine.runAndWait()
        else:
            os.system(f"gtts-cli --nocheck '{inp}' |mpg123 -q -")
        continue
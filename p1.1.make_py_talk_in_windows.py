# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 02:00:29 2025

@author: HP
# %%
"""

import pyttsx3
from mysr import voice_to_text

engine = pyttsx3.init()

while True:
    print("Python is listening....",flush=True)
    inp = voice_to_text()
    engine.say(inp)
    print(f"You said {inp}")
    engine.runAndWait()
    if "stop" in inp:
        engine.say("Good bye!!!!!!")
        engine.runAndWait()
        break
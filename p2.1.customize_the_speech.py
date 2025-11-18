# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:56:52 2025

@author: HP
"""

#See the default setting
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
    

rate = engine.getProperty('rate')
print("The default rate: ",rate)

vol = engine.getProperty('volume')
print("The default rate: ",vol)
engine.setProperty('rate',130) #default 200
engine.setProperty('volume', 0.8)
engine.say("This is a test of my speech id, speed, and volume.")
engine.runAndWait()


engine = pyttsx3.init()
#change setting
voice_id=1 #0 or 1 only
engine.setProperty('voice',voices[voice_id].id)
engine.setProperty('rate',150)
engine.setProperty('volume',1.2)

engine.say("This is a test of my speech id, speed, and volume.")
engine.runAndWait()
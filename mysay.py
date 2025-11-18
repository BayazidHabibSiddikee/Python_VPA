# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:34:50 2025

@author: HP
"""

import platform

#If you are using windows
if platform.system() =='Windows':
    import pyttsx3
    try:
        engine=pyttsx3.init()
    except ImportError:
        pass
    except RuntimeError:
        pass
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',130)   
    engine.setProperty('volume',1.2)
    
    def print_say(txt):
        print(txt)
        engine.say(txt)
        engine.runAndWait()

#For using MAC or linux
if platform.system() =='Darwin' or platform.system()=='Linux':
    import os
    def print_say(txt):
        print(txt)
        text = txt.replace('"','')
        text = txt.replace("'","")
        os.system(f'gtts-cli --nocheck "{text}" |mpg123 -q -')
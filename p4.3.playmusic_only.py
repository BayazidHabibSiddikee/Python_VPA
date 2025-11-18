# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 12:22:19 2025

@author: HP
"""
from pygame import mixer
import time
mixer.init()

try:
    mixer.music.load('files/112.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
except:
    print("file not found")
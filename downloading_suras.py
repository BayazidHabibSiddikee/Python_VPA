# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 05:00:28 2025

@author: HP
"""
#https://download.quranicaudio.com/quran/abdullaah_3awwaad_al-juhaynee/001.mp3
file = 'https://download.quranicaudio.com/quran/abdullaah_3awwaad_al-juhaynee/'

import os

filename = [str(x) for x in range(104,115)] # 104105,106

for a in filename:
    try:
        files = file + f"{a}.mp3"
        print(files)
        os.system(f"curl -O {files}")
    except:
        print("Could not found!!!")
    
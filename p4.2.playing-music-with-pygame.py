# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 11:51:51 2025

@author: HP
"""

import os, random, time
from pygame import mixer
from mptpkg import voice_to_text, print_say

#Start an loop to take your voice
while True:
    print_say("How may I help you?")
    inp = voice_to_text()
    print_say(f"You said {inp}")
     #stop the script 
    if inp and 'stop' in inp:
         print_say("good bye")
         break
    elif inp and 'play' in inp:
         inp = inp.replace('play ','')
         names = inp.split()
         first = names[0]
         if len(names)>1:
             last = names[1]
         else:
             last = first
             
         '''Create a list to contain song'''
         mysongs = []
         with os.scandir("./files") as f:
             for file in f:
                 if (first in file.name or last in file.name)\
                     and "mp3" in file.name:
                     mysongs.append(file.name)
                     
             #Randomly select one from the file
             mysong = random.choice(mysongs)
             print_say(f"Play the song {mysong} for you")
             mixer.init()
             try:
                 mixer.music.load(f"./files/{mysong}")
                 mixer.music.play()
            
            # Keep the program running while music plays
                 while mixer.music.get_busy():
                     time.sleep(1)
            
                 print_say("Song finished. What else can I do for you?")
        
             except Exception as e:
                 print_say(f"Error playing song: {e}")
             mixer.music.load(f"./files/{mysong}")
             mixer.music.play()            
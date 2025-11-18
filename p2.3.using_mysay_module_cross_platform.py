# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:45:06 2025

@author: HP
"""

from mysr import voice_to_text
from mysay import print_say

while True:
    print("Python is listening...")
    inp = voice_to_text()
    #print('\b'*len(inp),end='',flush=True)
    if inp=='stop listening':
        print_say("Good bye!!!")
        break
    else:
        print_say(inp)
        #print('\b'*len(inp),end='',flush=True)
        continue

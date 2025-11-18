# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 22:14:07 2025

@author: HP
"""

from mysr import voice_to_text

while True:
    print("Python is listening...")
    inp = voice_to_text()
    print(f"You entered {inp}")
    
    if inp=='stop listening':
        print("Good bye!!!!!")
        break
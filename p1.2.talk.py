# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 02:17:41 2025
@author: HP
"""
import pyttsx3
import time

# Initialize engine outside the loop
engine = pyttsx3.init()

# Optional: Set properties for better performance
engine.setProperty('rate', 150)  # Speed of speech (default 200)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

while True:
    inp = input("What do you want to convert to speech?\n")
    
    if inp.lower() == "done":
        print(f"You just typed in '{inp}'; goodbye!")
        engine.say(f"You just typed in {inp}; goodbye!")
        engine.runAndWait()
        time.sleep(1)  # Give engine time to finish
        break
    
    elif inp.strip():  # Only process non-empty input
        print(f"You just typed in '{inp}'")
        engine.say(f"You just typed in {inp}")
        engine.runAndWait()
        time.sleep(0.5)  # Small delay between iterations
    
    else:
        print("Please type something!")
        continue

# Clean shutdown
engine.stop()
print("Program ended")
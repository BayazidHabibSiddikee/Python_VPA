# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 13:46:04 2025

@author: HP
"""

from mptpkg import voice_to_text, print_say
#Voice control wikipedia
import wikipedia, threading, sys

ex = False
def takenap():
    global ex
    inp = voice_to_text()
    if inp and 'stop' in inp.lower():
        ex = True
        sys.exit(1)
def know():  
    global ex
    if ex:
        sys.exit()
    print_say("What do you want to know???\n>>>")
    query = voice_to_text()
    if query:
        if 'stop' in query:
            ex=True
            sys.exit()
        print_say(f"You said {query}")
        try:
            answer = wikipedia.summary(query, sentences=3)
            print_say(answer)
        except:
            print_say("Could not found the query")    
    
def main():
    print_say("Welcome to wikipedia in python")
    global ex
    #a = threading.Thread(target=takenap,daemon=True)
    #a.start()
    while not ex:
        if ex:
            sys.exit(1)
        know()
    
if __name__=='__main__':
    main()
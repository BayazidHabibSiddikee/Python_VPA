# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 19:57:15 2025

@author: HP
"""

from mptpkg import voice_to_text
from mptpkg import print_say

import sys, time

print_say('''Think of an integer,
          bigger or equal to 1 smaller or equal to 9,
          and write it in a piece of paper''')
print_say("You have 5 second to write your number down")
time.sleep(5)

print_say('''Now let\' start the game. I will guess the number you wrote until you say
          too high, too small or that is right''')

print_say("is it 5")
while True:
    re1 = voice_to_text().lower()
    print_say(f"You said {re1}")
    if re1 in ("too high", "too small", 'that is right'):
        continue
    if re1=='That is right':
        print_say("Yay, lucky me!!!")
    elif re1=='too high':
        print_say("Is it 3???")
        while True:
            re2 = voice_to_text().lower()
            print_say(f"You said {re2}")
            if re2 in ("too high", "too small", 'that is right'):
                break
        if re2=='That is right':
            print_say("Yay, lucky me!!!")
            sys.exit()
        elif re2=='too small':
            print_say("it is 4!")
            sys.exit()
        elif re2=='too high':
            print_say("is it one")
            #For third guess
            while True:
                re3 = voice_to_text().lower()
                print_say(f"You said {re3}")
                if re3 in ("too high", "too small", 'that is right'):
                    break
            if re3=='That is right':
                print_say("Yay, lucky me!!!")
                sys.exit()
    # If you say "too small", the computer keeps guessing 
    elif re1 == "too small":
        # The computer guesses 7 the second round
        print_say("Is it 7?")
        # The computer is trying to get your response to the second guess
        while True:
            re2 = voice_to_text()
            print_say(f"You said {re2}")
            if re2 in ("too high", "that is right", "too small"):
                break
        # If the second guess is right, game over
        if re2 == "that is right":
            print_say("Yay, lucky me!")
            sys.exit
        # If the second guess is too high, the computer knows it's 6
        elif re2 == "too high":
            print_say("Yay, it is 6!")
            sys.exit
        # If the second guess is too small, the computer guesses the third time
        elif re2 == "too small":
            # The third guess is 8
            print_say("Is it 8?")
            while True:
                re3 = voice_to_text ()
                print_say(f"You said {re3}")
                if re3 in ("too high", "that is right", "too small"):
                    break
                # If the third guess is too small, the computer knows it's 9
            if re3 == "too small":
                print_say("It is 9!")
                sys.exit
                # If the third guess is right, game over
            elif re3 == "that is right":
                print_say("Yay, lucky me!")
                sys.exit    
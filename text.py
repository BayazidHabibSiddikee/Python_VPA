# -*- coding: utf-8 -*-
"""
Text-to-Speech for Spyder (compatible version)
Run in command prompt, NOT in Spyder!
"""
import pyttsx3
import time

def initialize_engine():
    """Initialize engine with safe settings"""
    engine = pyttsx3.init()
    # Reinitialize each time to avoid kernel issues
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    return engine

def main():
    print("\n=== Text-to-Speech Converter ===")
    print("Type text and press Enter to hear it spoken")
    print("Type 'done' to exit\n")
    
    iteration = 0
    
    while True:
        try:
            inp = input("What do you want to convert to speech?\n>>> ")
            
            if not inp.strip():
                print("Please type something!")
                continue
            
            if inp.lower() == "done":
                # Create fresh engine for goodbye message
                engine = initialize_engine()
                print(f"You just typed in '{inp}'; goodbye!")
                engine.say(f"Goodbye!")
                engine.runAndWait()
                engine.stop()
                break
            
            else:
                # Create fresh engine each iteration (fixes kernel issues)
                engine = initialize_engine()
                print(f"You just typed in '{inp}'")
                
                # Speak the text
                engine.say(inp)
                engine.runAndWait()
                engine.stop()
                
                iteration += 1
                time.sleep(0.5)
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
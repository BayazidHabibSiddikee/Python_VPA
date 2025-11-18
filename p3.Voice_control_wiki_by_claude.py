# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 14:10:33 2025

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 13:46:04 2025
@author: HP
"""
from mptpkg import voice_to_text, print_say
import wikipedia
import threading
import sys
import time

# Global exit flag
exit_flag = False

def takenap():
    """Background thread listening for 'stop' command"""
    global exit_flag
    while not exit_flag:
        inp = voice_to_text()
        if inp and 'stop' in inp.lower():
            print_say("Stopping the program. Goodbye!")
            exit_flag = True
            sys.exit(0)
        time.sleep(0.5)  # Small delay to avoid busy waiting

def know():  
    """Get Wikipedia information based on voice query"""
    global exit_flag
    
    if exit_flag:
        return
    
    print_say("What do you want to know?")
    query = voice_to_text()
    
    if not query:
        print_say("I didn't hear anything. Please try again.")
        return
    
    if 'stop' in query.lower():
        print_say("Stopping the program. Goodbye!")
        sys.exit(0)
    
    print_say(f"You said: {query}")
    print_say("Searching Wikipedia...")
    
    try:
        # Get summary with sentence limit to avoid too long responses
        answer = wikipedia.summary(query, sentences=3)
        print_say(answer)
        
        # Ask if user wants more info
        print_say("Do you want to hear more? Say yes or no.")
        response = voice_to_text()
        
        if response and 'yes' in response.lower():
            full_answer = wikipedia.summary(query)
            print_say(full_answer)
    
    except wikipedia.exceptions.DisambiguationError as e:
        print_say(f"Your query is ambiguous. Did you mean one of these: {', '.join(e.options[:3])}")
    
    except wikipedia.exceptions.PageError:
        print_say(f"Sorry, I couldn't find any information about {query} on Wikipedia.")
    
    except Exception as e:
        print_say(f"An error occurred: {str(e)}")

def main():
    """Main function"""
    global exit_flag
    
    print_say("Welcome to Voice-Controlled Wikipedia!")
    print_say("Say 'stop' anytime to exit the program.")
    
    # Start the exit listener thread once
    exit_thread = threading.Thread(target=takenap, daemon=True)
    exit_thread.start()
    
    # Main loop
    while not exit_flag:
        try:
            know()
            
            if not exit_flag:
                print_say("Do you want to search again? Say yes or no.")
                response = voice_to_text()
                
                if response and 'no' in response.lower():
                    print_say("Thank you for using Voice Wikipedia. Goodbye!")
                    break
        
        except KeyboardInterrupt:
            print_say("Program interrupted. Goodbye!")
            break
        
        except Exception as e:
            print(f"Error in main loop: {e}")
            continue

if __name__ == '__main__':
    main()
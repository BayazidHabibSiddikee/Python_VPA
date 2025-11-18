# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 11:51:13 2025
@author: HP
"""
import speech_recognition as sr
import webbrowser, os
import subprocess

speech = sr.Recognizer()

# Map voice commands to actual executable paths/names
APP_MAP = {
    'calculator': 'calc.exe',
    'calc': 'calc.exe',
    'notepad': 'notepad.exe',
    'note': 'notepad.exe',
    'edge': 'msedge.exe',
    'brave': 'brave.exe',
    'chrome': 'chrome.exe',
    'matlab': 'matlab.exe',
    'arduino': 'arduino.exe',
    'labview': 'labview.exe',
    'proteus': 'proteus.exe',
}

def voice_to_text():
    inp = ''
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source, timeout=5)
            inp = speech.recognize_google(audio)
            inp = inp.lower().strip()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"API error: {e}")
        except sr.WaitTimeoutError:
            print("No speech detected")
    return inp

def open_app(app_name):
    """Open an application by name"""
    app_name = app_name.replace('open ', '').strip()
    
    if app_name in APP_MAP:
        try:
            subprocess.Popen(APP_MAP[app_name])
            print(f"Opening {app_name}...")
        except Exception as e:
            print(f"Could not open {app_name}: {e}")
    else:
        print(f"'{app_name}' not in my app list. Try: {', '.join(list(APP_MAP.keys())[:5])}...")

def close_app(app_name):
    """Close an application by name"""
    app_name = app_name.replace('close ', '').strip()
    
    if app_name in APP_MAP:
        process_name = APP_MAP[app_name]
        try:
            os.system(f'taskkill /IM {process_name} /F')
            print(f"Closed {app_name}")
        except Exception as e:
            print(f"Could not close {app_name}: {e}")
    else:
        print(f"'{app_name}' not in my app list")

def browse(inp):
    """Handle browse, search, open, and close commands"""
    
    if "close" in inp:
        # Extract app name after "close"
        app_name = inp.replace('close ', '').strip()
        close_app(app_name)
    
    elif "open" in inp:
        # Extract app name after "open"
        app_name = inp.replace('open ', '').strip()
        
        # Check if it's a known app
        if app_name in APP_MAP:
            open_app(inp)
        elif "game" in inp:
            game = os.path.join(os.getcwd(), 'game.html')
            webbrowser.open(f"file://{game}")
        else:
            print(f"Unknown app: {app_name}")
    
    elif "search" in inp:
        search_term = inp.replace("search ", '').strip()
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        print(f"Searching for: {search_term}")
    
    elif "browse" in inp:
        site = inp.replace("browse ", '').strip()
        webbrowser.open(f"https://{site}.com")
        print(f"Browsing: {site}")

def main():
    print("\n=== Voice Control System ===")
    print("Commands: 'open [app]', 'close [app]', 'search [term]', 'browse [website]', 'stop listening'")
    print("Available apps:", ', '.join(list(APP_MAP.keys())))
    print("=" * 30 + "\n")
    
    while True:
        print("Listening...")
        inp = voice_to_text()
        
        if not inp:
            continue
        
        print(f"You said: {inp}")
        
        if inp == 'stop listening':
            print("Goodbye!!")
            break
        else:
            browse(inp)

if __name__ == "__main__":
    main()
import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, pyautogui, threading
engine = pyttsx3.init()
engine.say("Hello, how can I assist you?")
pyautogui.alert("Voice Assistant Activated")
listener = sr.Recognizer()

def talk1(text):
    #engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)  # Speed of speech (default 200)
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    engine.say(text)
    #engine.runAndWait()

def talk2(text):
    #engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    #engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"Recognized command: {command}")
                talk2(f"You said: {command}")
            return command
    except Exception as e:
        print(f"Error {e}")
        return ''

def show_alert(text,title="Info"):
    pyautogui.alert(text,title=title)

def run_alexa():
    command = 'wiki Einstein' #take_command()
    '''command = 'play Tailor swift' #take_command()
    command="time?"
    command = 'wiki python'
    command = 'joke' '''
    print(command)
    if 'play' in command:
        command = command.replace('play', '')
        #import webbrowser
        #webbrowser.open(f"https://www.youtube.com/results?search_query={command}")
        talk1(f"Playing {command} on YouTube")
        print(f"Playing {command} on YouTube")
        pywhatkit.playonyt(command)
    elif 'time' in command:
        import datetime
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk1("The current time is " + time)
        print("The current time is " + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        talk1("Today's date is " + date)
        print("Today's date is " + date)
    elif 'are you single' in command:
        talk1("I am in a relationship with WiFi")
        print("I am in a relationship with WiFi")  
    elif 'wiki' in command:
        try:
            command = command.replace('wiki', '')
            info = wikipedia.summary(command, sentences=5)
            threading.Thread(target=talk2,args=(info,)).start()
            threading.Thread(target=print,args=(info,)).start()
            threading.Thread(target=show_alert,args=(info,"Wikipedia Info")).start()
            #print(info)
            #pyautogui.alert(info,title=("Wikipedia Info"))
        except:
            pass
    elif 'who the heck is' in command:
        try:
            command = command.replace('who the heck is', '')
            info = wikipedia.summary(command, sentences=1)
            threading.Thread(target=talk1,args=(info,)).start()
            threading.Thread(target=print,args=(info,)).start()
            threading.Thread(target=show_alert,args=(info,f'Who the heck is {command}')).start()
            #talk1(info)
            #print(info)
        except:
            pass
    elif 'joke' in command:
        import pyjokes
        joke = pyjokes.get_joke()
        threading.Thread(target=talk1,args=(joke,)).start()
        threading.Thread(target=show_alert,args=(joke,'Python Jokes')).start()
        threading.Thread(target=print,args=(joke,)).start()
        talk1(joke)
        pyautogui.alert(joke,title=("joke"))
        print(joke)
    else:
        talk2("Please say the command again.")
        print("Please say the command again.")    
    #talk1("Wow, that was amazing!")

def main():
    while True:
        command = ' hygf'#take_command()
        if command:
            run_alexa()
            engine.runAndWait()

def sleep_alexa():
    import time
    time.sleep(200)
    import sys
    sys.exit()

if __name__=='__main__':
    threading.Thread(target=main(),args=()).start()
    threading.Thread(target=sleep_alexa,args=()).start()
    talk1("Wow, that was amazing!")

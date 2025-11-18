import wikipedia
import pyautogui
import threading, pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
def talk2(text):
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def wiki_search(command):
    command = command.replace('wiki', '').strip()
    info = wikipedia.summary(command, sentences=5)

    # Define tasks
    def speak():
        talk2(info)

    def show_alert():
        pyautogui.alert(info, title="Wikipedia Info")

    def print_info():
        print(info)

    # Run tasks in parallel
    threads = []
    for task in [speak, show_alert, print_info]:
        t = threading.Thread(target=task)
        threads.append(t)
        t.start()

    # Optional: wait for all threads to finish
    for t in threads:
        t.join()

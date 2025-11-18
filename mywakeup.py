import speech_recognition as sr 

speech = sr.Recognizer()
#Define a wake up function to determine the status of VPA
def wakeup():
    wakeup = "StandBy"
    voice_input= ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = speech.listen(source, timeout=3)
            voice_input = speech.recognize_google(audio).lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
    if "hello" in voice_input and "python" in voice_input:
        wakeup = "Activated"
    elif "stop" in voice_input:
        wakeup = "ToQuit"
    return wakeup
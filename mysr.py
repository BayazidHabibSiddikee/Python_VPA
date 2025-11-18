# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 22:00:23 2025

@author: HP
"""

import platform
import speech_recognition as sr
speech = sr.Recognizer()

if platform.system() =='Linux':
    from ctypes import CFUNCTYPE, c_char_p, c_int, cdll
    
    #define error handler
    error_handler = CFUNCTYPE\
    (None, c_char_p, c_int, c_char_p, c_int, c_char_p)
        #Don't do anythings if there is an error message
    def py_error_handler(filename, line, function, err, fmt):
        pass
        #Pass to C
    c_error_handler = error_handler(py_error_handler)
    asound = cdll.LoadLibrary('libasound,so')
    asound.snd_lib_error_set_handler(c_error_handler)
        
        #Now we define voice to text function on all platform -_-
def voice_to_text():
    inp = ''
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            inp = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return inp


import pyttsx3
# import tkinter
text_speech = pyttsx3.init()

# answer = input("what you want to convert :")
# driver = pyttsx3.init()
text_speech.save_to_file('write here you want to convert', 'test.mp3')
# text_speech.say(answer)
text_speech.runAndWait()
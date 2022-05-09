import PyPDF2
import pyttsx3
from PyPDF2 import PdfFileReader
from pyttsx3 import Engine



pdfReader: PdfFileReader = PyPDF2.PdfFileReader(open('mata.pdf', 'rb'))
speaker: Engine = pyttsx3.init()
rate=speaker.getProperty('rate')

speaker.setProperty('rate', 150)

voices = speaker.getProperty('voices')

speaker.setProperty('voice', voices[1].id)

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
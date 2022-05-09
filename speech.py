from tkinter import *
import pyttsx3
from PIL import ImageTk,Image

root = Tk()
root.title("Sound Box")
root.geometry("800x500")
root.iconbitmap('C:\\Users\\Rahul Prasad\\OneDrive\\Desktop\\New folder\\image.ico')


def talk():
    engine = pyttsx3.init()
    # engine.setProperty('rate',250)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0,END)

myLabel = Label(root,text="Write what you want to convey :")
myLabel.pack()
# my_image = ImageTk,PhotoImage(Image.open("C:\\Users\\Rahul Prasad\\OneDrive\\Desktop\\New folder\\building.png"))
# my_label = Label(my_image)
# my_label.pack()
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack(pady=20)
my_button = Button(root, text="Speak",padx=50, command=talk)
my_button.pack(pady=20)

root.mainloop()

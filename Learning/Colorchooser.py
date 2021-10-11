from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg=colorchooser.askcolor()[1])
window = Tk()

window.geometry("420x420")

button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
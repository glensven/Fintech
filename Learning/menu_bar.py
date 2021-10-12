from tkinter import *

def openFile():
    print("file has been opened")

def saveFile():
    print("file has been saved")

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")

window = Tk()

menuBar = Menu(window)

window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0,font=("Arial", 15))

menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)
editMenu = Menu(menuBar, tearoff=0,font=("Arial", 15))
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()
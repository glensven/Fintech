from tkinter import *

def openFile():
    print("file has been opened")

def saveFile():
    print("file has been saved")

window = Tk()

menuBar = Menu(window)

window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)

menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

window.mainloop()
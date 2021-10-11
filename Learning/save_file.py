from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text File", ".txt"),
                                                                        ("HTML File", ".html"),
                                                                        ("All Files", ".*")])
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text="Save", command = saveFile)
button.pack()

text = Text(window)
text.pack()
window.mainloop()
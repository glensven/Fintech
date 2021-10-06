from tkinter import *

window = Tk()

photo = PhotoImage(file='Fry.png')

def click():
    print("You clicked the button")

button = Button(window, text = "click me", command=click, font = ("Comic Sans", 30), fg="#00FF00", bg='black',
                activeforeground = '#00FF00', activebackground="black", image=photo, compound = 'bottom')
button.pack()

window.mainloop()
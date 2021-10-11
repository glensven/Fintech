from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='This is an info message box', message='You have value')
    #messagebox.showwarning(title='Warning!', message='Stop hating yourself')
    #messagebox.showerror(title='Error', message='You have to focus')
    if messagebox.askyesno(title="ask ok or cancel", message='Do you love yourself?'):
        print('Good')
    else:
        print('Please be good to yourself')
window = Tk()

button = Button(window, command=click, text='click me')

button.pack()

window.mainloop()
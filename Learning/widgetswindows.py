from tkinter import *

window = Tk()
window.geometry()
window.title("Glen Coco Learning")

photo = PhotoImage(file='Fry.png')
#window.iconphoto(True, icon)

label = Label(window,
              text='Hello World',
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd = 10,
              padx=20,
              pady=20,
              image = photo,
              compound = 'top')
label.pack()
#label.place(x=0, y=0)

window.mainloop()


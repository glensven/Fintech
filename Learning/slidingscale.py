from tkinter import *
window = Tk()

hotImage = PhotoImage(file = 'hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

def submit():
    print("The temoerature is: "+ str(scale.get())+"degrees C")

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval=10,
              showvalue=1,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg = '#111111')

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window, text = 'submit', command=submit)
button.pack()
window.mainloop()
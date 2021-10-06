from tkinter import *
from PIL import Image, ImageTk

window = Tk()

food = ["pizza", "hamburger", "hotdog"]

def order():
    if (x.get()==0):
        print("You ordered pizza")
    elif(x.get()==1):
        print("You ordered a hamburger")
    elif (x.get()==2):
        print('You ordered a hotdog')
    else:
        print("Huh?")

x = IntVar()

pizzaImage = PhotoImage(Image.open("pizza.png").resize((25, 25)))
hamburgerImage = PhotoImage(Image.open("hamburger.png").resize((25, 25)))
hotdogImage = PhotoImage(Image.open("hotdog.png").resize((25, 25)))

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impact', 50),
                              image= foodImages[index],
                              compound= 'left',
                              command = order)

    radiobutton.pack(anchor="w")
window.mainloop()
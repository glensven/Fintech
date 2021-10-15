from tkinter import *

window = Tk()

def submit():
    firstname = firstNameEntry.get()
    lastname = lastNameEntry.get()
    email = emailEntry.get()
    print("Your name is " + firstname + " " + lastname)
    print("Your email is " + email)

firstNameLabel = Label(window, text="First name: ").grid(row=0,column=0)
firstNameEntry = Entry(window)
firstNameEntry.grid(row = 0, column = 1)

lastNameLabel = Label(window, text="Last name: ").grid(row=1,column=0)
lastNameEntry = Entry(window)
lastNameEntry.grid(row = 1, column = 1)

emailLabel = Label(window, text="Email: ").grid(row=2,column=0)
emailEntry = Entry(window)
emailEntry.grid(row = 2, column = 1)

submitButton = Button(window,text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

window.mainloop()


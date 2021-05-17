from tkinter import *

window = Tk()
title = Label(window, text='Enter you info', font=('Arial',25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window, text='First Name: ', width=20, bg='#ff0000').grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text='Last Name: ',  bg='#00ff00').grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text='Email: ', width=50, bg='#0000ff').grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text='Submit').grid(row=4, column=0, columnspan=2)


window.mainloop()
from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("450x450")
button = Button(text='click me', command=click)
button.pack()
window.mainloop()
from tkinter import *

def create_window():
    new_window = Tk()
    old_window.destroy()

old_window = Tk()

Button(old_window, text='Create new Window', command=create_window).pack()

old_window.mainloop()
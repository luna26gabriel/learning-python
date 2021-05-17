from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\gabri\\Documents\\Udemy\\Python\\Graphics',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text File', '.txt'),
                                        ('HTML File', '.html'),
                                        ('All Files', '.*'),
                                    ])
    # filetext = str(text.get('1.0', END))
    if file is None:
        return
    filetext = input('Enter Some text: ')
    file.write(filetext)
    file.close()

window = Tk()

button = Button(window, text="Save", command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
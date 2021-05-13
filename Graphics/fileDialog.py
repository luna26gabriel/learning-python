from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir='C:\\Documentos',  
                                          title='Open files okay?',
                                          filetypes=(('Arquivos de Textos', '*.txt'),('all files', '*.*'))
                                          )
    if (filepath):
        file = open(filepath, 'r')
        print(file.read())
        file.close()


window = Tk()
button = Button(window, text='Open', command=openFile)
button.pack() 
window.mainloop()
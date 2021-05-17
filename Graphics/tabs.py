from tkinter import *
from tkinter import ttk

window =Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack(expand=True, fill='both') #expand -> Expandir para completar o espaço, fill -> completar todo o espaço existente

Label(tab1, text='Hello, this is tab number 1', width=50, height=25).pack()
Label(tab2, text='Goodbye, this is tab number 2', width=50, height=25).pack()
window.mainloop()
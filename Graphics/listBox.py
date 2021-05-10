from tkinter import *

def submit():
    
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have order: ")
    for index in food:
        print(index)

    # print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(  window,
                    bg='#eee',
                    font=('Arial', 15),
                    width=25,
                    selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, 'Pizza')
listbox.insert(2, 'Hamburguer')
listbox.insert(3, 'Pastel')
listbox.insert(4, 'Pasta')
listbox.insert(5, 'Salad')

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()
add = Button(window, text='Add', command=add)
add.pack()
delete = Button(window, text='Delete', command=delete)
delete.pack()

submitButton = Button(window, text='submit', command=submit)
submitButton.pack()

window.mainloop()
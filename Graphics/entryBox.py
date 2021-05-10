from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)
    # entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=('Arial', 50),
              fg='#007700',
              bg='#333',
              show='#'
              )
# entry.insert(0, 'Default Text')
# entry.config(show='*')
entry.pack(side=LEFT)

submit = Button(window, text="Enviar", command=submit)
submit.pack(side=RIGHT)

delete = Button(window, text="Deletar", command=delete)
delete.pack(side=RIGHT)

backspace = Button(window, text="<--", command=backspace)
backspace.pack(side=RIGHT)



window.mainloop()
from tkinter import *

def display():
    if (x.get()):
        print("You agree")
    else:
        print("You dont agree") 

window = Tk()
x = BooleanVar()
# x = StringVar() #String type
# x = IntVar() #Int type

python = PhotoImage(file='C:\\Users\\gabri\\Documents\\Udemy\\Python\\python.png')

checkBox = Checkbutton(window,
                       text="I agree to something",
                       variable=x,
                       onvalue=True,
                       offvalue=False,
                       command=display,
                       font=('Arial', 20),
                       fg='#007700',
                       bg='#333',
                       activeforeground='#007700',
                       activebackground='#333',
                       padx=40,
                       pady=20,
                       image=python,
                       compound='left')

checkBox.pack()
window.mainloop()
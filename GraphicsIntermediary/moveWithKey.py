from tkinter import *

# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-10)
# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+10)
# def move_left(event):
#     label.place(x=label.winfo_x()-10, y=label.winfo_y())
# def move_right(event):
#     label.place(x=label.winfo_x()+10, y=label.winfo_y())

# window = Tk()
# window.geometry('500x500')

# window.bind('<w>', move_up)
# window.bind('<s>', move_down)
# window.bind('<a>', move_left)
# window.bind('<d>', move_right)
# window.bind('<Up>', move_up)
# window.bind('<Down>', move_down)
# window.bind('<Left>', move_left)
# window.bind('<Right>', move_right)

# slime = PhotoImage(file='C:\\Users\\gabri\\Documents\\Udemy\\Python\\GraphicsIntermediary\\slime.png')
# label = Label(window, image=slime)
# label.place(x=0,y=0)
# window.mainloop()



# CANVAS =======================================

def move_up(event):
    canvas.move(myslime, 0, -20)
def move_down(event):
    canvas.move(myslime, 0, 20)
def move_left(event):
    canvas.move(myslime, -20, 0)
def move_right(event):
    canvas.move(myslime, 20, 0)

window = Tk()

window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

slime = PhotoImage(file='C:\\Users\\gabri\\Documents\\Udemy\\Python\\GraphicsIntermediary\\slime.png')
myslime = canvas.create_image(0,0,image=slime, anchor=NW)
window.mainloop()
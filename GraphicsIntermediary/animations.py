from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
SPEED_X = 5
SPEED_Y = 2

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()


slime = PhotoImage(file='C:\\Users\\gabri\\Documents\\Udemy\\Python\\GraphicsIntermediary\\slime.png')
myslime = canvas.create_image(0,0,image=slime, anchor=NW)

image_width = slime.width()
image_height = slime.height()

while True:
    coordinates = canvas.coords(myslime)
    if(coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
        SPEED_X = -SPEED_X
    if(coordinates[1] >= (WIDTH-image_height) or coordinates[1] < 0):
        SPEED_Y = -SPEED_Y
    canvas.move(myslime, SPEED_X, SPEED_Y)
    window.update()
    time.sleep(0.01)

window.mainloop()

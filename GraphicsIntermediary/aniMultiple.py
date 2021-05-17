from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
                 #canvas, x, y, diameter, xSpeed, ySpeed, color
volley_ball = Ball(canvas, 0, 0, 70, 1.0, 0.7, 'white')
tennis_ball = Ball(canvas, 0, 0, 20, 2.0, 2.5, 'yellow')
basket_ball = Ball(canvas, 0, 0, 90, 1.0, 1.7, 'orange')
bolice_ball = Ball(canvas, 0, 0, 70, 0.5, 0.2, 'black')

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bolice_ball.move()
    window.update()
    time.sleep(0.00001)

window.mainloop()
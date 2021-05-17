from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
# canvas.create_line(0,0,500,500, fill='pink', width=5)
# canvas.create_line(0,500,500,0, fill='red', width=5)
# canvas.create_rectangle(50,50,250,250, fill='black')

# points = [250, 0, 500,500,0,500]
# canvas.create_polygon(points, fill='gold', outline='black', width=5)
# canvas.create_polygon(250, 500, 125,250,375,250, fill='grey', outline='black', width=5)

# canvas.create_arc(0,0,500,500, style=PIESLICE, start=270, extent=180) #style=CHORD, ARC

canvas.create_arc(50,50,450,450, start=0, extent=180, fill='red', width=6)
canvas.create_arc(50,50,450,450, start=180, extent=180, fill='white', width=6)
canvas.create_oval(180,180,320,320,fill='white', width=6)
canvas.pack()

window.mainloop()
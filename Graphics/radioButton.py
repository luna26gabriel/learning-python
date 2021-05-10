from tkinter import *

food = ['Pizza', 'Hamburger', 'Hotdog']

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered hamburguer")
    elif x.get() == 2:
        print("You ordered Hotdog")

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text atraves da lista
                              variable=x, #junto os radios buttons
                              value=index, #designa um index direferente para cada button
                              padx=25,
                              pady=2,
                              font=('Impact', 20),   
                              indicatoron=0, #elimina os circulos e deixa como se fosse botões                           
                              width = 13,
                              command=order
                              )
    radiobutton.pack(anchor=W)

window.mainloop()
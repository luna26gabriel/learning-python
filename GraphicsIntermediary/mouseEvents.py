from tkinter import *

def doSomething(event):
    print('You did a thing on ' + str(event.x)+':'+str(event.y))


window = Tk()

# window.bind('<Button-1>', doSomething) #Left Button \
# window.bind('<Button-2>', doSomething) #Middle Button -> Mouse
# window.bind('<Button-3>', doSomething) #Right Buton /

# window.bind('<ButtonRelease>', doSomething) #Solta o Mouse
# window.bind('<Enter>', doSomething) #Entrar na Janela
# window.bind('<Leave>', doSomething) #Saida da Janela

window.bind('<Motion>', doSomething)

window.mainloop()
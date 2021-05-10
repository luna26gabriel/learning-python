from tkinter import *

window = Tk() #Inicializando a janela visual
window.geometry("420x420")
window.title("Primeira Janela do Luna")

# Mudando a photo da janela, mas convertendo para um formato que o Tkinter consiga enteder
icon = PhotoImage(file='C:\\Users\\gabri\\Pictures\\fofinho.png')
window.iconphoto(True, icon)

#Mudando a cor de fundo
window.config(background="#000")

window.mainloop() #Mostrar a janela esperando os comandos
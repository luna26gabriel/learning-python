from tkinter import *
import time

window = Tk() #Inicializando a janela visual
window.geometry("420x420")
window.title("Primeira Janela do Luna")

# Mudando a photo da janela, mas convertendo para um formato que o Tkinter consiga enteder
icon = PhotoImage(file='C:\\Users\\gabri\\Pictures\\fofinho.png')
window.iconphoto(True, icon)

#Mudando a cor de fundo
window.config(background="#eee")

#photo
# photo = PhotoImage(file='C:\\Users\\gabri\\Pictures\\fofinho.png')

#Labels
label = Label(window,
              text="Hello Word", 
              bg='#eee', 
              font=('Arial', 40, 'bold'),
              fg='#005500',
              #relief=SUNKEN, #RAISED, SUNKEN
              bd=10,
              padx=20, #padding horizontal
              pady=20, #padding vertical
            #   image=photo, #imagem junto com a label // a imagem fofinho fica muito grande por isso está desabilitada
            #   compound='bottom'
              )
label.pack() #Coloca a Label Centralizada no topo da janela
# label.place(x=100,y=20) #Coloa a label com x e y fixos
count = 0
now = 0
def click():
    print("You clicked the button!")
    global count
    count += 1
    print(count)
    if count == 1:
        global now
        now = time.time()
    if count == 100:
        end = time.time()
        print(stopTimer(end-now))
        
def stopTimer(value):

    valueD = (((value/365)/24)/60)
    Days = int(valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)
    
    print(Days,";",Hours,":",Minutes,";",Seconds)


#Button
button = Button(window,
                text="Clica em mim :D",
                command=click,
                font=("Comic Sans", 20),
                fg='#007700',
                bg='#ddd',
                activeforeground="#007700",
                activebackground="#dfdfdf",
                )
button.pack()

button2 = Button(window,
                text="Não clica em mim :(",
                command=click,
                font=("Comic Sans", 20),
                fg='#007700',
                bg='#ddd',
                activeforeground="#007700",
                activebackground="#dfdfdf",
                state=DISABLED,
                pady=10
                )
button2.pack()


window.mainloop() #Mostrar a janela esperando os comandos
from tkinter import *

def submit():
    print("The temperature is " + str(scale.get()) + "ºC")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, #or HORIZONTAL 
              font=('Arial', 15),
              tickinterval = 10, #intervalo mostrado na scala
            #   showvalue=0, #Se tiver no 0, não vai aparecer o value
              troughcolor='#777',
              fg='#bb0000',
              bg='#ccc'
              )

# scale.set(50) #Seta o número padrão
# scale.set(((scale['from']-scale['to'])/2) + scale['to']) #Formula para fica exatamente no meio 
scale.pack()

button = Button(window, text='Enviar', command=submit)
button.pack()

window.mainloop()
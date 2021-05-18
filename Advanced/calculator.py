from tkinter import * 

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
    print(num)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))

        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_text = ''
        equation_label.set('You cant divide by 0')
    except SyntaxError:
        equation_text = ''
        equation_label.set('This makes no sense')

def clear():
    global equation_text
    equation_text = ''
    equation_label.set('')

window = Tk()
window.title('Calculator program')
window.geometry('400x500')

equation_text = ''

equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=('Consolas', 20), bg='black', fg='#aa0000', width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

#Criando os botoes para a numpad
button1 = Button(frame, text=1, height=4, width=9, font=55,
 command= lambda: button_press(1))
button2 = Button(frame, text=2, height=4, width=9, font=55,
 command= lambda: button_press(2))
button3 = Button(frame, text=3, height=4, width=9, font=55,
 command= lambda: button_press(3))
button4 = Button(frame, text=4, height=4, width=9, font=55,
 command= lambda: button_press(4))
button5 = Button(frame, text=5, height=4, width=9, font=55,
 command= lambda: button_press(5))
button6 = Button(frame, text=6, height=4, width=9, font=55,
 command= lambda: button_press(6))
button7 = Button(frame, text=7, height=4, width=9, font=55,
 command= lambda: button_press(7))
button8 = Button(frame, text=8, height=4, width=9, font=55,
 command= lambda: button_press(8))
button9 = Button(frame, text=9, height=4, width=9, font=55,
 command= lambda: button_press(9))
button0 = Button(frame, text=0, height=4, width=9, font=55,
 command= lambda: button_press(0))
plus = Button(frame, text=' + ', height=4, width=9, font=55,
 command= lambda: button_press('+'))
minus = Button(frame, text=' - ', height=4, width=9, font=55,
 command= lambda: button_press('-'))
times = Button(frame, text=' x ', height=4, width=9, font=55,
 command= lambda: button_press('*'))
divide = Button(frame, text=' / ', height=4, width=9, font=55,
 command= lambda: button_press('/'))
equals = Button(frame, text=' = ', height=4, width=9, font=55,
 command=equals)
column = Button(frame, text=',', height=4, width=9, font=55,
 command= lambda: button_press(','))
clear = Button(frame, text='Clear', height=4, width=9, font=55,
 command=clear)


#Inserindo os botoes no grid
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=1,column=0)
button5.grid(row=1,column=1)
button6.grid(row=1,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button0.grid(row=3,column=1)

plus.grid(row=0,column=3)
minus.grid(row=1,column=3)
times.grid(row=2,column=3)
divide.grid(row=3,column=3)

equals.grid(row=3,column=2)
column.grid(row=3,column=0)
clear.grid(row=4,column=0,columnspan=4)

window.mainloop()
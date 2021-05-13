from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="This is a info box", message="You are a person?")
    # messagebox.showerror(title="Error", message="This is a erro")
    # while True:
        # messagebox.showwarning(title="Warning", message="You are a person?")


    # if messagebox.askokcancel(title='Ask OK CANCECL', message='Do you want to do the thing'): 
    #     print("You did a thing")
    # else:
    #     print("You cancel a thing")

    # if messagebox.askretrycancel(title='Ask OK CANCECL', message='Do you want to retry the thing'):
    #     print("You retry a thing")
    # else:
    #     print("You cancel a thing")

    # if messagebox.askyesno(title='Ask YES NO', message='Yes or No?'):
    #     print('Yes')
    # else:
    #     print('No')

    answer = messagebox.askyesnocancel(title='Ask Yes No Cancel', message='Do want to do Yes No or Cancel', icon='warning') #icon='info', icon='error'
    if answer == True:
        print('Yes')
    elif answer == False:
        print('No')
    else:
        print('Cancel')

    # answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
    # if answer == 'yes':
    #     print('I like pie to')
    # else:
    #     print('Why do you not like pie')

window = Tk()

button = Button(window, command=click, text='Click Me')
button.pack()

window.mainloop()
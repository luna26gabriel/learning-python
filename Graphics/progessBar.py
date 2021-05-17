from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 1000
    download = 0
    speed = 4
    while download<GB:
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+'%')
        text.set(str(download)+'/'+str(GB) + ' GBs completed')
        window.update_idletasks()

window = Tk()
percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=250)
bar.pack(padx=10, pady=10)

percentLabel = Label(window, textvariable=percent).pack()
tasksLabel = Label(window, textvariable=text).pack()

button = Button(window, text='download',command=start).pack()
window.mainloop()
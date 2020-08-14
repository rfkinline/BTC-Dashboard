
#!/usr/bin/env python3
from tkinter import Tk, Label, Button, PhotoImage
import os, time, subprocess

def tick():
    time2 = time.strftime('%H:%M:%S')
    clock = Label(root, font=('Lato Light', 48, 'bold'))
    clock.grid(row=4, columnspan=7, pady=20)
    clock.config(text=time2)
    clock.after(200, tick)

class MyFirstGUI:
    def __init__(self, master):
        self.label = Label(master, text="HyperPixel Radio by @blogmywiki", font=('Lato Heavy',25), fg = 'blue')
        self.label.grid(columnspan=7, pady=20)

root = Tk()
root.configure(cursor='none')
root.geometry("+200+200")
my_gui = MyFirstGUI(root)
tick()
root.mainloop()
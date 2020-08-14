#!/usr/bin/env python3
from tkinter import *

class CryptoTicker:
	def __init__(self, master):
		self.master = master

		self.label = Label(master, text="CryptoTicker",justify=LEFT, font=('Helvetica',32, 'bold'), fg = 'black')
		self.label.grid(columnspan=6, pady=1)

		num=str(4)
		t1 = ("label = " + num)
		t2 ="ddddddddddds"
		t3="rrrr"
		self.down_label = Label(master, text=(t1 +'\n' + t2 + '\n' + t3),anchor=W, width = 19, justify=LEFT,relief=RAISED, font=('Lato Heavy',25))
		self.down_label.grid(row=2)

		num=str(6)
		t1 = ("label = " + num)
		t2 ="ddddsss"
		t3="rrrr"
		self.down_label = Label(master, text=(t1 +'\n' + t2 + '\n' + t3), anchor=W, width = 19, justify=LEFT,relief=RAISED, font=('Lato Heavy',25, 'bold'))
		self.down_label.grid(row=2, column=2, pady=2)

		self.close_button = Button(master, text="C", command=self.close, height=1, width=1)
		self.close_button.grid(row=0, pady=1)


	def close(self):
		root.destroy()


root = Tk()
#root.configure(background='cyan3')
root.configure(cursor='none')
root.attributes('-fullscreen', True)
my_gui = CryptoTicker(root)
root.mainloop()

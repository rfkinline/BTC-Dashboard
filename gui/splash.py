from tkinter import *
from PIL import ImageTk,Image
import config

def splashScreen():
	splash_width = 512
	splash_height = 325
	config.splash.configure(bg='black')
	config.splash.overrideredirect(True)
	try:
		splash_img = ImageTk.PhotoImage(Image.open(r"images\SplashScreen.jpg"))
	except:
		splash_img = ImageTk.PhotoImage(Image.open(r"images/SplashScreen.jpg"))
	
	splash_label = Label(config.splash, image=splash_img, borderwidth=0, highlightthickness = 0)
	splash_label.grid(row=0, column=0)
	config.width_value=config.root.winfo_screenwidth()
	config.height_value=config.root.winfo_screenheight()
	splash_x = int((config.width_value / 2) - (splash_width / 2))
	splash_y = int((config.height_value / 2) - (splash_height / 2))
	config.splash.geometry(f'{splash_width}x{splash_height}+{splash_x}+{splash_y}')
	print("Screen Width: " + str(config.width_value))
	print("Screen Height: " + str(config.height_value))
	splash_label2 = Label(config.splash, text="Detected screen dimensions: " + str(config.width_value) + " x " + str(config.height_value),anchor=NW, justify=LEFT,font=('Times',12), bg='black', fg = 'white')
	splash_label2.grid(row=2, column=0)
	splash_label3 = Label(config.splash, text= config.version,anchor=E, font=('Times',12, 'bold'), bg='black', fg = '#2B9B1B')
	splash_label3.grid(row=2, column=0, padx=(450,0))
	config.splash.update()
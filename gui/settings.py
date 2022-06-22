from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk,Image
from urllib.request import urlopen
import config
global customt
try:
	import customtkinter
	customt = 1
except:
	customt = 0

def settingsMenu():
	# slider values (min 1 second, max 24 hours)
	minval = 1
	maxval = 24

	def testConnection():
		#Tests custom node IP:Port to ensure proper connectivity
		try:
			e_url = ip_entry.get()
			urltest = requests.get(e_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + e_url + " Status code: " + str(status))
			b_url = e_url + "api/blocks/tip/height"
			urltest = requests.get(b_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + b_url + " Status code: " + str(status))
			d_url = e_url + 'api/v1/difficulty-adjustment'
			urltest = requests.get(b_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + d_url + " Status code: " + str(status))
			f_url = e_url + 'api/v1/fees/recommended'
			urltest = requests.get(f_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + f_url + " Status code: " + str(status))
			t_url = e_url + 'api/mempool'
			urltest = requests.get(t_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + t_url + " Status code: " + str(status))
			print("Success on all node tests!")
			messagebox.showinfo("Success!", "Success on all node tests!", parent=settings)
		except:
			print("Tried connecting to: " + e_url)
			print("Error Connecting to Node!")
			messagebox.showerror("Error!", "Error Connecting to Node!\nCheck your URL and try again.", parent=settings)

	def nodeEnable():
		#Check if Custom Node is checked to enable Custom Node IP:Port text field
		choice = src.get()
		if choice == 0:
			ip_entry.configure(state=DISABLED)
			test_button.configure(state=DISABLED)
		else:
			ip_entry.configure(state=NORMAL)
			test_button.configure(state=NORMAL)

	def connectToNode():
		#Update refresh time and mempool node source with and display updated values in a messagebox
		global node_connected
		global new_refreshtime
		global refresh_seconds

		try:
			refresh_seconds
		except NameError:
			refresh_seconds = int(config.refreshtime / 1000)
		
		config.new_refreshtime = int(refresh_seconds) * 1000
		if int(refresh_seconds) == int(config.refreshtime / 1000):
			refresh_msg = ""
		else:
			refresh_msg = "\nRefresh time set to " + time_text + ".\nNew refresh time will apply after next refresh"
		if src.get() == 0:
			try:
				urltest = requests.get('https://mempool.space/')
				status = urltest.status_code
				urltest.close()
				config.node_connected = 0
				messagebox.showinfo("Success!", "Successfully connected to Mempool.Space!" + refresh_msg, parent=settings)
				settings.destroy()
			except:
				messagebox.showerror("Error!", "Error Connecting to Mempool.Space!\nTry again later." + refresh_msg, parent=settings)
		else:
			try:
				node_url = ip_entry.get()
				urltest = requests.get(node_url)
				status = urltest.status_code
				urltest.close()
				print("Tried connecting to: " + node_url + " Status code: " + str(status))
				print("Successfully connected to custom node!")
				config.node_connected = 1
				config.ip_url = node_url
				messagebox.showinfo("Success!", "Successfully connected to custom node!" + refresh_msg, parent=settings)
				settings.destroy()
			except:
				print("Tried connecting to: " + node_url)
				print("Error Connecting to Node!")
				messagebox.showerror("Error!", "Error Connecting to Node!\nCheck your URL and try again." + refresh_msg, parent=settings)

	def slider_change(self):
		#Sets slider value to various refresh times
		global refresh_seconds
		global time_text
		global slider_value
		global var
		var = spin_var.get()
		x = var
		if var == 1:
			refresh_seconds = var
			time_text = "1 second"
		elif var > 1 and var <= 5:
			refresh_seconds = var
			time_text = str(var) + " seconds"
		elif var == 6:
			refresh_seconds = 10
			time_text= "10 seconds"
		elif var == 7:
			refresh_seconds = 15
			time_text= "15 seconds"
		elif var == 8:
			refresh_seconds = 30
			time_text= "30 seconds"
		elif var == 9:
			refresh_seconds = 60
			time_text = "1 minute"
		elif var > 9 and var < 14:
			x = var - 8
			refresh_seconds = x * 60
			time_text = str(x) + " minutes"
		elif var == 14:
			refresh_seconds = 10 * 60
			time_text = "10 minutes"
		elif var == 15:
			refresh_seconds = 15 * 60
			time_text = "15 minutes"
		elif var == 16:
			refresh_seconds = 30 * 60
			time_text = "30 minutes"
		elif var == 17:
			refresh_seconds = 60 * 60
			time_text = "1 hour"
		elif var > 17 and var < 21:
			x = var - 16
			refresh_seconds = x * 60 * 60
			time_text = str(x) + " hours"
		elif var == 21:
			refresh_seconds = 8 * 60 * 60
			time_text = "8 hours"
		elif var == 22:
			refresh_seconds = 12 * 60 * 60
			time_text = "12 hours"
		elif var == 23:
			refresh_seconds = 18 * 60 * 60
			time_text = "18 hours"
		elif var == 24:
			refresh_seconds = 24 * 60 * 60
			time_text = "24 hours"
		else:
			time_text = "Error"
		refresh_conv.configure(text=time_text)
		slider_value = var

	def checkCustomRefresh(check):
		global time_text
		if check < 60:
			secs = check
		elif check >= 60 and check < (60 * 60):
			mins = check // 60
			secs = check % 60
		elif check >= 60 * 60:
			hrs = check//3600
			mins = (check % 3600) // 60
			secs = (check % 3600) % 60
		if check == 1:
			time_text = str(secs) + " second"
			return 1
		elif check > 1 and check < 6:
			time_text = str(secs) + " seconds"
			return check
		elif check >= 6 and check <= 10:
			time_text = str(secs) + " seconds"
			return 6
		elif check > 10 and check <= 15:
			time_text = str(secs) + " seconds"
			return 7
		elif check > 15 and check <= 30:
			time_text = str(secs) + " seconds"
			return 8
		elif check > 30 and check < 60:
			time_text = str(secs) + " seconds"
			return 9
		elif check == 60:
			time_text = str(mins) + " minute"
			return 9
		elif check > 60 and check <= (60 * 5):
			time_text = str(mins) + " minutes " + str(secs) + " seconds"
			return 8 + (mins)
		elif check > (60 * 5) and check <= (60 * 10):
			time_text = str(mins) + " minutes " + str(secs) + " seconds"
			return 14
		elif check > (60 * 10) and check <= (60 * 15):
			time_text = str(mins) + " minutes " + str(secs) + " seconds"
			return 15
		elif check > (60 * 15) and check <= (60 * 30):
			time_text = str(mins) + " minutes " + str(secs) + " seconds"
			return 16
		elif check > (60 * 30) and check < (60 * 60):
			time_text = str(mins) + " minutes " + str(secs) + " seconds"
			return 17
		elif check == (60 * 60):
			time_text = str(hrs) + " hour"
			return 17
		elif check > (60 * 60) and check <= (60 * 60 * 4):
			time_text = str(hrs) + " hours " + str(mins) + " minutes " + str(secs) + " seconds"
			return 16 + hrs
		elif check > (4 * 60 * 60) and check <= (8 * 60 * 60):
			time_text = str(hrs) + " hours " + str(mins) + " minutes " + str(secs) + " seconds"
			return 21
		elif check > (8 * 60 * 60) and check <= (12 * 60 * 60):
			time_text = str(hrs) + " hours " + str(mins) + " minutes " + str(secs) + " seconds"
			return 22
		elif check > (12 * 60 * 60) and check <= (18 * 60 * 60):
			time_text = str(hrs) + " hours " + str(mins) + " minutes " + str(secs) + " seconds"
			return 23
		elif check > (18 * 60 * 60) and check < (24 * 60 * 60):
			time_text = str(hrs) + " hours " + str(mins) + " minutes " + str(secs) + " seconds"
			return 24
		else:
			time_text = str(hrs) + " hours"
			return 24

	def on_closing():
		#Set the slider value to the refresh time when closing the settings window
		global slider_value
		slider_value = checkCustomRefresh(config.new_refreshtime // 1000)
		settings.destroy()

	global ip_entry
	global settings
	global slider_value
	global src

	try:
		slider_value
	except NameError:
		slider_value = checkCustomRefresh(config.default_refresh)

	spin_var = IntVar()
	spin_var.set(slider_value)
	src = IntVar()
	src.set(config.node_connected)
	settings_width = 550
	settings_height = 300
	config.width_value=config.root.winfo_screenwidth()
	config.height_value=config.root.winfo_screenheight()
	settings_x = int((config.width_value / 2) - (settings_width / 2))
	settings_y = int((config.height_value / 2) - (settings_height / 2))

	if customt == 1:
		customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
		customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
		settings = customtkinter.CTkToplevel()
		refresh_label = customtkinter.CTkLabel(settings, text="Refresh Interval", text_font=('Helvetica',20, 'bold'))
		refresh_label.grid(row=0, column=1, columnspan=3, ipady=20)
		refresh_conv = customtkinter.CTkLabel(settings, text=time_text, text_font=('Helvetica', 16))
		slider = customtkinter.CTkSlider(settings, from_=minval, to=maxval, variable=spin_var, command=slider_change)
		top_label = customtkinter.CTkLabel(settings, text="Mempool Source", text_font=('Helvetica',20, 'bold'))
		r_memp = customtkinter.CTkRadioButton(settings, text="Default", variable=src, value=0, command=nodeEnable, text_font=('Helvetica',14))
		r_custom = customtkinter.CTkRadioButton(settings, text="Custom Node", variable=src, value=1, command=nodeEnable, text_font=('Helvetica',14))
		url_label = customtkinter.CTkLabel(settings, text="Custom Node URL", text_font=('Helvetica',14))
		ip_entry = customtkinter.CTkEntry(settings, text_font=('Helvetica',14), width=225)
		test_button = customtkinter.CTkButton(settings, text="Test", text_font=('Helvetica', 14), command=testConnection)
		connect_button = customtkinter.CTkButton(settings, text="Apply", text_font=('Helvetica',14, 'bold'), bg='#f2a900', width=30, command=connectToNode)
		connect_button.grid(row=6, column=0, columnspan=4, pady=30)
	else:
		settings = Toplevel()
		refresh_label = Label(settings, text="Refresh Interval", font=('Helvetica',18, 'bold'))
		refresh_label.grid(row=0, column=1, columnspan=3, ipady=5)
		refresh_conv = Label(settings, text=time_text, font=('Helvetica', 16))
		slider = Scale(settings, from_=minval, to=maxval, orient='horizontal', showvalue=0, variable=spin_var, command=slider_change)
		top_label = Label(settings, text="Mempool Source", font=('Helvetica',18, 'bold'))
		r_memp = Radiobutton(settings, text="Default", variable=src, value=0, command=nodeEnable, font=('Helvetica',14))
		r_custom = Radiobutton(settings, text="Custom Node", variable=src, value=1, command=nodeEnable, font=('Helvetica',14))
		url_label = Label(settings, text="Custom Node URL", font=('Helvetica',14))
		ip_entry = Entry(settings, font=('Helvetica',14), width=25)
		test_button = Button(settings, text="Test", font=('Helvetica', 14), command=testConnection)
		connect_button = Button(settings, text="Apply", font=('Helvetica',14, 'bold'), bg='#f2a900', width=30, command=connectToNode)
		connect_button.grid(row=6, column=0, columnspan=4, pady=10)
	
	settings.geometry(f'{settings_width}x{settings_height}+{settings_x}+{settings_y}')
	settings.title('Settings')
	try:
		img = PhotoImage(file=r'images\btcicon.png')
	except:
		img = PhotoImage(file=r'images/btcicon.png')
	settings.tk.call('wm', 'iconphoto', settings._w, img)
	refresh_conv.grid(row=1, column=1, columnspan=3)
	slider.grid(row=2, column=1, columnspan=3)
	slider.set(slider_value)
	top_label.grid(row=3, column=1, columnspan=3)
	r_memp.grid(row=4, column=1, columnspan=2, padx=(0,120), pady=(5,10))
	r_custom.grid(row=4, column=2, columnspan=2, padx=(0,50), pady=(5,10))
	url_label.grid(row=5, column=1)
	ip_entry.grid(row=5, column=2)
	test_button.grid(row=5, column=3)
	ip_entry.insert(0, config.ip_url)
	nodeEnable()
	settings.update()
	settings.protocol("WM_DELETE_WINDOW", on_closing)
	config.root.wait_window(settings)
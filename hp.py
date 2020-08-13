from tkinter import Tk, Label, Button, E, W, PhotoImage
import os, time

class MyFirstGUI:
    def __init__(self, master):
        global fiplogo
        self.master = master
        master.title("HyperPixelRadio")

        fiplogo = PhotoImage(file="fip100.gif")

        self.label = Label(master, text="HyperPixel Radio by @blogmywiki", font=('Roboto',25), fg = 'blue')
        self.label.grid(columnspan=7, pady=20)

        self.fip_button = Button(master, image=fiplogo, command=self.fip, height=100, width = 100)
        self.fip_button.image = fiplogo
        self.fip_button.grid(row=1, pady=10)

        r2logo = PhotoImage(file="radio2.gif")
        self.r2_button = Button(master, image=r2logo, command=self.r2, height=100, width = 100)
        self.r2_button.image = r2logo
        self.r2_button.grid(row=1, column=1)

        r4logo = PhotoImage(file="radio4.gif")
        self.r4_button = Button(master, image=r4logo, command=self.r4, height=100, width = 100)
        self.r4_button.image = r4logo
        self.r4_button.grid(row=1, column=2)

        x4logo = PhotoImage(file="4extra.gif")
        self.x4_button = Button(master, image=x4logo, command=self.x4, height=100, width = 100)
        self.x4_button.image = x4logo
        self.x4_button.grid(row=1, column=3)

        r5logo = PhotoImage(file="5live.gif")
        self.r5_button = Button(master, image=r5logo, command=self.r5, height=100, width = 100)
        self.r5_button.image = r5logo
        self.r5_button.grid(row=1, column=4)

        r6logo = PhotoImage(file="6music.gif")
        self.r6music_button = Button(master, image=r6logo, command=self.r6music, height=100, width = 100)
        self.r6music_button.image = r6logo
        self.r6music_button.grid(row=1, column=5)

        wslogo = PhotoImage(file="bbcws.gif")
        self.ws_button = Button(master, image=wslogo, command=self.ws, height=100, width = 100)
        self.ws_button.image = wslogo
        self.ws_button.grid(row=1, column=6)

        self.down_button = Button(master, text="< VOL", command=self.down, height=5, width=10)
        self.down_button.grid(row=3)

        self.stop_button = Button(master, text="STOP", command=self.stop, height=5, width = 10)
        self.stop_button.grid(row=3, column=2)

        self.close_button = Button(master, text="close app", command=self.close, height=5, width=10)
        self.close_button.grid(row=3, column=4)

        self.up_button = Button(master, text="VOL >", command=self.up, height=5, width=10)
        self.up_button.grid(row=3, column=6)

    def fip(self):
        print("fip!")
        self.label.config(text='fip - France Inter Paris')
        os.system("mpc play 1")

    def r4(self):
        print("BBC Radio 4 FM")
        self.label.config(text='BBC Radio 4 FM')
        os.system("mpc play 2")

    def x4(self):
        print("BBC Radio 4 Extra")
        self.label.config(text='BBC Radio 4 Extra')
        os.system("mpc play 7")

    def r6music(self):
        print("BBC 6music")
        self.label.config(text='BBC Radio 6Music')
        os.system("mpc play 3")

    def ws(self):
        print("BBC World Service News Stream")
        self.label.config(text='BBC World Service News')
        os.system("mpc play 4")

    def r2(self):
        print("BBC Radio 2")
        self.label.config(text='BBC Radio 2')
        os.system("mpc play 5")

    def r5(self):
        print("BBC Radio 5 Live")
        self.label.config(text='BBC Radio 5 Live')
        os.system("mpc play 6")

    def stop(self):
        print("stop MPC player")
        self.label.config(text='-paused-')
        os.system("mpc stop")

    def close(self):
        os.system("mpc stop")
        root.destroy()

    def up(self):
        os.system("mpc volume +30")

    def down(self):
        os.system("mpc volume -30")

root = Tk()

#root.geometry('720x480')
#root.configure(background='cyan3')
root.attributes('-fullscreen', True)
my_gui = MyFirstGUI(root)

time1 = ''
clock = Label(root, font=('Roboto', 48, 'bold'))
clock.grid(row=4, columnspan=7, pady=20)
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()

root.mainloop()
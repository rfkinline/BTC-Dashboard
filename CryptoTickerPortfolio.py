#!/usr/bin/env python3
from tkinter import *
import pandas as pd
import requests
import time
import sys
import datetime
import csv

pricebtc = 0
base = 0
summe = 0
now = datetime.datetime.now()
df = pd.read_csv('portfolio.csv', delimiter=';', names = ['Coin', 'Qty'])
tf = pd.read_csv('configticker.csv', delimiter=';', names = ['Name', 'Value', 'Zeit'])


class CryptoTicker:
	def __init__(self, master):
		self.master = master
		self.label = Label(master, text="CryptoTicker",justify=LEFT, relief=RAISED, font=('Helvetica',32, 'bold'), fg = 'black')
		self.label.grid(row=0, column=1, columnspan=5, pady=1)

		self.close_button = Button(text="C", command=self.close, height=1, width=1)
		self.close_button.grid(row=0, column=0, columnspan=1, pady=1)

	def labels():
		hwg()
		text1 = str(basemaxtime) #.strftime("%Y-%m-%d %H:%M")
		text2 =  "Current BTC = " + str(baseprint)
		text3 =  "Max BTC = " + str(basemaxprint)
		down_label = Label(text=(text2 + '\n' + text3 ),anchor=NW, width = 19, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=2, column=0, columnspan=5, pady=2)
		
		text4 = "Max $ date = " + str(summemaxtime)
		text5 = "Current $ = " + str(summeprint)
		text6 = "Max $ = " + str(summemaxprint)
		down_label = Label(text=(text5 + '\n' + text6), anchor=NW, width = 19, justify=LEFT,relief=RAISED, font=('Helvetica',25))
		down_label.grid(row=2, column=1, columnspan=5, pady=2)
		down_label = Label(text=(text4), anchor=NW, width = 19, justify=LEFT,font=('Helvetica',12))
		down_label.grid(row=3, column=1,  columnspan=5,pady=2)

		text7 = "BTC $ = " + str(pricebtc)
		down_label = Label(text=(text7), anchor=NW, width = 19, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=4, column=0, columnspan=5, pady=2)
		down_label.after(20000,CryptoTicker.labels)

	def close(self):
		root.destroy()

    def tick():
		time2 = time.strftime('%H:%M:%S')
		clock = Label(root, font=('Lato Light', 12))
		clock.grid(row=0, column=8, columnspan=2, pady=1)
		clock.config(text=time2)
		clock.after(200, CryptoTicker.tick)


def hwg():
	global summe
	global basemaxtime
	global basemax
	global summemax
	global summeprint
	global baseprint
	global basemaxprint
	global summemaxprint
	global summemaxtime
	global pricebtc
	
	for i in range(len(tf)) :
		if tf.loc[i,"Name"] == "summemax":
			summemax = float(tf.loc[i,"Value"])
			summemaxtime = str(tf.loc[i,"Zeit"])
		if tf.loc[i,"Name"] == "basemax":
			basemax = float(tf.loc[i,"Value"])
			basemaxtime = str(tf.loc[i,"Zeit"])

#	while True:
#		try:
#	print("in")
	for i in range(len(df)) :
		qtycoin = float(df.loc[i,"Qty"])
		ren = requests.get('https://api.coingecko.com/api/v3/coins/' + df.loc[i,"Coin"]).json()
		ren = { 'price_usd': ren['market_data']['current_price']['usd'] }
		pricecoin = float(ren['price_usd'])
		summe = summe + qtycoin * pricecoin    #		print (qtycoin,pricecoin,summe)
		if df.loc[i,"Coin"] == "bitcoin":
			pricebtc = pricecoin
#	print("out")
#		False
#	except:
#		print("Error reading Coin URL", df.loc[i,"Coin"])

	base = float(round(summe / pricebtc, 2))
	if (base > basemax):

		with open('configticker.csv', 'w', newline='') as csvfile:
			basemaxtime = datetime.datetime.now()
			savwriter = csv.writer(csvfile, delimiter=';')
			text2=["basemax"] + [basemax] + [basemaxtime]
			savwriter.writerow(text2)
			text2=["summemax"] + [summemax] + [summemaxtime]
			savwriter.writerow(text2)
		basemax = base

	summe = summe / 1000
	if (summe > summemax):
		summemaxtime = datetime.datetime.now()
		with open('configticker.csv', 'w', newline='') as csvfile:
			savwriter = csv.writer(csvfile, delimiter=';')
			text2=["summemax"] + [summemax] + [summemaxtime]
			savwriter.writerow(text2)
			text2=["basemax"] + [basemax] + [basemaxtime]
			savwriter.writerow(text2)
		summemax = summe

	summemaxprint = str(round(summemax,2))
	summeprint    = str(round(summe,2))
	basemaxprint  = str(basemax)
	baseprint     = str(base)
	print(summeprint)
	summe = 0

root = Tk()
root.configure(cursor='none')
root.attributes('-fullscreen', True)
my_gui = CryptoTicker(root)
hwg()
CryptoTicker.labels()
root.mainloop()
#time.sleep(3)

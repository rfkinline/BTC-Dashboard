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
summepurchase = 0
sellcoin = ' '
sellcoinsav = ' '
now = datetime.datetime.now()
df = pd.read_csv('portfolio.csv', delimiter=';', names = ['Coin', 'Qty', 'Purchase'])
tf = pd.read_csv('configticker.csv', delimiter=';', names = ['Name', 'Value', 'Zeit'])

for i in range(len(tf)) :
	if tf.loc[i,"Name"] == "summemax":
		summemax = float(tf.loc[i,"Value"])
		summemaxtime = str(tf.loc[i,"Zeit"])
	if tf.loc[i,"Name"] == "basemax":
		basemax = float(tf.loc[i,"Value"])
		basemaxtime = str(tf.loc[i,"Zeit"])

class CryptoTicker:
	def __init__(self, master):
		self.master = master
		self.close_button = Button(text="C", command=self.close)
		self.close_button.grid(row=0, column=0)

		self.label = Label(master, text="CryptoTicker",justify=LEFT, width=20, font=('Helvetica',32, 'bold'), fg = 'blue')
		self.label.grid(row=0, column=1, columnspan=2)

	def labels():
		hwg()
		text1 = str(basemaxtime) #.strftime("%Y-%m-%d %H:%M")
		text2 =  "Portfolio (BTC): " + str(baseprint)
		text3 =  "Max BTC____: " + str(basemaxprint)
		down_label = Label(text=(text2 + '\n' + text3 ),anchor=NW, width = 19, height=2, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=2, column=1)
		
		text5 = "Portfolio____: " + str(summeprint)
		text6 = "Max Portfolio: " + str(summemaxprint)
		down_label = Label(text=(text5 + '\n' + text6), anchor=NW, width = 19, height=2, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=2, column=2)

		text4 = "Max $ date: " + str(summemaxtime)
		down_label = Label(text=(text4), anchor=NW, width = 39, height=2, justify=LEFT,font=('Helvetica',12))
		down_label.grid(row=3, column=1)
		
		currency = "${:,.2f}".format(priceamp)
		text7 = "AMPL: " + str(currency)
		currency = "${:,.2f}".format(pricebtc)
		text8 = "BTC_: " + str(currency)
		down_label = Label(text=(text7 + '\n' + text8), anchor=NW, width = 19, justify=LEFT,font=('Helvetica',25, 'bold'))
		down_label.grid(row=4, column=1)

		investment = 86.44
		currency = "${:,.2f}T".format(investment)
		text9 = "Investment: " + str(currency)
		invperc = summe / investment
		currency = "{:,.0%}".format(invperc)
		text10 = "Change___: " + str(currency)
		down_label = Label(text=(text9 + '\n' + text10), anchor=NW, width = 19, justify=LEFT,font=('Helvetica',25, 'bold'))
		down_label.grid(row=4, column=2)

		down_label = Label(text=('Take Profit: '), anchor=SE, width = 19, height=2, justify=RIGHT,font=('Helvetica',25, 'bold'), fg="red")
		down_label.grid(row=5, column=1)

		text11 = str(sellcoinsav)
		currency = "{:,.0%}".format(sellcoinpercsav)
		text12 = str(currency)
		down_label = Label(text=(text11 + ' ' + text12), anchor=SW, width = 19, height=2, justify=LEFT,font=('Helvetica',25, 'bold'))
		down_label.grid(row=5, column=2)
		
		down_label.after(90000,CryptoTicker.labels)

	def close(self):
		root.destroy()

def hwg():
	global summe
	global sellcoinpercsav
	global sellcoinsav
	global summepurchase
	global basemaxtime
	global basemax
	global summemax
	global summeprint
	global baseprint
	global basemaxprint
	global summemaxprint
	global summemaxtime
	global pricebtc
	global priceamp

#	while True:
	try:
#		print("in")
		for i in range(len(df)) :
			qtycoin = float(df.loc[i,"Qty"])
			purchasecoin =  float(df.loc[i,"Purchase"])
			ren = requests.get('https://api.coingecko.com/api/v3/coins/' + df.loc[i,"Coin"]).json()
			ren = { 'price_usd': ren['market_data']['current_price']['usd'] }
			pricecoin = float(ren['price_usd'])
			summepurchase = summepurchase + qtycoin * purchasecoin
			sellcoinperc = (pricecoin - purchasecoin) / purchasecoin
			if (sellcoinperc > 4):
				sellcoinsav = df.loc[i,"Coin"]
				sellcoinpercsav = sellcoinperc
			summe = summe + qtycoin * pricecoin    
#			print (qtycoin,pricecoin,summe)
			if df.loc[i,"Coin"] == "bitcoin":
				pricebtc = pricecoin
			if df.loc[i,"Coin"] == "ampleforth":
				priceamp = pricecoin
	except:
			print("Error reading Coin URL", df.loc[i,"Coin"])

	base = float(round(summe / pricebtc, 2))
	if (base > basemax):

		with open('configticker.csv', 'a', newline='') as csvfile:
			basemaxtime = datetime.datetime.now()
			savwriter = csv.writer(csvfile, delimiter=';')
			text2=["basemax"] + [basemax] + [basemaxtime]
			savwriter.writerow(text2)
			text2=["summemax"] + [summemax] + [summemaxtime]
			savwriter.writerow(text2)
		basemax = base

	summe = summe / 1000
	if (summe > summemax):
		with open('configticker.csv', 'a', newline='') as csvfile:
			summemaxtime = datetime.datetime.now()
			savwriter = csv.writer(csvfile, delimiter=';')
			text2=["basemax"] + [basemax] + [basemaxtime]
			savwriter.writerow(text2)
			text2=["summemax"] + [summemax] + [summemaxtime]
			savwriter.writerow(text2)
		summemax = summe


	currency = "${:,.2f}T".format(summemax)
	summemaxprint = str(currency)
	currency = "${:,.2f}T".format(summe)
	summeprint    = str(currency)
	basemaxprint  = str(basemax)
	baseprint     = str(base)
	print(summeprint)
#	summe = 0

root = Tk()
root.configure(cursor='none')
root.attributes('-fullscreen', True)
my_gui = CryptoTicker(root)
hwg()
CryptoTicker.labels()
root.mainloop()
#time.sleep(3)

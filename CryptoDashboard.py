#!/usr/bin/env python3
from tkinter import *
import pigpio
import pandas as pd
import requests
import time
import sys
import datetime
import csv

gpio = pigpio.pi()

investusd = 8.44
investbtc = 0.77
pricebtc = 0
btc = 0
summe = 0
onlyonce = 0
#summepurchase = 0
sellcoinpercsav = 0
sellcoin = ' '
sellcoinsav = ' '
now = datetime.datetime.now()
df = pd.read_csv('portfolio.csv', delimiter=';', names = ['Coin', 'Qty', 'Purchase'])
tf = pd.read_csv('ConfigCryptoDashboard.csv', delimiter=';', names = ['Name', 'Value', 'Zeit'])
result=[]

for i in range(len(tf)) :
	if tf.loc[i,"Name"] == "summemax":
		summemax = float(tf.loc[i,"Value"])
		summemaxtime = str(tf.loc[i,"Zeit"])
	if tf.loc[i,"Name"] == "btcmax":
		btcmax = float(tf.loc[i,"Value"])
		btcmaxtime = str(tf.loc[i,"Zeit"])

class CryptoTicker:
	def __init__(self, master):
		self.master = master
		self.close_button = Button(text="C", command=self.close)
		self.close_button.grid(row=0, column=0)

		self.label = Label(master, text="Crypto Dashboard",justify=LEFT, width=20, font=('Helvetica',32, 'bold'), fg = 'blue')
		self.label.grid(row=0, column=1, columnspan=2)

	def labels():
		hwg()

#		investbtc = summepurchase * 1000 / purchasebtc
		currency = "{:,.2f}".format(investbtc)
		text1 = str(btcmaxtime) #.strftime("%Y-%m-%d %H:%M")
		text2 =  "Portfolio____: " + u'\u20bf' + str(btcprint)
		text3a =  "Portfolio Start: " + u'\u20bf' + str(currency)
		text3 =  "Portfolio ATH: " + u'\u20bf' + str(btcmaxprint)
		down_label = Label(text=(text2 + '\n' + text3a + '\n' + text3 ),anchor=NW, width = 19, height=3, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=2, column=1)
		
		currency = "${:,.2f}T".format(investusd)
		text5 = "Portfolio____: " + str(summeprint)
		text9 = "Portfolio Start: " + str(currency)
		text6 = "Portfolio ATH: " + str(summemaxprint)
		down_label = Label(text=(text5 + '\n' + text9 + '\n' + text6), anchor=NW, width = 19, height=3, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=2, column=2)

		text4 = "ATH $ date: " + str(summemaxtime)
		down_label = Label(text=(text4), anchor=NW, width = 39, height=2, justify=LEFT,font=('Helvetica',12))
		down_label.grid(row=3, column=2)
		
		currency = "${:,.2f}".format(priceamp)
		text7 = "AMPL: " + str(currency)
		currency = "${:,.2f}".format(pricebtc)
		text8 = "BTC_: " + str(currency)
		down_label = Label(text=(text7 + '\n' + text8), anchor=NW, width = 19, justify=LEFT,font=('Helvetica',25, 'bold'))
		down_label.grid(row=4, column=1)

		invperc = summe / investusd
		currency = "{:,.0%}".format(invperc)
		text10 = "RoI: " + str(currency)
		down_label = Label(text=(text10), width = 19, bg='#111118', justify=LEFT,relief=RAISED, font=('Helvetica',25,'bold'), fg='white')
		down_label.grid(row=4, column=2)

# Row 5 to 9 = top 4 performing coins (profit)
		down_label = Label(text=('Portfolio top 4 profit:'), anchor=NW, width = 19, height=4, justify=RIGHT,font=('Helvetica',25, 'bold'), fg="red")
		down_label.grid(row=5, column=1)

        text11=str(res.Coin.iloc[0])
        currencya = "{:,.0%}".format(res.result.iloc[0])
		text11a = str(currencya)
        text12=str(res.Coin.iloc[1])
        currencyb = "{:,.0%}".format(res.result.iloc[1])
		text12a = str(currencyb)
        text13=str(res.Coin.iloc[2])
        currencyc = "{:,.0%}".format(res.result.iloc[2])
		text13a = str(currencyc)
        text14=str(res.Coin.iloc[3])
        currencyd = "{:,.0%}".format(res.result.iloc[3])
		text14a = str(currencyd)
		down_label = Label(text=(text11 + ' ' + text11a + '\n' +  text12 + ' ' + text12a + '\n' + text13 + ' ' + text13a + '\n' +  text14 + ' ' + text14a), anchor=NW, width = 19, height=4, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=5, column=2)


# This is where you set the update time. 1000 - 1 sec	
		down_label.after(180000,CryptoTicker.labels)

	def close(self):
		root.destroy()

def bright():
	gpio.set_PWM_dutycycle(19, 255)

def dark():
	gpio.set_PWM_dutycycle(19, 30)

def hwg():
	global summe
	global res
	global sellcoinpercsav
	global sellcoinsav
	# global summepurchase
	global btcmaxtime
	global btcmax
	global summemax
	global summeprint
	global onlyonce
	global btcprint
	global btcmaxprint
	global summemaxprint
	global summemaxtime
	global pricebtc
	global priceamp
	global purchasebtc

#	while True:
	try:
#		print("in")
		for i in range(len(df)) :
			qtycoin = float(df.loc[i,"Qty"])
			purchasecoin =  float(df.loc[i,"Purchase"])
			ren = requests.get('https://api.coingecko.com/api/v3/coins/' + df.loc[i,"Coin"]).json()
			ren = { 'price_usd': ren['market_data']['current_price']['usd'] }
			pricecoin = float(ren['price_usd'])
#			summepurchase = summepurchase + qtycoin * purchasecoin
			sellcoinperc = (pricecoin - purchasecoin) / purchasecoin
			if (sellcoinperc > 4):
				sellcoinsav = df.loc[i,"Coin"]
				sellcoinpercsav = sellcoinperc
			summe = summe + qtycoin * pricecoin    
#			print (qtycoin,pricecoin,summe)
			if df.loc[i,"Coin"] == "bitcoin":
				pricebtc = pricecoin
				purchasebtc = purchasecoin
			if df.loc[i,"Coin"] == "ampleforth":
				priceamp = pricecoin
			result.append(sellcoinperc)

	except:
			print("Error reading Coin URL", df.loc[i,"Coin"])

	if onlyonce == 0:
		df["result"] = result
		onlyonce = onlyonce + 1

	res = df.nlargest(4,'result')
#    print(res)
#    print(res.Coin.iloc[0])

	btc = float(round(summe / pricebtc, 2))
	if (btc > btcmax):
		with open('ConfigCryptoDashboard.csv', 'a', newline='') as csvfile:
			btcmaxtime = datetime.datetime.now()
			savwriter = csv.writer(csvfile, delimiter=';')
			text2=["btcmax"] + [btcmax] + [btcmaxtime]
			savwriter.writerow(text2)
			text2=["summemax"] + [summemax] + [summemaxtime]
			savwriter.writerow(text2)
		btcmax = btc
		bright()
	else:
		dark()

	summe = summe / 1000
#	summepurchase = summepurchase / 1000
	if (summe > summemax):
		with open('ConfigCryptoDashboard.csv', 'a', newline='') as csvfile:
			summemaxtime = datetime.datetime.now()
			savwriter = csv.writer(csvfile, delimiter=';')
			text2=["btcmax"] + [btcmax] + [btcmaxtime]
			savwriter.writerow(text2)
			text2=["summemax"] + [summemax] + [summemaxtime]
			savwriter.writerow(text2)
		summemax = summe
		bright()
	else:
		dark()

	currency = "${:,.2f}T".format(summemax)
	summemaxprint = str(currency)
	
	currency = "{:,.2f}".format(btcmax)
	btcmaxprint = str(currency)
	
	currency = "${:,.2f}T".format(summe)
	summeprint    = str(currency)
	
	btcprint     = str(btc)
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

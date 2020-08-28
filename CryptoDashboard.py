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
specialcoin = 'ampleforth'
pricebtc = 0
btc = 0
summe = 0
onlyonce = 0
summemax = 0
summemaxtime = 0
btcmax = 0
btcmaxtime = 0
btcmaxtemp = 0
sellcoinpercsav = 0
sellcoin = ' '
sellcoinsav = ' '

now = datetime.datetime.now()
df = pd.read_csv('portfolio.csv', delimiter=';', names = ['Coin', 'Qty', 'Purchase'])
tf = pd.read_csv('ConfigCryptoDashboard.csv', delimiter=';', names = ['Name', 'Value', 'Zeit'])
result=[]

for i in range(len(tf)) :
	if tf.loc[i,"Name"] == "summemax":
		summemaxtemp = float(tf.loc[i,"Value"])
		summemaxtimetemp = str(tf.loc[i,"Zeit"])
		if summemax < summemaxtemp:
			summemax = summemaxtemp
			summemaxtime = summemaxtimetemp
	if tf.loc[i,"Name"] == "btcmax":
		btcmaxtemp = float(tf.loc[i,"Value"])
		btcmaxtimetemp = str(tf.loc[i,"Zeit"])
		if btcmax < btcmaxtemp:
			btcmax = btcmaxtemp
			btcmaxtime = btcmaxtimetemp

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

# Row 5 to 9 = bottom/top 4 performing coins (profit)
		text98 = "Losers"
		down_label = Label(text=(text98), anchor=SW, width = 19, height=1, justify=LEFT,font=('Helvetica',20))
		down_label.grid(row=5, column=1)
		text99 = "Winners"
		down_label = Label(text=(text99), anchor=SW, width = 19, height=1, justify=LEFT,font=('Helvetica',20))
		down_label.grid(row=5, column=2)

		text11=str(loose.Coin.iloc[0])
		currencya = "{:,.0%}".format(loose.result.iloc[0])
		text11a = str(currencya)
		text12=str(loose.Coin.iloc[1])
		currencyb = "{:,.0%}".format(loose.result.iloc[1])
		text12a = str(currencyb)
		text13=str(loose.Coin.iloc[2])
		currencyc = "{:,.0%}".format(loose.result.iloc[2])
		text13a = str(currencyc)
		text14=str(loose.Coin.iloc[3])
		currencyd = "{:,.0%}".format(loose.result.iloc[3])
		text14a = str(currencyd)
		down_label = Label(text=(text11 + ': ' + text11a + '\n' +  text12 + ': ' + text12a + '\n' + text13 + ': ' + text13a + '\n' +  text14 + ': ' + text14a), anchor=NW, width = 19, relief=RAISED, height=4, justify=LEFT,font=('Helvetica',20, 'bold'), fg='red')
		down_label.grid(row=6, column=1)

		text21=str(win.Coin.iloc[0])
		currencya = "{:,.0%}".format(win.result.iloc[0])
		text21a = str(currencya)
		text22=str(win.Coin.iloc[1])
		currencyb = "{:,.0%}".format(win.result.iloc[1])
		text22a = str(currencyb)
		text23=str(win.Coin.iloc[2])
		currencyc = "{:,.0%}".format(win.result.iloc[2])
		text23a = str(currencyc)
		text24=str(win.Coin.iloc[3])
		currencyd = "{:,.0%}".format(win.result.iloc[3])
		text24a = str(currencyd)
		down_label = Label(text=(text21 + ': ' + text21a + '\n' +  text22 + ': ' + text22a + '\n' + text23 + ': ' + text23a + '\n' +  text24 + ': ' + text24a), anchor=NW, width = 19, relief=RAISED, height=4, justify=LEFT,font=('Helvetica',20, 'bold'), fg='green')
		down_label.grid(row=6, column=2)


# This is where you set the update time. 1000 - 1 sec	
		down_label.after(180000,CryptoTicker.labels)

	def close(self):
		root.destroy()

def bright():
# settings for bright screen. 255 = max	
	gpio.set_PWM_dutycycle(19, 255)

def dark():
# brightness setting. 30 is dimmed display.
	gpio.set_PWM_dutycycle(19, 30)

def hwg():
	global summe
	global win
	global loose
	global sellcoinpercsav
	global sellcoinsav
	global btcmaxtime
	global btcmax
	global result
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

	try:
# here we pull the data from coingecko
		result=[]
		win=[]
		lose=[]
		for i in range(len(df)) :
			qtycoin = float(df.loc[i,"Qty"])
			purchasecoin =  float(df.loc[i,"Purchase"])
			ren = requests.get('https://api.coingecko.com/api/v3/coins/' + df.loc[i,"Coin"]).json()
			ren = { 'price_usd': ren['market_data']['current_price']['usd'] }
			pricecoin = float(ren['price_usd'])
#	accumulating the value of the portfolio
			summe = summe + qtycoin * pricecoin    
#			print (qtycoin,pricecoin,summe)
			if df.loc[i,"Coin"] == "bitcoin":
				pricebtc = pricecoin
				purchasebtc = purchasecoin
#	now we add the increase/decrease of the coin in relation to the pourchase value
			sellcoinperc = (pricecoin - purchasecoin) / purchasecoin
			result.append(sellcoinperc)
	except:
#	it happens sometimes that coingecko is not reachable. that is where this exception will be called
		print("Error reading Coin URL", df.loc[i,"Coin"])
		pricebtc = 0
		pricecoin = 0
#	This process is to get the price of our specialcoin
	try:
		ren = requests.get('https://api.coingecko.com/api/v3/coins/' + specialcoin).json()
		ren = { 'price_usd': ren['market_data']['current_price']['usd'] }
		priceamp = float(ren['price_usd'])
	except:
		print("Error reading Coin URL", specialcoin)
		priceamp = 0

#	collecting top gainers and losers
	df["result"] = 0
	df["result"] = result
	win = df.nlargest(4,'result')
	loose = df.nsmallest(4,'result')

# this section to store the max value of the portfolio in usd and btc
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

root = Tk()
root.configure(cursor='none')
root.attributes('-fullscreen', True)
my_gui = CryptoTicker(root)
hwg()
CryptoTicker.labels()
root.mainloop()
#time.sleep(3)

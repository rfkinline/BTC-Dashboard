#!/usr/bin/env python3
from tkinter import *
import pigpio
import pandas as pd
import requests
import time
import sys
import datetime
import csv
from urllib.request import urlopen
from json import loads

gpio = pigpio.pi()

specialcoin1 = 'lend'
specialcoin2 = 'ethereum'
pricebtc = 0
btc = 0
summe = 0
onlyonce = 0
btcmaxtemp = 0
sellcoinpercsav = 0
sellcoin = ' '
sellcoinsav = ' '

now = datetime.datetime.now()
df = pd.read_csv('portfolio.csv', delimiter=';', names = ['Coin', 'Qty', 'Purchase'])
result=[]

class CryptoTicker:
	def __init__(self, master):
		self.master = master
		self.close_button = Button(text="C", command=self.close)
		self.close_button.grid(row=0, column=0)
		self.label = Label(master, text="DeFi Dashboard",anchor=W, justify=LEFT, font=('Helvetica',32, 'bold'), fg = 'blue')
		self.label.grid(row=0, column=1, columnspan=1)

	def labels():
		hwg()

#		investbtc = summepurchase * 1000 / purchasebtc
		text1 = str(portsummemaxprint)
		down_label = Label(text=(text2 + '\n' + text3a + '\n' + text3 + text5 + '\n' + text9 + '\n' + text6),anchor=NW, width = 19, height=3, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=2, column=1)
		
        currency = "{:,.2f}".format(investbtc)
		text1 = "str(btcmaxtime) #.strftime("%Y-%m-%d %H:%M")
		text2 =  "Portfolio____: " + u'\u20bf' + str(btcprint)
		text3a =  "Portfolio Start: " + u'\u20bf' + str(currency)
		text3 =  "Portfolio ATH: " + u'\u20bf' + str(btcmaxprint)
		currency = "${:,.2f}T".format(investusd)
		text5 = "Portfolio____: " + str(summeprint)
		text9 = "Portfolio Start: " + str(currency)
		text6 = "Portfolio ATH: " + str(summemaxprint)
		down_label = Label(text=(text2 + '\n' + text3a + '\n' + text3 + text5 + '\n' + text9 + '\n' + text6),anchor=NW, width = 19, height=3, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=2, column=1)
		
		text4 = "ATH $ date: " + str(summemaxtime)
	
		currency = "${:,.2f}".format(pricespec1)
		text7 = str(specialcoin1) + ": " + str(currency)
		currency = "${:,.2f}".format(pricespec2)
		text8 = str(specialcoin2) + ": " + str(currency)
		invperc = summe / investusd
		currency = "{:,.0%}".format(invperc)
		text10b = "RoI: " + str(currency)
		text10 = "Index: " + str(fearindex) + " / " + str(fearindexvalue)
		down_label = Label(text=(text7 + '\n' + text8 + text10 + '\n' + text10b), anchor=NW, width = 19, justify=LEFT,font=('Helvetica',25, 'bold'))
		down_label.grid(row=4, column=1)

#		down_label = Label(text=(), anchor=W, width = 19, bg='#111118', justify=LEFT,relief=RAISED, font=('Helvetica',25,'bold'), fg='white')

# Row 5 to 9 = bottom/top 4 performing coins (profit)
#a		text98 = "Losers last 24hrs"
		text98 = "Losers"
		text99 = "Winners"
		down_label = Label(text=(text98 + text99), anchor=SW, width = 19, height=1, justify=LEFT,font=('Helvetica',20))
		down_label.grid(row=5, column=1)

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
	global fearindex
	global fearindexvalue
	global btcmaxprint
	global summemaxprint
	global summemaxtime
	global pricebtc
	global pricespec1
	global pricespec2
	global purchasebtc

	try:
# here we pull the data from coingecko
		pricespec1 = 0
		pricespec2 = 0
		pricebtc = 0
		pricecoin = 0
		result=[]
		win=[]
		lose=[]
		for i in range(len(df)) :
			qtycoin = float(df.loc[i,"Qty"])
			purchasecoin =  float(df.loc[i,"Purchase"])
			pricecoin = float(loads(urlopen('https://api.coingecko.com/api/v3/coins/' + df.loc[i,"Coin"]).read())['market_data']['current_price']['usd'])
#a			sellcoinperc = float(loads(urlopen('https://api.coingecko.com/api/v3/coins/' + df.loc[i,"Coin"]).read())['market_data']['price_change_percentage_24h'])

# "id":"dash"
# "symbol":"dash"
# "name":"Dash"
# "image":https://assets.coingecko.com/coins/images/19/large/dash-logo.png?1548385930
# "current_price":77.71
# "market_cap":754634637
# "market_cap_rank":31
# "fully_diluted_valuation":null
# "total_volume":330371413
# “high_24h":83.68
# "low_24h":77.36
# "price_change_24h":-5.59646068
# "price_change_percentage_24h":-6.71763
# "market_cap_change_24h":-47463423.19708491
# "market_cap_change_percentage_24h":-5.91741
# "circulating_supply":9688935.17191693
# "total_supply":18920000.0
# "max_supply":null,"ath":1493.59
# "ath_change_percentage":-94.7853
# "ath_date":"2017-12-20T00:00:00.000Z"
# "atl":0.213899
# "atl_change_percentage":36312.62015
# "atl_date":"2014-02-14T00:00:00.000Z"
# "roi":null
# "last_updated":"2020-09-03T13:06:04.156Z"
			
#	accumulating the value of the portfolio
			summe = summe + qtycoin * pricecoin    
#			print (qtycoin,pricecoin,summe)
			if df.loc[i,"Coin"] == "bitcoin":
				pricebtc = pricecoin
				purchasebtc = purchasecoin
#	now we add the increase/decrease of the coin in relation to the pourchase value
			sellcoinperc = (pricecoin - purchasecoin) / purchasecoin
#a			sellcoinperc = sellcoinperc / 100
			result.append(sellcoinperc)
	except:
#	it happens sometimes that coingecko is not reachable. that is where this exception will be called
		print("Error reading Coin URL", df.loc[i,"Coin"])

#	This process is to get the price of our specialcoin
	try:
		pricespec1 = float(loads(urlopen('https://api.coingecko.com/api/v3/coins/' + specialcoin1).read())['market_data']['current_price']['usd'])
		pricespec2 = float(loads(urlopen('https://api.coingecko.com/api/v3/coins/' + specialcoin2).read())['market_data']['current_price']['usd'])
	except:
		print("Error reading Coin URL", specialcoin1)

	try:
#	get the fearindex
		fearindex = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value_classification'])
		fearindexvalue = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value'])
	except:
		print("Error reading Fearindex URL")


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

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
#	get the fearindex
		fearindex = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value_classification'])
		fearindexvalue = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value'])
	except:
		print("Error reading Fearindex")
	try:

#	get blockchain data https://blockchair.com/api/docs#link_M03
# next_retarget_time_estimate
		pricebtc = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data'][0]['market_price_usd'])
		pricebtc24hrchange = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data'][0]['market_price_usd_change_24h_percentage'])
		marketcapbtc = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data'][0]['market_cap_usd'])
		suggested_transaction_fee = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data'][0]['suggested_transaction_fee_per_byte_sat'])
		hashrate24hr = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data'][0]['hashrate_24h'])
		mempool = str(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data'][0]['mempool_transactions'])
		blocks = str(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data'][0]['blocks'])
		hashrate24hr = hashrate24hr / 1000000000000000000  # in EH/s
		satsusd = 1 / pricebtc * 100000000
	except:
		print("Error reading Blockchair")

#	get GitHub data
		commits = str(loads(urlopen('https://api.coincodecap.com/v1/details_v1/BTC').read())['data'][0]['total_commits'])
	except:
		print("Error reading CoinCodeCap")

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

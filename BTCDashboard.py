#!/usr/bin/env python3
from tkinter import *
import pigpio
#import pandas as pd
import requests
#import time
import sys
import datetime
#import csv
from urllib.request import urlopen
from json import loads

gpio = pigpio.pi()

# now = datetime.datetime.now()

class BTCTicker:
	def __init__(self, master):
		self.master = master
		self.close_button = Button(text="C", command=self.close)
		self.close_button.grid(row=0, column=0)
		self.label = Label(master, text="BTC Dashboard",anchor=W, justify=LEFT, font=('Helvetica',32, 'bold'), fg = 'blue')
		self.label.grid(row=0, column=1, columnspan=1)

	def labels():
		hwg()
		currency = "{:,.2f}".format(pricebtc)
		text1 = "BTC Price: " + u'\u20bf' + str(currency)
		text2 = "Delta: " + str(pricebtc24hrchange)
		currency = "{:,.2f}".format(satsusd)
		text3 = "Sats: " + u'\u20bf' + str(currency)
		currency = "{:,.2f}".format(marketcapbtc)
		text4 = "Marketcap: " + u'\u20bf' + str(currency)
		text5 = "Hashrate: " + str(hashrate24hr)
		text6 = "mempool: " + str(mempool)
		text7 = "Blocks: " + str(blocks)
		currency = "{:,.2f}".format(suggested_transaction_fee)
		text8 = "Fees: " + str(currency)
		text9 = "Blocks: " + str(commits)
		text10 = "Findex: " + str(fearindex)
		text11 = "Fvalue: " + str(fearindexvalue)
	
		down_label = Label(text=(text1 + '\n' + text2 + '\n' + text3 + '\n'  + text4 + '\n' + text5 + '\n' + text6 + '\n' + text7 + '\n' + text8 + '\n'  + text9 + '\n' + text10 + '\n' + text11),anchor=NW, width = 19, justify=LEFT,font=('Helvetica',25))
		down_label.grid(row=2, column=1)
		
        
#		text1 = "str(btcmaxtime) #.strftime("%Y-%m-%d %H:%M")
#		text2 =  "Portfolio____: " + u'\u20bf' + str(btcprint)
		
# This is where you set the update time. 1000 - 1 sec	
		down_label.after(180000,BTCTicker.labels)

	def close(self):
		root.destroy()

def bright():
# settings for bright screen. 255 = max	
	gpio.set_PWM_dutycycle(19, 255)

def dark():
# brightness setting. 30 is dimmed display.
	gpio.set_PWM_dutycycle(19, 30)

def hwg():
	global commits
	global fearindex
	global fearindexvalue
	global satsusd
	global hashrate24hr
	global mempool
	global pricebtc
	global pricebtc24hrchange
	global marketcapbtc
	global suggested_transaction_fee
	global blocks

	try:
#	get the fearindex
		fearindex = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value_classification'])
		fearindexvalue = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value'])
		print(fearindex)
	except:
		print("Error reading Fearindex")
	try:

#	get blockchain data https://blockchair.com/api/docs#link_M03
# next_retarget_time_estimate
		pricebtc = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data']['market_price_usd'])
		pricebtc24hrchange = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data']['market_price_usd_change_24h_percentage'])
		marketcapbtc = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data']['market_cap_usd'])
		suggested_transaction_fee = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data']['suggested_transaction_fee_per_byte_sat'])
		hashrate24hr = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data']['hashrate_24h'])
		mempool = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data']['mempool_transactions'])
		blocks = float(loads(urlopen('https://api.blockchair.com/bitcoin/stats').read())['data']['blocks'])
		
		hashrate24hr = hashrate24hr / 1000000000000000000  # in EH/s
		satsusd = 1 / pricebtc * 100000000
	except:
		print("Error reading Blockchair")
	
	try:
#	get GitHub data
		commits = str(loads(urlopen('https://api.coincodecap.com/v1/details_v1/BTC').read())['data']['total_commits'])
	except:
		print("Error reading CoinCodeCap")

#	currency = "${:,.2f}T".format(summemax)
#	summemaxprint = str(currency)
#	currency = "{:,.2f}".format(btcmax)
#	btcmaxprint = str(currency)
#	currency = "${:,.2f}T".format(summe)
#	summeprint    = str(currency)
#	btcprint     = str(btc)
#	print(summeprint)

root = Tk()
root.configure(cursor='none')
root.attributes('-fullscreen', True)
my_gui = BTCTicker(root)
BTCTicker.labels()
root.mainloop()
#time.sleep(3)

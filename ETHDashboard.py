#!/usr/bin/env python3
from tkinter import *
import requests
import sys
import time
import datetime
from urllib.request import urlopen
from json import loads

#display tresholds (change color if x value increased more than y%). 
disppriceeth1hrchangediff = 2    # checked once / hr
dispmarketcap24h = 2          # checked once / day
dispaverage_transaction_fee_usd_24hdiff = 10      # checked every 5 minutes

class ETHTicker:
	def __init__(self, master):
		self.master = master
		self.close_button = Button(image=ethlogo, command=self.close)
		self.close_button.grid(row=0, column=0)
		self.label = Label(master, text=("ETH Dashboard"), font=('Helvetica',32, 'bold'), fg='black', bg = 'gold')
		self.label.grid(row=0, column=1)

	def labels():
		global then
		global onlyonce
		global average_transaction_fee_usd_24hsav
		global average_transaction_fee_usd_24hdiff

		hwg()
		title = "Market Data"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='#454A75', fg='gold')
		down_label.grid(row=2, column=1, sticky=W)

		if priceeth1hrchange * 100 > disppriceeth1hrchangediff:
				color = "lightgreen"
		elif priceeth1hrchange * 100 < disppriceeth1hrchangediff * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.2f}".format(priceeth)
		text1 = "ETH Price: $" + str(currency)
		down_label = Label(text=(text1),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg = color)
		down_label.grid(row=3, column=1, sticky=W)
   

		currency = "{:,.2%}".format(priceeth24hrchange)
		text2 = "24hr change: " + str(currency)
		down_label = Label(text=(text2),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg = "white")
		down_label.grid(row=4, column=1, sticky=W)
		currency = "{:,.2%}".format(market_dominance_percentage)
		text2a = "ETH Dominance: " + str(currency)
		currency = "{:,.0f}".format(xxxx)
		text3 = "Sats per $: " + str(currency)
		down_label = Label(text=(text2a + '\n'+  text3),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg = 'white')
		down_label.grid(row=5, column=1, sticky=W)

		if marketcap24h > dispmarketcap24h:
				color = "lightgreen"
		elif marketcap24h < dispmarketcap24h * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.0f}".format(marketcapeth)
		text4 = "Marketcap: $" + str(currency)
		down_label = Label(text=(text4 + '\n'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg = color)
		down_label.grid(row=6, column=1, sticky=W)

average_gasfee
average_block_time
average_wait_time
dominancepercentage
defilockedusd
dominance_name


		title = "Blockchain Data"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='#454A75', fg='gold')
		down_label.grid(row=7, column=1, sticky=W)

		currency = "{:,.0f}".format(xxxx)
		text5 = "Hashrate 24hr: " + str(currency) + " EH/s"
		down_label = Label(text=(text5),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg=color)
		down_label.grid(row=8, column=1, sticky=W)

		currency = "{:,.02%}".format(xxxx)
		text5a = "Next difficulty estimate: " + str(currency)
		date_time_obj = datetime.datetime.strptime(xxxx time, '%Y-%m-%d %H:%M:%S')
		text5b = "Next adjustment: " + str(date_time_obj.date()) #.strftime("%Y-%m-%d %H:%M")
		down_label = Label(text=(text5a + '\n' + text5b),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg='white')
		down_label.grid(row=9, column=1, sticky=W)

		currency = "{:,.0f}".format(xxxx)
		text6 = "Mempool: " + str(currency) + " transactions   "
		down_label = Label(text=(text6),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg=color)
		down_label.grid(row=10, column=1, sticky=W)

		currency = "{:,.0f}".format(xxxx)
		text7 = "Last block: " + str(currency)
		down_label = Label(text=(text7),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg='white')
		down_label.grid(row=11, column=1, sticky=W)

		if average_transaction_fee_usd_24hdiff > dispaverage_transaction_fee_usd_24hdiff:
				color = "lightcoral"
		elif average_transaction_fee_usd_24hdiff < dispaverage_transaction_fee_usd_24hdiff * -1:
				color = "lightgreen"
		else:
				color = "white"
		currency = "${:,.2f}".format(average_transaction_fee_usd_24h)
		text8 = "Average Fee: " + str(currency)
		currency = "{:,.0f}".format(suggested_transaction_fee)
		down_label = Label(text=(text8),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg=color)
		down_label.grid(row=12, column=1, sticky=W)


		text8a = "Recommended Fee: " + str(currency) + " sat/vB  "
		down_label = Label(text=(text8a + '\n'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg='white')
		down_label.grid(row=13, column=1, sticky=W)

		title = "Others"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='#454A75', fg='gold')
		down_label.grid(row=14, column=1, sticky=W)

		text10 = "Fear & Greed Index: " + str(fearindex)
		text11 = "Fear Value: " + str(fearindexvalue)
		down_label = Label(text=(text10 + '\n' + text11 + '\n'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='#454A75', fg='white')
		down_label.grid(row=15, column=1, sticky=W)
		
		now = datetime.datetime.now()
		duration = now - then
		duration_in_s = duration.total_seconds()
#		print(duration_in_s)
		text99 = "Current time: " + str(now)
		down_label = Label(text=(text99),anchor=NW, justify=LEFT,font=('Helvetica',12), bg='#454A75', fg='white')
		down_label.grid(row=18, column=1, sticky=W)

# first time
		if onlyonce == 0:
			average_transaction_fee_usd_24hsav = average_transaction_fee_usd_24h
			onlyonce = 1

# to calculated the hourly differences
		if duration_in_s > 300:
			average_transaction_fee_usd_24hdiff = average_transaction_fee_usd_24h - average_transaction_fee_usd_24hsav
			average_transaction_fee_usd_24hdiff = average_transaction_fee_usd_24hdiff / average_transaction_fee_usd_24hsav * 100
			average_transaction_fee_usd_24hsav = average_transaction_fee_usd_24h
			then = datetime.datetime.now()
		
# This is where you set the update time. 290000 is about 5 minutes	
		down_label.after(290000,ETHTicker.labels)

	def close(self):
		root.destroy()

def hwg():

	global fearindex
	global fearindexvalue
	global priceeth
	global priceeth1hrchange
	global priceeth24hrchange
	global marketcapeth
	global marketcap24h
	global market_dominance_percentage
	global average_transaction_fee_usd_24h
	global dominancepercentage
	global defilockedusd
	global dominance_name

	fearindex = " "
	fearindexvalue = 0
	priceeth = 0
	priceeth1hrchange = 0
	priceeth24hrchange = 0
	marketcapeth = 0
	marketcap24h = 0
	market_dominance_percentage = 0
	suggested_transaction_fee = 0
	average_transaction_fee_usd_24h = 0

	try:
#	get the defipulse data
		defipuls_api_request = urlopen('https://data-api.defipulse.com/api/v1/defipulse/api/MarketData').read()
		defilockedusd = float(loads(defipuls_api_request)['All']['total'])
		dominance_valueusd = float(loads(defipuls_api_request)['All']['dominance_value'])
		dominance_name = str(loads(defipuls_api_request)['All']['dominance_name'])
		dominancepercentage = dominance_valueusd / defilockedusd
	except:
		print("Error reading DeFiPulse")
		time.sleep(10)
		hwg()

	try:
#	get the fearindex
		fearindex = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value_classification'])
		fearindexvalue = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value'])
	except:
		print("Error reading Fearindex")
		time.sleep(10)
		hwg()

	try:
#	https://docs.ethgasstation.info/gas-price
		ethgasstation_api_request = urlopen('https://ethgasstation.info/api/ethgasAPI.json?').read()
		average_gasfee = float(loads(ethgasstation_api_request)['average'])
		average_block_time = float(loads(ethgasstation_api_request)['block_time'])
		average_wait_time = float(loads(ethgasstation_api_request)['avgWait'])

		average_gasfee = average_gasfee / 10

	except:
		print("Error reading Ethgasstation.info")
		time.sleep(10)
		hwg()
	
	try:
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/coins/ethereum').read()	
		marketcap24h = float(loads(coingecko_api_request)['market_data']['market_cap_change_percentage_24h'])
		priceeth1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		priceeth24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])
		marketcapeth = float(loads(coingecko_api_request)['market_data']['market_cap']['usd'])
		priceeth = float(loads(coingecko_api_request)['market_data']['current_price']['usd'])
		priceeth24hrchange = priceeth24hrchange / 100
		priceeth1hrchange = priceeth1hrchange / 100
		print(priceeth)

	except:
		print("Error reading Coingecko")
		time.sleep(10)
		hwg()

average_transaction_fee_usd_24hsav = 0 
average_transaction_fee_usd_24hdiff = 0 
onlyonce = 0
then = datetime.datetime.now()
root = Tk()
root.configure(cursor='none', bg='#454A75')
root.attributes('-fullscreen', True)
logo = PhotoImage(file=r"ethlogo.png")
ethlogo = logo.subsample(23,23)
my_gui = ETHTicker(root)
ETHTicker.labels()
root.mainloop()

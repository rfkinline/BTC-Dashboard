#!/usr/bin/env python3
from tkinter import *
import requests
import sys
import time
import datetime
from urllib.request import urlopen
from json import loads

class BTCTicker:
	def __init__(self, master):
		self.master = master
		self.close_button = Button(image=btclogo, command=self.close)
		self.close_button.grid(row=0, column=0)
		self.label = Label(master, text=("BTC Dashboard"), font=('Helvetica',32, 'bold'), fg='black', bg = 'gold')
		self.label.grid(row=0, column=1)

	def labels():
		global average_transaction_fee_usd_24hdiff
		global average_transaction_fee_usd_24hsav
		global errormessage
		global hashrate24hrdiff
		global hashrate24hrsav
		global mempool
		global mempooldiff
		global mempoolsav
		global onlyonce
		global then

		hwg()
		internet_on()
		title = "Market Data"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='gold')
		down_label.grid(row=2, column=1, sticky=W)

		if pricebtc1hrchange * 100 > disppricebtc1hrchangediff:
				color = "lightgreen"
		elif pricebtc1hrchange * 100 < disppricebtc1hrchangediff * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.2f}".format(pricebtc)
		text1 = "BTC Price: $" + str(currency)
		down_label = Label(text=(text1),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = color)
		down_label.grid(row=3, column=1, sticky=W)
   
		currency = "{:,.2%}".format(pricebtc24hrchange)
		text2 = "24hr change: " + str(currency)
		down_label = Label(text=(text2),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = "white")
		down_label.grid(row=4, column=1, sticky=W)
		currency = "{:,.2%}".format(market_dominance_percentage)
		text2a = "BTC Dominance: " + str(currency)
		currency = "{:,.0f}".format(satsusd)
		text3 = "Sats per $: " + str(currency)
		down_label = Label(text=(text2a + '\n'+  text3),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		down_label.grid(row=5, column=1, sticky=W)

		if marketcap24h > dispmarketcap24h:
				color = "lightgreen"
		elif marketcap24h < dispmarketcap24h * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.0f}".format(marketcapbtc)
		text4 = "Marketcap: $" + str(currency)
		down_label = Label(text=(text4),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = color)
		down_label.grid(row=6, column=1, sticky=W)

		textempty = " "
		down_label = Label(text=(textempty),anchor=NW, justify=LEFT,font=('Helvetica',5), bg='black', fg = color)
		down_label.grid(row=7, column=1, sticky=W)

		title = "Blockchain Data"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='gold')
		down_label.grid(row=8, column=1, sticky=W)

		if hashrate24hrdiff > disphashrate24hrdiff:
				color = "lightgreen"
		elif hashrate24hrdiff < disphashrate24hrdiff * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.0f}".format(hashrate24hr)
		text5 = "Hashrate 24hr: " + str(currency) + " EH/s"
		down_label = Label(text=(text5),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg=color)
		down_label.grid(row=9, column=1, sticky=W)

		currency = "{:,.02%}".format(next_difficulty_estimate)
		text5a = "Next difficulty estimate: " + str(currency)
		date_time_obj = datetime.datetime.strptime(next_retarget_time_estimate, '%Y-%m-%d %H:%M:%S')
		text5b = "Next adjustment: " + str(date_time_obj.date()) #.strftime("%Y-%m-%d %H:%M")
		down_label = Label(text=(text5a + '\n' + text5b),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=10, column=1, sticky=W)

		if mempooldiff > dispmempooldiff:
				color = "lightcoral"
		elif mempooldiff < dispmempooldiff * -1:
				color = "lightgreen"
		else:
				color = "white"
		currency = "{:,.0f}".format(mempool)
		text6 = "Mempool: " + str(currency) + " transactions   "
		down_label = Label(text=(text6),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg=color)
		down_label.grid(row=11, column=1, sticky=W)

		currency = "{:,.0f}".format(blocks)
		text7 = "Last block: " + str(currency)
		down_label = Label(text=(text7),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=12, column=1, sticky=W)

		if average_transaction_fee_usd_24hdiff > dispaverage_transaction_fee_usd_24hdiff:
				color = "lightcoral"
		elif average_transaction_fee_usd_24hdiff < dispaverage_transaction_fee_usd_24hdiff * -1:
				color = "lightgreen"
		else:
				color = "white"
		currency = "${:,.2f}".format(average_transaction_fee_usd_24h)
		text8 = "Average Fee: " + str(currency)
		currency = "{:,.0f}".format(suggested_transaction_fee)
		down_label = Label(text=(text8),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg=color)
		down_label.grid(row=13, column=1, sticky=W)

		text8a = "Recommended Fee: " + str(currency) + " sat/vB  "
		down_label = Label(text=(text8a),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=14, column=1, sticky=W)

		textempty = " "
		down_label = Label(text=(textempty),anchor=NW, justify=LEFT,font=('Helvetica',5), bg='black', fg = color)
		down_label.grid(row=15, column=1, sticky=W)

		title = "Others"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='gold')
		down_label.grid(row=16, column=1, sticky=W)

		text10 = "Fear & Greed Index: " + str(fearindex)
		text11 = "Fear Value: " + str(fearindexvalue)
		currency = "{:,.0f}".format(LNDBTC)
		text12a = "Lightning Netw volume: " + str(currency) + u'\u20bf'
		down_label = Label(text=(text10 + '\n' + text11 + '\n' + text12a),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=17, column=1, sticky=W)
		
		text98 = str(errormessage)
		down_label = Label(text=(text98),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='red')
		down_label.grid(row=18, column=1, sticky=W)
		errormessage = " "
		
		now = datetime.datetime.now()
		duration = now - then
		duration_in_s = duration.total_seconds()
		text99 = "Current time: " + str(now)
		down_label = Label(text=(text99),anchor=NW, justify=LEFT,font=('Helvetica',12), bg='black', fg='white')
		down_label.grid(row=19, column=1, sticky=W)

# first time
		if onlyonce == 0:
			hashrate24hrsav = hashrate24hr
			mempoolsav = mempool
			average_transaction_fee_usd_24hsav = average_transaction_fee_usd_24h
			onlyonce = 1

# to calculated the hourly differences
		if duration_in_s > 300:
			hashrate24hrdiff =  hashrate24hr - hashrate24hrsav
			hashrate24hrdiff =  hashrate24hrdiff / hashrate24hrsav * 100
			hashrate24hrsav = hashrate24hr
			if mempool == 0:
				mempool = 1
			mempooldiff = mempool  - mempoolsav 
			mempooldiff = mempooldiff / mempoolsav * 100
			mempoolsav = mempool 
			average_transaction_fee_usd_24hdiff = average_transaction_fee_usd_24h - average_transaction_fee_usd_24hsav
			average_transaction_fee_usd_24hdiff = average_transaction_fee_usd_24hdiff / average_transaction_fee_usd_24hsav * 100
			average_transaction_fee_usd_24hsav = average_transaction_fee_usd_24h
			then = datetime.datetime.now()
		
# This is where you set the update time. 290000 is about 5 minutes	
		down_label.after(290000,BTCTicker.labels)

	def close(self):
		root.destroy()

def hwg():

	global average_transaction_fee_usd_24h
	global blocks
	global errormessage
	global fearindex
	global fearindexvalue
	global hashrate24hr
	global LNDBTC
	global market_dominance_percentage
	global marketcap24h
	global marketcapbtc
	global mempool
	global next_difficulty_estimate
	global next_retarget_time_estimate
	global pricebtc
	global pricebtc1hrchange
	global pricebtc24hrchange
	global satsusd
	global status
	global suggested_transaction_fee

	average_transaction_fee_usd_24h = 0
	blocks = 0
	fearindex = " "
	fearindexvalue = 0
	hashrate24hr = 0
	market_dominance_percentage = 0
	marketcap24h = 0
	marketcapbtc = 0
	mempool = 1
	next_difficulty_estimate = 0
	next_retarget_time_estimate = 0
	pricebtc = 0
	pricebtc1hrchange = 0
	pricebtc24hrchange = 0
	satsusd = 0
	suggested_transaction_fee = 0
	
	try:
#	get the defipulse Project data 
		status = 0
		defi_pulse_url = 'https://data-api.defipulse.com/api/v1/defipulse/api/GetProjects?api-key='+ defipulseApikey
		urltest = requests.get(defi_pulse_url)
		status = urltest.status_code
		if status == 200:
			total_value_locked = requests.get(defi_pulse_url)
			json_obj = total_value_locked.json()
			for project in json_obj:
				name = project.get("name")
				if name == 'Lightning Network':
					LNDBTC = project['value']['tvl']['BTC'].get("value")
		elif status == 429:
			print("Error DefiPulse. Wrong or expired API key")
			errormessage = "Error DefiPulse. Wrong or expired API key"
			raise
		else:
			print("Error reading DeFiPulse. Error-code: " + str(status))
			errormessage = "Unknown error reading DeFiPulse Project"
	except:
		if status == 204:
			time.sleep(5)
			hwg()

	try:
#	get the fearindex
		fearindex = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value_classification'])
		fearindexvalue = str(loads(urlopen('https://api.alternative.me/fng/').read())['data'][0]['value'])
	except:
		errormessage = "Error reading Fearindex"
		print(errormessage)
		if status == 204:
			time.sleep(5)
			hwg()

	try:
#	get blockchain data https://blockchair.com/api/docs#link_M03
		blockchair_api_request = urlopen('https://api.blockchair.com/bitcoin/stats').read()	
		market_dominance_percentage = float(loads(blockchair_api_request)['data']['market_dominance_percentage'])
		suggested_transaction_fee = float(loads(blockchair_api_request)['data']['suggested_transaction_fee_per_byte_sat'])
		average_transaction_fee_usd_24h = float(loads(blockchair_api_request)['data']['average_transaction_fee_usd_24h'])
		hashrate24hr = float(loads(blockchair_api_request)['data']['hashrate_24h'])
		mempool = float(loads(blockchair_api_request)['data']['mempool_transactions'])
		blocks = float(loads(blockchair_api_request)['data']['blocks'])
		next_retarget_time_estimate = str(loads(blockchair_api_request)['data']['next_retarget_time_estimate'])
		next_difficulty_estimate = float(loads(blockchair_api_request)['data']['next_difficulty_estimate'])
		difficulty = float(loads(blockchair_api_request)['data']['difficulty'])

		market_dominance_percentage = market_dominance_percentage / 100
		hashrate24hr = hashrate24hr / 1000000000000000000  # in EH/s
		next_difficulty_estimate = 1 - difficulty / next_difficulty_estimate

	except:
		errormessage = "Error reading Blockchair"
		print(errormessage)
		if status == 204:
			time.sleep(5)
			hwg()
	
	try:
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/coins/bitcoin').read()	
		marketcap24h = float(loads(coingecko_api_request)['market_data']['market_cap_change_percentage_24h'])
		pricebtc1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		pricebtc24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])
		marketcapbtc = float(loads(coingecko_api_request)['market_data']['market_cap']['usd'])
		pricebtc = float(loads(coingecko_api_request)['market_data']['current_price']['usd'])
		satsusd = 1 / pricebtc * 100000000
		pricebtc24hrchange = pricebtc24hrchange / 100
		pricebtc1hrchange = pricebtc1hrchange / 100
		print(pricebtc)

	except:
		errormessage = "Error reading Coingecko"
		print(errormessage)
		if status == 204:
			time.sleep(5)
			hwg()

def internet_on(url='http://www.google.com/', timeout=5):
	try:
		_ = requests.get(url, timeout=timeout)
		return True
	except requests.ConnectionError:
		errormessage = "No internet connection available."
	return False

exec(open(r"variables").read())
errormessage=""
LNDBTC = 0
hashrate24hrsav = 0
mempoolsav = 0
average_transaction_fee_usd_24hsav = 0 
hashrate24hrdiff = 0
mempooldiff = 0
average_transaction_fee_usd_24hdiff = 0 
onlyonce = 0
then = datetime.datetime.now()
root = Tk()
root.configure(cursor='none', bg='black')
root.attributes('-fullscreen', True)
logo = PhotoImage(file=r"btclogo.png")
btclogo = logo.subsample(23,23)
my_gui = BTCTicker(root)
BTCTicker.labels()
root.mainloop()
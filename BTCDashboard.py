#!/usr/bin/env python3
from tkinter import *
import requests
import socket
import sys
import time
import datetime
from urllib.request import urlopen
from json import loads
# This is where you set the refresh time in miliseconds. 1000 = 1 second. Do not go less than 100
refreshtime = 1500

class BTCTicker:
	def __init__(self, master):

		global price_label
		global change24_label
		global dom_label
		global sats_label
		global mcap_label
		global hash_label
		global dif_label
		global adj_label
		global memp_label
		global block_label
		global avgfee_label
		global recfee_label
		global high24_label
		global low24_label
		global ath_label
		global athchg_label
		global athdate_label
		global circ_label
		global fearindex_label
		global fearvalue_label
		global lgtcap_label
		global error_label1
		global error_label2
		global error_label3
		global error_label4
		global update_label
		
		self.master = master
		self.close_button = Button(image=btclogo, command=self.close)
		self.close_button.grid(row=0, column=0)
		self.label = Label(master, text=("   \u20bfitcoin Dashboard       "), font=('Helvetica',32, 'bold'), fg='black', bg = '#f2a900')
		self.label.grid(row=0, column=1)

		title = "Market Data"
		market_label = Label(master, text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='#f2a900')
		market_label.grid(row=2, column=1, sticky=W)
		price_label = Label(text=("BTC Price: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20, 'bold'), bg='black', fg = 'white')
		price_label.grid(row=3, column=1, sticky=W)
		change24_label = Label(text=("24hr change: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = "white")
		change24_label.grid(row=4, column=1, sticky=W)
		dom_label = Label(text=("BTC Dominance: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		dom_label.grid(row=5, column=1, sticky=W)
		sats_label = Label(text=("Sats per $: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		sats_label.grid(row=6, column=1, sticky=W)
		mcap_label = Label(text=("Marketcap: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		mcap_label.grid(row=7, column=1, sticky=W)
		textempty = " "
		empty_label = Label(master, text=(textempty),anchor=NW, justify=LEFT,font=('Helvetica',5), bg='black', fg = '#f2a900')
		empty_label.grid(row=8, column=1, sticky=W)

		title2 = "Blockchain Data"
		blockchain_label = Label(master, text=(title2),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='#f2a900')
		blockchain_label.grid(row=9, column=1, sticky=W)
		hash_label = Label(text=("Hashrate 24hr: " + str(0) + " EH/s"),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		hash_label.grid(row=10, column=1, sticky=W)
		dif_label = Label(text=("Next difficulty estimate: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		dif_label.grid(row=11, column=1, sticky=W)
		adj_label = Label(text=("Next adjustment: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		adj_label.grid(row=12, column=1, sticky=W)
		memp_label = Label(text=("Mempool: " + str(0) + " transactions"),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		memp_label.grid(row=13, column=1, sticky=W)
		block_label = Label(text=("Last block: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		block_label.grid(row=14, column=1, sticky=W)
		avgfee_label = Label(text=("Average Fee: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		avgfee_label.grid(row=15, column=1, sticky=W)
		recfee_label = Label(text=("Recommended Fee: " + str(0) + " sat/vB"),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		recfee_label.grid(row=16, column=1, sticky=W)

		title3 = "Others"
		others_label = Label(master, text=(title3),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='#f2a900')
		others_label.grid(row=2, column=3, sticky=W)
		high24_label = Label(text=("BTC High 24hr: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		high24_label.grid(row=3, column=3, sticky=W)
		low24_label = Label(text=("BTC Low 24hr: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		low24_label.grid(row=4, column=3, sticky=W)
		ath_label = Label(text=("ATH: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		ath_label.grid(row=5, column=3, sticky=W)
		athchg_label = Label(text=("ATH change: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		athchg_label.grid(row=6, column=3, sticky=W)
		athdate_label = Label(text=("ATH Date: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		athdate_label.grid(row=7, column=3, sticky=W)
		circ_label = Label(text=("Circulating BTC: " + str(0) + u'\u20bf'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		circ_label.grid(row=8, column=3, sticky=W)
		fearindex_label = Label(text=("Fear & Greed Index: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		fearindex_label.grid(row=9, column=3, sticky=W)
		fearvalue_label = Label(text=("Fear Value: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		fearvalue_label.grid(row=10, column=3, sticky=W)
		lgtcap_label = Label(text=("Lightning Netw Capacity: " + str(0) + u'\u20bf'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		lgtcap_label.grid(row=11, column=3, sticky=W)
		error_label1 = Label(text=(""),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='red')
		error_label1.grid(row=12, column=3, sticky=W)
		error_label2 = Label(text=(""),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='red')
		error_label2.grid(row=13, column=3, sticky=W)
		error_label3 = Label(text=(""),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='red')
		error_label3.grid(row=14, column=3, sticky=W)	
		error_label4 = Label(text=(""),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='red')
		error_label4.grid(row=15, column=3, sticky=W)
		update_label = Label(text=("Last Update: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',12), bg='black', fg='white')
		update_label.grid(row=16, column=3, sticky=W)
		print("Static Labels Initialized")

	def labels():
		#### Global Variables ####
		global average_transaction_fee_usd_24hdiff
		global average_transaction_fee_usd_24hsav
		global interneterrormessage
		global mlerrormessage
		global alterrormessage
		global bserrormessage
		global bcerrormessage
		global cgerrormessage
		global hashrate24hrdiff
		global hashrate24hrsav
		global mempool
		global mempooldiff
		global mempoolsav
		global onlyonce
		global pricebtc
		global then
		global refreshtime
		#### API Timers ####
		global altstart
		global bitstampstart
		global blockchairstart
		global coingeckostart
		global ml1start
		#### Global Labels ####
		global price_label
		global change24_label
		global dom_label
		global sats_label
		global mcap_label
		global hash_label
		global dif_label
		global adj_label
		global memp_label
		global block_label
		global avgfee_label
		global recfee_label
		global high24_label
		global low24_label
		global ath_label
		global athchg_label
		global athdate_label
		global circ_label
		global fearindex_label
		global fearvalue_label
		global lgtcap_label
		global error_label1
		global error_label2
		global error_label3
		global error_label4
		global update_label	

# Test Internet Connection
		internet_on()

#Free API Request Limits Enforcement

	# Bitstamp allows 800 calls per minute	
		if time.time() - bitstampstart > 0.1:
			bitstamp()
			#print(time.time() - bitstampstart)
			bitstampstart = time.time()
	# Coingecko allows 100 calls per minute
		if time.time() - coingeckostart > 1:
			coingecko()
			#print(time.time() - coingeckostart)
			coingeckostart = time.time()		
	#Blockchair allows 1 call per minute
		if time.time() - blockchairstart > 60:
			blockchair()
			#print(time.time() - blockchairstart)
			blockchairstart = time.time()
			
	# Alternative updates their data every 5 minutes
	# However Alternative allows 60 calls per minute
		if time.time() - altstart > 150:
			alt()
			#print(time.time() - altstart)
			altstart = time.time()
			
	# 1ML unknown API Limit, set to 5 minutes to be safe
		if time.time() - ml1start > 300:
			ml1()
			ml1start = time.time()
		
		#print("Refreshing data on screen")
		refreshtimer = time.time()	

		if pricebtc1hrchange * 100 > disppricebtc1hrchangediff:
				color = "lightgreen"
		elif pricebtc1hrchange * 100 < disppricebtc1hrchangediff * -1:
				color = "lightcoral"
		else:
				color = "white"
		pricebtc = "{:,.2f}".format(pricebtc)
		price_label.configure(text="BTC Price: $" + str(pricebtc), fg = color)
		currency = "{:,.2%}".format(pricebtc24hrchange)
		change24_label.configure(text="24hr change: " + str(currency))
		currency = "{:,.2%}".format(market_dominance_percentage)
		dom_label.configure(text="BTC Dominance: " + str(currency))
		currency = "{:,.0f}".format(satsusd)
		sats_label.configure(text="Sats per $: " + str(currency))

		if marketcap24h > dispmarketcap24h:
				color = "lightgreen"
		elif marketcap24h < dispmarketcap24h * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.0f}".format(marketcapbtc)
		mcap_label.configure(text="Marketcap: $" + str(currency), fg = color)

		if hashrate24hrdiff > disphashrate24hrdiff:
				color = "lightgreen"
		elif hashrate24hrdiff < disphashrate24hrdiff * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.0f}".format(hashrate24hr)
		hash_label.configure(text=("Hashrate 24hr: " + str(currency) + " EH/s"), fg=color)
		currency = "{:,.02%}".format(next_difficulty_estimate)
		dif_label.configure(text="Next difficulty estimate: " + str(currency))
		try:
			date_time_obj = datetime.datetime.strptime(str(next_retarget_time_estimate), '%Y-%m-%d %H:%M:%S')
			textadj = str(date_time_obj.date()) #.strftime("%Y-%m-%d %H:%M")
		except:
			textadj = "Date Error"
		adj_label.configure(text="Next adjustment: " + textadj)

		if mempooldiff > dispmempooldiff:
				color = "lightcoral"
		elif mempooldiff < dispmempooldiff * -1:
				color = "lightgreen"
		else:
				color = "white"
		currency = "{:,.0f}".format(mempool)
		memp_label.configure(text=("Mempool: " + str(currency) + " transactions"), fg=color)
		currency = "{:,.0f}".format(blocks)
		block_label.configure(text="Last block: " + str(currency))

		if average_transaction_fee_usd_24hdiff > dispaverage_transaction_fee_usd_24hdiff:
				color = "lightcoral"
		elif average_transaction_fee_usd_24hdiff < dispaverage_transaction_fee_usd_24hdiff * -1:
				color = "lightgreen"
		else:
				color = "white"
		currency = "${:,.2f}".format(average_transaction_fee_usd_24h)
		avgfee_label.configure(text=("Average Fee: " + str(currency)), fg=color)
		avgfee_label.grid(row=15, column=1, sticky=W)
		currency = "{:,.0f}".format(suggested_transaction_fee)
		recfee_label.configure(text="Recommended Fee: " + str(currency) + " sat/vB")

#	Second Column
		currency = "{:,.2f}".format(high24h)
		high24_label.configure(text="BTC High 24hr: $" + str(currency))
		currency = "{:,.2f}".format(low24h)
		low24_label.configure(text="BTC Low 24hr: $" + str(currency))
		currency = "{:,.2f}".format(ath)
		ath_label.configure(text="ATH: $" + str(currency))
		currency = "{:,.2%}".format(ath_change)
		athchg_label.configure(text="ATH change: " + str(currency))
		try:
			athdate_label.configure(text="ATH Date: " + str(athdate[0:10]))
		except:
			athdate_label.configure(text="ATH Date: Date Error")
		currency = "{:,.0f}".format(circulating_supply)
		circ_label.configure(text="Circulating BTC: " + str(currency) + u'\u20bf')
		fearindex_label.configure(text="Fear & Greed Index: " + str(fearindex))
		fearvalue_label.configure(text="Fear Value: " + str(fearindexvalue))
		currency = "{:,.2f}".format(LNDCap)
		lgtcap_label.configure(text="Lightning Netw Capacity: " + str(currency) + u'\u20bf')
		
		if interneterrormessage == "":
			error_label1.configure(text=str(bserrormessage))
			error_label2.configure(text=str(cgerrormessage))
			error_label3.configure(text=str(bcerrormessage))
			error_label4.configure(text=str(alterrormessage + mlerrormessage))
		else:
			error_label1.configure(text=str(interneterrormessage))
			error_label2.configure(text=str("Please Check Your Internet Connection"))
		
		now = datetime.datetime.now()
		duration = now - then
		duration_in_s = duration.total_seconds()
		update_label.configure(text="Last Update: " + str(now.strftime("%c")))
		#print("Refresh time in seconds: " + str(time.time() - refreshtimer))

# first time
		if onlyonce == 0:
			hashrate24hrsav = hashrate24hr
			mempoolsav = mempool
			average_transaction_fee_usd_24hsav = average_transaction_fee_usd_24h
			onlyonce = 1

# to calculate the hourly differences
		if duration_in_s > 300:
			print("Calculating duration_in_s > 300")
			hashrate24hrdiff =  hashrate24hr - hashrate24hrsav
			try:
				hashrate24hrdiff =  hashrate24hrdiff / hashrate24hrsav * 100
			except ZeroDivisionError:
				print("Zero Division Error Calculating Hashrate 24H diff")
			hashrate24hrsav = hashrate24hr
			if mempool == 0:
				mempool = 1
			mempooldiff = mempool  - mempoolsav 
			try:
				mempooldiff = mempooldiff / mempoolsav * 100
			except ZeroDivisionError:
				print("Zero Division Error Calculating Mempool diff")
			mempoolsav = mempool
			average_transaction_fee_usd_24hdiff = average_transaction_fee_usd_24h - average_transaction_fee_usd_24hsav
			try:
				average_transaction_fee_usd_24hdiff = average_transaction_fee_usd_24hdiff / average_transaction_fee_usd_24hsav * 100
			except ZeroDivisionError:
				print("Zero Division Error Calculating Average Transaction Fee 24H diff")
			average_transaction_fee_usd_24hsav = average_transaction_fee_usd_24h
			then = datetime.datetime.now()
			
		update_label.after(refreshtime,BTCTicker.labels) 
	def close(self):
		root.destroy()

def ml1():
	
	global LNDCap
	global mlerrormessage
	
	LNDCap = 0
	status = 0
	
	try:
		#mltime = time.time()
		ml1_url = 'https://1ml.com/statistics?json=true'
		ml1_api_request = urlopen(ml1_url).read()
		LNDCap = float(loads(ml1_api_request)['networkcapacity'])	
		LNDCap = LNDCap / 100000000
		print("Lightning Stats Updated ") # + str(time.time() - mltime))
		mlerrormessage = ""
	except:
		try:
			urltest = requests.get(ml1_url)
			status = urltest.status_code
			urltest.close()
			mlerrormessage = "Error Reading 1ML "
			print(errormessage + "Status code: " + str(status))
		except:
			mlerrormessage = "1ML Connection Refused "
			print(mlerrormessage)

def alt():
	
	global alterrormessage
	global fearindex
	global fearindexvalue
	
	#alttime = time.time()
	fearindex = " "
	fearindexvalue = 0
	status = 0
	try:
		
	# get the fearindex
		alt_url = 'https://api.alternative.me/fng/'
		alt_api_request = urlopen(alt_url).read()
		fearindex = str(loads(alt_api_request)['data'][0]['value_classification'])
		fearindexvalue = str(loads(alt_api_request)['data'][0]['value'])
		print("Updated Fear Index ") # + str(time.time() - alttime))
		alterrormessage = ""
		
	except:
		try:
			urltest = requests.get(alt_url)
			status = urltest.status_code
			urltest.close()
			alterrormessage = "Error Reading Fear Index "
			print(errormessage + "Status code: " + str(status))
		except:
			alterrormessage = "Alt Connection Refused "
			print(alterrormessage)

def bitstamp():
	
	global bserrormessage
	global pricebtc
	global satsusd
	
	#bittime = time.time()
	pricebtc = 0
	satsusd = 0
	status = 0
	
	try:
		bitstamp_url = 'https://bitstamp.net/api/ticker'
		bitstamp_api_request = urlopen(bitstamp_url).read()
		pricebtc = float(loads(bitstamp_api_request)['last'])
		try:
			satsusd = 1 / pricebtc * 100000000
			bserrormessage = ""
		except ZeroDivisionError:
			print("Zero Division Error Calculating Sats per Dollar")
			bserrormessage = "Bitstamp Price Error "
		print(pricebtc)
		# print(str(time.time() - bittime))

	except:
		try:
			urltest = requests.get(bitstamp_url)
			status = urltest.status_code
			urltest.close()
			bserrormessage = "Error Reading BitStamp "
			print(errormessage + "Status code: " + str(status))
		except:
			bserrormessage = "Bitstamp Connection Refused "
			print(bserrormessage)

def blockchair():
	
	global average_transaction_fee_usd_24h
	global blocks
	global bcerrormessage
	global hashrate24hr
	global market_dominance_percentage
	global mempool
	global next_difficulty_estimate
	global next_retarget_time_estimate
	global suggested_transaction_fee
	
	#blocktime = time.time()
	average_transaction_fee_usd_24h = 0
	blocks = 0
	hashrate24hr = 0
	market_dominance_percentage = 0
	mempool = 1
	next_difficulty_estimate = 0
	next_retarget_time_estimate = 0
	status = 0
	suggested_transaction_fee = 0
	
	try:
#	get blockchain data https://blockchair.com/api/docs#link_M03
		blockchair_url = 'https://api.blockchair.com/bitcoin/stats'
		blockchair_api_request = urlopen(blockchair_url).read()	
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
		try:
			next_difficulty_estimate = 1 - difficulty / next_difficulty_estimate
			bcerrormessage = ""
		except ZeroDivisionError:
			print("Zero Division Error While Calculating Next Difficulty Estimate")
			bcerrormessage = "Bitstamp Diff Est Error "
		print("Updated Blockchair Stats ") # + str(time.time() - blocktime))

	except:
		try:
			urltest = requests.get(blockchair_url)
			status = urltest.status_code
			urltest.close()
			bcerrormessage = "Error Reading Blockchair "
			print(errormessage + "Status code: " + str(status))
		except:
			bcerrormessage = "Blockchair Connection Refused "
			print(bcerrormessage)

def coingecko():

	global ath
	global ath_change
	global athdate
	global circulating_supply
	global cgerrormessage
	global high24h
	global low24h
	global LNDBTC
	global marketcap24h
	global marketcapbtc
	global pricebtc1hrchange
	global pricebtc24hrchange
	global status

	#cointime = time.time()
	ath = 0
	ath_change = 0
	circulating_supply = 0
	high24h = 0
	low24h = 0
	marketcap24h = 0
	marketcapbtc = 0
	pricebtc1hrchange = 0
	pricebtc24hrchange = 0
	status = 0
	
	try:
		coingecko_url = 'https://api.coingecko.com/api/v3/coins/bitcoin'
		coingecko_api_request = urlopen(coingecko_url).read()	
		marketcap24h = float(loads(coingecko_api_request)['market_data']['market_cap_change_percentage_24h'])
		pricebtc24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])
		pricebtc1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		high24h = float(loads(coingecko_api_request)['market_data']['high_24h']['usd'])
		low24h = float(loads(coingecko_api_request)['market_data']['low_24h']['usd'])
		marketcapbtc = float(loads(coingecko_api_request)['market_data']['market_cap']['usd'])
		ath = float(loads(coingecko_api_request)['market_data']['ath']['usd'])
		ath_change = float(loads(coingecko_api_request)['market_data']['ath_change_percentage']['usd'])
		athdate = str(loads(coingecko_api_request)['market_data']['ath_date']['usd'])
		circulating_supply = float(loads(coingecko_api_request)['market_data']['circulating_supply'])
		pricebtc24hrchange = pricebtc24hrchange / 100
		ath_change = ath_change / 100
		print("Updated CoinGecko Stats ") # + str(time.time() - cointime))
		cgerrormessage = ""

	except:
		try:
			urltest = requests.get(coingecko_url)
			status = urltest.status_code
			urltest.close()
			cgerrormessage = "Error reading Coingecko "
			print(errormessage + "Status code: " + str(status))
		except:
			cgerrormessage = "CoinGecko Connection Refused "
			print(cgerrormessage)

def internet_on(host="8.8.8.8", port=53, timeout=3):
	global interneterrormessage
	"""
	Host: 8.8.8.8 (google-public-dns-a.google.com)
	OpenPort: 53/tcp
	Service: domain (DNS/TCP)
	"""
	try:
		#print("Testing Internet Connection")
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		interneterrormessage = ""
		return True
	except socket.error as ex:
		interneterrormessage = "No Internet Connection Available"
		print(interneterrormessage)
		print(ex)
		return False

exec(open(r"variables").read())
mlerrormessage = alterrormessage = bserrormessage = bcerrormessage = cgerrormessage = interneterrormessage = ""
ml1start = altstart = bitstampstart = blockchairstart = coingeckostart = time.time()
LNDBTC = 0
hashrate24hrsav = 0
mempoolsav = 0
average_transaction_fee_usd_24hsav = 1 
hashrate24hrdiff = 0
mempooldiff = 0
average_transaction_fee_usd_24hdiff = 0 
onlyonce = 0
then = datetime.datetime.now()
root = Tk()
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
print("Screen Width: " + str(width_value))
print("Screen Height: " + str(height_value))
root.geometry("%dx%d+0+0" % (width_value, height_value))
root.configure(bg='black', cursor= 'crosshair')
root.attributes('-fullscreen', True)
price_label = Label(root)
change24_label = Label(root)
dom_label = Label(root)
sats_label = Label(root)
mcap_label = Label(root)
hash_label = Label(root)
dif_label = Label(root)
adj_label = Label(root)
memp_label = Label(root)
block_label = Label(root)
avgfee_label = Label(root)
recfee_label = Label(root)
high24_label = Label(root)
low24_label = Label(root)
ath_label = Label(root)
athchg_label = Label(root)
athdate_label = Label(root)
circ_label = Label(root)
fearindex_label = Label(root)
fearvalue_label = Label(root)
lgtcap_label = Label(root)
error_label1 = Label(root)
error_label2 = Label(root)
error_label3 = Label(root)
error_label4 = Label(root)
update_label = Label(root)
logo = PhotoImage(file=r"btclogo.png")
biglogo = logo.subsample(5,5)
btclogo = logo.subsample(23,23)
my_gui = BTCTicker(root)
internet_on()
bitstamp()
coingecko()
blockchair()
alt()
ml1()
BTCTicker.labels()
root.mainloop()
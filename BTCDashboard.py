#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import requests
import sys
import time
import threading
from time import strftime
from time import gmtime
import datetime
from PIL import ImageTk,Image
from urllib.request import urlopen
from json import loads

version = "v2.1.1"
refreshtime = 5000

class BTCTicker:
	def __init__(self, master):

		global price_label
		global change24_label
		global dom_label
		global sats_label
		global mcap_label
		global blockchain_label
		global hash_label
		global dif_label
		global memp_label
		global block_label
		global avgfee_label
		global recfee_label
		global recfeeusd_label
		global high24_label
		global low24_label
		global ath_label
		global athchg_label
		global athdate_label
		global circ_label
		global fearindex_label
		global lightning_label
		global lgtcap_label
		global lnodes_label
		global lnchannels_label
		global error_label1
		global error_label2
		global update_label
		
		self.master = master
		self.close_button = Button(image=btclogo, borderwidth=0, highlightthickness = 0, command=self.close)
		self.close_button.grid(row=0, column=0)
		self.label = Label(master, text=("   \u20bfitcoin Dashboard       "), font=('Helvetica',32, 'bold'), fg='black', bg = '#f2a900')
		self.label.grid(row=0, column=1)

		title = "Market Data"
		market_label = Label(master, text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='#f2a900')
		market_label.grid(row=2, column=1, sticky=W)
		price_label = Label(text=("Price: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20, 'bold'), bg='black', fg = 'white')
		price_label.grid(row=3, column=1, sticky=W)
		sats_label = Label(text=("Sats per $: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		sats_label.grid(row=4, column=1, sticky=W)
		change24_label = Label(text=("24hr change: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = "white")
		change24_label.grid(row=5, column=1, sticky=W)
		dom_label = Label(text=("Dominance: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		dom_label.grid(row=6, column=1, sticky=W)
		circ_label = Label(text=("Circulating supply: " + str(0) + u'\u20bf'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		circ_label.grid(row=7, column=1, sticky=W)
		mcap_label = Label(text=("Marketcap: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		mcap_label.grid(row=8, column=1, sticky=W)

		title2 = "Mempool Data"
		blockchain_label = Label(master, text=(title2),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='#f2a900')
		blockchain_label.grid(row=9, column=1, sticky=W)
		block_label = Label(text=("Block Height: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		block_label.grid(row=10, column=1, sticky=W)
		memp_label = Label(text=("Mempool: " + str(0) + " transactions"),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		memp_label.grid(row=11, column=1, sticky=W)
		avgfee_label = Label(text=("Average Fee 24hr: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		avgfee_label.grid(row=12, column=1, sticky=W)
		recfeeusd_label = Label(text=("Fees: " + "$" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		recfeeusd_label.grid(row=13, column=1, sticky=W)
		recfee_label = Label(text=("Fees: " + str(0) + " sat/vB"),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		recfee_label.grid(row=14, column=1, sticky=W)
		hash_label = Label(text=("Hashrate 24hr: " + str(0) + " EH/s"),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		hash_label.grid(row=15, column=1, sticky=W)
		dif_label = Label(text=("Next difficulty estimate: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		dif_label.grid(row=16, column=1, sticky=W)
		title3 = "More Data"
		others_label = Label(master, text=(title3),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='#f2a900')
		others_label.grid(row=2, column=2, sticky=W)
		high24_label = Label(text=("High 24hr: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		high24_label.grid(row=3, column=2, sticky=W)
		low24_label = Label(text=("Low 24hr: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		low24_label.grid(row=4, column=2, sticky=W)
		ath_label = Label(text=("ATH: $" + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		ath_label.grid(row=5, column=2, sticky=W)
		athchg_label = Label(text=("ATH change: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		athchg_label.grid(row=6, column=2, sticky=W)
		athdate_label = Label(text=("ATH Date: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		athdate_label.grid(row=7, column=2, sticky=W)
		fearindex_label = Label(text=("F&G Index: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		fearindex_label.grid(row=8, column=2, sticky=W)
		title4 = "Lightning Network"
		lightning_label = Label(master, text=(title4),anchor=NW, justify=LEFT,font=('Helvetica',28, 'bold'), bg='black', fg='#f2a900')
		lightning_label.grid(row=9, column=2, sticky=W)
		lgtcap_label = Label(text=(u'\u26A1' + " Capacity: " + str(0) + u'\u20bf'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		lgtcap_label.grid(row=10, column=2, sticky=W)
		lnodes_label = Label(text=(u'\u26A1' + " Nodes: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		lnodes_label.grid(row=11, column=2, sticky=W)
		lnchannels_label = Label(text=(u'\u26A1' + " Channels: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		lnchannels_label.grid(row=12, column=2, sticky=W)
		error_label1 = Label(text=(""),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='hot pink')
		error_label1.grid(row=14, column=2, sticky=W)
		error_label2 = Label(text=(""),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='hot pink')
		error_label2.grid(row=15, column=2, sticky=W)	
		update_label = Label(text=("Last Update: " + str(0)),anchor=NW, justify=LEFT,font=('Helvetica',12), bg='black', fg='white')
		update_label.grid(row=16, column=2, sticky=W)
		self.settings_button = Button(image=settingsicon, borderwidth=0, highlightthickness = 0, command=lambda: threading.Thread(target=settingsMenu).start())
		self.settings_button.grid(row=0, column=3)
	
	#Scale the output to the screen size
		Grid.columnconfigure(root,2,weight=1)
		Grid.rowconfigure(root,1,weight=1)
		Grid.rowconfigure(root,2,weight=1)
		Grid.rowconfigure(root,3,weight=1)
		Grid.rowconfigure(root,4,weight=1)
		Grid.rowconfigure(root,5,weight=1)
		Grid.rowconfigure(root,6,weight=1)
		Grid.rowconfigure(root,7,weight=1)
		Grid.rowconfigure(root,8,weight=1)
		Grid.rowconfigure(root,9,weight=1)
		Grid.rowconfigure(root,10,weight=1)
		Grid.rowconfigure(root,11,weight=1)
		Grid.rowconfigure(root,12,weight=1)
		Grid.rowconfigure(root,13,weight=1)
		Grid.rowconfigure(root,14,weight=1)
		Grid.rowconfigure(root,15,weight=1)
		Grid.rowconfigure(root,16,weight=1)
		print("Static Labels Initialized")

	def labels():

		global ath
		global athnew
		global average_transaction_fee_usd_24hdiff
		global average_transaction_fee_usd_24hsav
		global blocks
		global fearemoji
		global hashrate24hrdiff
		global hashrate24hrsav
		global lnodes
		global mempool
		global mempooldiff
		global mempoolsav
		global oldblock
		global onlyonce
		global prevpricebtc
		global pricebtc
		global then
		global timestamp
		global refreshtime
		global new_refreshtime
		#### API Timers ####
		global altstart
		global bitstampstart
		global blockchairstart
		global blocktime
		global coingeckostart
		global mempoolstart
		global ml1start

		try:
			new_refreshtime
		except NameError:
			new_refreshtime = refreshtime
		refreshtime = new_refreshtime

#Free API Requests Limit Enforcement
	# Bitstamp allows 800 calls per minute	
		if time.time() - bitstampstart > 0.1:
			bitstamp_thread = threading.Thread(target=bitstamp, name="Bitstamp")
			bitstamp_thread.start()
			#print(time.time() - bitstampstart)
			bitstampstart = time.time()
	# Coingecko allows 100 calls per minute
		if time.time() - coingeckostart > 1:
			coingecko_thread = threading.Thread(target=coingecko, name="CoinGecko")
			coingecko_thread.start()
			#print(time.time() - coingeckostart)
			coingeckostart = time.time()
	#Mempool allows 200 calls per minute
		if time.time() - mempoolstart > 2:
			mempool_thread = threading.Thread(target=mempoolspace, name="Mempool")
			mempool_thread.start()
			#print(time.time() - mempoolstart)
			mempoolstart = time.time()		
	#Blockchair allows 1 call per minute
		if time.time() - blockchairstart > 60:
			blockchair_thread = threading.Thread(target=blockchair, name="BlockChair")
			blockchair_thread.start()
			#blockchair()
			#print(time.time() - blockchairstart)
			blockchairstart = time.time()
			
	# Alternative updates their data every 5 minutes
	# However Alternative allows 60 calls per minute
		if time.time() - altstart > 150:
			alt_thread = threading.Thread(target=alt, name="Alternative")
			alt_thread.start()
			#alt()
			#print(time.time() - altstart)
			altstart = time.time()
			
	# 1ML unknown API Limit, set to 5 minutes to be safe
		if time.time() - ml1start > 300:
			ml1_thread = threading.Thread(target=ml1, name="ML1")
			ml1_thread.start()
			#ml1()
			ml1start = time.time()
		
	# Join threads so that all data is fetched before refreshing the screen
		try:
			if bitstamp_thread.is_alive() == True:
				bitstamp_thread.join()
		except NameError:
			pass
		try:
			if coingecko_thread.is_alive() == True:
				coingecko_thread.join()
		except NameError:
			pass
		try:
			if mempool_thread.is_alive() == True:	
				mempool_thread.join()
		except NameError:
			pass
		try:
			if blockchair_thread.is_alive() == True:
				blockchair_thread.join()
		except NameError:
			pass
		try:
			if alt_thread.is_alive() == True:
				alt_thread.join()
		except NameError:
			pass
		try:
			if ml1_thread.is_alive() == True:
				ml1_thread.join()
		except NameError:
			pass
	# Refresh the screen with the newly fetched data
		print("Refreshing data on screen")
		refreshtimer = time.time()
		if pricebtc1hrchange >= disppricebtc1hrchangediff:
				trend1hr = u'\u25B2'
		elif pricebtc1hrchange <= disppricebtc1hrchangediff * -1:
				trend1hr = u'\u25BC'
		else:
				trend1hr = ""
		try:
			prevpricebtc
		except NameError:
			prevpricebtc = pricebtc			
		if pricebtc > prevpricebtc:
			color = 'lightgreen'
		elif pricebtc < prevpricebtc:
			color = 'lightcoral'
		else:
			color = 'white'
		currency = "{:,.2f}".format(pricebtc)
		price_label.configure(text="Price: $" + str(currency) + " " + trend1hr, fg = color)
		prevpricebtc = pricebtc
		currency = "{:,.2%}".format(pricebtc24hrchange)
		change24_label.configure(text="24hr change: " + str(currency), fg='white')
		currency = "{:,.2%}".format(market_dominance_percentage)
		dom_label.configure(text="Dominance: " + str(currency), fg='white')
		currency = "{:,.0f}".format(satsusd)
		sats_label.configure(text="Sats per $: " + str(currency), fg='white')
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
		currency = "{:,.02%}".format(diffadj/100)
		try:
			date_time_obj = datetime.datetime.strptime(str(next_retarget_time_estimate), '%Y-%m-%d %H:%M:%S')
			textadj = str(date_time_obj.date()) #.strftime("%Y-%m-%d %H:%M")
		except:
			textadj = "Date Error"
		dif_label.configure(text="Difficulty adjustment: " + textadj + " " + str(currency), fg='white')
		if mempooldiff > dispmempooldiff:
				color = "lightcoral"
		elif mempooldiff < dispmempooldiff * -1:
				color = "lightgreen"
		else: 
				color = "white"
		currency = "{:,.0f}".format(mempool)
		memp_label.configure(text=("Mempool: " + str(currency) + " transactions"), fg=color)
		currency = "{:,.0f}".format(blocks)
		if time.time() - timestamp <= 120:
				color = "lightgreen"
		else:
				color = "white"
		if timestamp == 0:
			timedif = ""
		elif timestamp == 1:
			timedif = ""
			color = "lightgreen"
		else:
			timedif = time.time() - timestamp
			if strftime("%H", gmtime(timedif)) == "00":
				timedif = strftime("%M:%S", gmtime(timedif))
			else:
				timedif = strftime("%H:%M:%S", gmtime(timedif))
		block_label.configure(text="Block height: " + str(currency) + " - " + timedif, fg=color)
		if average_transaction_fee_usd_24hdiff > dispaverage_transaction_fee_usd_24hdiff:
				color = "lightcoral"
		elif average_transaction_fee_usd_24hdiff < dispaverage_transaction_fee_usd_24hdiff * -1:
				color = "lightgreen"
		else:
				color = "white"
		currency = "${:,.2f}".format(average_transaction_fee_usd_24h)
		avgfee_label.configure(text=("Average fee 24hr: " + str(currency)), fg=color)
		hfee = "{:,.0f}".format(highfee)
		mfee = "{:,.0f}".format(mediumfee)
		lfee = "{:,.0f}".format(lowfee)
		recfee_label.configure(text="Fees:" + u'\u2191' + str(hfee) + " sat/vB " + u'\u2195' + str(mfee) + " sat/vB " + u'\u2193' + str(lfee) + " sat/vB", fg='white')
		try:
			husd = "{:,.2f}".format((highfee * 140.5) / satsusd)
			musd = "{:,.2f}".format((mediumfee * 140.5) / satsusd)
			lusd = "{:,.2f}".format((lowfee * 140.5) / satsusd)
		except:
			husd = "{:,.2f}".format(0)
			musd = "{:,.2f}".format(0)
			lusd = "{:,.2f}".format(0)

		recfeeusd_label.configure(text="Fees:" + u'\u2191' + "$" + husd + "  " + u'\u2195' + "$" + musd + "  " + u'\u2193' + "$" + lusd, fg='white')
#	Second Column
		currency = "{:,.2f}".format(high24h)
		high24_label.configure(text="High 24hr: $" + str(currency), fg='white')
		currency = "{:,.2f}".format(low24h)
		low24_label.configure(text="Low 24hr: $" + str(currency), fg='white')
		try:
			today = datetime.datetime.now()
			if today.strftime("%Y-%m-%d") <= athdate[0:10]:
				color = "lightgreen"
				athfnt = ('Helvetica', 20, 'bold')
			else:
				color = "white"
				athfnt = ('Helvetica', 20)
				athtrend = ""
			athdate_label.configure(text="ATH date: " + str(athdate[0:10]), fg=color)
		except:
			athdate_label.configure(text="ATH date: Date Error", fg='lightcoral')
			athfnt = ('Helvetica', 20)
			athtrend = ""
		try:
			athtrend
		except NameError:
			athtrend = ""
		try:
			athnew
		except NameError:
			athnew = ath
		if pricebtc > ath and pricebtc > athnew:
			athnew = pricebtc
			color = 'lightgreen'
			athfnt = ('Helvetica', 20, 'bold')
			athtrend = u'\u25B2'
		elif ath > athnew:
			athnew = ath
		currency = "{:,.2f}".format(athnew)
		ath_label.configure(text="ATH: $" + str(currency) + " " + athtrend, font=athfnt, fg=color)
		try:
			ath_change = (float(pricebtc) - athnew)/athnew
		except ZeroDivisionError:
			try:
				ath_change
			except NameError:
				ath_change = -1
		if ath_change * 100 >= -5:
			color = 'lightgreen'
		elif ath_change * 100 <= -50:
			color = 'lightcoral'
		else:
			color = 'white'
		currency = "{:,.2%}".format(ath_change)
		athchg_label.configure(text="ATH change: " + str(currency), fg=color)
		currency = "{:,.0f}".format(circulating_supply)
		circ_label.configure(text="Circulating supply: " + str(currency) + u'\u20bf', fg='white')
		if fearindex == "Extreme Greed":
			fearemoji = "🤩"
		elif fearindex == "Greed":
			fearemoji = "🤤"
		elif fearindex == "Neutral":
			fearemoji = "😐"
		elif fearindex == "Fear":
			fearemoji = "😨"
		elif fearindex == "Extreme Fear":
			fearemoji = "😱"
		fearindex_label.configure(text="F&G index: " + str(fearindexvalue)  + " - " + str(fearindex) + " " + str(fearemoji), fg='white')

		if lndcap_chg > 0:
			trend = "+"
		else:
			trend = ""
		currency = "{:,.2f}".format(LNDCap)
		change =  "{:,.2f}".format(lndcap_chg)
		lgtcap_label.configure(text=u'\u26A1' + " Capacity: " + str(currency) + u'\u20bf' + " " + trend + str(change) + "%", fg='lightyellow')
		if lnodes_chg > 0:
			trend = "+"
		else:
			trend = ""
		currency = "{:,.0f}".format(lnodes)
		change = "{:,.2f}".format(lnodes_chg)
		lnodes_label.configure(text=u'\u26A1' + " Nodes: " + str(currency) + " " + trend + str(change) + "%", fg='lightyellow')
		if lnchannels_chg > 0:
			trend = "+"
		else:
			trend = ""
		currency = "{:,.0f}".format(lnchannels)
		change = "{:,.2f}".format(lnchannels_chg)
		lnchannels_label.configure(text=u'\u26A1' + " Channels: " + str(currency) + " " + trend + str(change) + "%", fg='lightyellow')

		### Error Handling ###
		error_label1.configure(text=str(""))
		error_label2.configure(text=str(""))
		if bcerror == 1 or bserror == 1 or cgerror == 1 or alterror == 1 or mlerror == 1 or mempoolerror == 1: 
			error_label1.configure(text=str("Error Reading " + bs1 + mp1 + cg1 + bc1 + alte1 + mle1), font=('Helvetica', 14))
		if bcerror == 2 or bserror == 2 or cgerror == 2 or alterror == 2 or mlerror == 2 or mempoolerror == 2:
			error_label2.configure(text=str(bs2 + mp2 + cg2 + bc2 + alte2 + mle2 + "Connection Refused!"), font=('Helvetica', 14))
		if bcerror > 0:
			dom_label.configure(fg='plum1')
			avgfee_label.configure(fg='plum1')
			hash_label.configure(fg='plum1')
			dif_label.configure(fg='plum1')
		if bserror > 0:
			price_label.configure(fg='plum1')
			sats_label.configure(fg='plum1')
			athchg_label.configure(fg='plum1')
		if cgerror > 0:
			change24_label.configure(fg='plum1')
			circ_label.configure(fg='plum1')
			mcap_label.configure(fg='plum1')
			high24_label.configure(fg='plum1')
			low24_label.configure(fg='plum1')
			ath_label.configure(fg='plum1')
			athdate_label.configure(fg='plum1')
		if alterror > 0:
			fearindex_label.configure(fg='plum1')
		if mlerror > 0:
			lnodes_label.configure(fg='plum1')
			lgtcap_label.configure(fg='plum1')
			lnchannels_label.configure(fg='plum1')
		if mempoolerror > 0:
			block_label.configure(fg='plum1')
			memp_label.configure(fg='plum1')
			recfeeusd_label.configure(fg='plum1')
			recfee_label.configure(fg='plum1')
		if bserror > 1 and cgerror > 1 and mempoolerror > 1:
			error_label1.configure(text=str("No Internet Connection Available!"), font=('Helvetica',16, 'bold'))
			error_label2.configure(text=str("Please Check Your Internet Connection"),font=('Helvetica',14, 'bold'))
			price_label.configure(fg='plum1')
			sats_label.configure(fg='plum1')
			change24_label.configure(fg='plum1')
			dom_label.configure(fg='plum1')
			circ_label.configure(fg='plum1')
			mcap_label.configure(fg='plum1')
			block_label.configure(fg='plum1')
			memp_label.configure(fg='plum1')
			avgfee_label.configure(fg='plum1')
			recfeeusd_label.configure(fg='plum1')
			recfee_label.configure(fg='plum1')
			hash_label.configure(fg='plum1')
			dif_label.configure(fg='plum1')
			high24_label.configure(fg='plum1')
			low24_label.configure(fg='plum1')
			ath_label.configure(fg='plum1')
			athchg_label.configure(fg='plum1')
			athdate_label.configure(fg='plum1')
			fearindex_label.configure(fg='plum1')
			lnodes_label.configure(fg='plum1')
			lgtcap_label.configure(fg='plum1')
			lnchannels_label.configure(fg='plum1')
		
		now = datetime.datetime.now()
		duration = now - then
		duration_in_s = duration.total_seconds()
		update_label.configure(text="Last Update: " + str(now.strftime("%c")))
		#print("Refresh time in seconds: " + str(time.time() - refreshtimer))

#first time
		#print("First Time Check")
		if onlyonce == 0:
			hashrate24hrsav = hashrate24hr
			mempoolsav = mempool
			average_transaction_fee_usd_24hsav = average_transaction_fee_usd_24h
			splash.destroy()
			onlyonce = 1

# to calculate the hourly differences
		#print("Hourly Differences Check")
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
	
def settingsMenu():
	# min 1 second, max 24 hours
	minval = 1
	maxval = 86400
	# Validate Refresh Time Spin Box to ensure its numeric and within min/max value
	def validate(user_input):
		if user_input.isdigit():
			if int(user_input) >= minval and int(user_input) <= maxval:
				m, s = divmod(int(user_input), 60)
				h, m = divmod(m, 60)
				refresh_conv.configure(text=f'{h:d} hr {m:02d} min {s:02d} sec')
				return user_input.isdigit()
			else:
				print("Out of Range")
				return False
		elif user_input == "":
			return True
		else:
			print("Not a digit")
			return False
	def testConnection():
		try:
			e_url = ip_entry.get()
			urltest = requests.get(e_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + e_url + " Status code: " + str(status))
			#settings_label.configure(text="Tried connecting to: " + e_url + " Status code: " + str(status))
			b_url = e_url + "api/blocks/tip/height"
			urltest = requests.get(b_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + b_url + " Status code: " + str(status))
			d_url = e_url + 'api/v1/difficulty-adjustment'
			urltest = requests.get(b_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + d_url + " Status code: " + str(status))
			f_url = e_url + 'api/v1/fees/recommended'
			urltest = requests.get(f_url)
			status = urltest.status_code
			urltest.close()
			print("Tried connecting to: " + f_url + " Status code: " + str(status))
			print("Success on all node tests!")
			messagebox.showinfo("Success!", "Success on all node tests!", parent=settings)
		except:
			print("Tried connecting to: " + e_url)
			print("Error Connecting to Node!")
			messagebox.showerror("Error!", "Error Connecting to Node!\nCheck your URL and try again.", parent=settings)

	def nodeEnable():
		choice = src.get()
		if choice == 0:
			ip_entry.configure(state=DISABLED)
			test_button.configure(state=DISABLED)
		else:
			ip_entry.configure(state=NORMAL)
			test_button.configure(state=NORMAL)

	def connectToNode():
		global node_connected
		global ip_url
		global new_refreshtime
		rspin = refresh_spin.get()
		print("RSPIN = " + rspin)
		if rspin == "":
			rspin = refreshtime / 1000
			print("Reset refresh time to " + str(rspin))
		new_refreshtime = int(rspin) * 1000
		if int(rspin) == int(refreshtime / 1000):
			refresh_msg = ""
		else:
			refresh_msg = "\nRefresh time set to " + str(rspin) + "\nNew refresh time will apply after next refresh"
		if src.get() == 0:
			try:
				urltest = requests.get('https://mempool.space/')
				status = urltest.status_code
				urltest.close()
				node_connected = 0
				blockchain_label.configure(text="Mempool Data")
				messagebox.showinfo("Success!", "Successfully connected to Mempool.Space!" + refresh_msg, parent=settings)
				settings.destroy()
			except:
				messagebox.showerror("Error!", "Error Connecting to Mempool.Space!\nTry again later." + refresh_msg, parent=settings)
		else:
			try:
				node_url = ip_entry.get()
				urltest = requests.get(node_url)
				status = urltest.status_code
				urltest.close()
				print("Tried connecting to: " + node_url + " Status code: " + str(status))
				print("Successfully connected to custom node!")
				node_connected = 1
				ip_url = node_url
				blockchain_label.configure(text=u'\u26A1' + " Mempool Data")
				messagebox.showinfo("Success!", "Successfully connected to custom node!" + refresh_msg, parent=settings)
				settings.destroy()
			except:
				print("Tried connecting to: " + node_url)
				print("Error Connecting to Node!")
				messagebox.showerror("Error!", "Error Connecting to Node!\nCheck your URL and try again." + refresh_msg, parent=settings)

	global ip_entry
	global ip_url
	global src
	spin_var = IntVar()
	spin_var.set(new_refreshtime / 1000)
	m, s = divmod(spin_var.get(), 60)
	h, m = divmod(m, 60)
	src = IntVar()
	src.set(node_connected)
	settings = Toplevel()
	settings_width = 550
	settings_height = 300
	width_value=root.winfo_screenwidth()
	height_value=root.winfo_screenheight()
	settings_x = int((width_value / 2) - (settings_width / 2))
	settings_y = int((height_value / 2) - (settings_height / 2))
	settings.geometry(f'{settings_width}x{settings_height}+{settings_x}+{settings_y}')
	settings.title('Settings')
	img = PhotoImage(file='btcicon.png')
	settings.tk.call('wm', 'iconphoto', settings._w, img)
	anchor_label = Label(settings, text="    ", font=('Helvetica',12))
	anchor_label.grid(row=0, column=0)
	range_validation = settings.register(validate)
	refresh_label = Label(settings, text="Refresh Interval:", font=('Helvetica',14))
	refresh_label.grid(row=0, column=1, sticky=E, ipady=20)
	refresh_spin = Spinbox(settings, from_=minval, to=maxval, font=('Helvetica',18), width=5, textvariable=spin_var)
	refresh_spin.grid(row=0, column=2, sticky=W)
	refresh_spin.config(validate ="key", validatecommand =(range_validation, '%P'))
	refresh_conv = Label(settings, text=f'{h:d} hr {m:02d} min {s:02d} sec', font=('Helvetica', 16))
	refresh_conv.grid(row=0, column=2, columnspan=2, padx=(100,0))
	top_label = Label(settings, text="Mempool Source", font=('Helvetica',20, 'bold'))
	top_label.grid(row=1, column=1, columnspan=3)
	r_memp = Radiobutton(settings, text="Default", variable=src, value=0, command=nodeEnable, font=('Helvetica',14))
	r_memp.grid(row=2, column=1, columnspan=2, padx=(0,120), ipady=10)
	r_custom = Radiobutton(settings, text="Custom Node", variable=src, value=1, command=nodeEnable, font=('Helvetica',14))
	r_custom.grid(row=2, column=2, columnspan=2, padx=(0,50))
	url_label = Label(settings, text="Custom Node URL", font=('Helvetica',14))
	url_label.grid(row=3, column=1)
	ip_entry = Entry(settings, font=('Helvetica',14), width=25)
	ip_entry.grid(row=3, column=2)
	test_button = Button(settings, text="Test", font=('Helvetica', 14), command=testConnection)
	test_button.grid(row=3, column=3)
	connect_button = Button(settings, text="Apply", font=('Helvetica',14, 'bold'), bg='#f2a900', width=30, command=connectToNode)
	connect_button.grid(row=5, column=0, columnspan=4, pady=30)
	try:
		ip_url
	except NameError:
		ip_url = "http://192.168.1.2:3006/"
	ip_entry.insert(0, ip_url)
	nodeEnable()
	settings.update()
	root.wait_window(settings)

def mempoolspace():
	#print("Fethcing from Mempool.space")
	
	global blocks
	global oldblock
	global mp1, mp2
	global mempool
	global mempoolerror
	global highfee
	global mediumfee
	global lowfee
	global diffadj
	global timestamp
	global lasthash
	global node_connected
	
	try:
		blocks
	except NameError:
		blocks = 0
	try:
		mempool
	except NameError:
		mempool = 0
	try:
		highfee
	except NameError:
		highfee = 0
	try:
		mediumfee
	except NameError:
		mediumfee = 0
	try:
		lowfee
	except NameError:
		lowfee = 0
	try:
		diffadj
	except NameError:
		diffadj = 0
	try:
		newBlock
	except NameError:
		newBlock = 0
	try:
		timestamp
	except NameError:
		timestamp = 0
	try:
		lasthash
	except NameError:
		lasthash = 0
	try:
		node_connected
	except NameError:
		node_connected = 0
	status = 0
	try:
		#mempooltime = time.time()
		if node_connected != 1:
			block_url = 'https://mempool.space/api/blocks/tip/height'
			difadj_url = 'https://mempool.space/api/v1/difficulty-adjustment'
			fees_url = 'https://mempool.space/api/v1/fees/recommended'
		else:
			block_url = ip_url + 'api/blocks/tip/height'
			difadj_url = ip_url + 'api/v1/difficulty-adjustment'
			fees_url = ip_url + 'api/v1/fees/recommended'
		transaction_url = 'https://mempool.space/api/mempool'
		transaction_api_request = urlopen(transaction_url).read()
		mempool = float(loads(transaction_api_request)['count'])
		block_api_request = urlopen(block_url).read()
		newBlock = float(loads(block_api_request))
		fees_api_request = urlopen(fees_url).read()
		highfee = float(loads(fees_api_request)['fastestFee'])
		mediumfee = float(loads(fees_api_request)['halfHourFee'])
		lowfee = float(loads(fees_api_request)['hourFee'])
		difadj_api_request = urlopen(difadj_url).read()
		diffadj = float(loads(difadj_api_request)['difficultyChange'])

		if newBlock > oldblock:
			blocks = newBlock
			timestamp = 1
			blockhash_url = 'https://mempool.space/api/blocks/tip/hash'
			blockh = urlopen(blockhash_url).read()
			blockh = (str(blockh)[1:100])
			blockh = blockh.replace("'", "")
			if blockh != lasthash:
				if node_connected != 1:
					blockh_url = "https://mempool.space/api/block/" + blockh
				else:
					blockh_url = ip_url + "api/block/" + blockh
				hash_api_request = urlopen(blockh_url).read()
				timestamp = int(loads(hash_api_request)['timestamp'])
				lasthash = blockh
				oldblock = newBlock
		if node_connected != 1:
			print("Mempool Stats Updated ") #+ str(time.time() - mempooltime))
		else:
			print("Node Mempool Stats Updated ")
		mempoolerror = 0
	except:
		try:
			urltest = requests.get('https://mempool.space/')
			status = urltest.status_code
			urltest.close()
			mempoolerror = 1
			print("Error Reading Mempool. Status code: " + str(status))
		except:
			mempoolerror = 2
			print("Mempool Connection Refused ")
	if mempoolerror == 1:
		mp1 = "Mempool "
		mp2 = ""
	elif mempoolerror == 2:
		mp1 = ""
		mp2 = "Mempool "
	else:
		mp1 = ""
		mp2 = ""

def ml1():
	global LNDCap
	global lnodes
	global lnchannels
	global lndcap_chg
	global lnodes_chg
	global lnchannels_chg
	global mle1, mle2
	global mlerror
	
	try:
		LNDCap
	except NameError:
		LNDCap = 0
	try:
		lnodes
	except NameError:
		lnodes = 0
	try:
		lnchannels
	except NameError:
		lnchannels = 0
	try:
		lndcap_chg
	except NameError:
		lndcap_chg = 0
	try:
		lnodes_chg
	except NameError:
		lnodes_chg = 0
	try:
		lnchannels_chg
	except NameError:
		lnchannels_chg = 0
	status = 0
	
	try:
		#mltime = time.time()
		ml1_url = 'https://1ml.com/statistics?json=true'
		ml1_api_request = urlopen(ml1_url).read()
		LNDCap = float(loads(ml1_api_request)['networkcapacity'])	
		LNDCap = LNDCap / 100000000
		lnodes = float(loads(ml1_api_request)['numberofnodes'])
		lnchannels = int(loads(ml1_api_request)['numberofchannels'])
		lndcap_chg = float(loads(ml1_api_request)['networkcapacity30dchange'])
		lnodes_chg = float(loads(ml1_api_request)['numberofnodes30dchange'])
		lnchannels_chg = float(loads(ml1_api_request)['numberofchannels30dchange'])
		print("Lightning Stats Updated ") # + str(time.time() - mltime))
		mlerror = 0
	except:
		try:
			urltest = requests.get(ml1_url)
			status = urltest.status_code
			urltest.close()
			mlerror = 1
			print("Error Reading 1ML. Status code: " + str(status))
		except:
			mlerror = 2 
			print("1ML Connection Refused ")
	if mlerror == 1:
		mle1 = "1ML "
		mle2 = ""
	elif mlerror == 2:
		mle1 = ""
		mle2 = "1ML "
	else:
		mle1 = ""
		mle2 = ""

def alt():
	global alte1, alte2
	global alterror
	global fearindex
	global fearindexvalue
	
	#alttime = time.time()
	try:
		fearindex
	except NameError:
		fearindex = ""
	try:
		fearindexvalue
	except NameError:
		fearindexvalue = 0
	status = 0
	try:
		
	# get the fearindex
		alt_url = 'https://api.alternative.me/fng/'
		alt_api_request = urlopen(alt_url).read()
		fearindex = str(loads(alt_api_request)['data'][0]['value_classification'])
		fearindexvalue = str(loads(alt_api_request)['data'][0]['value'])
		print("Updated Fear Index ") # + str(time.time() - alttime))
		alterror = 0
	except:
		try:
			urltest = requests.get(alt_url)
			status = urltest.status_code
			urltest.close()
			alterror = 1
			print("Error Reading Fear Index. Status code: " + str(status))
		except:
			alterror = 2
			print("Alt Connection Refused ")
	if alterror == 1:
		alte1 = "Alternative "
		alte2 = ""
	elif alterror == 2:
		alte1 = ""
		alte2 = "Alternative "
	else:
		alte1 = ""
		alte2 = ""

def bitstamp():
	global bs1, bs2
	global bserror
	global pricebtc
	global satsusd
	
	#bittime = time.time()
	status = 0
	try:
		pricebtc
	except NameError:
		pricebtc = 0
	try:
		satsusd
	except NameError:
		satsusd = 0
	
	try:
		bitstamp_url = 'https://bitstamp.net/api/ticker'
		bitstamp_api_request = urlopen(bitstamp_url).read()
		pricebtc = float(loads(bitstamp_api_request)['last'])
		try:
			satsusd = 1 / pricebtc * 100000000
			bserror = 0
		except ZeroDivisionError:
			print("Zero Division Error Calculating Sats per Dollar")
			bserror = 1
		print(pricebtc)
		#print(str(time.time() - bittime))

	except:
		try:
			urltest = requests.get(bitstamp_url)
			status = urltest.status_code
			urltest.close()
			bserror = 1
			print("Error Reading BitStamp. Status code: " + str(status))
		except:
			bserror = 2
			print("Bitstamp Connection Refused ")
	if bserror == 1:
		bs1 = "Bitstamp "
		bs2 = ""
	elif bserror == 2:
		bs1 = ""
		bs2 = "Bitstamp "
	else:
		bs1 = ""
		bs2 = ""

def blockchair():
	global average_transaction_fee_usd_24h
	global bc1, bc2
	global bcerror
	global hashrate24hr
	global market_dominance_percentage
	global next_retarget_time_estimate
	
	#blocktime = time.time()
	try:
		average_transaction_fee_usd_24h
	except NameError:
		average_transaction_fee_usd_24h = 0
	try:
		hashrate24hr
	except NameError:
		hashrate24hr = 0
	try:
		market_dominance_percentage
	except NameError:	
		market_dominance_percentage = 0
	try:
		next_retarget_time_estimate
	except NameError:
		next_retarget_time_estimate = 0
	status = 0
	
	try:
#	get blockchain data https://blockchair.com/api/docs#link_M03
		blockchair_url = 'https://api.blockchair.com/bitcoin/stats'
		blockchair_api_request = urlopen(blockchair_url).read()	
		market_dominance_percentage = float(loads(blockchair_api_request)['data']['market_dominance_percentage'])
		average_transaction_fee_usd_24h = float(loads(blockchair_api_request)['data']['average_transaction_fee_usd_24h'])
		hashrate24hr = float(loads(blockchair_api_request)['data']['hashrate_24h'])
		next_retarget_time_estimate = str(loads(blockchair_api_request)['data']['next_retarget_time_estimate'])

		market_dominance_percentage = market_dominance_percentage / 100
		hashrate24hr = hashrate24hr / 1000000000000000000  # in EH/s
		print("Updated Blockchair Stats ") # + str(time.time() - blocktime))
		bcerror = 0
	except:
		try:
			urltest = requests.get(blockchair_url)
			status = urltest.status_code
			urltest.close()
			bcerror = 1
			print("Error reading BlockChair. Status code: " + str(status))
		except:
			bcerror = 2
			print("Blockchair Connection Refused ")
	if bcerror == 1:
		bc1 = "Blockchair "
		bc2 = ""
	elif bcerror == 2:
		bc1 = ""
		bc2 = "Blockchair "
	else:
		bc1 = ""
		bc2 = ""

def coingecko():
	global ath
	global athdate
	global circulating_supply
	global cg1, cg2
	global cgerror
	global high24h
	global low24h
	global marketcap24h
	global marketcapbtc
	global pricebtc1hrchange
	global pricebtc24hrchange
	global status

	#cointime = time.time()
	try:
		ath
	except NameError:
		ath = 0
	try:
		circulating_supply
	except NameError:
		circulating_supply = 0
	try:
		high24h
	except NameError:
		high24h = 0
	try:
		low24h
	except NameError:
		low24h = 0
	try:
		marketcap24h
	except NameError:
		marketcap24h = 0
	try:
		marketcapbtc
	except NameError:
		marketcapbtc = 0
	try:
		pricebtc1hrchange
	except NameError:
		pricebtc1hrchange = 0
	try:
		pricebtc24hrchange
	except NameError:
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
		athdate = str(loads(coingecko_api_request)['market_data']['ath_date']['usd'])
		circulating_supply = float(loads(coingecko_api_request)['market_data']['circulating_supply'])
		pricebtc24hrchange = pricebtc24hrchange / 100
		print("Updated CoinGecko Stats ") # + str(time.time() - cointime))
		cgerror = 0

	except:
		try:
			urltest = requests.get(coingecko_url)
			status = urltest.status_code
			urltest.close()
			cgerror = 1
			print("Error reading Coingecko. Status code: " + str(status))
		except:
			cgerror = 2
			print("CoinGecko Connection Refused ")
	if cgerror == 1:
		cg1 = "CoinGecko "
		cg2 = ""
	elif cgerror == 2:
		cg1 = ""
		cg2 = "CoinGecko "
	else:
		cg1 = ""
		cg2 = ""

exec(open(r"variables").read())
ml1start = altstart = bitstampstart = blockchairstart = coingeckostart = mempoolstart = time.time()
LNDBTC = 0
hashrate24hrsav = 0
mempoolsav = 0
average_transaction_fee_usd_24hsav = 1 
hashrate24hrdiff = 0
mempooldiff = 0
oldblock = 0
average_transaction_fee_usd_24hdiff = 0 
onlyonce = 0
then = datetime.datetime.now()
root = Tk()
splash = Toplevel()
splash_width = 512
splash_height = 325
splash.configure(bg='black')
splash.overrideredirect(True)
splash_img = ImageTk.PhotoImage(Image.open("SplashScreen.jpg"))
splash_label = Label(splash, image=splash_img, borderwidth=0, highlightthickness = 0)
splash_label.grid(row=0, column=0)
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
splash_x = int((width_value / 2) - (splash_width / 2))
splash_y = int((height_value / 2) - (splash_height / 2))
splash.geometry(f'{splash_width}x{splash_height}+{splash_x}+{splash_y}')
print("Screen Width: " + str(width_value))
print("Screen Height: " + str(height_value))
splash_label2 = Label(splash, text="Detected screen dimensions: " + str(width_value) + " x " + str(height_value),anchor=NW, justify=LEFT,font=('Times',12), bg='black', fg = 'white')
splash_label2.grid(row=2, column=0)
splash_label3 = Label(splash, text= version,anchor=E, font=('Times',12, 'bold'), bg='black', fg = '#2B9B1B')
splash_label3.grid(row=2, column=0, padx=(450,0))
splash.update()
root.geometry("%dx%d+0+0" % (width_value, height_value))
root.configure(bg='black', cursor= 'crosshair')
root.attributes('-fullscreen', True)
btclogo = PhotoImage(file=r"btclogo.png")
settingsicon = PhotoImage(file=r"settings.png")
my_gui = BTCTicker(root)
bitstamp()
coingecko()
mempoolspace()
blockchair()
alt()
ml1()
BTCTicker.labels()
mainloop()
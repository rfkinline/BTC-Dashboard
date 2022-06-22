#!/usr/bin/env python3
from tkinter import *
import requests
import time
import threading
from time import strftime
from time import gmtime
import datetime
from PIL import ImageTk,Image
from urllib.request import urlopen
import config
import api.apicall
import gui.splash
from gui.settings import settingsMenu

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
		
		# Initialize the main interface
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
		Grid.columnconfigure(config.root,2,weight=1)
		Grid.rowconfigure(config.root,1,weight=1)
		Grid.rowconfigure(config.root,2,weight=1)
		Grid.rowconfigure(config.root,3,weight=1)
		Grid.rowconfigure(config.root,4,weight=1)
		Grid.rowconfigure(config.root,5,weight=1)
		Grid.rowconfigure(config.root,6,weight=1)
		Grid.rowconfigure(config.root,7,weight=1)
		Grid.rowconfigure(config.root,8,weight=1)
		Grid.rowconfigure(config.root,9,weight=1)
		Grid.rowconfigure(config.root,10,weight=1)
		Grid.rowconfigure(config.root,11,weight=1)
		Grid.rowconfigure(config.root,12,weight=1)
		Grid.rowconfigure(config.root,13,weight=1)
		Grid.rowconfigure(config.root,14,weight=1)
		Grid.rowconfigure(config.root,15,weight=1)
		Grid.rowconfigure(config.root,16,weight=1)

		print("Static Labels Initialized")

	def labels():

		global ath
		global athnew
		global average_transaction_fee_usd_24hdiff
		global average_transaction_fee_usd_24hsav
		global blocks
		global hashrate24hrdiff
		global hashrate24hrsav
		global lnodes
		global mempool
		global mempooldiff
		global mempoolsav
		global onlyonce
		global prevpricebtc
		global then

		#Call the API's and fetch new values
		api.apicall.apiCall()

		# Refresh the screen with the newly fetched data
		print("Refreshing data on screen")
		#refreshtimer = time.time()
		if config.node_connected == 0:
			blockchain_label.configure(text="Mempool Data")
		else:
			blockchain_label.configure(text=u'\u26A1' + " Mempool Data")
		if config.pricebtc1hrchange >= config.disppricebtc1hrchangediff:
			trend1hr = u'\u25B2'
		elif config.pricebtc1hrchange <= config.disppricebtc1hrchangediff * -1:
			trend1hr = u'\u25BC'
		else:
			trend1hr = ""
		try:
			prevpricebtc
		except NameError:
			prevpricebtc = config.pricebtc			
		if config.pricebtc > prevpricebtc:
			color = 'lightgreen'
		elif config.pricebtc < prevpricebtc:
			color = 'lightcoral'
		else:
			color = 'white'
		pricechange = config.pricebtc - prevpricebtc
		pricechangelabel = "{:,.2f}".format(pricechange)
		if pricechange > 0:
			sign = "+"
		elif pricechange == 0:
			pricechangelabel = ""
			sign = ""
		else:
			sign = ""
		currency = "{:,.2f}".format(config.pricebtc)
		price_label.configure(text="Price: $" + str(currency) + " " + trend1hr + " " + sign + str(pricechangelabel), fg = color)
		prevpricebtc = config.pricebtc
		currency = "{:,.2%}".format(config.pricebtc24hrchange)
		change24_label.configure(text="24hr change: " + str(currency), fg='white')
		currency = "{:,.2%}".format(config.market_dominance_percentage)
		dom_label.configure(text="Dominance: " + str(currency), fg='white')
		currency = "{:,.0f}".format(config.satsusd)
		sats_label.configure(text="Sats per $: " + str(currency), fg='white')
		if config.marketcap24h > config.dispmarketcap24h:
				color = "lightgreen"
		elif config.marketcap24h < config.dispmarketcap24h * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.0f}".format(config.marketcapbtc)
		mcap_label.configure(text="Marketcap: $" + str(currency), fg = color)

		if hashrate24hrdiff > config.disphashrate24hrdiff:
				color = "lightgreen"
		elif hashrate24hrdiff < config.disphashrate24hrdiff * -1:
				color = "lightcoral"
		else:
				color = "white"
		currency = "{:,.0f}".format(config.hashrate24hr)
		hash_label.configure(text=("Hashrate 24hr: " + str(currency) + " EH/s"), fg=color)
		currency = "{:,.02%}".format(config.diffadj/100)
		try:
			date_time_obj = datetime.datetime.strptime(str(config.next_retarget_time_estimate), '%Y-%m-%d %H:%M:%S')
			textadj = str(date_time_obj.date()) #.strftime("%Y-%m-%d %H:%M")
		except:
			textadj = "Date Error"
		dif_label.configure(text="Difficulty adjustment: " + textadj + " " + str(currency), fg='white')
		if mempooldiff > config.dispmempooldiff:
				color = "lightcoral"
		elif mempooldiff < config.dispmempooldiff * -1:
				color = "lightgreen"
		else: 
				color = "white"
		currency = "{:,.0f}".format(config.mempool)
		memp_label.configure(text=("Mempool: " + str(currency) + " transactions"), fg=color)
		currency = "{:,.0f}".format(config.blocks)
		if time.time() - config.timestamp <= 120:
				color = "lightgreen"
		else:
				color = "white"
		if config.timestamp == 0:
			timedif = ""
		elif config.timestamp == 1:
			timedif = ""
			color = "lightgreen"
		else:
			timedif = time.time() - config.timestamp
			if strftime("%H", gmtime(timedif)) == "00":
				timedif = strftime("%M:%S", gmtime(timedif))
			else:
				timedif = strftime("%H:%M:%S", gmtime(timedif))
		block_label.configure(text="Block height: " + str(currency) + " - " + timedif, fg=color)
		if average_transaction_fee_usd_24hdiff > config.dispaverage_transaction_fee_usd_24hdiff:
				color = "lightcoral"
		elif average_transaction_fee_usd_24hdiff < config.dispaverage_transaction_fee_usd_24hdiff * -1:
				color = "lightgreen"
		else:
				color = "white"
		currency = "${:,.2f}".format(config.average_transaction_fee_usd_24h)
		avgfee_label.configure(text=("Average fee 24hr: " + str(currency)), fg=color)
		hfee = "{:,.0f}".format(config.highfee)
		mfee = "{:,.0f}".format(config.mediumfee)
		lfee = "{:,.0f}".format(config.lowfee)
		recfee_label.configure(text="Fees:" + u'\u2191' + str(hfee) + " sat/vB " + u'\u2195' + str(mfee) + " sat/vB " + u'\u2193' + str(lfee) + " sat/vB", fg='white')
		try:
			husd = "{:,.2f}".format((config.highfee * 140.5) / config.satsusd)
			musd = "{:,.2f}".format((config.mediumfee * 140.5) / config.satsusd)
			lusd = "{:,.2f}".format((config.lowfee * 140.5) / config.satsusd)
		except:
			husd = "{:,.2f}".format(0)
			musd = "{:,.2f}".format(0)
			lusd = "{:,.2f}".format(0)

		recfeeusd_label.configure(text="Fees:" + u'\u2191' + "$" + husd + "  " + u'\u2195' + "$" + musd + "  " + u'\u2193' + "$" + lusd, fg='white')
		
		#Second Column
		currency = "{:,.2f}".format(config.high24h)
		high24_label.configure(text="High 24hr: $" + str(currency), fg='white')
		currency = "{:,.2f}".format(config.low24h)
		low24_label.configure(text="Low 24hr: $" + str(currency), fg='white')
		try:
			today = datetime.datetime.now()
			if today.strftime("%Y-%m-%d") <= config.athdate[0:10]:
				color = "lightgreen"
				athfnt = ('Helvetica', 20, 'bold')
			else:
				color = "white"
				athfnt = ('Helvetica', 20)
				athtrend = ""
			athdate_label.configure(text="ATH date: " + str(config.athdate[0:10]), fg=color)
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
			athnew = config.ath
		if config.pricebtc > config.ath and config.pricebtc > athnew:
			athnew = config.pricebtc
			color = 'lightgreen'
			athfnt = ('Helvetica', 20, 'bold')
			athtrend = u'\u25B2'
		elif config.ath > athnew:
			athnew = config.ath
		currency = "{:,.2f}".format(athnew)
		ath_label.configure(text="ATH: $" + str(currency) + " " + athtrend, font=athfnt, fg=color)
		try:
			ath_change = (float(config.pricebtc) - athnew)/athnew
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
		currency = "{:,.0f}".format(config.circulating_supply)
		circ_label.configure(text="Circulating supply: " + str(currency) + u'\u20bf', fg='white')
		fearindex_label.configure(text="F&G index: " + str(config.fearindexvalue)  + " - " + str(config.fearindex), fg='white')

		if config.lndcap_chg > 0:
			trend = "+"
		else:
			trend = ""
		currency = "{:,.2f}".format(config.LNDCap)
		change =  "{:,.2f}".format(config.lndcap_chg)
		lgtcap_label.configure(text=u'\u26A1' + " Capacity: " + str(currency) + u'\u20bf' + " " + trend + str(change) + "%", fg='lightyellow')
		if config.lnodes_chg > 0:
			trend = "+"
		else:
			trend = ""
		currency = "{:,.0f}".format(config.lnodes)
		change = "{:,.2f}".format(config.lnodes_chg)
		lnodes_label.configure(text=u'\u26A1' + " Nodes: " + str(currency) + " " + trend + str(change) + "%", fg='lightyellow')
		if config.lnchannels_chg > 0:
			trend = "+"
		else:
			trend = ""
		currency = "{:,.0f}".format(config.lnchannels)
		change = "{:,.2f}".format(config.lnchannels_chg)
		lnchannels_label.configure(text=u'\u26A1' + " Channels: " + str(currency) + " " + trend + str(change) + "%", fg='lightyellow')

		### Error Handling ###
		error_label1.configure(text=str(""))
		error_label2.configure(text=str(""))
		if config.bcerror == 1 or config.bserror == 1 or config.cgerror == 1 or config.alterror == 1 or config.mlerror == 1 or config.mempoolerror == 1: 
			error_label1.configure(text=str("Error Reading " + config.bs1 + config.mp1 + config.cg1 + config.bc1 + config.alte1 + config.mle1), font=('Helvetica', 14))
		if config.bcerror == 2 or config.bserror == 2 or config.cgerror == 2 or config.alterror == 2 or config.mlerror == 2 or config.mempoolerror == 2:
			error_label2.configure(text=str(config.bs2 + config.mp2 + config.cg2 + config.bc2 + config.alte2 + config.mle2 + "Connection Refused!"), font=('Helvetica', 14))
		if config.bcerror > 0:
			dom_label.configure(fg='plum1')
			avgfee_label.configure(fg='plum1')
			hash_label.configure(fg='plum1')
			dif_label.configure(fg='plum1')
		if config.bserror > 0:
			price_label.configure(fg='plum1')
			sats_label.configure(fg='plum1')
			athchg_label.configure(fg='plum1')
		if config.cgerror > 0:
			change24_label.configure(fg='plum1')
			circ_label.configure(fg='plum1')
			mcap_label.configure(fg='plum1')
			high24_label.configure(fg='plum1')
			low24_label.configure(fg='plum1')
			ath_label.configure(fg='plum1')
			athdate_label.configure(fg='plum1')
		if config.alterror > 0:
			fearindex_label.configure(fg='plum1')
		if config.mlerror > 0:
			lnodes_label.configure(fg='plum1')
			lgtcap_label.configure(fg='plum1')
			lnchannels_label.configure(fg='plum1')
		if config.mempoolerror > 0:
			block_label.configure(fg='plum1')
			memp_label.configure(fg='plum1')
			recfeeusd_label.configure(fg='plum1')
			recfee_label.configure(fg='plum1')
		if config.bserror > 1 and config.cgerror > 1 and config.mempoolerror > 1:
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

		#Runs only once
		if onlyonce == 0:
			hashrate24hrsav = config.hashrate24hr
			mempoolsav = config.mempool
			average_transaction_fee_usd_24hsav = config.average_transaction_fee_usd_24h
			config.splash.destroy()
			onlyonce = 1

		# to calculate the hourly differences
		if duration_in_s > 300:
			print("Calculating duration_in_s > 300")
			hashrate24hrdiff =  config.hashrate24hr - hashrate24hrsav
			try:
				hashrate24hrdiff =  hashrate24hrdiff / hashrate24hrsav * 100
			except ZeroDivisionError:
				print("Zero Division Error Calculating Hashrate 24H diff")
			hashrate24hrsav = config.hashrate24hr
			if config.mempool == 0:
				config.mempool = 1
			mempooldiff = config.mempool  - mempoolsav 
			try:
				mempooldiff = mempooldiff / mempoolsav * 100
			except ZeroDivisionError:
				print("Zero Division Error Calculating Mempool diff")
			mempoolsav = config.mempool
			average_transaction_fee_usd_24hdiff = config.average_transaction_fee_usd_24h - average_transaction_fee_usd_24hsav
			try:
				average_transaction_fee_usd_24hdiff = average_transaction_fee_usd_24hdiff / average_transaction_fee_usd_24hsav * 100
			except ZeroDivisionError:
				print("Zero Division Error Calculating Average Transaction Fee 24H diff")
			average_transaction_fee_usd_24hsav = config.average_transaction_fee_usd_24h
			then = datetime.datetime.now()

		update_label.after(config.refreshtime,BTCTicker.labels) 

	def close(self):
		#Close all windows when Bitcoin button is pressed
		try:
			settings.destroy()
			gc.collect()
			#sys.exit()
		except:
			pass
		config.root.destroy()

hashrate24hrsav = 0
mempoolsav = 0
average_transaction_fee_usd_24hsav = 1 
hashrate24hrdiff = 0
mempooldiff = 0
average_transaction_fee_usd_24hdiff = 0 
onlyonce = 0
then = datetime.datetime.now()
gui.splash.splashScreen()
config.root.geometry("%dx%d+0+0" % (config.width_value, config.height_value))
config.root.configure(bg='black', cursor= 'crosshair')
config.root.attributes('-fullscreen', True)
try:
	btclogo = PhotoImage(file=r"images\btclogo.png")
except:
	btclogo = PhotoImage(file=r"images/btclogo.png")
try:
	settingsicon = PhotoImage(file=r"images\settings.png")
except:
	settingsicon = PhotoImage(file=r"images/settings.png")
my_gui = BTCTicker(config.root)
api.apicall.initialCall()
BTCTicker.labels()
mainloop()
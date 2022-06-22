import config
import requests
from urllib.request import urlopen
from json import loads

def bitstamp():
	status = 0
	try:
		bitstamp_url = 'https://bitstamp.net/api/ticker'
		bitstamp_api_request = urlopen(bitstamp_url).read()
		config.pricebtc = float(loads(bitstamp_api_request)['last'])
		try:
			config.satsusd = 1 / config.pricebtc * 100000000
			config.bserror = 0
		except ZeroDivisionError:
			print("Zero Division Error Calculating Sats per Dollar")
			config.bserror = 1
		print(config.pricebtc)
	except:
		try:
			urltest = requests.get(bitstamp_url)
			status = urltest.status_code
			urltest.close()
			config.bserror = 1
			print("Error Reading BitStamp. Status code: " + str(status))
		except:
			config.bserror = 2
			print("Bitstamp Connection Refused ")
	if config.bserror == 1:
		config.bs1 = "Bitstamp "
		config.bs2 = ""
	elif config.bserror == 2:
		config.bs1 = ""
		config.bs2 = "Bitstamp "
	else:
		config.bs1 = ""
		config.bs2 = ""
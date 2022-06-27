import config
import requests
from urllib.request import urlopen
from json import loads

def blockchair():
	status = 0
	try:
		#get blockchain data https://blockchair.com/api/docs#link_M03
		blockchair_url = 'https://api.blockchair.com/bitcoin/stats'
		blockchair_api_request = urlopen(blockchair_url).read()	
		config.market_dominance_percentage = float(loads(blockchair_api_request)['data']['market_dominance_percentage'])
		config.average_transaction_fee_usd_24h = float(loads(blockchair_api_request)['data']['average_transaction_fee_usd_24h'])
		config.hashrate24hr = float(loads(blockchair_api_request)['data']['hashrate_24h'])
		config.market_dominance_percentage = config.market_dominance_percentage / 100
		config.hashrate24hr = config.hashrate24hr / 1000000000000000000  # in EH/s
		print("Updated Blockchair Stats ")
		config.bcerror = 0
	except:
		try:
			urltest = requests.get(blockchair_url)
			status = urltest.status_code
			urltest.close()
			config.bcerror = 1
			print("Error reading BlockChair. Status code: " + str(status))
		except:
			config.bcerror = 2
			print("Blockchair Connection Refused ")
	if config.bcerror == 1:
		config.bc1 = "Blockchair "
		config.bc2 = ""
	elif config.bcerror == 2:
		config.bc1 = ""
		config.bc2 = "Blockchair "
	else:
		config.bc1 = ""
		config.bc2 = ""
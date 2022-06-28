import config
import requests
from urllib.request import urlopen
from json import loads

def blockchair():
	status = 0
	try:
		#Blockchair API documentation -> https://blockchair.com/api/docs#link_M03
		blockchair_url = 'https://api.blockchair.com/bitcoin/stats'
		blockchair_api_request = urlopen(blockchair_url).read()	
		config.market_dominance_percentage = float(loads(blockchair_api_request)['data']['market_dominance_percentage'])

		### Currently unused data, potential future use ###
		config.average_transaction_fee_sats_24h = float(loads(blockchair_api_request)['data']['average_transaction_fee_24h'])
		config.average_transaction_fee_usd_24h = float(loads(blockchair_api_request)['data']['average_transaction_fee_usd_24h'])
		config.blocks_24h = int(loads(blockchair_api_request)['data']['blocks_24h'])
		config.hashrate24hr = float(loads(blockchair_api_request)['data']['hashrate_24h'])
		config.hodling_addresses = int(loads(blockchair_api_request)['data']['hodling_addresses'])
		config.median_transaction_fee_sats_24h = float(loads(blockchair_api_request)['data']['median_transaction_fee_24h'])
		config.median_transaction_fee_usd_24h = float(loads(blockchair_api_request)['data']['median_transaction_fee_usd_24h'])
		config.mempool_total_fee_usd = float(loads(blockchair_api_request)['data']['mempool_total_fee_usd'])
		config.mempool_tps = float(loads(blockchair_api_request)['data']['mempool_tps'])
		config.timechain_size = float(loads(blockchair_api_request)['data']['blockchain_size'])
		config.total_outputs = int(loads(blockchair_api_request)['data']['outputs'])
		config.total_transactions = int(loads(blockchair_api_request)['data']['transactions'])
		config.volume_24h = float(loads(blockchair_api_request)['data']['volume_24h'])

		### Calculations ###
		config.market_dominance_percentage = config.market_dominance_percentage / 100
		config.timechain_size = config.timechain_size / 1000000000 # in GB
		config.hashrate24hr = config.hashrate24hr / 1000000000000000000  # in EH/s
		config.volume_24h = config.volume_24h / 100000000 # in BTC
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
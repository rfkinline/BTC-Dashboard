import config
import requests
from urllib.request import urlopen
from json import loads

def mempoolspace():
	status = 0
	try:
		if config.node_connected != 1:
			block_url = 'https://mempool.space/api/blocks/tip/height'
			difadj_url = 'https://mempool.space/api/v1/difficulty-adjustment'
			fees_url = 'https://mempool.space/api/v1/fees/recommended'
			transaction_url = 'https://mempool.space/api/mempool'
		else:
			block_url = config.ip_url + 'api/blocks/tip/height'
			difadj_url = config.ip_url + 'api/v1/difficulty-adjustment'
			fees_url = config.ip_url + 'api/v1/fees/recommended'
			transaction_url = config.ip_url + 'api/mempool'
		transaction_api_request = urlopen(transaction_url).read()
		config.mempool = float(loads(transaction_api_request)['count'])
		block_api_request = urlopen(block_url).read()
		newBlock = float(loads(block_api_request))
		fees_api_request = urlopen(fees_url).read()
		config.highfee = float(loads(fees_api_request)['fastestFee'])
		config.mediumfee = float(loads(fees_api_request)['halfHourFee'])
		config.lowfee = float(loads(fees_api_request)['hourFee'])
		difadj_api_request = urlopen(difadj_url).read()
		config.diffadj = float(loads(difadj_api_request)['difficultyChange'])

		if newBlock > config.oldblock:
			config.blocks = newBlock
			config.timestamp = 1
			blockhash_url = 'https://mempool.space/api/blocks/tip/hash'
			blockh = urlopen(blockhash_url).read()
			blockh = (str(blockh)[1:100])
			blockh = blockh.replace("'", "")
			if blockh != config.lasthash:
				if config.node_connected != 1:
					blockh_url = "https://mempool.space/api/block/" + blockh
				else:
					blockh_url = config.ip_url + "api/block/" + blockh
				hash_api_request = urlopen(blockh_url).read()
				config.timestamp = int(loads(hash_api_request)['timestamp'])
				config.lasthash = blockh
				config.oldblock = newBlock
		if config.node_connected != 1:
			print("Mempool Stats Updated ")
		else:
			print("Node Mempool Stats Updated ")
		config.mempoolerror = 0
	except:
		try:
			if config.node_connected != 1:
				urltest = requests.get('https://mempool.space/')
			else:
				urltest = requests.get(config.ip_url)
			status = urltest.status_code
			urltest.close()
			config.mempoolerror = 1
			print("Error Reading Mempool. Status code: " + str(status))
		except:
			config.mempoolerror = 2
			print("Mempool Connection Refused ")
			print (status)
	if config.mempoolerror == 1:
		config.mp1 = "Mempool "
		config.mp2 = ""
	elif config.mempoolerror == 2:
		config.mp1 = ""
		config.mp2 = "Mempool "
	else:
		config.mp1 = ""
		config.mp2 = ""
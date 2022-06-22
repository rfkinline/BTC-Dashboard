import config
import requests
from urllib.request import urlopen
from json import loads

def ml1():
	status = 0	
	try:
		ml1_url = 'https://1ml.com/statistics?json=true'
		ml1_api_request = urlopen(ml1_url).read()
		config.LNDCap = float(loads(ml1_api_request)['networkcapacity'])	
		config.LNDCap = config.LNDCap / 100000000
		config.lnodes = float(loads(ml1_api_request)['numberofnodes'])
		config.lnchannels = int(loads(ml1_api_request)['numberofchannels'])
		config.lndcap_chg = float(loads(ml1_api_request)['networkcapacity30dchange'])
		config.lnodes_chg = float(loads(ml1_api_request)['numberofnodes30dchange'])
		config.lnchannels_chg = float(loads(ml1_api_request)['numberofchannels30dchange'])
		print("Lightning Stats Updated ")
		config.mlerror = 0
	except:
		try:
			urltest = requests.get(ml1_url)
			status = urltest.status_code
			urltest.close()
			config.mlerror = 1
			print("Error Reading 1ML. Status code: " + str(status))
		except:
			config.mlerror = 2 
			print("1ML Connection Refused ")
	if config.mlerror == 1:
		config.mle1 = "1ML "
		config.mle2 = ""
	elif config.mlerror == 2:
		config.mle1 = ""
		config.mle2 = "1ML "
	else:
		config.mle1 = ""
		config.mle2 = ""
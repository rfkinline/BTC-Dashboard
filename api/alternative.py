import config
import requests
from urllib.request import urlopen
from json import loads

def alt():
	status = 0
	try:	
		# get the fear and greed index
		alt_url = 'https://api.alternative.me/fng/'
		alt_api_request = urlopen(alt_url).read()
		config.fearindex = str(loads(alt_api_request)['data'][0]['value_classification'])
		config.fearindexvalue = str(loads(alt_api_request)['data'][0]['value'])
		print("Updated Fear Index ")
		config.alterror = 0
	except:
		try:
			urltest = requests.get(alt_url)
			status = urltest.status_code
			urltest.close()
			config.alterror = 1
			print("Error Reading Fear Index. Status code: " + str(status))
		except:
			config.alterror = 2
			print("Alt Connection Refused ")
	if config.alterror == 1:
		config.alte1 = "Alternative "
		config.alte2 = ""
	elif config.alterror == 2:
		config.alte1 = ""
		config.alte2 = "Alternative "
	else:
		config.alte1 = ""
		config.alte2 = ""
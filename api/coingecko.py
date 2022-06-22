import config
import requests
from urllib.request import urlopen
from json import loads

def coingecko():
	status = 0	
	try:
		coingecko_url = 'https://api.coingecko.com/api/v3/coins/bitcoin'
		coingecko_api_request = urlopen(coingecko_url).read()	
		config.marketcap24h = float(loads(coingecko_api_request)['market_data']['market_cap_change_percentage_24h'])
		config.pricebtc24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])
		config.pricebtc1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		config.high24h = float(loads(coingecko_api_request)['market_data']['high_24h']['usd'])
		config.low24h = float(loads(coingecko_api_request)['market_data']['low_24h']['usd'])
		config.marketcapbtc = float(loads(coingecko_api_request)['market_data']['market_cap']['usd'])
		config.ath = float(loads(coingecko_api_request)['market_data']['ath']['usd'])
		config.athdate = str(loads(coingecko_api_request)['market_data']['ath_date']['usd'])
		config.circulating_supply = float(loads(coingecko_api_request)['market_data']['circulating_supply'])
		config.pricebtc24hrchange = config.pricebtc24hrchange / 100
		print("Updated CoinGecko Stats ")
		config.cgerror = 0
	except:
		try:
			urltest = requests.get(coingecko_url)
			status = urltest.status_code
			urltest.close()
			config.cgerror = 1
			print("Error reading Coingecko. Status code: " + str(status))
		except:
			config.cgerror = 2
			print("CoinGecko Connection Refused ")
	if config.cgerror == 1:
		config.cg1 = "CoinGecko "
		config.cg2 = ""
	elif config.cgerror == 2:
		config.cg1 = ""
		config.cg2 = "CoinGecko "
	else:
		config.cg1 = ""
		config.cg2 = ""
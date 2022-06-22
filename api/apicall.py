import config
import time
import threading
from api.alternative import alt
from api.bitstamp import bitstamp
from api.mempool import mempoolspace
from api.ml1 import ml1
from api.blockchair import blockchair
from api.coingecko import coingecko

ml1start = altstart = bitstampstart = blockchairstart = coingeckostart = mempoolstart = time.time()

def initialCall():
	bitstamp()
	coingecko()
	mempoolspace()
	blockchair()
	alt()
	ml1()

def apiCall():
	global ml1start, altstart, bitstampstart, blockchairstart, coingeckostart, mempoolstart
	config.refreshtime = config.new_refreshtime

	#Free API Requests Limit Enforcement
	# Bitstamp allows 800 calls per minute	
	if time.time() - bitstampstart > 0.1:
		bitstamp_thread = threading.Thread(target=bitstamp, name="Bitstamp")
		bitstamp_thread.start()
		bitstampstart = time.time()

	# Coingecko allows 100 calls per minute
	if time.time() - coingeckostart > 1:
		coingecko_thread = threading.Thread(target=coingecko, name="CoinGecko")
		coingecko_thread.start()
		coingeckostart = time.time()

	#Mempool allows 200 calls per minute
	if time.time() - mempoolstart > 2:
		mempool_thread = threading.Thread(target=mempoolspace, name="Mempool")
		mempool_thread.start()
		mempoolstart = time.time()

	#Blockchair allows 1 call per minute
	if time.time() - blockchairstart > 60:
		blockchair_thread = threading.Thread(target=blockchair, name="BlockChair")
		blockchair_thread.start()
		blockchairstart = time.time()
			
	# Alternative updates their data every 5 minutes
	# However Alternative allows 60 calls per minute
	if time.time() - altstart > 150:
		alt_thread = threading.Thread(target=alt, name="Alternative")
		alt_thread.start()
		altstart = time.time()
			
	# 1ML unknown API Limit, set to 5 minutes to be safe
	if time.time() - ml1start > 300:
		ml1_thread = threading.Thread(target=ml1, name="ML1")
		ml1_thread.start()
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
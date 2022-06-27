from tkinter import *

version = "v2.3.1"

### Default refresh time in seconds (change to your liking) ###
default_refresh = 10

### Trend Indicators and Color Controls ###
# Display tresholds (change color if value increased/decreased more than x%).  
disppricebtc1hrchangediff = 2    # checked once / hr
dispmarketcap24h = 2          # checked once / day
disphashrate24hrdiff = 1      # checked every 5 minutes
dispmempooldiff = 5          # checked every 5 minutes
dispaverage_transaction_fee_usd_24hdiff = 10      # checked every 5 minutes

### GUI Variables ###
root = Tk()
splash = Toplevel()
width_value = 0
height_value = 0

### API Call Variables ###
try:
	refreshtime
except NameError:
	if default_refresh < 1 or default_refresh > 86400:
		default_refresh = 10
		refreshtime = default_refresh * 1000
	else:
		refreshtime = default_refresh * 1000
try:
	new_refreshtime
except NameError:
	new_refreshtime = refreshtime

### Alternative API Variables ###
alterror = 0
alte1 = ""
alte2 = ""
try:
	fearindex
except NameError:
	fearindex = ""
try:
	fearindexvalue
except NameError:
	fearindexvalue = 0

### Bitstamp API Variables ###
bserror = 0
bs1 = ""
bs2 = ""

try:
	pricebtc
except NameError:
	pricebtc = 0
try:
	satsusd
except NameError:
	satsusd = 0

### BlockChair API Variables ###
bcerror = 0
bc1 = ""
bc2 = ""
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

### CoinGecko API Variables ###
cgerror = 0
cg1 = ""
cg2 = ""
try:
	ath
except NameError:
	ath = 0
try:
	athdate
except NameError:
	athdate = "2009-01-03"
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

### Mempool API Variables ###
mempoolerror = 0
mp1 = ""
mp2 = ""
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
	currenthashrate
except NameError:
	currenthashrate = 0
try:
	currentdifficulty
except NameError:
	currentdifficulty = 0
try:
	diffadj
except NameError:
	diffadj = 0
try:
	oldblock
except NameError:
	oldblock = 0
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
try:
	ip_url
except NameError:
	ip_url = "http://192.168.1.2:3006/"

### ML1 API Variables ###
mlerror = 0
mle1 = ""
mle2 = ""
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
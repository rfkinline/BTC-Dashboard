# BTC Dashboard
BTC dashboard is a Python program that you can run on a Raspberry Pi or PC and displays the output on a LCD Screen. The program provides up-to-date tracking of key Bitcoin indicators. The program uses free API's online and automatically respects their free data request limits. <br>
No accounts, API keys, or log-ins required<br>
The dashboard indicators include:<br>
<li> Market Data: Price, sats/USD, 24hr Change, BTC Dominance, Circulating Supply, and MarketCap.
<li> Mempool Data: Block Height, # of Transactions in the Mempool, Average Fee 24hr($), Recommended Fees: Fast, Medium, Low ($ & sats/vByte), Hashrate/24hrs, and Next difficulty adjustment estimate.
<li> Other Indicators: BTC High 24hr, BTC Low 24hr, ATH (All Time High), ATH change (%), ATH Date, Fear & Greed Index, Fear Value, # of Lightning Network Nodes, Lightning Network Capacity, Error messages, and Date/Time of Last update
<li> Colors: red or green when the change is over 5%. Currently implemented in: BTC Price, Marketcap, Mempool and Hashrate.
<br>Block Height turns green when block height increases and it remains green for 60 seconds thereafter.

<img src="https://cypherhive.com/wp-content/uploads/2021/03/BTC-Dashboard-scaled.jpg" border="1"><br>

## Minimum Hardware Requirements
<li>A Raspberry Pi (0w, 1, 2, 3, 4+) or you can also run on a PC with Git Bash and Python installed
<li>Constant internet connection
<li>7 Inch Display Monitor 1024X600. Larger displays should also do the job.

## Install on Raspberry Pi
Install [Raspberry Pi OS](https://www.raspberrypi.org/software/) on your Raspberry Pi<br>
Make sure everything is updated
```shell
sudo apt-get update && sudo apt-get upgrade -y
```
Install XTERM dependency to allow the screensaver to be suppressed
```shell
sudo apt-get install xterm
```
Install PILLOW dependecy
```shell
sudo apt-get install python3-pil python3-pil.imagetk
```
Clone this repository
```shell
git clone https://github.com/ChuckinBits/BTC-Dashboard.git
```
Now you will have BTC-Dashboard directory under /home/pi/
<br>Right mouse click btclauncher.sh and click properties
<br>Click the "Permissions" tab and change Execute option to "Anyone" and click OK

## Start BTC Dashboard
Open BTC-Dashboard folder and [copy](https://projects.raspberrypi.org/en/projects/rpi-gui-copying-files) btclauncher.sh to your desktop. (optional) <br>
Double click or open btclauncher.sh and if prompted select "Execute" to run the program. <br>
Select "Execute in Terminal" to run the program and have a terminal screen running in the background which shows you what the program is doing behind the scenes and is great for debugging if there are any errors.
<br>Enjoy the Dashboard!

## Why run btclauncher.sh and not just BTCDashboard.py?
btclauncher.sh contains commands which suppress the default screensaver so that the screen always stays on and doesn't turn off after a certain period of time. <br>
If you already have your screensaver suppressed or prefer not to suppress the screensaver than you can simply run BTCDashboard.py using Python3
```shell
python3 BTCDashboard.py
```

## To stop the program
To stop the program, click on the Bitcoin logo. 

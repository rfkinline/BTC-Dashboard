# BTC Dashboard
BTC dashboard is a Python program that you can run on a Raspberry Pi or PC and displays the output on a LCD Screen. The program provides up-to-date tracking of key Bitcoin indicators. The program uses free API's online and automatically respects their free data request limits. <br>
No accounts, API keys, or log-ins required<br>
The dashboard indicators include:<br>
<li> Market Data: Price, sats/USD, 24hr Change, BTC Dominance, Circulating Supply, and MarketCap.
<li> Mempool Data: Block Height - time since block added, # of Transactions in the Mempool, Average Fee 24hr($), Recommended Fees: Fast, Medium, Low ($ & sats/vByte), Hashrate/24hrs, and Next difficulty adjustment estimate.
<li> Other Indicators: BTC High 24hr, BTC Low 24hr, ATH (All Time High), ATH change (%), ATH Date, Fear & Greed Index, Fear Value, # of Lightning Network Nodes, Lightning Network Capacity, Error messages, and Date/Time of Last update
<li> Bitcoin Price trend arrow appears next to the price when Bitcoin price goes up or down 2%+ in an hour.
<li> Colors: Green (up) or Red (down) depending on the change. Currently implemented in: BTC Price, Marketcap, and Hashrate.
<li> Colors reversed for Mempool transactions. Green (down) and Red (up) show when # of transactions goes up or down 5% in 5 minutes
<li> ATH Price turns green and bold if new ATH was reached in the same day. Green ATH date on same day. ATH Change turns green within 5% of ATH and red when 50% and below 
<li>Block Height turns green when a new block is added and it remains green for 2 minutes thereafter.

<img src="https://cypherhive.com/wp-content/uploads/2021/01/BTC-Dashboard8ATHBHgreen.jpg" border="1"><br>

## Minimum Hardware Requirements
<li>A Raspberry Pi 0w, 1, 2, 3, 4+ (tested on 0w and 4) or you can also run on a computer with Python installed
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
Select "Execute in Terminal" to run the program and have a terminal screen running in the background which shows you what the program is doing behind the scenes and is great for debugging if there are any errors. To see the terminal while the program is running use CTL + ESC.
<br>Enjoy the Dashboard!

## Why run btclauncher.sh and not just BTCDashboard.py?
btclauncher.sh contains commands which suppress the default screensaver so that the screen always stays on and doesn't turn off after a certain period of time. <br>
If you already have your screensaver suppressed or prefer not to suppress the screensaver than you can simply run BTCDashboard.py using Python3
```shell
python3 BTCDashboard.py
```

## To stop the program
To stop the program, click on the Bitcoin logo.

## Errors
Error messages will appear in purple below Lightning Capacity and above Last update time. <br>
The associated indicators will still show the previous values but turn purple letting you know that those indicators have been potentially affected by the error and may not be up to date. <br>
The associated indicators will turn back to normal colors when the error clears and connection to the associated data source is restored. <br>
The program will keep running and attempt to reestablish connection at least once every 5 minutes depending on the free API limits.

## To update the BTC-Dashboard program
We continually try and improve the program on our spare time.<br>
Be sure to update every once and a while for performance improvements, new features, and bug fixes. <br>
<br>
Navigate to the BTC-Dashboard directory in the terminal
```shell
cd BTC-Dashboard
```
Once in the directory run this command
```shell
git pull
```
If there are any updates, it will download them.<br>
Enjoy!


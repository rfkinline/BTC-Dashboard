# BTC Dashboard
#### v2.1.0
BTC dashboard is a Python program that you can run on a Raspberry Pi or computer of your choice and displays the output on a screen. The program provides up-to-date tracking of key Bitcoin indicators. The program uses free API's online and automatically respects their free data request limits. <br>
No accounts, API keys, or log-ins required<br>
The dashboard indicators include:<br>
<li> Market Data: Price, sats/USD, 24hr Change, BTC Dominance, Circulating Supply, and MarketCap.
<li> Mempool Data: Block Height - time since block added, # of Transactions in the Mempool, Average Fee 24hr($), Recommended Fees: Fast, Medium, Low ($ & sats/vByte), Hashrate/24hrs, and Next difficulty adjustment estimate.
<li> Other Indicators: BTC High 24hr, BTC Low 24hr, ATH (All Time High), ATH change (%), ATH Date, Fear & Greed Index, Fear Value, Blocks until Taproot activation, Taproot date, Lightning Network Capacity + 30 day change, # of Lightning Nodes + 30 day change, # of Lightning Channels + 30 day change, Error messages, and Date/Time of Last update
<li> Bitcoin Price trend arrow appears next to the price when Bitcoin price goes up or down 2%+ in an hour.
<li> Colors: Green (up) or Red (down) depending on the change. Currently implemented in: BTC Price, Marketcap, and Hashrate.
<li> Colors reversed for Mempool transactions. Green (down) and Red (up) show when # of transactions goes up or down 5% in 5 minutes
<li> ATH Price turns green and bold if new ATH was reached in the same day. Green ATH date on same day. ATH Change turns green within 5% of ATH and red when 50% and below 
<li>Block Height turns green when a new block is added and it remains green for 2 minutes thereafter.

<img src="https://cypherhive.com/wp-content/uploads/2021/01/BTC-Dashboard8ATHBHgreen.jpg" border="1"><br>

## Minimum Hardware Requirements
- A Raspberry Pi [0w](https://amzn.to/2RLVBFs), 1, 2, 3, 4+ (tested on 0w and 4) or you can also run on a computer with Python installed
- Constant internet connection
- [7 Inch Display Monitor](https://amzn.to/3fnSYCP) 1024X600. Larger displays should also work.

## Install on Raspberry Pi
#### [Detailed Tutorial](https://cypherhive.com/bitcoindashboard/)
Install [Raspberry Pi OS](https://www.raspberrypi.org/software/) on your Raspberry Pi<br>
Make sure everything is updated
```shell
sudo apt-get update && sudo apt-get upgrade -y
```
Clone this repository
```shell
git clone https://github.com/ChuckinBits/BTC-Dashboard.git
```
Now you will have BTC-Dashboard directory under /home/pi/
<br>Right mouse click btclauncher.sh and click properties
<br>Click the "Permissions" tab and change Execute option to "Anyone" and click OK

## Install Dependencies

### Automatically Install All Dependencies 
Navigate to the BTC-Dashboard directory in the terminal
```shell
cd BTC-Dashboard
```
Automatically install all of the required dependencies from the requirements.txt file
```shell
pip install -r requirements.txt
```

### Manually Install Dependencies
Intall Requests dependency to allow requesting of the API data
```shell
pip install requests
```
Install XTERM dependency to allow the screensaver to be suppressed
```shell
sudo apt-get install xterm
```
Install PILLOW dependecy
```shell
sudo apt-get install python3-pil python3-pil.imagetk
```

## Start BTC Dashboard
Open BTC-Dashboard folder and [copy](https://projects.raspberrypi.org/en/projects/rpi-gui-copying-files) btclauncher.sh to your desktop. (optional) Also feel free to rename it to whatever you want <br>
Double click or open btclauncher.sh and if prompted select "Execute" to run the program. <br>
Select "Execute in Terminal" to run the program and have a terminal screen running in the background which shows you what the program is doing behind the scenes and is great for debugging if there are any errors. To see the terminal while the program is running use ALT + TAB or ALT + ESC
<br>Enjoy the Dashboard!

## Why run btclauncher.sh and not just BTCDashboard.py?
btclauncher.sh contains commands which suppress the default screensaver so that the screen always stays on and doesn't turn off after a certain period of time. <br>
If you already have your screensaver suppressed or prefer not to suppress the screensaver than you can simply run BTCDashboard.py using Python3
```shell
python3 BTCDashboard.py
```

## How to connect your own Node for Mempool Data
Open the settings menu by clicking on the settings button in the upper right hand corner of the Dashboard <br>
Under Mempool Data there are to options: "Default" and "Custom Node" <br>
Click "Custom Node" <br>
In the Input box type or paste your Node's Mempool URL and port <br>
The prefilled text in the Custom Node URL input box shows you an example of how this should look <br> 
Click on "Test Connection" button <br>
A messagebox will appear to let you know if the program is able to successfully connect to your node <br>
If successful, click the "Apply" button

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
Version is now shown on the splash screen as of v2.0.0 <br>
Navigate to the BTC-Dashboard directory in the terminal
```shell
cd BTC-Dashboard
```
Once in the directory run this command
```shell
git pull
```
If there are any updates, it will download and apply them.<br>
Enjoy!
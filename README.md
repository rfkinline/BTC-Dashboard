# BTC Dashboard
BTC dashboard is a Python program that you can run on a Raspberry Pi device and displays the output on a LCD Screen. The program provides up-to-date tracking of key Bitcoin indicators and does not require you to sign up for anything. The program uses free API's online and automatically respects their data request limits. <br>
The dashboard indicators include:<br>
<li> Market Data: Price, 24hr Change, BTC Dominance, sats/USD and MarketCap.
<li> Blockchain Data: Hashrate/24hrs, Next difficulty adjustment estimate, Next adjustment date, # of Transactions in the Mempool, Current Block Height, Average Fee ($), Recommended fee (sat/vB).
<li> Other Indicators: BTC High 24hr, BTC Low 24hr, ATH (All Time High), ATH change (%), ATH Date, Circulating BTC, Fear & Greed Index, Fear Value, Lightning Network Capacity, Date/Time of Last update
<li> Colors: red or green when the change is over 5%. Currently implemented in: BTC Price, Marketcap, and Hashrate.

<img src="https://cypherhive.com/wp-content/uploads/2021/01/20210126_145547-1024x576.jpg" border="1"><br>

## Hardware
<li>Raspberry Pi with a constant internet connection
<li>7 Inch Display Monitor 1024X600. Other displays should also do the job but may require some code modification.

## Start BTC Dashboard
Open BTC-Dashboard folder and copy btclauncher.sh to your desktop. (optional) <br>
https://projects.raspberrypi.org/en/projects/rpi-gui-copying-files <br>
Double click or open btclauncher.sh and if prompted select "Execute" to run the program. <br>
Select "Execute in Terminal" to run the program and have a terminal screen running in the background which shows you what the program is doing behind the scenes and is great for debugging if there are any errors.

## Why run btclauncher.sh and not just BTCDashboard.py?
btclauncher.sh contains commands which suppress the default screensaver so that the screen always stays on and doesn't turn off after a certain period of time. <br>
If you already have your screensaver suppressed or prefer not to suppress the screensaver than you can simply run BTCDashboard.py 

## To stop the program
To stop the program, click on the BTC logo. 

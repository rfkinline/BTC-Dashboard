<h1>NEW FEATURE</h1>
The display will be dimmed to 20% until an event happens (ie all-time high)

<h1>Hardware</h1>
<li>Standard Raspberry Pi 3
<li>Hyperpixel display (as seen in image below) or Phat/What paper displays
<li>OS depends on the display you chose. For Phat/What use standard OS, for Hyperpixel follow instructions below (Install for Hyperpixel)

<h1>Instructions for CryptoDashboard.py</h1>

<img src="https://i.ibb.co/s22NsyW/IMG-20200817-094113.jpg" alt="" border="0"></a><br>
<img src="https://i.ibb.co/0YZDJhP/IMG-20200817-0941132.jpg" width=200 alt="" border="0"></a><br>Dimmed display when nothing is happening

What I am currently working on:
1. include: best performing coin (24hrs), total marketcap, incorporate other indicators
2. Improve GUI

# Install for HyperPixel 4.0 (3.5" display)
Only follow these instructions. It will save you a lot of time:
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-hyperpixel-4

# Install for Phat/What (paper display)
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat


# to read-write the csv files install Pandas
sudo apt-get install python3-pandas

additional documentation: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html

# ConfigCryptoDashboard.csv
Create a file called ConfigCryptoDashboard.csv with the following content (just copy and paste):<br>
summemax;0.1;2011-08-05 10:58<br>
basemax;0.01;2011-08-05 10:58<br>

summemax = the current value of your portfolio in USD<br>
basemax = the current value of your portfolio in BTC<br>
You need to do this only onece at the start. After that, the program will maintain these values

# Portfolio.csv
Create a file called portfolio.csv that includes your portfolio<br>
Column coin: this will be used to complete the CoinGecko URL: https://api.coingecko.com/api/v3/coins/ampleforth Check this URL before using it. For exmple REN is republic-network<br>
Column Qty: quantity in your portfolio<br>
Column Purchase: price of the coin at the time you purchased it<br>

# to let the program automatically start after reboot
crontab -e

insert the following code at the end:<br>
@reboot DISPLAY=:0 sudo pigpiod
@reboot DISPLAY=:0 python3 /home/pi/CryptoDashboard.py

additional documentation: https://www.raspberrypi.org/documentation/linux/usage/cron.md

# C Button on display
To stop the program, click on the "C" button. 

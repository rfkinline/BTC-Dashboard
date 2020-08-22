# NEW FEATURE
The display will be dimmed to 20% until an event happens (ie all-time high)

# Hardware
<li>Standard Raspberry Pi 3
<li>Hyperpixel 3.5" display (as seen in image below) or Phat/What paper displays
<li>OS depends on the display you chose. For Phat/What use standard OS, for Hyperpixel follow instructions below (Install for Hyperpixel)

## Instructions for CryptoDashboard.py

<img src="https://i.ibb.co/r0BzBfF/IMG-20200821-195719.jpg" alt="" border="0"></a><br>
<img src="https://i.ibb.co/4Vb7BJn/ct3.jpg" alt="ct3" width=200 alt="" border="0"></a><br>Dimmed display when nothing is happening

## What I am currently working on:
1. include: total marketcap, incorporate other indicators
2. Improve GUI
3. Minimize hardcoded variables
4. Eventually move away from TKinter. It is too complicated. iE kivy, QT, GTK
5. Indicators like: Mayer Multiple or Number of coins with more than 15% gain, divided by coins more than 15% loss (7 days), ???
6. Marketcap: total, DeFi
7. Coinbase Index
8. Investment value dilema. I chose to hardcode the value of the investment in USD and BTC as othrwise there will be the dilema: at what exchange rate to the USD and BTC was the coin / token purchased? It makes everything complicated and therefore those 2 numbers are hardcoded. In case you prefer to calculate them, then add a column "purchase price in BTC" to the portfolio. The column purchase price in the portfolio is needed so the program can calculate the "take profit" of a coin
9. Clean up code and document in code

## Display
CryptoDashboard is using the HyperPixel display and CryptoDashboard-Phat-What is built on the Phat or What paper display.<br>

<p><b>A) Install for HyperPixel 4.0 (3.5" display)</b><br>
    Only follow these instructions. It will save you a lot of time:<br>
    https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-hyperpixel-4</p>

<p><b>B) Install for Phat/What (paper display)</b><br>
    https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat</p>


## ConfigCryptoDashboard.csv
Create a file called ConfigCryptoDashboard.csv with the following content (just copy and paste):<br>
> summemax;0.1;2011-08-05 10:58<br>
> basemax;0.01;2011-08-05 10:58<br>

summemax = the current value of your portfolio in USD<br>
basemax = the current value of your portfolio in BTC<br>
You need to do this only onece at the start. After that, the program will maintain these values

## Portfolio.csv
Create a file called portfolio.csv that includes your portfolio<br>
Column coin: this will be used to complete the CoinGecko URL: https://api.coingecko.com/api/v3/coins/ampleforth Check this URL before using it. For exmple REN will only work if you use: republic-network<br>
Column Qty: quantity in your portfolio<br>
Column Purchase: price of the coin at the time you purchased it<br>

## Install PANDAS
to read-write the csv files you need to install PANDAS:<br>
> sudo apt-get install python3-pandas

additional documentation: https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html


## Let the program automatically start after reboot
> crontab -e

insert the following code at the end:<br>
> @reboot DISPLAY=:0 sudo pigpiod<br>
> @reboot DISPLAY=:0 python3 /home/pi/CryptoDashboard.py

additional documentation: https://www.raspberrypi.org/documentation/linux/usage/cron.md

## There is a C Button on HyperPixel display
To stop the program, click on the "C" button. 

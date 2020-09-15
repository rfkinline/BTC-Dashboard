# DeFi Dashboard
The dashboard is an up-to-date tracking of your portfolio. Instead of having to use apps like Blockfolio you use this code that runs on a Pi with a LCD display. It includes:<br>
<li> Value of portfolio in BTC and USD as well as current, beginning and all-time-high
<li> Current price of Bitcoin and a selected coin in USD
<li> Return on investment of portfolio
<li> Bitcoin Fear & Greed Index
<li> The display dims down when nothing is happening

<img src="https://i.ibb.co/9sxxNMt/Untitled-1.jpg" alt="ct" border="0"><br>
<img src="https://i.ibb.co/4Vb7BJn/ct3.jpg" alt="ct3" width=200 alt="" border="0"></a><br>

ROTATE DISPLAY


## Hardware
<li>Standard Raspberry Pi 3 or 4
<li>Hyperpixel 3.5" display 
<li>Don't use the default OS supplied by Raspberry. Follow the instructions described below (Install for Hyperpixel)

## What I am currently working on:
1. include other indicators
2. Minimize hardcoded variables
3. Eventually move away from TKinter. It is too complicated. iE kivy, QT, GTK
4. Include indicators like: Mayer Multiple or Number of coins with more than 15% gain, divided by coins more than 15% loss (7 days), ???
5. Include Marketcap: total, DeFi
6. Investment-value dilemma. I chose to hardcode the value of the investment in USD and BTC as otherwise there will be the dilema: at what exchange rate to the USD and BTC was the coin / token purchased? It makes everything complicated and therefore those 2 numbers are hardcoded. In case you prefer to calculate them, then add a column "purchase price in BTC" to the portfolio. The column purchase price in the portfolio is needed so the program can calculate the "take profit" of a coin

## Display
<b>Install for HyperPixel 4.0 (3.5" display)</b><br>
    Only follow these instructions. It will save you a lot of time:<br>
    https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-hyperpixel-4

To rotate the display: <br>
> sudo nano /boot/config.txt
change display_rotate=1 to display_rotate=2<br>
now reboot the machine and the display should be vertical.

## ConfigCryptoDashboard.csv
Create a file called ConfigCryptoDashboard.csv with the following content (just copy and paste):<br>
> summemax;0.1;2011-08-05 10:58<br>
> basemax;0.01;2011-08-05 10:58<br>

summemax = the current value of your portfolio in USD<br>
basemax = the current value of your portfolio in BTC<br>
You need to do this only once at the start. After that, the program will maintain these values

## Portfolio.csv
Create a file called portfolio.csv that includes your portfolio<br>
Column coin: this will be used to complete the CoinGecko URL: https://api.coingecko.com/api/v3/coins/ampleforth Check this URL before using it (in Coingecko search in the source code for "api-symbol"). For example REN will only work if you use: republic-network<br>
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

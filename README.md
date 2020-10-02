# BTC Dashboard
The dashboard is an up-to-date tracking of your key BTC indicators. Instead of having to use apps like Blockfolio or websites, you use this code that runs on a Pi with a LCD display. The dashboard includes:<br>
<li> Market: Price, sats/USD and MarketCap, Dominance
<li> Mempool: Transactions, blocks to clear
<li> Blockchain: height and fees (sats/b and USD), hash-rate, next difficulty, date of next difficulty adjustment
<li> Bitcoin Fear & Greed Index
<li> Colors: red or green when the change is over 5%. Currently implemented in: Marketcap and Price

<img src="https://i.ibb.co/qsWd4yb/IMG-20200930-155742.jpg" width="300" alt="IMG-20200930-072821" border="1"><br>

## Hardware
<li>Standard Raspberry Pi 3 or 4
<li>Hyperpixel 3.5" display 
<li>Don't use the default OS supplied by Raspberry. Follow the instructions described below (Install for Hyperpixel)

## What I am currently working on:
1. include colors and maybe color grading
2. Capacity Lightning Network
3. GitHub stats
4. Needs at least two other modes of this, like one to get your local breakout price and another as we approach/pass ATH
5. Automatic screensaver (by time) to save display
6. Automatic start with using variables (for example display switch off/on time)

## Display
<b>Install for HyperPixel 4.0 (3.5" display)</b><br>
    Only follow these instructions. It will save you a lot of time:<br>
    https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-hyperpixel-4

To rotate the display: <br>
> sudo nano /boot/config.txt
change display_rotate=1 to display_rotate=2<br>
now reboot the machine and the display should be vertical.

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

## There is a C Button on the display
To stop the program, click on the "C" button. 

## Python
Start the program with "python3" and not "python" 

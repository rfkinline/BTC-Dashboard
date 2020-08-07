Instructions for cointickerportfolio.py


What I am currently working on:
1. display: best performing coin (24hrs)
2. use larger display (3.5")
3. error: when 404 on url, then the values are updated incorrectly (16.18 - 8.53)
4. It looks like the display stops working after a few hours
5. Improve GUI
6. Plot some data?

# install inky for the display
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat


# to read-write the csv files install Pandas
sudo apt-get install python3-pandas

# Configticker.csv
Create a file called configticker.csv with the following content (just copy and paste):
summemax;0.1;2011-08-05 10:58
basemax;0.01;2011-08-05 10:58

summemax = the current value of your portfolio in USD
basemax = the current value of your portfolio in BTC
You need to do this only onece at the start. After that, the program will maintain these values

# Portfolio.csv
Create a file called portfolio.csv that includes your portfolio
Column coin: this will be used to complete the CoinGecko URL: https://api.coingecko.com/api/v3/coins/ampleforth
Column Qty: quantity in your portfolio

# to let the program automatically start after reboot
crontab -e

insert the following code at the end:
@reboot python3 /home/pi/CryptoTickerPortfolio.py &

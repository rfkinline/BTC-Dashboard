Instructions for cointickerportfolio.py


What I am currently working on:
1. display: best performing coin (24hrs)
2. use larger display (3.5")
3. error: when 404 on url, then the values are updated incorrectly (16.18 - 8.53)
4. It looks like the display stops working after a few hours
5. Improve GUI

# install automatic start of program after reboot
crontab -e
and insert the following code at the end:
@reboot python3 /home/pi/CryptoTickerPortfolio.py &

# install inky for the display
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat


# for read-write the csv files install Pandas
sudo apt-get install python3-pandas

Create a file called cointicker.csv with the following content. Only when starting for the first time. After that the program will maintain these values
summemax;0.1;2011-08-05 10:58
basemax;0.01;2011-08-05 10:58

summemax = the current value of your portfolio in USD
basemax = the current value of your portfolio in BTC

Create a file called portfolio.csv that includes your portfolio
Column coin: this will be used to complete the CoinGecko URL: https://api.coingecko.com/api/v3/coins/ampleforth
Column Qty: quantity in your portfolio

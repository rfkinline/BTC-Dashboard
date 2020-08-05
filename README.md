Instructions for cointickerportfolio.py


What I am currently working on:
display best performing coin (24hrs)
display 

# install automatic start of program after reboot
@reboot python3 /home/pi/CryptoTickerPortfolio.py --type phat --colour yellow --target USD &

# install inky for the display
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat


# for read-write the csv files install Pandas
sudo apt-get install python3-pandas

Create a file called cointicker.csv with the following content
summemax;0.1;2011-08-05 10:58
basemax;0.01;2011-08-05 10:58

summemx = the current value of your portfolio in USD
basemax = the current value of your portfolio in BTC

Create a file called portfolio.csv that includes your portfolio

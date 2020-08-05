#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#install cron
#*/2 * * * * /usr/bin/python3 /home/pi/Projects/inky/ink_BTC.py --type what --colour red --target usd
#install inky 
#https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat

# python3 ticker.py --type phat --colour yellow --target USD
#git add.
#git commit -m "text"
#git push

# for read-write csv format:
#sudo apt-get install python3-pandas

#check coin api gets values
#include best performing coin

import numpy as np
import pandas as pd
import requests
import json
import time
import argparse
from subprocess import check_output
import sys
import datetime

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from font_fredoka_one import FredokaOne
from inky import InkyPHAT, InkyWHAT

pricebtc = 0
base = 0
summe = 0
summeprint = float(round(333.58,2))
basemax = str(round(19.19,2))
now = datetime.datetime.now()
nowsav = datetime.datetime.now()

df = pd.read_csv('portfolio.csv', delimiter=';', names = ['Coin', 'Symbol', 'Qty'])
tf = pd.read_csv('demo.csv', delimiter=';', names = ['Name', 'Value', 'Zeit'])
for i in range(len(tf)) :
        if tf.loc[i,"Name"] == "summemax":
                summemax = float(tf.loc[i,"Value"])

        if tf.loc[i,"Name"] == "baseemax":
                baseemax = str(tf.loc[i,"Value"])


# Command line arguments to set display type and colour, and enter your name
parser = argparse.ArgumentParser()
parser.add_argument('--type', '-t', type=str, required=True, choices=["what", "phat"], help="type of disp$
parser.add_argument('--colour', '-c', type=str, required=True, choices=["white", "black", "yellow"], help$
parser.add_argument('--target', '-n', type=str, required=False, help="eur or usd")
args = parser.parse_args()
colour = args.colour

       # Set up the correct display and scaling factors
if args.type == "phat":
        inky_display = InkyPHAT(colour)
        scale_size = 1
        padding = 0
elif args.type == "what":
        inky_display = InkyWHAT(colour)
        scale_size = 2.20
        padding = 15
# Load the fonts
fredoka_font = ImageFont.truetype(FredokaOne, int(30 * scale_size))
hanken_bold_font = ImageFont.truetype(HankenGroteskMedium, int(14 * scale_size))
hanken_medium_font = ImageFont.truetype(HankenGroteskBold, int(30 * scale_size))

while True:
        for i in range(len(df)) :
#               if df.loc[i,"Coin"] != "summemax":
                qtycoin = int(df.loc[i,"Qty"])
                ren = requests.get('https://api.coingecko.com/api/v3/coins/' + df.loc[i,"Coin"]).json()
                ren = { 'price_usd': ren['market_data']['current_price']['usd'] }
                pricecoin = float(ren['price_usd'])
                summe = summe + qtycoin * pricecoin
#               print (qtycoin,pricecoin,summe)
                if df.loc[i,"Coin"] == "bitcoin":
                        pricebtc = pricecoin

        base = str(round(summe / pricebtc, 2))
        if (base >= basemax):
                basemax = base
                nowsav = now

        if (summe >= summemax):
                summemax = summe

        # inky_display.set_rotation(180)
        inky_display.set_border(inky_display.BLACK)

        # Create a new canvas to draw on

        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        summemaxprint = str(round(summemax/1000,2))
        summeprint = str(round(summe/1000,2))
        print(summeprint)
        summemax = 0
        summe = 0
           # Grab the text to be displayed
#       text1 = " "
        text1 = nowsav.strftime("%Y-%m-%d %H:%M")
        text2 =  str(base) + " - " + str(basemax)
        text22 = " "
        text3 = str(summeprint) + " - " + str(summemaxprint)
        # Top and bottom y-coordinates for the white strip

        y_top = int(inky_display.HEIGHT * (5.0 / 10.0))
        y_bottom = y_top + int(inky_display.HEIGHT * (4.0 / 10.0))

        # Draw the red, white, and red strips

        for y in range(0, y_top):
          for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.YELLOW)

        for y in range(y_top, y_bottom):
          for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.BLACK)

        for y in range(y_bottom, inky_display.HEIGHT):
          for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.RED)

        # Calculate the positioning and draw the 1st text

        row1_w, row1_h = hanken_bold_font.getsize(text1)
        row1_x = int((inky_display.WIDTH - row1_w) / 2)
        row1_y = 0 + padding
        draw.text((row1_x, row1_y), text1, inky_display.BLACK, font=hanken_bold_font)
        # Calculate the positioning and draw the 2nd texts

        text2_w, text2_h = hanken_medium_font.getsize(text2)
        text2_x = int((inky_display.WIDTH - text2_w) / 2)
        text2_y = row1_h + (2 * padding)
        draw.text((text2_x, text2_y), text2, inky_display.WHITE, font=fredoka_font)

        text22_w, text22_h = hanken_medium_font.getsize(text22)
        text22_x = int((inky_display.WIDTH - text22_w) / 2)
        text22_y = text2_y + text2_h - padding
        draw.text((text22_x, text22_y), text22, inky_display.WHITE, font=fredoka_font)

        # Calculate the positioning and draw the 3rd text

        name_w, name_h = fredoka_font.getsize(text3)
        name_x = int((inky_display.WIDTH - name_w) / 2)
        name_y = int(y_top + ((y_bottom - y_top - name_h) / 2))
        draw.text((name_x, name_y), text3, inky_display.WHITE, font=fredoka_font)

        # Display the completed name badge

        flipped = img.rotate(180)
        inky_display.set_image(flipped)
        #   inky_display.set_image(img)
        inky_display.show()

        time.sleep(300)





#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#install cron
#*/2 * * * * /usr/bin/python3 /home/pi/Projects/inky/ink_BTC.py --type what --colour red --target usd
#install inky 
#https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat

# python3 ticker.py --type phat --colour yellow --target USD
#git add.
#git commit -m "text"
#git push

# for read-write csv format:
#sudo apt-get install python3-pandas

#check coin api gets values

import requests
import json
import time
import argparse
from subprocess import check_output
import sys
import datetime


from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from font_fredoka_one import FredokaOne
from inky import InkyPHAT, InkyWHAT

qtybtc = 1
qtyeth = 2
qtyada = 3
qtyxio = 4
qtyamp = 5
qtyban = 6
qtyakr = 7
qtyubt = 8
qtyswa = 9
base = 0
basemax = str(round(0, 2))
summemax = str(round(0, 2))
now = datetime.datetime.now() 
nowsav = datetime.datetime.now() 

# Command line arguments to set display type and colour, and enter your name
parser = argparse.ArgumentParser()
parser.add_argument('--type', '-t', type=str, required=True, choices=["what", "phat"], help="type of display")
parser.add_argument('--colour', '-c', type=str, required=True, choices=["white", "black", "yellow"], help="ePaper display colour")
parser.add_argument('--target', '-n', type=str, required=False, help="eur or usd")
args = parser.parse_args()


while True:

        swa = requests.get('https://api.coingecko.com/api/v3/coins/trustswap').json()
        swa = { 'price_usd': swa['market_data']['current_price']['usd'] }
        priceswa = float(swa['price_usd'])

        akr = requests.get('https://api.coingecko.com/api/v3/coins/akropolis').json()
        akr = { 'price_usd': akr['market_data']['current_price']['usd'] }
        priceakr = float(akr['price_usd'])

        ubt = requests.get('https://api.coingecko.com/api/v3/coins/unibright').json()
        ubt = { 'price_usd': ubt['market_data']['current_price']['usd'] }
        priceubt = float(ubt['price_usd'])

        ban = requests.get('https://api.coingecko.com/api/v3/coins/band-protocol').json()
        ban = { 'price_usd': ban['market_data']['current_price']['usd'] }
        priceban = float(ban['price_usd'])

        amp = requests.get('https://api.coingecko.com/api/v3/coins/ampleforth').json()
        amp = { 'price_usd': amp['market_data']['current_price']['usd'] }
        priceamp = float(amp['price_usd'])

        xio = requests.get('https://api.coingecko.com/api/v3/coins/xio').json()
        xio = { 'price_usd': xio['market_data']['current_price']['usd'] }
        pricexio = float(xio['price_usd'])

        ada = requests.get('https://api.coingecko.com/api/v3/coins/cardano').json()
        ada = { 'price_usd': ada['market_data']['current_price']['usd'] }
        priceada = float(ada['price_usd'])

        eth = requests.get('https://api.coingecko.com/api/v3/coins/ethereum').json()
        eth = { 'price_usd': eth['market_data']['current_price']['usd'] }
        priceeth = float(eth['price_usd'])

        btc = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin').json()
        btc = { 'market_cap_usd': btc['market_data']['market_cap']['usd'],
                'price_usd': btc['market_data']['current_price']['usd'] }
        pricebtc = float(btc['price_usd'])


        summe = int(pricebtc*qtybtc + priceeth*qtyeth + priceada*qtyada + pricexio*qtyxio + priceamp*qtyamp + priceban*qtyban + priceubt*qtyubt + priceakr*qtyakr + priceswa*qtyswa)

        base = str(round(summe / pricebtc, 2))
        if (base >= basemax):
                basemax = base
                nowsav = now

        summe = str(round(summe / 1000, 2))

        if (summe >= summemax):
                summemax = summe

        print( pricebtc,priceeth,priceada,priceamp,pricexio,priceban,priceubt,priceakr,summe)
#       if (summe >= base):
#         base = summe

        colour = args.colour

        # Set up the correct display and scaling factors
       if args.type == "phat":
          inky_display = InkyPHAT(colour)
          scale_size = 1
          padding = 0
        elif args.type == "what":
          inky_display = InkyWHAT(colour)
          scale_size = 2.20
          padding = 15

        # inky_display.set_rotation(180)
        inky_display.set_border(inky_display.BLACK)

        # Create a new canvas to draw on

        img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        # Load the fonts

        fredoka_font = ImageFont.truetype(FredokaOne, int(30 * scale_size))
        hanken_bold_font = ImageFont.truetype(HankenGroteskMedium, int(14 * scale_size))
        hanken_medium_font = ImageFont.truetype(HankenGroteskBold, int(30 * scale_size))

            # Grab the text to be displayed
        text1 = " "
        text1 = nowsav.strftime("%Y-%m-%d %H:%M")
        text2 =  str(base) + " - " + str(basemax)
        text22 = " "
        text3 =  str(summe) + " - " + str(summemax)

     # Top and bottom y-coordinates for the white strip

        y_top = int(inky_display.HEIGHT * (5.0 / 10.0))
        y_bottom = y_top + int(inky_display.HEIGHT * (4.0 / 10.0))

        # Draw the red, white, and red strips

        for y in range(0, y_top):
          for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.YELLOW)

        for y in range(y_top, y_bottom):
          for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.BLACK)

        for y in range(y_bottom, inky_display.HEIGHT):
          for x in range(0, inky_display.width):
            img.putpixel((x, y), inky_display.RED)

        # Calculate the positioning and draw the 1st text

        row1_w, row1_h = hanken_bold_font.getsize(text1)
        row1_x = int((inky_display.WIDTH - row1_w) / 2)
        row1_y = 0 + padding
        draw.text((row1_x, row1_y), text1, inky_display.BLACK, font=hanken_bold_font)
        # Calculate the positioning and draw the 2nd texts

        text2_w, text2_h = hanken_medium_font.getsize(text2)
        text2_x = int((inky_display.WIDTH - text2_w) / 2)
        text2_y = row1_h + (2 * padding)
        draw.text((text2_x, text2_y), text2, inky_display.BLACK, font=fredoka_font)

        text22_w, text22_h = hanken_medium_font.getsize(text22)
        text22_x = int((inky_display.WIDTH - text22_w) / 2)
        text22_y = text2_y + text2_h - padding
        draw.text((text22_x, text22_y), text22, inky_display.WHITE, font=fredoka_font)

        # Calculate the positioning and draw the 3rd text

        name_w, name_h = fredoka_font.getsize(text3)
        name_x = int((inky_display.WIDTH - name_w) / 2)
        name_y = int(y_top + ((y_bottom - y_top - name_h) / 2))
        draw.text((name_x, name_y), text3, inky_display.WHITE, font=fredoka_font)

        # Display the completed name badge

        flipped = img.rotate(180)
        inky_display.set_image(flipped)
        #   inky_display.set_image(img)
        inky_display.show()

        time.sleep(180)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import requests
import time
import sys
import datetime
import csv

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from font_fredoka_one import FredokaOne
from inky import InkyPHAT, InkyWHAT

pricebtc = 0
base = 0
summe = 0
now = datetime.datetime.now()

df = pd.read_csv('portfolio.csv', delimiter=';', names = ['Coin', 'Qty'])
tf = pd.read_csv('ConfigCryptoDashboard.csv', delimiter=';', names = ['Name', 'Value', 'Zeit'])
for i in range(len(tf)) :
	if tf.loc[i,"Name"] == "summemax":
		summemax = float(tf.loc[i,"Value"])
		summemaxtime = str(tf.loc[i,"Zeit"])
	if tf.loc[i,"Name"] == "basemax":
		basemax = float(tf.loc[i,"Value"])
		basemaxtime = str(tf.loc[i,"Zeit"])

displaytype = "phat"
# Set up the correct display and scaling factors
if displaytype == "phat":
	inky_display = InkyPHAT("yellow")
	scale_size = 1
	padding = 0
elif displaytype == "what":
	inky_display = InkyWHAT("yellow")
	scale_size = 2.20
	padding = 15

# Load the fonts
small_font  = ImageFont.truetype(FredokaOne, int(10 * scale_size))
medium_font = ImageFont.truetype(HankenGroteskMedium, int(14 * scale_size))
large_font  = ImageFont.truetype(HankenGroteskBold, int(30 * scale_size))

# inky_display.set_rotation(180)
inky_display.set_border(inky_display.BLACK)

# Create a new canvas to draw on
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

while True:
	try:
		for i in range(len(df)) :
			qtycoin = float(df.loc[i,"Qty"])
			ren = requests.get('https://api.coingecko.com/api/v3/coins/' + df.loc[i,"Coin"]).json()
			ren = { 'price_usd': ren['market_data']['current_price']['usd'] }
			pricecoin = float(ren['price_usd'])
			summe = summe + qtycoin * pricecoin
	#		print (qtycoin,pricecoin,summe)
			if df.loc[i,"Coin"] == "bitcoin":
				pricebtc = pricecoin
	except:
		print("Error reading Coin URL", df.loc[i,"Coin"])

	base = float(round(summe / pricebtc, 2))

	if (base > basemax):
		with open('ConfigCryptoDashboard.csv', 'w', newline='') as csvfile:
			basemaxtime = datetime.datetime.now()
			savwriter = csv.writer(csvfile, delimiter=';')
			text2=["basemax"] + [basemax] + [basemaxtime]
			savwriter.writerow(text2)
			text2=["summemax"] + [summemax] + [summemaxtime]
			savwriter.writerow(text2)
		basemax = base

	summe = summe / 1000

	if (summe > summemax):
		summemaxtime = datetime.datetime.now()
		with open('ConfigCryptoDashboard.csv', 'w', newline='') as csvfile:
			savwriter = csv.writer(csvfile, delimiter=';')
			text2=["summemax"] + [summemax] + [summemaxtime]
			savwriter.writerow(text2)
			text2=["basemax"] + [basemax] + [basemaxtime]
			savwriter.writerow(text2)
		summemax = summe

	summemaxprint = str(round(summemax,2))
	summeprint    = str(round(summe,2))
	basemaxprint  = str(basemax)
	baseprint     = str(base)
	print(summeprint)
	summe = 0

	# Grab the text to be displayed
	text1 = str(basemaxtime) #.strftime("%Y-%m-%d %H:%M")
	text2 =  str(baseprint) + " - " + str(basemaxprint)
	text3 = " "
#	text3 = str(summemaxtime)
	text4 = str(summeprint) + " - " + str(summemaxprint)

	# Top and bottom y-coordinates for rowbackground
	y_top = int(inky_display.HEIGHT * (5.0 / 10.0))
	y_bottom = y_top + int(inky_display.HEIGHT * (5.0 / 10.0))

	# Draw the red, white, and red strips

	for y in range(0, y_top):
	  for x in range(0, inky_display.width):
	    img.putpixel((x, y), inky_display.YELLOW)

	for y in range(y_top, y_bottom):
	  for x in range(0, inky_display.width):
	    img.putpixel((x, y), inky_display.BLACK)

#	for y in range(y_bottom, inky_display.HEIGHT):
#	  for x in range(0, inky_display.width):
#	    img.putpixel((x, y), inky_display.RED)

	# Calculate the positioning and draw the 1st row
	row1_w, row1_h = medium_font.getsize(text1)
	row1_x = int((inky_display.WIDTH - row1_w) / 2)
	row1_y = 0 + padding
	draw.text((row1_x, row1_y), text1, inky_display.BLACK, font=medium_font)

	# Calculate the positioning and draw the 2nd row
	row2_w, row2_h = large_font.getsize(text2)
	row2_x = int((inky_display.WIDTH - row2_w) / 2)
	row2_y = row1_h + (2 * padding)
	draw.text((row2_x, row2_y), text2, inky_display.WHITE, font=large_font)


	# Calculate the positioning and draw the 3rd row
	row3_w, row3_h = small_font.getsize(text3)
	row3_x = int((inky_display.WIDTH - row3_w) / 2)
	row3_y = row2_y + row2_h - padding
	draw.text((row3_x, row3_y), text3, inky_display.WHITE, font=small_font)

	# Calculate the positioning and draw the 4th row
	row4_w, row4_h = large_font.getsize(text4)
	row4_x = int((inky_display.WIDTH - row4_w) / 2)
	row4_y = int(y_top + ((y_bottom - y_top - row4_h) / 2))
	draw.text((row4_x, row4_y), text4, inky_display.WHITE, font=large_font)


	# Display the completed name badge

	flipped = img.rotate(180)
	inky_display.set_image(flipped)
	#   inky_display.set_image(img)
	inky_display.show()

	time.sleep(300)
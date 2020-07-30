#!/usr/bin/env python

#install cron
#*/2 * * * * /usr/bin/python3 /home/pi/Projects/inky/ink_BTC.py --type what --colour red --target usd

import argparse
import json
from subprocess import check_output
import sys
#import pprint
import datetime
import time


from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from font_fredoka_one import FredokaOne
from inky import InkyPHAT, InkyWHAT

while True:
	#see doc at https://www.cryptonator.com/api
	url = "https://api.cryptonator.com/api/ticker/"
	#Base - Base currency code
	base = "amp"
	# Target - Target currency code
	target = "usd"

	# Command line arguments to set display type and colour, and enter your name
	parser = argparse.ArgumentParser()
	parser.add_argument('--type', '-t', type=str, required=True, choices=["what", "phat"], help="type of display")
	parser.add_argument('--colour', '-c', type=str, required=True, choices=["white", "black", "yellow"], help="ePaper display colour")
	parser.add_argument('--target', '-n', type=str, required=False, help="eur or usd")
	args = parser.parse_args()

	if args.target is not None:
		target = args.target


	url = url + base + "-" + target

	print("reading: " + url)
    output = check_output(['/usr/bin/curl', url])
    #print(output)

    now = datetime.datetime.now() 

    #response = urlopen(url)
    #data = response.read()
    values = json.loads(output.decode('utf-8'))
    price = float(values['ticker']['price'])
    print("retrieved: " + str(price))

    #sys.exit("Oy!")

    #install fonts using
    #sudo python3 -m pip install font-hanken-grotesk

#   from PIL import Image, ImageFont, ImageDraw
#   from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
#   from font_intuitive import Intuitive
#   from font_fredoka_one import FredokaOne
#   from inky import InkyPHAT, InkyWHAT

    #print("""Inky pHAT/wHAT: Hello... my name is:
    #Use Inky pHAT/wHAT as a personalised name badge!
    #""")

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
    #text1 = now.strftime("%Y-%m-%d %H:%M")
    text2 = "1 " + base.upper()
    text22 = " "
    text3 = target.upper() + " " + str(price)

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
    text2_y = hello_h + (2 * padding)
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

    time.sleep(60)


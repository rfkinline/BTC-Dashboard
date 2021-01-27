#!/bin/sh
# turn off screensaver then check settings
# launcher.sh
# navigate to home directory, then to this dir, then exec py script, then back home

sudo xset s off
sudo xset -dpms
sudo xset q
cd /
cd home/pi/BTC-Dashboard
sudo python3 BTCDashboard.py
cd /

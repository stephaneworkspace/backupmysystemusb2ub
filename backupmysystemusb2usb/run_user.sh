#!/bin/bash
# Author: Stéphane Bressani <s.bressani@bluewin.ch>
# Backup usb 2 usb with same size complete
export DISPLAY=${DISPLAY:-":0"}
/usr/bin/gnome-screensaver-command
cd /hom/stephane/Code/Python/backupmysystemusb2usb/
/usr/bin/python3 /home/stephane/Code/Python/backupmysystemusb2usb/run_user.py

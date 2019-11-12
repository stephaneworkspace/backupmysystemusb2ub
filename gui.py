#!/usr/bin/env python3
"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import sys
import yaml
from backupmysystemusb2usb.usb2usb import usb2usb
try:
    u2u = usb2usb(sys.argv[1])
    u2u.gui()
except yaml.YAMLError:
    exit()

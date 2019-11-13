#!/usr/bin/env python3
"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import sys
import yaml
from backupmysystemusb2usb.usb2usb import usb2usb
CONFIG_FILE = 'config.yml'
try:
    if (len(sys.argv) - 1) > 0:
        config_file = sys.argv[1]
    else:
        config_file = CONFIG_FILE
    u2u = usb2usb(config_file)
    u2u.backup()
except yaml.YAMLError:
    exit()

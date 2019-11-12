#!/usr/bin/env python3
"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from __future__ import print_function
import time
from backupmysystemusb2usb.backup_system import backup_system
from backupmysystemusb2usb import const

REFRESH_SEC = .1

print(const.TTY_U_1)
print('')
print(const.TTY_U_2)
print(const.TTY_U_3)
print(const.TTY_U_4)
print('')

print(const.TTY_YML_TRY)
bs = backup_system()
if bs.status is False:
    print(const.TTY_YML_FAILED)
    print(bs.error)
    exit()
print(const.TTY_YML_SUCCESS)
print('')

last_value = ''
while 1:
    time.sleep(REFRESH_SEC)
    try:
        log_file = open(bs.data[const.YML_TEMP_LOG], "r")
        arr_file = log_file.readlines()
        if len(arr_file) > 0 :
            value = arr_file[len(arr_file) - 1]
        else
            value = ''
        if last_value == '':
            last_value = value
            print(value, end='')
        elif not last_value == value:
            last_value = value
            print(value, end='')
        log_file.close()
    except IOError:
        pass

"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from __future__ import print_function
import time
from backupsystemusb2usb import const

FILE_NAME = '/home/stephane/Temp/output.log'
REFRESH_SEC = .1

print(const.TTY_U_1)
print('')
print(const.TTY_U_2)
print(const.TTY_U_3)
print(const.TTY_U_3)
print('')
last_value = ''
while 1:
    time.sleep(REFRESH_SEC)
    try:
        log_file = open(FILE_NAME, "r")
        arr_file = log_file.readlines()
        value = arr_file[len(arr_file) - 1]
        if last_value == '':
            last_value = value
            print(value, end='')
        elif not last_value == value:
            last_value = value
            print(value, end='')
        log_file.close()
    except IOError:
        pass

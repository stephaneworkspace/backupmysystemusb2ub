#!/bin/bash
# Author: Stéphane Bressani <s.bressani@bluewin.ch>
# Backup usb 2 usb with same size complete
cd /home/stephane/Code/Python/backupmysystemusb2usb/
rm /home/stephane/Temp/BackupMySytem-Temp.log
touch /home/stephane/Temp/BackupMySytem-Temp.log
/usr/bin/python3 /home/stephane/Code/Python/backupmysystemusb2usb/run.py > /home/stephane/Temp/BackupMySytem-Temp.log

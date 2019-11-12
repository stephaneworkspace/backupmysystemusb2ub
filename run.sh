#!/bin/bash
# Author: Stéphane Bressani <s.bressani@bluewin.ch>
# Backup usb 2 usb with the same size complete
cd /home/stephane/Code/Python/backupmysystemusb2usb/
rm /home/stephane/Temp/BackupMySytem-Temp.log
touch /home/stephane/Temp/BackupMySytem-Temp.log
/home/stephane/Code/Python/backupmysystemusb2usb/run.py > /home/stephane/Temp/BackupMySytem-Temp.log

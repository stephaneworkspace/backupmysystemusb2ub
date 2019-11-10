#!/bin/bash
# Author: Stéphane Bressani <s.bressani@bluewin.ch>
# Backup usb 2 usb same size complete
# The param is the UUID of usb key (after a backup is the same,
# this application work with LABEL with the date of the system
#
# For UUID -> sudo blkid
python3 run.py "790d1fbb-96ed-46c3-868d-08e05e223fa7"

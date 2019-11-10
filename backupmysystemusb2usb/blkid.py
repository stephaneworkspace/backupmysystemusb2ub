"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import subprocess
from . import const

UUID = const.UUID
DEVICE = const.DEVICE


class blkid:
    def __init__(self, uuid_source, uuid_copy):
        self.source = {}
        self.copy = {}
        self.source[UUID] = uuid_source
        self.copy[UUID] = uuid_copy
        self.__compute()

    def __compute(self):
        global BLKIDOUTPUT
        cmd = subprocess.Popen("sudo blkid", stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, shell=True)
        BLKIDOUTPUT = cmd.communicate()[0]
        print(BLKIDOUTPUT)

        self.source[DEVICE] = '/dev/sda/'

    def same_label_and_uuid(self):
        return False

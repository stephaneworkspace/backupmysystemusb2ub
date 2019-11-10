"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import subprocess
import re
from . import const

UUID = const.UUID
DEVICE = const.DEVICE
LABEL = const.LABEL


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
        array = str(BLKIDOUTPUT.decode('UTF-8')).split('\n')
        print(array)
        print(' ')
        blkid_list = []
        for i, a in enumerate(array):
            # Create dict only if device detected
            pattern = '\\/dev\\/sd([a-z]+)'
            if not re.search(pattern, a) is None:
                for f in re.findall(pattern, a):
                    blkid_list.append(i)
                    blkid_list[i] = {}
                    blkid_list[i][DEVICE] = '/dev/sd' + f
            else:
                continue
            pattern = '(?<= UUID=")([^"]*)'
            if not re.search(pattern, a) is None:
                for f in re.findall(pattern, a):
                    blkid_list[i][UUID] = f
            else:
                blkid_list[i][UUID] = None
            pattern = '(?<=LABEL=")([^"]*)'
            if not re.search(pattern, a) is None:
                for f in re.findall(pattern, a):
                    blkid_list[i][LABEL] = f
            else:
                blkid_list[i][LABEL] = None

        for b in blkid_list:
            print(b)

    def same_label_and_uuid(self):
        return False

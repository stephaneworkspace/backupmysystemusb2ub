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
PARTITION = const.PARTITION
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
            pattern = '\\/dev\\/sd([a-z][0-9]+)'
            if not re.search(pattern, a) is None:
                for f in re.findall(pattern, a):
                    blkid_list[i][PARTITION] = '/dev/sd' + f
            else:
                blkid_list[i][PARTITION] = None
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

        blkid_l_g = []
        i = -1
        for b in blkid_list:
            if i > 0:
                if blkid_l_g[i][DEVICE] == b[DEVICE]:
                    j = len(blkid_l_g[i]) + 1
                    blkid_l_g[i][j] = {}
                    blkid_l_g[i][j][PARTITION] = b[PARTITION]
                    continue
            i += 1
            blkid_l_g.append(i)
            blkid_l_g[i] = {}
            blkid_l_g[i][DEVICE] = b[DEVICE]
            blkid_l_g[i][0] = {}
            blkid_l_g[i][0][PARTITION] = b[PARTITION]

        for b in blkid_l_g:
            print(b)

    def same_label_and_uuid(self):
        return False

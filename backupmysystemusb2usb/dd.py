"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>

https://stackoverflow.com/questions/7581710/python-subprocess-dd-and-stdout ->
to do
"""
from __future__ import print_function
import re
import signal
import time
from subprocess import Popen, PIPE, CalledProcessError
from . import const

UUID = const.UUID
DEVICE = const.DEVICE
ROOT = 'root'
REFRESH = ['pkill', '--uid', ROOT, '--signal', 'SIGUSR1', '^dd$']
REFRESH_SEC = 30


class dd:
    def __init__(self, blkid, img_path):
        self.blkid = blkid
        self.img_path = img_path

    def copy_master_to_img(self):
        """
        Copy master to img
        """
        x = 'sudo dd if=%s of=%s bs=4M'
        try:
            cmd_list = ['sudo', 'dd', 'if=' + self.blkid.master[DEVICE], 'of='
                        + self.img_path, 'bs=4M']
            self.__cmd(cmd_list)
        except CalledProcessError:
            print('Error in dd (Destroy disk ?) in the copy of master to img')
            xx = x % (self.blkid.master[DEVICE], self.img_path)
            print('Command: %s' % (xx))

    def copy_img_to_slave(self):
        """
        Copy img to slave
        """
        x = 'sudo dd if=%s of=%s bs=4m'
        try:
            cmd_list = ['sudo', 'dd', 'if=' + self.img_path, 'of=' +
                        self.blkid.slave[DEVICE], 'bs=4M']
            self.__cmd(cmd_list)
        except CalledProcessError:
            print('Error in dd (Destroy disk ?) in the copy of img to slave')
            xx = x % (self.img_path, self.blkid.slave[DEVICE])
            print('Command: %s' % (xx))

    def __cmd(self, cmd_list):
        try:
            cmd = Popen(cmd_list, stderr=PIPE)
            while cmd.poll() is None:
                time.sleep(REFRESH_SEC)
                Popen(REFRESH)
                cmd.send_signal(signal.SIGUSR1)
                while 1:
                    output = bytes(cmd.stderr.readline()).decode('utf-8')
                    for o in output.split('\r'):
                        pattern = r'\b(?:MB|GB|TB)\b'
                        if re.search(pattern, o):
                            print(o, end='')
                    break
            print(cmd.stderr.read())
        except CalledProcessError:
            print('Error in dd')

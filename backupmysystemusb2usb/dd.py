"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import subprocess
from subprocess import CalledProcessError
from . import const

UUID = const.UUID
DEVICE = const.DEVICE


class dd:
    def __init__(self, blkid, img_path):
        self.blkid = blkid
        self.img_path = img_path

    def copy_master_to_img(self):
        """
        Copy master to img
        """
        global DDOUTPUT1
        x = 'sudo dd if=%s of=%s bs=4M'
        try:
            cmd = subprocess.Popen(x % (self.blkid.master[DEVICE],
                                        self.img_path))
            DDOUTPUT1 = cmd.communicate()[0]
            print(DDOUTPUT1)
        except CalledProcessError:
            print('Error in dd (Destroy disk ?) in the copy of master to img')
            xx = x % (self.blkid.master[DEVICE], self.img_path)
            print('Command: %s' % (xx))

    def copy_img_to_slave(self):
        """
        Copy img to slave
        """
        global DDOUTPUT2
        x = 'sudo dd if=%s of=%s bs=4m'
        try:
            cmd = subprocess.Popen(x % (self.img_path,
                                        self.blkid.slave[DEVICE]))
            DDOUTPUT2 = cmd.communicate()[0]
            print(DDOUTPUT2)
        except CalledProcessError:
            print('Error in dd (Destroy disk ?) in the copy of img to slave')
            xx = x % (self.img_path, self.blkid.slave[DEVICE])
            print('Command: %s' % (xx))

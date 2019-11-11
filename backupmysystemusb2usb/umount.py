"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import Popen, CalledProcessError
from . import const

DEVICE = const.DEVICE


class umount:
    def __init__(self, blkid):
        self.blkid = blkid
        self.__umount()

    def __umount(self):
        """
        Umount disks
        """
        print(TTY_UMOUNT % (self.blkid.master[DEVICE],
                            self.blkid.slave[DEVICE]))
        x = 'sudo umount %s'
        try:
            xx = x % (self.blkid.master[DEVICE])
            cmd_list = ['sudo', 'umount', self.blkid.master[DEVICE]]
            cmd = Popen(cmd_list)
            cmd.wait()
            xx = x % (self.blkid.slave[DEVICE])
            cmd_list = ['sudo', 'umount', self.blkid.slave[DEVICE]]
            cmd = Popen(cmd_list)
            cmd.wait()
        except CalledProcessError:
            print(ERR_UMOUNT)
            print(ERR_CMD % (xx))

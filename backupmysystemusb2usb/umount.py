"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import Popen, CalledProcessError
from . import const

DEVICE = const.DEVICE


class umount:
    def __init__(self, blkid):
        self.blkid = blkid
        self.__unmount()

    def __umount(self):
        """
        Umount disks
        """
        global DDOUTPUT1
        global DDOUTPUT2
        print('umount %s and %s' % (self.blkid.master[DEVICE],
                                    self.blkid.slave[DEVICE]))
        x = 'sudo umount %s'
        try:
            xx = x % (self.blkid.master[DEVICE])
            # cmd = subprocess.Popen(x % (self.blkid.master[DEVICE]))
            cmd_list = ['sudo', 'umount', self.blkid.master[DEVICE] + '1']
            cmd = Popen(cmd_list)
            cmd.wait()
            DDOUTPUT1 = cmd.communicate()[0]
            print(xx)
            print(DDOUTPUT1)
            xx = x % (self.blkid.slave[DEVICE])
            # cmd = subprocess.Popen(x % (self.blkid.slave[DEVICE]))
            cmd_list = ['sudo', 'umount', self.blkid.slave[DEVICE] + '1']
            cmd = Popen(cmd_list)
            cmd.wait()
            DDOUTPUT2 = cmd.communicate()[0]
            print(xx)
            print(DDOUTPUT2)
        except CalledProcessError:
            print('Error in sudo umount')
            print('Command: %s' % (xx))

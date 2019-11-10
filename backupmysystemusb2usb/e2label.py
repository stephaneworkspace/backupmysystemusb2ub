"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import subprocess, CalledProcessError
from . import const

UUID = const.UUID
DEVICE = const.DEVICE


class e2label:
    def __init__(self, blkid):
        self.blkid = blkid

    def write_time_stamp_label_to_master(self):
        """
        Write time stamp label to master
        """
        from datetime import datetime
        now = datetime.now()
        dt_string = now.strftime('%Y%m%d%H%M%S')
        print('New timestamp for master "%s"' % (dt_string))
        x = 'sudo e2label %s1 "%s"'
        try:
            cmd = subprocess.Popen(x % (self.blkid.master[DEVICE], dt_string))
            DDOUTPUT = cmd.communicate()[0]
            print(DDOUTPUT)
        except CalledProcessError:
            print('Error in sudo e2label')
            print('Command: %s' % (x))

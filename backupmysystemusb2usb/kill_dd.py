"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import Popen, CalledProcessError


class kill_dd:
    def run(self):
        """
        Run sudo killall -9 dd
        """
        x = ['sudo', 'killall', '-9', 'dd']
        try:
            cmd_list = x
            cmd = Popen(cmd_list)
            cmd.wait()
        except CalledProcessError:
            print('Error in sudo killall -9 dd')

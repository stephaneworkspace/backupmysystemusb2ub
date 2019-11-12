"""
    This software is a part of backupmysystemusb2usb and its functionality is
    to backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""


class print_log:
    def __init__(self, log_file):
        self.log_file = log_file

    def add_log(self, message):
        """
        Print to the console and to the temporary file
        """
        print(message)
        try:
            log = open(self.log_file, 'a')
            log.write(message)
            log.write('\n')
            log.close()
        except IOError:
            pass

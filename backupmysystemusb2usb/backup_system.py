"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import yaml


class backup_system:
    def __init__(self):
        with open('config.yml', 'r') as stream:
            try:
                self.status = True
                self.data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                self.status = False
                self.error = exc

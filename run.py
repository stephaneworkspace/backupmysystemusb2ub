"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import sys
from backupmysystemusb2usb.backup_system import backup_system
from backupmysystemusb2usb.blkid import blkid


UUID = sys.argv[1]

print('Backup Usb To Usb')
print('UUID : %s' % (UUID))

print('Try to open config.yml')
bs = backup_system()
if bs.status is False:
    print(bs.error)
else:
    print(bs.success)

# If same uuid and same label, failed
b = blkid(UUID, UUID)
if b.same_label_and_uuid():
    print('Same label and UUID -> No copy is posible')
    exit()

"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import sys
from backupmysystemusb2usb.backup_system import backup_system
from backupmysystemusb2usb.blkid import blkid
from backupmysystemusb2usb import const

UUID = sys.argv[1]

print('Backup Usb To Usb')
print('UUID : %s' % (UUID))

print('Try to open config.yml')
bs = backup_system()
if bs.status is False:
    print('Open failed')
    print(bs.error)
    exit()
print('Open with success')
print('')
print('Variables used:')
for key in bs.data:
    print('%s: %s' % (key, bs.data[key]))
# If same uuid and same label, failed
UUID_1_MASTER = bs.data[const.YML_UUID_1_MASTER]
UUID_1_SLAVE = bs.data[const.YML_UUID_1_SLAVE]
try:
    b = blkid(UUID_1_MASTER, UUID_1_SLAVE)
except Exception:
    exit()
if b.same_label_and_uuid():
    print('Same label and UUID -> No copy is posible')
    exit()

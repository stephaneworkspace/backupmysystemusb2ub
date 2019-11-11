"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import sys
from subprocess import CalledProcessError
from backupmysystemusb2usb.backup_system import backup_system
from backupmysystemusb2usb.blkid import blkid
from backupmysystemusb2usb.dd import dd
from backupmysystemusb2usb.e2label import e2label
from backupmysystemusb2usb.kill_dd import kill_dd
from backupmysystemusb2usb.unmount import unmount
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
except CalledProcessError as error:
    print(error)
    exit()
except Exception:
    exit()
print('')
print('Master: %s' % (b.master))
print('Slave: %s' % (b.slave))
print('')
print('Copy master to img...')
try:
    if bs.data[const.YML_KILL_DD]:
        k = kill_dd()
        k.run()
    d = dd(b, bs.data[const.YML_TEMP_IMG])
    d.copy_master_to_img()
    print('')
    print('Copy succefull !')
    print('')
    print('Copy to slave device now (this take the same time as before...)')
    d.copy_img_to_slave()
    print('')
    print('Writing label on master upper than slave with timespan')
    e = e2label(b)
    e.write_time_stamp_label_to_master()
    print('')
    u = unmount(b)
    print('All ok')
except IOError as error:
    print(error)
    exit()
except CalledProcessError as error:
    print(error)
    exit()

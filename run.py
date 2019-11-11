"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
from subprocess import CalledProcessError
from backupmysystemusb2usb.backup_system import backup_system
from backupmysystemusb2usb.blkid import blkid
from backupmysystemusb2usb.dd import dd
from backupmysystemusb2usb.e2label import e2label
from backupmysystemusb2usb.kill_dd import kill_dd
from backupmysystemusb2usb.umount import umount
from backupmysystemusb2usb import const

print('Backup usb key to usb key')

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
# If same UUID and same label, failed
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
try:
    u = umount(b)
    if bs.data[const.YML_KILL_DD]:
        k = kill_dd()
        k.run()
        print('')
    print('Copy master to img...')
    print('')
    d = dd(b, bs.data[const.YML_TEMP_IMG])
    d.copy_master_to_img()
    print('')
    print('Copy successfull !')
    print('')
    print('Copy img to slave device now...')
    print('')
    d.copy_img_to_slave()
    print('')
    print('Copy successfull !')
    print('')
    print('Writing label on master upper than slave with timespan')
    e = e2label(b)
    e.write_time_stamp_label_to_master()
    print('')
    u = umount(b)
    print('All ok')
except IOError as error:
    print(error)
    exit()
except CalledProcessError as error:
    print(error)
    exit()

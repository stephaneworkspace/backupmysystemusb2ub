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

print(const.TTY_INTRO)
print('')

print(const.TTY_YML_TRY)
bs = backup_system()
if bs.status is False:
    print(const.TTY_YML_FAILED)
    print(bs.error)
    exit()
print(const.TTY_YML_SUCCESS)
print('')
print(const.TTY_YML_VARIABLES_USED)
for key in bs.data:
    print(const.TTY_YML_VARIABLE % (key, bs.data[key]))

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
print(const.TTY_MASTER % (b.master))
print(const.TTY_SLAVE % (b.slave))
print('')

try:
    u = umount(b)
    if bs.data[const.YML_KILL_DD]:
        k = kill_dd()
        k.run()
        print('')
    d = dd(b, bs.data[const.YML_TEMP_IMG])
    d.copy_master_to_img()
    d.copy_img_to_slave()
    e = e2label(b)
    e.write_time_stamp_label_to_master()
    print('')
    print(const.TTY_ALL_OK)
except IOError as error:
    print(error)
    exit()
except CalledProcessError as error:
    print(error)
    exit()

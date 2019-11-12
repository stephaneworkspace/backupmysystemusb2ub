#!/usr/bin/env python3
"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import os
import sys
from subprocess import CalledProcessError
from backupmysystemusb2usb.backup_system import backup_system
from backupmysystemusb2usb.blkid import blkid
from backupmysystemusb2usb.dd import dd
from backupmysystemusb2usb.e2label import e2label
from backupmysystemusb2usb.print_log import print_log
from backupmysystemusb2usb.kill_dd import kill_dd
from backupmysystemusb2usb.umount import umount
from backupmysystemusb2usb import const
# Loading Yaml
print(const.TTY_YML_TRY)
bs = backup_system(sys.argv[0])
if bs.status is False:
    print(const.TTY_YML_FAILED)
    print(bs.error)
    exit()
LOG = bs.data[const.YML_TEMP_LOG]

# Log remove
os.remove(LOG)
try:
    log = open(LOG, 'w')
    log.write('')
except IOError:
    pass
log = print_log(LOG)
log.add_log(const.TTY_INTRO)
log.add_log('')
log.add_log(const.TTY_YML_SUCCESS)
log.add_log('')
log.add_log(const.TTY_YML_VARIABLES_USED)
for key in bs.data:
    log.add_log(const.TTY_YML_VARIABLE % (key, bs.data[key]))

# If same UUID and same label, failed
UUID_1_MASTER = bs.data[const.YML_UUID_1_MASTER]
UUID_1_SLAVE = bs.data[const.YML_UUID_1_SLAVE]
try:
    b = blkid(UUID_1_MASTER, UUID_1_SLAVE, log)
except CalledProcessError as error:
    log.add_log(error)
    exit()
except Exception:
    exit()
log.add_log('')
log.add_log(const.TTY_MASTER % (b.master))
log.add_log(const.TTY_SLAVE % (b.slave))
log.add_log('')

try:
    u = umount(b, log)
    if bs.data[const.YML_KILL_DD]:
        k = kill_dd(log)
        k.run()
        log.add_log('')
    d = dd(b, bs.data[const.YML_TEMP_IMG], log)
    d.copy_master_to_img()
    d.copy_img_to_slave()
    e = e2label(b, log)
    e.write_time_stamp_label_to_master()
    log.add_log('')
    log.add_log(const.TTY_ALL_OK)
except IOError as error:
    log.add_log(error)
    exit()
except CalledProcessError as error:
    log.add_log(error)
    exit()

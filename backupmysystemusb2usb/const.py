"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with the same sapce disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
DEVICE = 'device'
PARTITION = 'partiton'
LABEL = 'label'
UUID = 'UUID'

YML_UUID_1_MASTER = 'UUID_1_Master'
YML_UUID_1_SLAVE = 'UUID_1_Slave'
YML_TEMP_IMG = 'Temp_img'
YML_KILL_DD = 'Kill_dd'

YYYYMMDDHHMMSS = 'YYYYMMddHHMMSS'

ERR_COUNT = 'Count error'
ERR_RENAME1 = 'rename with `sudo e2label /dev/sd_1 "YYYYMMddHHMMSS"`'
ERR_RENAME2 = 'with slave in past and master in present'
ERR_SAME_LABEL = 'Same label, %s %s' % (ERR_RENAME1, ERR_RENAME2)
ERR_UNKNOW_LABEL = 'The label on device is unknow, %s %s' % (ERR_RENAME1,
                                                             ERR_RENAME2)
ERR_CMD = 'Command: %s'
ERR_BLKID_COMPUTE = 'Error in sudo blkid'
ERR_BLKID_NO_OPERATION_IF = 'No operation if the count is not = 2 (count = %s)'
ERR_DD_CMTI = 'Error in dd (destroy disk ?) in the copy of master to img'
ERR_DD_CITS = 'Error in dd (destroy disk ?) in the copy of img to slave'
ERR_CMD_DD = 'Error in dd'
ERR_E2LABEL_WTSLTM = 'Error in sudo e2label'
ERR_KILL_DD = 'Error in sudo killall -9 dd'
ERR_UMOUNT = 'Error in sudo umount'

TTY_BLKID_DEVICE_LIST = 'Device(s) list:'
TTY_BLKID_DEVICE_LIST_MATCH = 'Device(s) list match with config (count = %s)'
TTY_E2LABEL_WTSLTM = 'New timestamp for master "%s"'
TTY_UMOUNT = 'Umount %s and %s:'

"""
    This software is a part of backupmystemusb2usb and its functionality is to
    backup one usb key to another usb with same sapce disk
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
ERR_RENAME2 = 'with slave in past and master in presant'
ERR_SAME_LABEL = 'Same label, %s %s' % (ERR_RENAME1, ERR_RENAME2)
ERR_UNKNOW_LABEL = 'The label on device is unknow, %s %s' % (ERR_RENAME1,
                                                             ERR_RENAME2)

backupmystemusb2usb: Backup my system usb to usb
================================================

backupmystemusb2usb is a GPLv3-liscensed Python package for copy usb key.

Its runs on Python 3.7 and has a dependency for yaml, and another one for the gui.

Installation without the source
-------------------------------

To install *backupmystemusb2usb* package run the following command:

.. code-block:: bash

   sudo apt-get install libyaml-dev python3-gi
   sudo -H pip3 install backupmystemusb2usb

You have to create a config.yml file

.. code-block:: bash
   
   UUID_1_Master: 790d1fbb-96ed-46c3-868d-08e05e223fa7
   UUID_1_Slave: 790d1fbb-96ed-46c3-868d-08e05e223fa7
   Temp_img: /home/stephane/Temp/Linux.img
   Temp_log: /home/stephane/Temp/BackupMySystem-Temp.log
   Kill_dd: True

UUID list

.. code-block:: bash
   
   sudo blkid

Find your device and for change the label. If the device master UUID is the same as the slave UUID (if you cancel in copy img to slave), you have to put a date upper on master than slave

*Warning* UUID is not Label !

.. code-block:: bash

   sudo e2label /dev/sd_1 "19991231235959"
   
For the deamon, write a *run.py* for running by user root with chmod 700

.. code-block:: bash

   #!/usr/bin/env python3
   import sys
   import yaml
   from backupmystemusb2usb.usb2usb import usb2usb
   try:
      u2u = usb2usb(sys.argv[1])
      u2u.backup()
   except yaml.YAMLError:
      exit()

You can create a service systemd if you planed to backup your usb key evry day in the morning. You can wakeonlan from a raspberrypi or other technique

.. code-block:: bash

   wakeonlan MACADRESS
   crontab -e
   # write your cron
   sudo service cron reload

Now for create a daemon in startup (without console)

.. code-block:: bash

   cd /etc/systemd/system
   vi backupmysytemusb2usb.service

Write
   
.. code-block:: bash

   [Unit]
   After=ssh.service

   [Service]
   WorkingDirectory=/your/working/path/
   ExecStart=/usr/bin/sh -c "/your/working/path/run.py /your/working/path/config.yml"

   [Install]
   WantedBy=default.target

Enable and start

.. code-block:: bash
   
   sudo systemctl daemon-reload
   sudo systemctl enabled backupmysytemusb2usb

Then the service start on reboot.
If you will test now the service :

.. code-block:: bash

   sudo systemctl start backupmysytemusb2usb

Check the log (no detail just the command like dd)

.. code-block:: bash

   sudo journalctl --unit backupmysystemusb2usb -n 20

You can go to check your ouput log file configured by config.yml
   
Now we have to create the shell return for no-root user

.. code-block:: bash

   WORK IN PROGRESS FOR THE X11 GTK INTERFACE...

You can have the display of progress with run_user.py and run_user.sh in my github (modifiy the path for config.yml)

You can create a Gnome desktop startup

.. code-block:: bash

   cd ~/.config/autostart
   touch backupmysytemusb2usb.desktop
   chmod 744
   vi backupmysytemusb2usb.desktop

And in your editor enter

.. code-block:: bash

   [Desktop Entry]
   Name=Backup my system usb to usb
   Comment=Copy disk with the same space
   Exec=/your/working/path/run_user.sh
   Icon=org.gnome.Terminal
   Path=/your/working/path/
   Terminal=true
   Hidden=false
   Type=Application
   Categories=Utility;Application;

Installation from source
------------------------

To install the latest developpement version run the following command:

.. code-block:: bash

   git clone https://github.com/stephaneworkspace/backupmystemusb2usb

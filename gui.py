#!/usr/bin/env python3
import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')

GUI_TITLE = 'Backup my system usb to usb'
GUI_HBOX_SPACING = 5
GUI_BUTTON_CANCEL = 'Cancel operation'


class LogWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=GUI_TITLE)
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=GUI_HBOX_SPACING)
        self.add(hbox)

        button = Gtk.Button.new_with_label(GUI_BUTTON_CANCEL)
        button.connect('clicked', self.on_click_cancel)
        hbox.pack_start(button, True, True, 0)

    def on_click_cancel(self, button):
        """
        Cancel operation
        """
        Gtk.main_quit()


win = LogWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()

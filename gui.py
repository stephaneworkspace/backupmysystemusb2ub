#!/usr/bin/env python3
import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')

GUI_TITLE = 'Backup my system usb to usb'
GUI_HBOX_SPACING = 5
GUI_BUTTON_CANCEL = 'Cancel operation'

log_list = [('1'), ('2'), ('3')]
"""
https://python-gtk-3-tutorial.readthedocs.io/en/latest/treeview.html#the-view
"""


class LogWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title=GUI_TITLE)
        self.set_border_width(10)

        # Setting up the self.grid in wich the element are to be positione
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        # Creating the ListStore model
        self.log_list_liststore = Gtk.ListStore(str)
        for l in log_list:
            self.log_list_liststore.append(list(l))
        self.current_filter = None
        # Creating the treeview, making it use the filter as a model,
        # and adding the columns
        self.treeview = Gtk.TreeView.new_with_model()
        for i, column_title in enumerate(['Log']):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=1)
            self.treeview.append_column(column)

        hbox = Gtk.Box(spacing=GUI_HBOX_SPACING)
        self.add(hbox)

        button = Gtk.Button.new_with_label(GUI_BUTTON_CANCEL)
        button.connect('clicked', self.on_click_cancel)
        hbox.pack_start(button, True, True, 0)

        # Setting up the layout, putting the treeview in scrollwindow, and
        # the button in
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_expand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        self.grid.attach_next_to(self.hbox, self.scrollable_treelist,
                                 Gtk.PositionType.BOTTOM, 1, 1)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

    def on_click_cancel(self, button):
        """
        Cancel operation
        """
        Gtk.main_quit()


win = LogWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()

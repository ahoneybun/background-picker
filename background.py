#!/usr/bin/python3

# Imports
import gi
import subprocess
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        #### HeaderBar Define
        self.headerbar = Gtk.HeaderBar()
        self.set_titlebar(self.headerbar)
        self.headerbar.set_show_close_button(True)
        self.headerbar.props.title = "Background Picker"

        ### Hiding the About button until it's coded in.
        #self.button = Gtk.Button()
        #icon = Gio.ThemedIcon(name="open-menu-symbolic")
        #image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        #self.button.add(image)
        #self.headerbar.pack_end(self.button)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        vbox.set_property("margin", 100)
        self.add(vbox)

        ### Background Label Definition
        self.background_label = Gtk.Label(label="Background")

        ### Lockscreen Label Definition
        self.lockscreen_label = Gtk.Label(label="Lockscreen")

        ### Our FileChooserDialogs
        self.background_dialog = Gtk.FileChooserDialog()
        self.background_dialog.set_title('Select an image')
        self.background_dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK
        )
        self.add_filters(self.background_dialog)

        ### Our FileChooserDialog
        self.lockscreen_dialog = Gtk.FileChooserDialog()
        self.lockscreen_dialog.set_title('Select an image')
        self.lockscreen_dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK
        )
        self.add_filters(self.lockscreen_dialog)

        ### Button Definement
        self.background_button = Gtk.FileChooserButton.new_with_dialog(self.background_dialog)
        self.background_button.set_title("Select Background Image")
        self.background_button.set_halign(Gtk.Align.CENTER)
        self.background_button.set_valign(Gtk.Align.CENTER)
        self.background_button.set_size_request(300, 150)
        self.background_button.connect('file-set', self.on_file_set, "background")
        
        self.lockscreen_button = Gtk.FileChooserButton.new_with_dialog(self.lockscreen_dialog)
        self.lockscreen_button.set_title("Select Lockscreen Image")
        self.lockscreen_button.set_halign(Gtk.Align.CENTER)
        self.lockscreen_button.set_valign(Gtk.Align.CENTER)
        self.lockscreen_button.set_size_request(300, 150)
        self.lockscreen_button.connect('file-set', self.on_file_set, "lockscreen")

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(6)
        self.grid.set_halign(Gtk.Align.CENTER)
        self.grid.set_valign(Gtk.Align.CENTER)

        ### Connect Signal handlers
        #self.leftbutton.connect("clicked", self.on_button_clicked)
        #self.leftbutton.connect("color-set", self.on_color_activated, "left")

        #self.centerbutton.connect("clicked", self.on_button_clicked)
        #self.centerbutton.connect("color-set", self.on_color_activated, "center")

        #self.rightbutton.connect("clicked", self.on_button_clicked)
        #self.rightbutton.connect("color-set", self.on_color_activated, "right")

        ### Grid Setup
        self.grid.attach(self.background_label, 0, 5, 1, 1)
        self.grid.attach(self.background_button, 0, 1, 1, 1)
        self.grid.attach(self.lockscreen_label, 1, 5, 1, 1)
        self.grid.attach(self.lockscreen_button, 1, 1, 1, 1)

        #vbox.pack_start(self.aboutlabel, True, True, 0)
        #vbox.pack_start(self.aboutcenterlabel, True, True, 0)
        vbox.pack_start(self.grid, True, True, 0)
    
    def on_file_set(self, widget, data=None):
        """Handler for our FileChooserButtons"""
        file_path = widget.get_filename()
        if data == "background":
            print(f'Background: {file_path}')
            # insert code for setting background here
            subprocess.run(['feh', '--bg-scale', file_path])
        elif data == "lockscreen":
            print(f'Lockscreen: {file_path}')
            # insert code for setting lockscreen here
            subprocess.run(['ls', '-l', '-a', file_path])
    
    def add_filters(self, dialog):
        filter_image = Gtk.FileFilter()
        filter_image.set_name("Images")
        filter_image.add_mime_type('image/jpg')
        filter_image.add_mime_type('image/jpeg')
        filter_image.add_mime_type('image/png')
        dialog.add_filter(filter_image)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("All Files")
        filter_any.add_pattern('*')
        dialog.add_filter(filter_any)

    def on_button_clicked(self, widget):
        win.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

#!/usr/bin/python3

# Imports
import gi
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

        ### Button Definement
        self.background_button = Gtk.FileChooserButton()
        self.background_button.set_title("Select Background Image")
        self.background_button.set_halign(Gtk.Align.CENTER)
        self.background_button.set_valign(Gtk.Align.CENTER)
        self.background_button.set_size_request(300, 150)
        self.background_button.connect('file-set' self.on_file.set)
        
        self.lockscreen_button = Gtk.FileChooserButton()
        self.lockscreen_button.set_title("Select Lockscreen Image")
        self.lockscreen_button.set_halign(Gtk.Align.CENTER)
        self.lockscreen_button.set_valign(Gtk.Align.CENTER)
        self.lockscreen_button.set_size_request(300, 150)

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
        """When we get a filename from one of the buttons."""
        dialog = widget.props.dialog
        file_path = dialog.get_filename()
        print(file_path)

    def on_button_clicked(self, widget):
        win.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

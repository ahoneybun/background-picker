#!/usr/bin/python3

# Imports
import gi
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(100)

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
        self.add(vbox)

        ### Button Definement
        self.Backgroundbutton = Gtk.FileChooserButton()
        self.Backgroundbutton.set_title("Select Background Image")
        self.Backgroundlabel = Gtk.Label()
        self.Backgroundlabel.set_text("Background")
        self.Backgroundbutton.set_halign(Gtk.Align.CENTER)
        self.Backgroundbutton.set_valign(Gtk.Align.CENTER)
        self.Backgroundbutton.set_size_request(300, 150)

        self.Lockscreenbutton = Gtk.FileChooserButton()
        self.Lockscreenbutton.set_title("Select Lockscreen Image")
        self.Lockscreenlabel = Gtk.Label()
        self.Lockscreenlabel.set_text("Lockscreen")
        self.Lockscreenbutton.set_halign(Gtk.Align.CENTER)
        self.Lockscreenbutton.set_valign(Gtk.Align.CENTER)
        self.Lockscreenbutton.set_size_request(300, 150)

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
        self.grid.attach(self.Backgroundlabel, 0, 5, 1, 1)
        self.grid.attach(self.Backgroundbutton, 0, 1, 1, 1)
        self.grid.attach(self.Lockscreenlabel, 1, 5, 1, 1)
        self.grid.attach(self.Lockscreenbutton, 1, 1, 1, 1)

        #vbox.pack_start(self.aboutlabel, True, True, 0)
        #vbox.pack_start(self.aboutcenterlabel, True, True, 0)
        vbox.pack_start(self.grid, True, True, 0)

    def on_button_clicked(self, widget):
        win.show_all()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

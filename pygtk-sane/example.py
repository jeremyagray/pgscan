#!/usr/bin/env python

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class PGSaneWindow(Gtk.Window):
    def __init__(self):
        # super().__init__(self, title="Hello World")
        super().__init__(title="Hello World")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button_hello = Gtk.Button(label="hello")
        self.button_world = Gtk.Button(label="world")

        self.button_hello.connect("clicked",
                                  self.on_button_click, 'hello')
        self.button_world.connect("clicked",
                                  self.on_button_click, 'world')
        self.box.pack_start(self.button_hello, True, True, 0)
        self.box.pack_start(self.button_world, True, True, 0)

    def on_button_click(self, widget, msg):
        print(msg)


win = PGSaneWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()

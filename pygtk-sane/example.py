#!/usr/bin/env python
#
# pygtk-sane:  a Python/GTK SANE front-end
# Copyright (C) 2020 Jeremy A Gray <jeremy.a.gray@gmail.com>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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


# For 'About.'
# pygtk-sane  Copyright (C) 2020 Jeremy A Gray <jeremy.a.gray@gmail.com>
# This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; type `show c' for details.

win = PGSaneWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()

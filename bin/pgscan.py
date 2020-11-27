#!/usr/bin/env python
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# pgscan.py:  The GTK frontend of pgscan.
#
# pgscan:  a Python/GTK SANE front-end
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
import sane
from PIL import Image

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


def init():
    # Initialize.
    sane.init()


def get_devices():
    # Try to find the devices.
    try:
        return sane.get_devices()
    except _sane.error:
        print('no devices found')
    finally:
        sane.exit()


def get_device_names():
    names = []
    for device in get_devices():
        names.append(device[0])


class PGSaneWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="pgscan")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button_hello = Gtk.Button(label="hello")
        self.button_world = Gtk.Button(label="world")

        self.button_hello.connect("clicked",
                                  self.on_button_click, 'hello')
        self.button_world.connect("clicked",
                                  self.on_button_click, 'world')

        self.select_device_combo = Gtk.ComboBoxText()
        self.select_device_combo.set_entry_text_column(0)
        self.select_device_combo.connect('changed', self.select_device, 'hi')
        # self.select_device_combo.append_text(get_device_names())
        self.select_device_combo.append_text(('Fujitsu ScanSnap', 'Fujitsu', 'ix500', 'ScanSnap')[0])

        self.box.pack_start(self.button_hello, True, True, 0)
        self.box.pack_start(self.button_world, True, True, 0)
        self.box.pack_start(self.select_device_combo, True, True, 1)

    def on_button_click(self, widget, msg):
        print(msg)

    def select_device(self, widget, msg):
        print(msg)


win = PGSaneWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()

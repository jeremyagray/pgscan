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

import sane
from PIL import Image

# Python-Sane Reference
# =====================

# sane.init()

#    Initialize sane.

#    Returns:
#       A tuple "(sane_ver, ver_maj, ver_min, ver_patch)".

#    Raises _sane.error:
#       If an error occurs.

# sane.get_devices(localOnly=False)

#    Return a list of 4-tuples containing the available scanning
#    devices. If *localOnly* is *True*, only local devices will be
#    returned. Each tuple is of the format "(device_name, vendor, model,
#    type)", with:

#    * *device_name* -- The device name, suitable for passing to
#      "sane.open()".

#    * *vendor* -- The device vendor.

#    * *mode* -- The device model vendor.

#    * *type* -- the device type, such as ""virtual device"" or
#      ""video camera"".

#    Returns:
#       A list of scanning devices.

#    Raises _sane.error:
#       If an error occurs.

# sane.open(devname)

#    Open a device for scanning. Suitable values for devname are
#    returned in the first item of the tuples returned by
#    "sane.get_devices()".

#    Returns:
#       A "SaneDev" object on success.

#    Raises _sane.error:
#       If an error occurs.

# sane.exit()

#    Exit sane.

# class class sane.SaneDev(devname)

#    Class representing a SANE device. Besides the functions documented
#    below, the class has some special attributes which can be read:

#    * *devname*        -- The scanner device name (as passed to

#         "sane.open()").

#    * *sane_signature* -- The tuple "(devname, brand, name, type)".

#    * *scanner_model*  -- The tuple "(brand, name)".

#    * *opt*            -- Dictionary of options.

#    * *optlist*        -- List of option names.

#    * *area*           -- Scan area.

#    Furthermore, the scanner options are also exposed as attributes,
#    which can be read and set:

#       print(scanner.mode)
#       scanner.mode = 'Color'

#    An "Option" object for a scanner option can be retrieved via
#    "__getitem__()", i.e.:

#       option = scanner['mode']

#    arr_scan()

#       Convenience method which calls "SaneDev.start()" followed by
#       "SaneDev.arr_snap()".

#    arr_snap()

#       Read image data and return a 3d numpy array of the shape
#       "(nbands, width, height)".

#       Returns:
#          A "numpy.array" object.

#       Raises:
#          * **_sane.error** -- If an error occurs.

#          * **RuntimeError** -- If *numpy* cannot be imported.

#    cancel()

#       Cancel an in-progress scanning operation.

#    close()

#       Close the scanning device.

#    fileno()

#       Returns:
#          The file descriptor for the scanning device, if any.

#       Raises _sane.error:
#          If an error occurs.

#    get_options()

#       Returns:
#          A list of tuples describing all the available options.

#    get_parameters()

#       Returns a 5-tuple holding all the current device settings:
#       "(format, last_frame, (pixels_per_line, lines), depth,
#       bytes_per_line)"

#       * *format*          -- One of ""grey"", ""color"", ""red"",

#            ""green"", ""blue"" or ""unknown format"".

#       * *last_frame*      -- Whether this is the last frame of a
#         multi frame

#            image.

#       * *pixels_per_line* -- Width of the scanned image.

#       * *lines*           -- Height of the scanned image.

#       * *depth*           -- The number of bits per sample.

#       * *bytes_per_line*  -- The number of bytes per line.

#       Returns:
#          A tuple containing the device settings.

#       Raises _sane.error:
#          If an error occurs.

#       Note: Some backends may return different parameters depending on
#       whether "SaneDev.start()" was called or not.

#    multi_scan()

#       Returns:
#          A "_SaneIterator" for ADF scans.

#    scan()

#       Convenience method which calls "SaneDev.start()" followed by
#       "SaneDev.snap()".

#    snap(no_cancel=False)

#       Read image data and return a "PIL.Image" object. An RGB image is
#       returned for multi-band images, an L image for single-band
#       images. "no_cancel" is used for ADF scans by "_SaneIterator".

#       Returns:
#          A "PIL.Image" object.

#       Raises:
#          * **_sane.error** -- If an error occurs.

#          * **RuntimeError** -- If *PIL.Image* cannot be imported.

#    start()

#       Initiate a scanning operation.

#       Throws _sane.error:
#          If an error occurs, for instance if an option is set to an
#          invalid value.

# class class sane.Option(args, scanDev)

#    Class representing a SANE option. These are returned by a
#    "SaneDev.__getitem__()" lookup of an option on the device, i.e.:

#       option = scanner["mode"]

#    The "Option" class has the following attributes:

#       * *index* -- Number from "0" to "n", giving the option number.

#       * *name* -- A string uniquely identifying the option.

#       * *title* -- Single-line string containing a title for the
#         option.

#       * *desc* -- A long string describing the option, useful as a
#         help

#            message.

#       * *type* -- Type of this option: "TYPE_BOOL", "TYPE_INT",

#            "TYPE_STRING", etc.

#       * *unit* -- Units of this option. "UNIT_NONE", "UNIT_PIXEL",
#         etc.

#       * *size* -- Size of the value in bytes.

#       * *cap* -- Capabilities available: "CAP_EMULATED",
#         "CAP_SOFT_SELECT",

#            etc.

#       * *constraint* -- Constraint on values. Possible values:

#         * None : No constraint

#         * "(min,max,step)" : Range

#         * list of integers or strings: listed of permitted values

#    is_active()

#       Returns:
#          Whether the option is active.

#    is_settable()

#       Returns:
#          Whether the option is settable.

# class class sane._SaneIterator(device)

#    Iterator for ADF scans.

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


if __name__ == '__main__':
    # For 'About.'
    # pygtk-sane  Copyright (C) 2020 Jeremy A Gray <jeremy.a.gray@gmail.com>
    # This program comes with ABSOLUTELY NO WARRANTY; for details type
    # `show w'.  This is free software, and you are welcome to
    # redistribute it under certain conditions; type `show c' for
    # details.

    init()

    devices = get_devices()
    scanner = sane.open(devices[0][0])
    # options = scanner.get_options()
    # for option in options:
    #     print(option)

    # 600 dpi.
    scanner.mode = 'Color'
    scanner.resolution = 600
    scanner.start()
    img = scanner.snap()

    # Letter paper: 600 dpi * 8.5 in = 5100 width
    #               600 dpi * 11 in = 6600 length

    img.resize((5100, 6600)).save('test.pdf')

    scanner.close()

    sane.exit()

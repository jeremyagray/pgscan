# pgscan

A small Python/GTK and Python script front-end for SANE.

## What is pgscan?

pgscan is a pair of programs with a common internal interface.  Both are front-ends to SANE and are designed to find scanners, load their options, and produce scans in the chosen format.  The main goal is to be able to drop a document in a scanner, issue a command, and scan and archive the document (and possibly metadata) as a PDF.

## Installation

```
pip install pgscan
```

## Usage

Console:

```
pscan scan.png
```

GUI (background):

```
pgscan &
```

## Copyright and License

SPDX-License-Identifier: GPL-3.0-or-later

pgscan, a Python/GTK front-end for SANE.
Copyright (C) 2020 Jeremy A Gray <jeremy.a.gray@gmail.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the [GNU General Public License](LICENSE) as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the [GNU General Public
License](LICENSE) along with this program.  If not, see
<https://www.gnu.org/licenses/>.

## Author

Jeremy A Gray <jeremy.a.gray@gmail.com>

#!/usr/bin/env python2
# Startup from single-user installation
# Copyright (C) 2002-2018 John Goerzen & contributors
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA

import os
import sys
if sys.version_info.major > 2:
    print ("Offlineimap runs with python2 only. To use python 3, switch to using Offlineimap3")
    sys.exit(1)
from offlineimap import OfflineImap

oi = OfflineImap()
oi.run()

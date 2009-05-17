#! /usr/bin/env python
# -*- coding: utf-8 -*-

#   eLyXer -- convert LyX source files to HTML output.
#
#   Copyright (C) 2009 Alex Fernández
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

# --end--
# Alex 20090503
# eLyXer table parsing

from util.trace import Trace
from gen.container import *
from parse.parser import *
from io.output import *


class TableParser(BoundedParser):
  "Parse the whole table"

  def __init__(self):
    BoundedParser.__init__(self)
    self.columns = list()

  def parseheader(self, reader):
    "Parse table headers"
    reader.nextline()
    while self.startswithlist(reader, ContainerConfig.tableheaders):
      self.parseparameter(reader)
      reader.nextline()
    return []

  def startswithlist(self, reader, list):
    "Check if the current line starts with any of the given strings"
    for start in list:
      if reader.currentline().strip().startswith(start):
        return True
    return False

class TablePartParser(BoundedParser):
  "Parse a table part (row or cell)"

  def parseheader(self, reader):
    "Parse the header"
    tablekey, parameters = self.parsexml(reader)
    self.parameters = parameters
    return list()

class ColumnParser(LoneCommand):
  "Parse column properties"

  def parse(self, reader):
    "Parse the column definition"
    key, parameters = self.parsexml(reader)
    self.parameters = parameters


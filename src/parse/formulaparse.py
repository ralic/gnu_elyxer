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
# eLyXer formula parsing

import sys
from gen.container import *
from util.trace import Trace
from conf.config import *
from parse.position import *


class FormulaParser(Parser):
  "Parses a formula"

  def parseheader(self, reader):
    "See if the formula is inlined"
    self.begin = reader.linenumber + 1
    if reader.currentline().find(FormulaConfig.starts['simple']) > 0:
      return ['inline']
    if reader.currentline().find(FormulaConfig.starts['complex']) > 0:
      return ['block']
    if reader.currentline().find(FormulaConfig.starts['unnumbered']) > 0:
      return ['block']
    return ['numbered']
  
  def parse(self, reader):
    "Parse the formula until the end"
    formula = self.parseformula(reader)
    while not reader.currentline().startswith(self.ending):
      stripped = reader.currentline().strip()
      if len(stripped) > 0:
        Trace.error('Unparsed formula line ' + stripped)
      reader.nextline()
    reader.nextline()
    return [formula]

  def parseformula(self, reader):
    "Parse the formula contents"
    simple = FormulaConfig.starts['simple']
    if simple in reader.currentline():
      rest = reader.currentline().split(simple, 1)[1]
      if simple in rest:
        # formula is $...$
        return self.parsesingleliner(reader, simple, simple)
      # formula is multiline $...$
      return self.parsemultiliner(reader, simple, simple)
    if FormulaConfig.starts['complex'] in reader.currentline():
      # formula of the form \[...\]
      return self.parsemultiliner(reader, FormulaConfig.starts['complex'],
          FormulaConfig.endings['complex'])
    beginbefore = FormulaConfig.starts['beginbefore']
    beginafter = FormulaConfig.starts['beginafter']
    if beginbefore in reader.currentline():
      if reader.currentline().strip().endswith(beginafter):
        current = reader.currentline().strip()
        endsplit = current.split(beginbefore)[1].split(beginafter)
        startpiece = beginbefore + endsplit[0] + beginafter
        endbefore = FormulaConfig.endings['endbefore']
        endafter = FormulaConfig.endings['endafter']
        endpiece = endbefore + endsplit[0] + endafter
        return startpiece + self.parsemultiliner(reader, startpiece, endpiece) + endpiece
      Trace.error('Missing ' + beginafter + ' in ' + reader.currentline())
      return ''
    begincommand = FormulaConfig.starts['command']
    beginbracket = FormulaConfig.starts['bracket']
    if begincommand in reader.currentline() and beginbracket in reader.currentline():
      endbracket = FormulaConfig.endings['bracket']
      return self.parsemultiliner(reader, beginbracket, endbracket)
    Trace.error('Formula beginning ' + reader.currentline() + ' is unknown')
    return ''

  def parsesingleliner(self, reader, start, ending):
    "Parse a formula in one line"
    line = reader.currentline().strip()
    if not start in line:
      Trace.error('Line ' + line + ' does not contain formula start ' + start)
      return ''
    if not line.endswith(ending):
      Trace.error('Formula ' + line + ' does not end with ' + ending)
      return ''
    index = line.index(start)
    rest = line[index + len(start):-len(ending)]
    reader.nextline()
    return rest

  def parsemultiliner(self, reader, start, ending):
    "Parse a formula in multiple lines"
    formula = ''
    line = reader.currentline()
    if not start in line:
      Trace.error('Line ' + line.strip() + ' does not contain formula start ' + start)
      return ''
    index = line.index(start)
    formula = line[index + len(start):].strip()
    reader.nextline()
    while not reader.currentline().endswith(ending):
      formula += reader.currentline()
      reader.nextline()
    formula += reader.currentline()[:-len(ending)]
    reader.nextline()
    return formula


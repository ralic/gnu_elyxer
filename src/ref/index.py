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
# Alex 20100713
# eLyXer: indexing entries

from util.trace import Trace
from util.translate import *
from parse.parser import *
from out.output import *
from gen.container import *
from gen.styles import *
from ref.link import *
from ref.partkey import *
from proc.process import *


class ListInset(Container):
  "An inset with a list, normally made of links."

  def __init__(self):
    self.parser = InsetParser()
    self.output = ContentsOutput()

  def sortdictionary(self, dictionary):
    "Sort all entries in the dictionary"
    keys = dictionary.keys()
    # sort by name
    keys.sort()
    return keys

class ListOf(ListInset):
  "A list of entities (figures, tables, algorithms)"

  def process(self):
    "Parse the header and get the type"
    self.type = self.header[2]
    text = Translator.translate('list-' + self.type)
    self.contents = [TaggedText().constant(text, 'div class="tocheader"', True)]

class TableOfContents(ListInset):
  "Table of contents"

  def process(self):
    "Parse the header and get the type"
    self.create(Translator.translate('toc'))

  def create(self, heading):
    "Create a table of contents with the given heading text."
    self.output = TaggedOutput().settag('div class="fulltoc"', True)
    self.contents = [TaggedText().constant(heading, 'div class="tocheader"', True)]
    return self

  def add(self, entry):
    "Add a new entry to the TOC."
    self.contents.append(entry)

class IndexReference(Link):
  "A reference to an entry in the alphabetical index"

  name = 'none'

  def process(self):
    "Put entry in index"
    if 'name' in self.parameters:
      name = self.parameters['name'].strip()
    else:
      name = self.extracttext()
    entry = IndexEntry.get(name)
    entry.addref(self)

  def __unicode__(self):
    "Return a printable representation."
    return 'Reference to ' + self.name

class IndexArrow(Link):
  "An arrow in an index entry."

  def create(self, reference):
    "Create an arrow pointing to a reference."
    self.contents = [Constant(u'↑')]
    self.destination = reference
    return self

class IndexEntry(Container):
  "An entry in the alphabetical index"

  entries = dict()
  arrows = dict()

  keyescapes = {'!':'_', '|':'-', ' ':'-', '--':'-', ',':'', '\\':'', '@':'_', u'°':''}

  def create(self, name):
    "Create an index entry with the given name."
    self.output = TaggedOutput().settag('p class="printindex"', True)
    self.arrows = []
    self.name = name
    self.key = self.escape(self.name, self.keyescapes)
    self.anchor = Link().complete('', 'index-' + self.key, None, 'printindex')
    self.contents = [self.anchor, Constant(self.name + ': ')]
    return self

  def addref(self, reference):
    "Add a reference to the entry."
    reference.index = unicode(len(self.arrows))
    reference.complete(u'↓', 'entry-' + self.key + '-' + reference.index)
    reference.destination = self.anchor
    arrow = IndexArrow().create(reference)
    if len(self.arrows) > 0:
      self.contents.append(Constant(u', '))
    self.arrows.append(arrow)
    self.contents.append(arrow)

  def get(cls, name):
    "Get the index entry for the given name."
    if not name in cls.entries:
      cls.entries[name] = IndexEntry().create(name)
    return cls.entries[name]

  def __unicode__(self):
    "Return a printable representation."
    return 'Index entry for ' + self.name

  get = classmethod(get)

class PrintIndex(ListInset):
  "Command to print an index"

  def process(self):
    "Create the alphabetic index"
    self.name = Translator.translate('index')
    self.partkey = PartKeyGenerator.forindex(self)
    self.contents = [self.partkey.toclabel(),
        TaggedText().constant(self.name, 'h1 class="index"')]
    for key in self.sortdictionary(IndexEntry.entries):
      self.contents.append(IndexEntry.entries[key])

class NomenclatureEntry(Link):
  "An entry of LyX nomenclature"

  entries = dict()

  def process(self):
    "Put entry in index"
    symbol = self.parameters['symbol']
    description = self.parameters['description']
    key = symbol.replace(' ', '-').lower()
    if key in NomenclatureEntry.entries:
      Trace.error('Duplicated nomenclature entry ' + key)
    self.complete(u'↓', 'noment-' + key)
    entry = Link().complete(u'↑', 'nom-' + key)
    entry.symbol = symbol
    entry.description = description
    self.setmutualdestination(entry)
    NomenclatureEntry.entries[key] = entry

class PrintNomenclature(ListInset):
  "Print all nomenclature entries"

  def process(self):
    "Create the nomenclature."
    self.name = Translator.translate('nomenclature')
    self.partkey = PartKeyGenerator.forindex(self)
    self.contents = [self.partkey.toclabel(),
        TaggedText().constant(self.name, 'h1 class="nomenclature"')]
    for key in self.sortdictionary(NomenclatureEntry.entries):
      entry = NomenclatureEntry.entries[key]
      contents = [entry, Constant(entry.symbol + u' ' + entry.description)]
      text = TaggedText().complete(contents, 'div class="Nomenclated"', True)
      self.contents.append(text)

class PreListInset(object):
  "Preprocess any container that contains a list inset."

  def preprocess(self, container):
    "Preprocess a container, extract any list inset and return it."
    listinsets = container.searchall(ListInset)
    if len(listinsets) == 0:
      return container
    if len(listinsets) > 1:
      Trace.error('More than one ListInset in container: ' + unicode(listinsets))
      return container
    return listinsets[0]

Processor.prestages += [PreListInset()]


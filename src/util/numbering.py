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
# Alex 20090418
# eLyXer number generator

from util.trace import Trace
from util.translate import *
from util.docparams import *
from conf.config import *


class NumberGenerator(object):
  "A number generator for unique sequences and hierarchical structures. Used in:"
  "  * ordered part numbers: Chapter 3, Section 5.3."
  "  * unique part numbers: Footnote 15, Bibliography cite [15]."
  "  * chaptered part numbers: Figure 3.15, Equation (8.3)."
  "  * unique roman part numbers: Part I, Book IV."

  letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  unique = None
  ordered = None
  roman = None
  chaptered = None

  romanlayouts = NumberingConfig.layouts['roman']
  orderedlayouts = NumberingConfig.layouts['ordered']

  def increase(self, number):
    "Increase the number (or letter)."
    if not isinstance(number, str):
      return number + 1
    if number == '-':
      index = 0
    elif not number in NumberGenerator.letters:
      Trace.error('Unknown letter numeration ' + number)
      return 0
    else:
      index = NumberGenerator.letters.index(number) + 1
    return self.letter(index)

  def letter(self, index):
    "Get the letter that corresponds to the given index."
    return NumberGenerator.letters[index % len(NumberGenerator.letters)]

  def startappendix(self):
    "Start appendices here."
    self.number = ['-']
    self.appendix = True

  def deasterisk(self, type):
    "Remove the possible asterisk in a layout type."
    return type.replace('*', '')

  def isunique(self, type):
    "Find out if the layout type corresponds to a unique part."
    return self.deasterisk(type) in NumberGenerator.romanlayouts

  def isinordered(self, type):
    "Find out if the layout type corresponds to an (un)ordered part."
    return self.deasterisk(type) in NumberGenerator.orderedlayouts

  def isnumbered(self, type):
    "Find out if the type for a layout corresponds to a numbered layout."
    if '*' in type:
      return False
    if self.getlevel(type) > DocumentParameters.maxdepth:
      return False
    return True

  def isunordered(self, type):
    "Find out if the type contains an asterisk, basically."
    return '*' in type

  def getlevel(self, type):
    "Get the level that corresponds to a layout type."
    type = self.deasterisk(type)
    if type in self.romanlayouts:
      return 0
    if not type in self.orderedlayouts:
      Trace.error('Unknown layout type ' + type)
      return 0
    level = self.orderedlayouts.index(type) + 1
    return level - DocumentParameters.startinglevel

  def getnumber(self, type):
    "Get the number for a layout type, can be unique or ordered."
    "Unique part types such as Part or Book generate roman numbers: Part I."
    "Ordered part types return dot-separated tuples: Chapter 5, Section 2.3."
    "Everything else generates unique numbers: Bibliography [1]."
    if self.isunique(type):
      return NumberGenerator.roman.generate(type)
    if self.isnumbered(type):
      return NumberGenerator.ordered.generate(type)
    return NumberGenerator.unique.generate(type)

  def getparttype(self, type):
    "Obtain the type for the part: without the asterisk, "
    "and switched to Appendix if necessary."
    if NumberGenerator.ordered.appendix and self.getlevel(type) == 1:
      return 'Appendix'
    return self.deasterisk(type)

class UniqueGenerator(NumberGenerator):
  "Generate unique part numbers."
  "Used in footnotes or bibliographical entry numbers: [3]."

  def __init__(self):
    "Initialize the dictionary for unique parts."
    self.uniques = dict()

  def generate(self, type):
    "Generate unique numbering: a number to place in the title,"
    "but not to append to others. Example: Footnote 15."
    return unicode(self.create(type))

  def create(self, type):
    "Return a unique numbering as an integer."
    if not type in self.uniques:
      self.uniques[type] = 0
    self.uniques[type] = self.increase(self.uniques[type])
    return self.uniques[type]

class OrderedGenerator(NumberGenerator):
  "Generate ordered part numbers separated by a dot, as in 2.3 or 7.5.4."
  "Used in chapters, sections... as in Chapter 5, Section 5.3."

  def __init__(self):
    self.number = []
    self.appendix = False

  def generate(self, type):
    "Generate ordered numbering: a number to use and possibly concatenate "
    "with others. Example: Chapter 1, Section 1.5."
    level = self.getlevel(type)
    if level == 0:
      Trace.error('Impossible level 0 for ordered part')
      return '.'
    if len(self.number) >= level:
      self.number = self.number[:level]
    else:
      while len(self.number) < level:
        self.number.append(0)
    self.number[level - 1] = self.increase(self.number[level - 1])
    return self.dotseparated(self.number)

  def dotseparated(self, number):
    "Get the number separated by dots: 1.1.3"
    dotsep = ''
    if len(number) == 0:
      Trace.error('Empty number')
      return '.'
    for piece in number:
      dotsep += '.' + unicode(piece)
    return dotsep[1:]

  def getchapter(self):
    "Get the current chapter number."
    if len(self.number) == 0:
      return 0
    else:
      return self.number[0]

class ChapteredGenerator(OrderedGenerator):
  "Generate chaptered numbers, as in Chapter.Number."
  "Used in equations, figures: Equation (5.3), figure 8.15."

  def __init__(self):
    self.chaptered = dict()

  def generate(self, type, chapter = None):
    "Generate a number which goes with first-level numbers (chapters). "
    "For the article classes a unique number is generated."
    if DocumentParameters.startinglevel > 0:
      return NumberGenerator.unique.generate(type)
    if not chapter:
      chapter = NumberGenerator.ordered.getchapter()
    if not type in self.chaptered or self.chaptered[type][0] != chapter:
      self.chaptered[type] = [chapter, 0]
    chaptered = self.chaptered[type]
    chaptered[1] = self.increase(chaptered[1])
    self.chaptered[type] = chaptered
    return self.dotseparated(chaptered)

class RomanGenerator(UniqueGenerator):
  "Generate roman numerals for part numbers."
  "Used in parts and books: Part I, Book IV."

  romannumerals = [
      ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
      ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
      ('IV', 4), ('I', 1)
      ]

  def generate(self, type):
    "Generate a part number in roman numerals, to use in unique part numbers."
    "E.g.: Part I, Book IV."
    return self.getroman(self.create(type))

  def getroman(self, number):
    "Get the roman numeral that corresponds to the given arabic numeral."
    result = ''
    for numeral, value in self.romannumerals:
      if number >= value:
        result += numeral * (number / value)
        number = number % value
    return result


NumberGenerator.unique = UniqueGenerator()
NumberGenerator.ordered = OrderedGenerator()
NumberGenerator.chaptered = ChapteredGenerator()
NumberGenerator.roman = RomanGenerator()


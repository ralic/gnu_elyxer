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
# Alex 20091226
# Port a Java program to a Python equivalent. Used to port MathToWeb.

import sys
import os.path
from io.fileline import *
from parse.position import *
from util.trace import Trace


def readargs(args):
  "Read arguments from the command line"
  del args[0]
  if len(args) == 0:
    usage()
    return
  inputfile = args[0]
  del args[0]
  outputfile = os.path.splitext(inputfile)[0] + '.py'
  if len(args) > 0:
    outputfile = args[0]
    del args[0]
  if len(args) > 0:
    usage()
    return
  return inputfile, outputfile

def usage():
  Trace.error('Usage: javatopy.py filein.java [fileout.py]')
  return

class JavaPorter(object):
  "Ports a Java file."

  javatokens = {
      'if':'parensblock', 'catch':'parensblock', 'import':'ignorestatement',
      'public':'classormember', 'protected':'classormember', 'private':'classormember',
      'class':'parseclass', 'else':'tokenblock', 'try':'tokenblock',
      'return':'tokenstatement', '{':'openblock', '}':'closeblock'
      }

  def __init__(self):
    self.depth = 0
    self.inclass = None
    self.inmethod = None
    self.waitingforblock = False

  def topy(self, inputfile, outputfile):
    "Port the Java input file to Python."
    tok = Tokenizer(FilePosition(inputfile))
    writer = LineWriter(outputfile)
    while not tok.pos.finished():
      statement = self.nextstatement(tok)
      Trace.debug('Statement: ' + statement)
      writer.writeline(statement)
    writer.close()

  def nextstatement(self, tok):
    "Return the next statement."
    if tok.pos.finished():
      raise Exception('Read after the end.')
    statement = None
    while not statement:
      indent = '  ' * self.depth
      statement = self.parsestatement(tok)
    return indent + statement

  def parsestatement(self, tok):
    "Parse a single statement."
    token = tok.next()
    Trace.debug('Token: ' + token)
    if token in self.javatokens:
      function = getattr(self, self.javatokens[token])
      return function(token, tok)
    return self.tokenstatement(token, tok)

  def classormember(self, token, tok):
    "Parse a class or member (attribute or method)."
    if self.inclass:
      return self.translateinternal(tok)
    else:
      return self.translateclass(tok)

  def parensblock(self, token, tok):
    "Parse a parens () and then a block {}."
    parens = self.parseparens(tok)
    self.waitingforblock = True
    return token + ' ' + parens + ':'

  def tokenblock(self, token, tok):
    "Parse a block (after a try or an else)."
    self.waitingforblock = True
    return token + ':'

  def openblock(self, token, tok):
    "Open a block of code."
    self.waitingforblock = False
    self.depth += 1
    return None

  def closeblock(self, token, tok):
    "Close a block of code."
    self.depth -= 1
    return None

  def tokenstatement(self, token, tok):
    "A token that starts a statement."
    statement = token
    while tok.next() != ';':
      statement += ' ' + self.processtoken(tok)
    if self.waitingforblock:
      self.waitingforblock = False
      self.depth -= 1
    return statement

  def processstatement(self, tok):
    "Process a single statement and return the result."
    statement = self.parsestatement(tok)
    Trace.debug('Statement: ' + statement)
    tok.pos.skipspace()
    while tok.pos.finished():
      self.closebracket(tok)
      tok.pos.skipspace()
    return statement

  def parsestatementold(self, tok):
    "Parse a single statement."
    indent = self.depth * '  '
    token = tok.next()
    if tok.pos.finished():
      Trace.error('Nothing to see! ' + tok.pos.current() + ' ' + unicode(tok.pos.endinglist))
      return ''
    return indent + self.translatestatement(tok)

  def translatestatement(self, tok):
    "Translate a Java statement to Python."
    if token in self.javatokens:
      return self.translatetoken(tok)
    if token in tok.javasymbols:
      return self.translatesymbol(tok)
    return self.translateunknown(tok)

  def translateunknown(self, tok):
    "Translate an unknown token."
    return tok.current() + ' ' + self.parseupto(';', tok)

  def translatesymbol(self, tok):
    "Translate a java symbol."
    if tok.current() in tok.comments:
      return tok.skipcomment()
    return tok.current() + ' ' + self.parseupto(';', tok)

  def translatetoken(self, tok):
    "Translate a java token."
    token = tok.current()
    if token == 'import':
      return self.translateimport(tok)
    if token in ['public', 'private', 'protected']:
      if self.inclass:
        return self.translateinternal(tok)
      else:
        return self.translateclass(tok)
    if token in ['if', 'catch']:
      return self.translateifcatch(token, tok)
    if token in ['else', 'try']:
      self.openbracket(tok)
      return token + ':'
    if token == 'return':
      result = self.parseupto(';', tok)
      return token + ' ' + result
    Trace.error('Untranslated token ' + token)
    return token

  def translateif(self, token, tok):
    "Translate an if or catch clause: token() and optional {"
    result = token + ' ' + self.parseparens(tok)
    if tok.next() == '{':
      self.addclosebracket(tok)
      return result
    # parse next statement directly

  def ignorestatement(self, token, tok):
    "Ignore a whole statement."
    tok.pos.globincluding(';')
    return None

  def translateclass(self, tok):
    "Translate a class definition."
    token = tok.next()
    if token != 'class':
      Trace.error('Unrecognized token: ' + token)
      return ''
    name = tok.next()
    self.inclass = name
    inheritance = ''
    while tok.next() != '{':
      inheritance += ' ' + tok.current()
    Trace.error('Unused inheritance ' + inheritance)
    self.openblock(tok.current(), tok)
    return 'class ' + name + ':'

  def translateinternal(self, tok):
    "Translate an internal element (attribute or method)."
    token = tok.next()
    name = tok.next()
    if token == self.inclass and name == '(':
      # constructor
      return self.translatemethod(token, tok)
    if tok.pos.current() == ';':
      return self.translateemptyattribute(name)
    if tok.next() != '(':
      return self.translateattribute(name)
    return self.translatemethod(name, tok)

  def translatemethod(self, name, tok):
    "Translate a class method."
    self.inmethod = name
    pars = self.parseparameters(tok)
    self.waitingforblock = True
    return 'def ' + name + '(self' + '):'

  def translateemptyattribute(self, name):
    "Translate an empty attribute definition."
    return name + ' = None'

  def translateattribute(self, name, tok):
    "Translate a class attribute."
    return name + ' ' + self.parseupto(';')

  def parseparameters(self, tok):
    "Parse the parameters of a method definition."
    parens = self.parseinparens(tok)
    return parens.split(',')

  def processpart(self, tok):
    "Process a part of a statement."
    tok.next()
    return ' ' + self.processtoken(tok)

  def processtoken(self, tok):
    "Process a single token."
    if tok.current() in tok.javasymbols:
      return self.processsymbol(tok)
    return tok.current()
  
  def processsymbol(self, tok):
    "Process a single java symbol."
    if tok.current() == '"':
      result = tok.current() + tok.pos.globincluding('"')
      while result.endswith('\\"') and not result.endswith('\\\\"'):
        result += tok.pos.globincluding('"')
      Trace.debug('quoted sequence: ' + result)
      return result
    if tok.current() == '\'':
      result = tok.current()
      while not tok.pos.checkskip('\''):
        result += tok.pos.currentskip()
      return result + '\''
    if tok.current() == '}':
      Trace.error('Erroneously closing }')
      self.closebracket(tok)
      return ''
    if tok.current() == '(':
      result = self.parseinparens(tok)
      return result
    if tok.current() == ')':
      Trace.error('Erroneously closing )')
      return ')'
    if tok.current() in tok.modified:
      return tok.modified[tok.current()]
    return tok.current()

  def parseparens(self, tok):
    "Parse a couple of () and the contents inside."
    if tok.next() != '(':
      Trace.error('No opening ( for a parens, found ' + tok.current())
      return
    return self.parseinparens(tok)

  def parseinparens(self, tok):
    "Parse the contents inside ()."
    result = self.parseupto(')', tok)
    return '(' + result + ')'

  def parseupto(self, ending, tok):
    "Parse the tokenizer up to the supplied ending."
    result = ''
    while not tok.next() == ending:
      result += ' ' + self.processtoken(tok)
    if len(result) > 0:
      result = result[1:]
    return result

  def openbracket(self, tok):
    "Open a {."
    while tok.next() != '{':
      Trace.error('Ignored token before {: ' + tok.current())
      if tok.pos.finished():
        Trace.error('Finished while waiting for {')
        return
    self.depth += 1
    Trace.error('Opening {')
    tok.pos.pushending('}')

  def closebracket(self, tok):
    "Close a }."
    self.depth -= 1
    if tok.pos.popending('}') != '}':
      exit()

class Tokenizer(object):
  "Tokenizes a parse position."

  unmodified = [
      '&', '|', '=', '!', '(', ')', '{', '}', '.', '+', '-', '"', ',', '/',
      '*', '<', '>', '\'', '[', ']', '%', ';',
      '!=','++','--','<=','>=', '=='
      ]
  modified = {
      '&&':'and', '||':'or'
      }
  comments = ['//', '/*']
  javasymbols = comments + unmodified + modified.keys()

  def __init__(self, pos):
    self.pos = pos
    self.currenttoken = None

  def next(self):
    "Get the next single token, and store it for current()."
    self.currenttoken = self.extracttoken()
    while self.currenttoken in self.comments:
      self.skipcomment()
      self.currenttoken = self.extracttoken()
    return self.currenttoken

  def extracttoken(self):
    "Extract the next token."
    self.pos.skipspace()
    if self.pos.finished():
      raise Exception('Finished looking for next token.')
    if self.isalphanumeric(self.pos.current()):
      return self.pos.glob(self.isalphanumeric)
    if self.pos.current() in self.javasymbols:
      result = self.pos.currentskip()
      while result + self.pos.current() in self.javasymbols:
        result += self.pos.currentskip()
      return result
    current = self.pos.currentskip()
    raise Exception('Unrecognized character: ' + current)

  def current(self):
    "Get the current token."
    return self.currenttoken

  def isalphanumeric(self, char):
    "Detect if a character is alphanumeric or underscore."
    if char.isalpha():
      return True
    if char.isdigit():
      return True
    if char == '_':
      return True
    return False

  def skipcomment(self):
    "Skip over a comment."
    if self.current() == '//':
      comment = self.pos.globexcluding('\n')
      return
    if self.current() == '/*':
      while not self.pos.checkskip('/'):
        comment = self.pos.globincluding('*')
      return
    Trace.error('Unknown comment type ' + self.current())

inputfile, outputfile = readargs(sys.argv)
Trace.debugmode = True
if inputfile:
  JavaPorter().topy(inputfile, outputfile)
  Trace.message('Conversion done, running ' + outputfile)
  os.system('python ' + outputfile)



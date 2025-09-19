from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from Evaler import Evaler
import sys

stream = FileStream(sys.argv[1], encoding='utf-8')

lexer = gLexer(stream)

t_stream = CommonTokenStream(lexer)

parser = gParser(t_stream)

tree = parser.program()

ev = Evaler()
ev.visit(tree)
from antlr4 import *
from EvalVisitor import EvalVisitor
from ex8Lexer import ex8Lexer 
from ex8Parser import ex8Parser
import sys

stream = FileStream(sys.argv[1], encoding="utf-8")

lexer = ex8Lexer(stream)

token_stream = CommonTokenStream(lexer)

parser = ex8Parser(token_stream)

root = parser.program()

visitor = EvalVisitor()
visitor.visit(root)
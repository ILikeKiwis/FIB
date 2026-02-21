"""
El programa principal de l'intèrpret:
    1. Llegeix l'arxiu .j que rep com a paràmetre.
    2. Amb gLexer fem l'anàlisi lèxic.
    3. Després conjuntament amb el token stream creem l'AST amb el gParser.
    4. Agafem l'arrel del programa tree.program() i li passem a l'Evaler.
"""


import sys


from antlr4 import CommonTokenStream, FileStream


from gLexer import gLexer
from gParser import gParser
from Evaler import Evaler


if __name__ == "__main__":
    stream = FileStream(sys.argv[1], encoding='utf-8')

    lexer = gLexer(stream)

    t_stream = CommonTokenStream(lexer)

    parser = gParser(t_stream)

    parser.removeErrorListeners()

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() == 0:
        ev = Evaler()
        ev.visit(tree)
    else:
        print(parser.getNumberOfSyntaxErrors(), " errors de sintaxi")
        print(tree.toStringTree(recog=parser))

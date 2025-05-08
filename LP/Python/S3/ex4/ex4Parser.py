# Generated from ex4.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,113,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,5,4,47,8,4,10,4,12,4,50,9,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,5,5,60,8,5,10,5,12,5,63,9,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,92,8,6,1,7,1,7,1,7,3,7,97,8,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,5,7,108,8,7,10,7,12,7,111,9,7,1,7,0,1,14,8,
        0,2,4,6,8,10,12,14,0,2,1,0,15,16,1,0,17,18,119,0,19,1,0,0,0,2,32,
        1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,41,1,0,0,0,10,54,1,0,0,0,12,
        91,1,0,0,0,14,96,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,21,1,0,0,
        0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,
        5,0,0,1,23,1,1,0,0,0,24,25,3,4,2,0,25,26,5,21,0,0,26,33,1,0,0,0,
        27,28,3,6,3,0,28,29,5,21,0,0,29,33,1,0,0,0,30,33,3,8,4,0,31,33,3,
        10,5,0,32,24,1,0,0,0,32,27,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,
        3,1,0,0,0,34,35,5,20,0,0,35,36,5,1,0,0,36,37,3,14,7,0,37,5,1,0,0,
        0,38,39,5,2,0,0,39,40,3,14,7,0,40,7,1,0,0,0,41,42,5,3,0,0,42,43,
        3,12,6,0,43,44,5,4,0,0,44,48,5,21,0,0,45,47,3,2,1,0,46,45,1,0,0,
        0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,
        1,0,0,0,51,52,5,5,0,0,52,53,5,21,0,0,53,9,1,0,0,0,54,55,5,6,0,0,
        55,56,3,12,6,0,56,57,5,7,0,0,57,61,5,21,0,0,58,60,3,2,1,0,59,58,
        1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,
        63,61,1,0,0,0,64,65,5,5,0,0,65,66,5,21,0,0,66,11,1,0,0,0,67,68,3,
        14,7,0,68,69,5,8,0,0,69,70,3,14,7,0,70,92,1,0,0,0,71,72,3,14,7,0,
        72,73,5,9,0,0,73,74,3,14,7,0,74,92,1,0,0,0,75,76,3,14,7,0,76,77,
        5,10,0,0,77,78,3,14,7,0,78,92,1,0,0,0,79,80,3,14,7,0,80,81,5,11,
        0,0,81,82,3,14,7,0,82,92,1,0,0,0,83,84,3,14,7,0,84,85,5,12,0,0,85,
        86,3,14,7,0,86,92,1,0,0,0,87,88,3,14,7,0,88,89,5,13,0,0,89,90,3,
        14,7,0,90,92,1,0,0,0,91,67,1,0,0,0,91,71,1,0,0,0,91,75,1,0,0,0,91,
        79,1,0,0,0,91,83,1,0,0,0,91,87,1,0,0,0,92,13,1,0,0,0,93,94,6,7,-1,
        0,94,97,5,19,0,0,95,97,5,20,0,0,96,93,1,0,0,0,96,95,1,0,0,0,97,109,
        1,0,0,0,98,99,10,5,0,0,99,100,5,14,0,0,100,108,3,14,7,5,101,102,
        10,4,0,0,102,103,7,0,0,0,103,108,3,14,7,5,104,105,10,3,0,0,105,106,
        7,1,0,0,106,108,3,14,7,4,107,98,1,0,0,0,107,101,1,0,0,0,107,104,
        1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,15,1,
        0,0,0,111,109,1,0,0,0,8,19,32,48,61,91,96,107,109
    ]

class ex4Parser ( Parser ):

    grammarFileName = "ex4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'write'", "'if'", "'then'", "'end'", 
                     "'while'", "'do'", "'='", "'<>'", "'<='", "'>='", "'<'", 
                     "'>'", "'^'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "ID", 
                      "NL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_write = 3
    RULE_cond = 4
    RULE_while = 5
    RULE_boolexpr = 6
    RULE_expr = 7

    ruleNames =  [ "program", "statement", "assign", "write", "cond", "while", 
                   "boolexpr", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    NUM=19
    ID=20
    NL=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ex4Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ex4Parser.StatementContext,i)


        def getRuleIndex(self):
            return ex4Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ex4Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048652) != 0):
                self.state = 16
                self.statement()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(ex4Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(ex4Parser.AssignContext,0)


        def NL(self):
            return self.getToken(ex4Parser.NL, 0)

        def write(self):
            return self.getTypedRuleContext(ex4Parser.WriteContext,0)


        def cond(self):
            return self.getTypedRuleContext(ex4Parser.CondContext,0)


        def while_(self):
            return self.getTypedRuleContext(ex4Parser.WhileContext,0)


        def getRuleIndex(self):
            return ex4Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ex4Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.assign()
                self.state = 25
                self.match(ex4Parser.NL)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.write()
                self.state = 28
                self.match(ex4Parser.NL)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.cond()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.while_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ex4Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ex4Parser.ExprContext,0)


        def getRuleIndex(self):
            return ex4Parser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ex4Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ex4Parser.ID)
            self.state = 35
            self.match(ex4Parser.T__0)
            self.state = 36
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ex4Parser.ExprContext,0)


        def getRuleIndex(self):
            return ex4Parser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = ex4Parser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ex4Parser.T__1)
            self.state = 39
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolexpr(self):
            return self.getTypedRuleContext(ex4Parser.BoolexprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ex4Parser.NL)
            else:
                return self.getToken(ex4Parser.NL, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ex4Parser.StatementContext,i)


        def getRuleIndex(self):
            return ex4Parser.RULE_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = ex4Parser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ex4Parser.T__2)
            self.state = 42
            self.boolexpr()
            self.state = 43
            self.match(ex4Parser.T__3)
            self.state = 44
            self.match(ex4Parser.NL)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048652) != 0):
                self.state = 45
                self.statement()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(ex4Parser.T__4)
            self.state = 52
            self.match(ex4Parser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolexpr(self):
            return self.getTypedRuleContext(ex4Parser.BoolexprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ex4Parser.NL)
            else:
                return self.getToken(ex4Parser.NL, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex4Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ex4Parser.StatementContext,i)


        def getRuleIndex(self):
            return ex4Parser.RULE_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = ex4Parser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ex4Parser.T__5)
            self.state = 55
            self.boolexpr()
            self.state = 56
            self.match(ex4Parser.T__6)
            self.state = 57
            self.match(ex4Parser.NL)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048652) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(ex4Parser.T__4)
            self.state = 65
            self.match(ex4Parser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex4Parser.ExprContext,i)


        def getRuleIndex(self):
            return ex4Parser.RULE_boolexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolexpr" ):
                return visitor.visitBoolexpr(self)
            else:
                return visitor.visitChildren(self)




    def boolexpr(self):

        localctx = ex4Parser.BoolexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_boolexpr)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(ex4Parser.T__7)
                self.state = 69
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.expr(0)
                self.state = 72
                self.match(ex4Parser.T__8)
                self.state = 73
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.expr(0)
                self.state = 76
                self.match(ex4Parser.T__9)
                self.state = 77
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.expr(0)
                self.state = 80
                self.match(ex4Parser.T__10)
                self.state = 81
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(ex4Parser.T__11)
                self.state = 85
                self.expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.expr(0)
                self.state = 88
                self.match(ex4Parser.T__12)
                self.state = 89
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ex4Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex4Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumSub" ):
                return visitor.visitSumSub(self)
            else:
                return visitor.visitChildren(self)


    class PotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex4Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPot" ):
                return visitor.visitPot(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ex4Parser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ex4Parser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class MultDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex4Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultDiv" ):
                return visitor.visitMultDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ex4Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = ex4Parser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 94
                self.match(ex4Parser.NUM)
                pass
            elif token in [20]:
                localctx = ex4Parser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(ex4Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 107
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ex4Parser.PotContext(self, ex4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 98
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 99
                        self.match(ex4Parser.T__13)
                        self.state = 100
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ex4Parser.MultDivContext(self, ex4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 102
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 103
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ex4Parser.SumSubContext(self, ex4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 105
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expr(4)
                        pass

             
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         





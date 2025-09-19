# Generated from g.g4 by ANTLR 4.13.2
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
        4,1,16,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,5,1,29,8,1,10,1,12,1,32,9,1,1,1,1,1,5,1,36,8,1,10,1,12,1,39,9,
        1,3,1,41,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,3,3,57,8,3,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,1,3,1,
        3,1,3,5,3,71,8,3,10,3,12,3,74,9,3,1,3,5,3,77,8,3,10,3,12,3,80,9,
        3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,91,8,5,1,6,4,6,94,8,6,
        11,6,12,6,95,1,7,3,7,99,8,7,1,7,1,7,1,8,1,8,1,8,0,1,6,9,0,2,4,6,
        8,10,12,14,16,0,0,112,0,21,1,0,0,0,2,40,1,0,0,0,4,42,1,0,0,0,6,56,
        1,0,0,0,8,81,1,0,0,0,10,90,1,0,0,0,12,93,1,0,0,0,14,98,1,0,0,0,16,
        102,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,
        0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,
        1,0,0,0,26,30,3,6,3,0,27,29,5,15,0,0,28,27,1,0,0,0,29,32,1,0,0,0,
        30,28,1,0,0,0,30,31,1,0,0,0,31,41,1,0,0,0,32,30,1,0,0,0,33,37,3,
        4,2,0,34,36,5,15,0,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,
        38,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,40,26,1,0,0,0,40,33,1,0,0,
        0,41,3,1,0,0,0,42,43,5,11,0,0,43,44,5,1,0,0,44,45,3,6,3,0,45,5,1,
        0,0,0,46,47,6,3,-1,0,47,48,3,10,5,0,48,49,3,6,3,4,49,57,1,0,0,0,
        50,57,3,12,6,0,51,52,5,3,0,0,52,53,3,6,3,0,53,54,5,4,0,0,54,57,1,
        0,0,0,55,57,5,11,0,0,56,46,1,0,0,0,56,50,1,0,0,0,56,51,1,0,0,0,56,
        55,1,0,0,0,57,78,1,0,0,0,58,59,10,6,0,0,59,63,5,2,0,0,60,62,3,8,
        4,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,
        1,0,0,0,65,63,1,0,0,0,66,77,3,6,3,6,67,68,10,5,0,0,68,72,5,12,0,
        0,69,71,3,8,4,0,70,69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,
        1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,75,77,3,6,3,5,76,58,1,0,0,0,
        76,67,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,7,1,0,
        0,0,80,78,1,0,0,0,81,82,5,5,0,0,82,9,1,0,0,0,83,91,5,6,0,0,84,91,
        5,7,0,0,85,86,5,12,0,0,86,91,5,8,0,0,87,88,5,12,0,0,88,91,5,9,0,
        0,89,91,5,2,0,0,90,83,1,0,0,0,90,84,1,0,0,0,90,85,1,0,0,0,90,87,
        1,0,0,0,90,89,1,0,0,0,91,11,1,0,0,0,92,94,3,14,7,0,93,92,1,0,0,0,
        94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,13,1,0,0,0,97,99,3,
        16,8,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,14,0,
        0,101,15,1,0,0,0,102,103,5,10,0,0,103,17,1,0,0,0,12,21,30,37,40,
        56,63,72,76,78,90,95,98
    ]

class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=:'", "'#'", "'('", "')'", "'~'", "']'", 
                     "'i.'", "':'", "'/'", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "BOP", 
                      "COMMENT", "NUM", "NL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_flip = 4
    RULE_uop = 5
    RULE_numList = 6
    RULE_num = 7
    RULE_neg = 8

    ruleNames =  [ "program", "statement", "assign", "expr", "flip", "uop", 
                   "numList", "num", "neg" ]

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
    ID=11
    BOP=12
    COMMENT=13
    NUM=14
    NL=15
    WS=16

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
            return self.getToken(gParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.StatementContext)
            else:
                return self.getTypedRuleContext(gParser.StatementContext,i)


        def getRuleIndex(self):
            return gParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 23756) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(gParser.EOF)
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


        def getRuleIndex(self):
            return gParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.NL)
            else:
                return self.getToken(gParser.NL, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSt" ):
                return visitor.visitExprSt(self)
            else:
                return visitor.visitChildren(self)


    class AssignStContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assign(self):
            return self.getTypedRuleContext(gParser.AssignContext,0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.NL)
            else:
                return self.getToken(gParser.NL, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignSt" ):
                return visitor.visitAssignSt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = gParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = gParser.ExprStContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.expr(0)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 27
                    self.match(gParser.NL)
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = gParser.AssignStContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.assign()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 34
                    self.match(gParser.NL)
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


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
            return self.getToken(gParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def getRuleIndex(self):
            return gParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = gParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(gParser.ID)
            self.state = 43
            self.match(gParser.T__0)
            self.state = 44
            self.expr(0)
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
            return gParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnitaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def uop(self):
            return self.getTypedRuleContext(gParser.UopContext,0)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitaryOp" ):
                return visitor.visitUnitaryOp(self)
            else:
                return visitor.visitChildren(self)


    class FilterOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExprContext)
            else:
                return self.getTypedRuleContext(gParser.ExprContext,i)

        def flip(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.FlipContext)
            else:
                return self.getTypedRuleContext(gParser.FlipContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterOp" ):
                return visitor.visitFilterOp(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numList(self):
            return self.getTypedRuleContext(gParser.NumListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class PrioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrio" ):
                return visitor.visitPrio(self)
            else:
                return visitor.visitChildren(self)


    class BinaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ExprContext)
            else:
                return self.getTypedRuleContext(gParser.ExprContext,i)

        def BOP(self):
            return self.getToken(gParser.BOP, 0)
        def flip(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.FlipContext)
            else:
                return self.getTypedRuleContext(gParser.FlipContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 6, 7, 12]:
                localctx = gParser.UnitaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 47
                self.uop()
                self.state = 48
                self.expr(4)
                pass
            elif token in [10, 14]:
                localctx = gParser.ListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.numList()
                pass
            elif token in [3]:
                localctx = gParser.PrioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(gParser.T__2)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(gParser.T__3)
                pass
            elif token in [11]:
                localctx = gParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(gParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = gParser.FilterOpContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 59
                        self.match(gParser.T__1)
                        self.state = 63
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==5:
                            self.state = 60
                            self.flip()
                            self.state = 65
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 66
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = gParser.BinaryOpContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 68
                        self.match(gParser.BOP)
                        self.state = 72
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==5:
                            self.state = 69
                            self.flip()
                            self.state = 74
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 75
                        self.expr(5)
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FlipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_flip

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlip" ):
                return visitor.visitFlip(self)
            else:
                return visitor.visitChildren(self)




    def flip(self):

        localctx = gParser.FlipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_flip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(gParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOP(self):
            return self.getToken(gParser.BOP, 0)

        def getRuleIndex(self):
            return gParser.RULE_uop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUop" ):
                return visitor.visitUop(self)
            else:
                return visitor.visitChildren(self)




    def uop(self):

        localctx = gParser.UopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_uop)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(gParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(gParser.T__6)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.match(gParser.BOP)
                self.state = 86
                self.match(gParser.T__7)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.match(gParser.BOP)
                self.state = 88
                self.match(gParser.T__8)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.match(gParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.NumContext)
            else:
                return self.getTypedRuleContext(gParser.NumContext,i)


        def getRuleIndex(self):
            return gParser.RULE_numList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumList" ):
                return visitor.visitNumList(self)
            else:
                return visitor.visitChildren(self)




    def numList(self):

        localctx = gParser.NumListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 92
                    self.num()

                else:
                    raise NoViableAltException(self)
                self.state = 95 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(gParser.NUM, 0)

        def neg(self):
            return self.getTypedRuleContext(gParser.NegContext,0)


        def getRuleIndex(self):
            return gParser.RULE_num

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = gParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 97
                self.neg()


            self.state = 100
            self.match(gParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_neg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg" ):
                return visitor.visitNeg(self)
            else:
                return visitor.visitChildren(self)




    def neg(self):

        localctx = gParser.NegContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_neg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(gParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         





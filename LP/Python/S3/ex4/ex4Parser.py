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
        4,1,20,97,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        5,4,44,8,4,10,4,12,4,47,9,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,76,8,5,1,6,1,6,1,6,3,6,81,8,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,92,8,6,10,6,12,6,95,9,6,1,6,0,1,12,7,0,2,4,6,8,
        10,12,0,2,1,0,13,14,1,0,15,16,102,0,17,1,0,0,0,2,29,1,0,0,0,4,31,
        1,0,0,0,6,35,1,0,0,0,8,38,1,0,0,0,10,75,1,0,0,0,12,80,1,0,0,0,14,
        16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,
        0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,3,
        4,2,0,23,24,5,19,0,0,24,30,1,0,0,0,25,26,3,6,3,0,26,27,5,19,0,0,
        27,30,1,0,0,0,28,30,3,8,4,0,29,22,1,0,0,0,29,25,1,0,0,0,29,28,1,
        0,0,0,30,3,1,0,0,0,31,32,5,18,0,0,32,33,5,1,0,0,33,34,3,12,6,0,34,
        5,1,0,0,0,35,36,5,2,0,0,36,37,3,12,6,0,37,7,1,0,0,0,38,39,5,3,0,
        0,39,40,3,10,5,0,40,41,5,4,0,0,41,45,5,19,0,0,42,44,3,2,1,0,43,42,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,1,0,0,0,
        47,45,1,0,0,0,48,49,5,5,0,0,49,50,5,19,0,0,50,9,1,0,0,0,51,52,3,
        12,6,0,52,53,5,6,0,0,53,54,3,12,6,0,54,76,1,0,0,0,55,56,3,12,6,0,
        56,57,5,7,0,0,57,58,3,12,6,0,58,76,1,0,0,0,59,60,3,12,6,0,60,61,
        5,8,0,0,61,62,3,12,6,0,62,76,1,0,0,0,63,64,3,12,6,0,64,65,5,9,0,
        0,65,66,3,12,6,0,66,76,1,0,0,0,67,68,3,12,6,0,68,69,5,10,0,0,69,
        70,3,12,6,0,70,76,1,0,0,0,71,72,3,12,6,0,72,73,5,11,0,0,73,74,3,
        12,6,0,74,76,1,0,0,0,75,51,1,0,0,0,75,55,1,0,0,0,75,59,1,0,0,0,75,
        63,1,0,0,0,75,67,1,0,0,0,75,71,1,0,0,0,76,11,1,0,0,0,77,78,6,6,-1,
        0,78,81,5,17,0,0,79,81,5,18,0,0,80,77,1,0,0,0,80,79,1,0,0,0,81,93,
        1,0,0,0,82,83,10,5,0,0,83,84,5,12,0,0,84,92,3,12,6,5,85,86,10,4,
        0,0,86,87,7,0,0,0,87,92,3,12,6,5,88,89,10,3,0,0,89,90,7,1,0,0,90,
        92,3,12,6,4,91,82,1,0,0,0,91,85,1,0,0,0,91,88,1,0,0,0,92,95,1,0,
        0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,13,1,0,0,0,95,93,1,0,0,0,7,17,
        29,45,75,80,91,93
    ]

class ex4Parser ( Parser ):

    grammarFileName = "ex4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'write'", "'if'", "'then'", "'end'", 
                     "'='", "'<>'", "'<='", "'>='", "'<'", "'>'", "'^'", 
                     "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "ID", "NL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_write = 3
    RULE_cond = 4
    RULE_boolexpr = 5
    RULE_expr = 6

    ruleNames =  [ "program", "statement", "assign", "write", "cond", "boolexpr", 
                   "expr" ]

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
    NUM=17
    ID=18
    NL=19
    WS=20

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262156) != 0):
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.assign()
                self.state = 23
                self.match(ex4Parser.NL)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.write()
                self.state = 26
                self.match(ex4Parser.NL)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.cond()
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
            self.state = 31
            self.match(ex4Parser.ID)
            self.state = 32
            self.match(ex4Parser.T__0)
            self.state = 33
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
            self.state = 35
            self.match(ex4Parser.T__1)
            self.state = 36
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
            self.state = 38
            self.match(ex4Parser.T__2)
            self.state = 39
            self.boolexpr()
            self.state = 40
            self.match(ex4Parser.T__3)
            self.state = 41
            self.match(ex4Parser.NL)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262156) != 0):
                self.state = 42
                self.statement()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(ex4Parser.T__4)
            self.state = 49
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
        self.enterRule(localctx, 10, self.RULE_boolexpr)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(ex4Parser.T__5)
                self.state = 53
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.expr(0)
                self.state = 56
                self.match(ex4Parser.T__6)
                self.state = 57
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(ex4Parser.T__7)
                self.state = 61
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(ex4Parser.T__8)
                self.state = 65
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(ex4Parser.T__9)
                self.state = 69
                self.expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.expr(0)
                self.state = 72
                self.match(ex4Parser.T__10)
                self.state = 73
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = ex4Parser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 78
                self.match(ex4Parser.NUM)
                pass
            elif token in [18]:
                localctx = ex4Parser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.match(ex4Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ex4Parser.PotContext(self, ex4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 83
                        self.match(ex4Parser.T__11)
                        self.state = 84
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = ex4Parser.MultDivContext(self, ex4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 86
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = ex4Parser.SumSubContext(self, ex4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 89
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 90
                        self.expr(4)
                        pass

             
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self._predicates[6] = self.expr_sempred
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
         





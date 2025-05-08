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
        4,1,13,78,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,5,1,23,8,1,10,1,12,1,26,
        9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,2,1,2,1,2,5,
        2,42,8,2,10,2,12,2,45,9,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,
        9,2,1,2,5,2,57,8,2,10,2,12,2,60,9,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,71,8,4,1,5,4,5,74,8,5,11,5,12,5,75,1,5,0,1,4,6,0,2,4,
        6,8,10,0,0,84,0,15,1,0,0,0,2,20,1,0,0,0,4,36,1,0,0,0,6,61,1,0,0,
        0,8,70,1,0,0,0,10,73,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,
        0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,
        19,5,0,0,1,19,1,1,0,0,0,20,24,3,4,2,0,21,23,5,12,0,0,22,21,1,0,0,
        0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,0,0,0,26,24,1,
        0,0,0,27,28,6,2,-1,0,28,29,3,8,4,0,29,30,3,4,2,3,30,37,1,0,0,0,31,
        37,3,10,5,0,32,33,5,2,0,0,33,34,3,4,2,0,34,35,5,3,0,0,35,37,1,0,
        0,0,36,27,1,0,0,0,36,31,1,0,0,0,36,32,1,0,0,0,37,58,1,0,0,0,38,39,
        10,5,0,0,39,43,5,1,0,0,40,42,3,6,3,0,41,40,1,0,0,0,42,45,1,0,0,0,
        43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,57,3,
        4,2,5,47,48,10,4,0,0,48,52,5,9,0,0,49,51,3,6,3,0,50,49,1,0,0,0,51,
        54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,
        0,55,57,3,4,2,4,56,38,1,0,0,0,56,47,1,0,0,0,57,60,1,0,0,0,58,56,
        1,0,0,0,58,59,1,0,0,0,59,5,1,0,0,0,60,58,1,0,0,0,61,62,5,4,0,0,62,
        7,1,0,0,0,63,71,5,5,0,0,64,71,5,6,0,0,65,66,5,9,0,0,66,71,5,7,0,
        0,67,68,5,9,0,0,68,71,5,8,0,0,69,71,5,1,0,0,70,63,1,0,0,0,70,64,
        1,0,0,0,70,65,1,0,0,0,70,67,1,0,0,0,70,69,1,0,0,0,71,9,1,0,0,0,72,
        74,5,11,0,0,73,72,1,0,0,0,74,75,1,0,0,0,75,73,1,0,0,0,75,76,1,0,
        0,0,76,11,1,0,0,0,9,15,24,36,43,52,56,58,70,75
    ]

class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'('", "')'", "'~'", "']'", "'i.'", 
                     "':'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOP", "COMMENT", "NUM", "NL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_flip = 3
    RULE_uop = 4
    RULE_numList = 5

    ruleNames =  [ "program", "statement", "expr", "flip", "uop", "numList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    BOP=9
    COMMENT=10
    NUM=11
    NL=12
    WS=13

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2662) != 0):
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
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



    def statement(self):

        localctx = gParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            localctx = gParser.ExprStContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.expr(0)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 21
                self.match(gParser.NL)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 5, 6, 9]:
                localctx = gParser.UnitaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 28
                self.uop()
                self.state = 29
                self.expr(3)
                pass
            elif token in [11]:
                localctx = gParser.ListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.numList()
                pass
            elif token in [2]:
                localctx = gParser.PrioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(gParser.T__1)
                self.state = 33
                self.expr(0)
                self.state = 34
                self.match(gParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 58
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 56
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = gParser.FilterOpContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 39
                        self.match(gParser.T__0)
                        self.state = 43
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==4:
                            self.state = 40
                            self.flip()
                            self.state = 45
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 46
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = gParser.BinaryOpContext(self, gParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 48
                        self.match(gParser.BOP)
                        self.state = 52
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==4:
                            self.state = 49
                            self.flip()
                            self.state = 54
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 55
                        self.expr(4)
                        pass

             
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_flip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(gParser.T__3)
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
        self.enterRule(localctx, 8, self.RULE_uop)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(gParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(gParser.T__5)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(gParser.BOP)
                self.state = 66
                self.match(gParser.T__6)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.match(gParser.BOP)
                self.state = 68
                self.match(gParser.T__7)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.match(gParser.T__0)
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

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(gParser.NUM)
            else:
                return self.getToken(gParser.NUM, i)

        def getRuleIndex(self):
            return gParser.RULE_numList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumList" ):
                return visitor.visitNumList(self)
            else:
                return visitor.visitChildren(self)




    def numList(self):

        localctx = gParser.NumListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 72
                    self.match(gParser.NUM)

                else:
                    raise NoViableAltException(self)
                self.state = 75 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self._predicates[2] = self.expr_sempred
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
         





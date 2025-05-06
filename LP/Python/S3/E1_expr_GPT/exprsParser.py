# Generated from exprs.g4 by ANTLR 4.13.2
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
        4,1,6,45,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,3,1,3,1,3,1,3,
        3,3,43,8,3,1,3,0,2,2,4,4,0,2,4,6,0,0,45,0,8,1,0,0,0,2,10,1,0,0,0,
        4,24,1,0,0,0,6,42,1,0,0,0,8,9,3,2,1,0,9,1,1,0,0,0,10,11,6,1,-1,0,
        11,12,3,4,2,0,12,21,1,0,0,0,13,14,10,3,0,0,14,15,5,1,0,0,15,20,3,
        4,2,0,16,17,10,2,0,0,17,18,5,1,0,0,18,20,3,4,2,0,19,13,1,0,0,0,19,
        16,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,3,1,0,0,
        0,23,21,1,0,0,0,24,25,6,2,-1,0,25,26,3,6,3,0,26,35,1,0,0,0,27,28,
        10,3,0,0,28,29,5,2,0,0,29,34,3,6,3,0,30,31,10,2,0,0,31,32,5,3,0,
        0,32,34,3,6,3,0,33,27,1,0,0,0,33,30,1,0,0,0,34,37,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,5,1,0,0,0,37,35,1,0,0,0,38,39,5,5,0,0,39,
        40,5,4,0,0,40,43,3,6,3,0,41,43,5,5,0,0,42,38,1,0,0,0,42,41,1,0,0,
        0,43,7,1,0,0,0,5,19,21,33,35,42
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "WS" ]

    RULE_expr = 0
    RULE_addExpr = 1
    RULE_mulExpr = 2
    RULE_powExpr = 3

    ruleNames =  [ "expr", "addExpr", "mulExpr", "powExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUM=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self):
            return self.getTypedRuleContext(exprsParser.AddExprContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_expr




    def expr(self):

        localctx = exprsParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.addExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_addExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addExpr(self):
            return self.getTypedRuleContext(exprsParser.AddExprContext,0)

        def mulExpr(self):
            return self.getTypedRuleContext(exprsParser.MulExprContext,0)



    class RestaContext(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def addExpr(self):
            return self.getTypedRuleContext(exprsParser.AddExprContext,0)

        def mulExpr(self):
            return self.getTypedRuleContext(exprsParser.MulExprContext,0)



    class ToMulContext(AddExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.AddExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(exprsParser.MulExprContext,0)




    def addExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.AddExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_addExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = exprsParser.ToMulContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 11
            self.mulExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 19
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.SumaContext(self, exprsParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 13
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 14
                        self.match(exprsParser.T__0)
                        self.state = 15
                        self.mulExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.RestaContext(self, exprsParser.AddExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_addExpr)
                        self.state = 16
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 17
                        self.match(exprsParser.T__0)
                        self.state = 18
                        self.mulExpr(0)
                        pass

             
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_mulExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(exprsParser.MulExprContext,0)

        def powExpr(self):
            return self.getTypedRuleContext(exprsParser.PowExprContext,0)



    class MultContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mulExpr(self):
            return self.getTypedRuleContext(exprsParser.MulExprContext,0)

        def powExpr(self):
            return self.getTypedRuleContext(exprsParser.PowExprContext,0)



    class ToPowContext(MulExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.MulExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def powExpr(self):
            return self.getTypedRuleContext(exprsParser.PowExprContext,0)




    def mulExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.MulExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_mulExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = exprsParser.ToPowContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 25
            self.powExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.MultContext(self, exprsParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 27
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 28
                        self.match(exprsParser.T__1)
                        self.state = 29
                        self.powExpr()
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.DivContext(self, exprsParser.MulExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mulExpr)
                        self.state = 30
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 31
                        self.match(exprsParser.T__2)
                        self.state = 32
                        self.powExpr()
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PowExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_powExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PowContext(PowExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.PowExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprsParser.NUM, 0)
        def powExpr(self):
            return self.getTypedRuleContext(exprsParser.PowExprContext,0)



    class ToNUMContext(PowExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.PowExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprsParser.NUM, 0)



    def powExpr(self):

        localctx = exprsParser.PowExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_powExpr)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = exprsParser.PowContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(exprsParser.NUM)
                self.state = 39
                self.match(exprsParser.T__3)
                self.state = 40
                self.powExpr()
                pass

            elif la_ == 2:
                localctx = exprsParser.ToNUMContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(exprsParser.NUM)
                pass


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
        self._predicates[1] = self.addExpr_sempred
        self._predicates[2] = self.mulExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def addExpr_sempred(self, localctx:AddExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mulExpr_sempred(self, localctx:MulExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





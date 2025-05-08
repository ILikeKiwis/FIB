# Generated from ex8.g4 by ANTLR 4.13.2
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
        4,1,28,201,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,
        42,8,1,1,1,1,1,1,1,5,1,47,8,1,10,1,12,1,50,9,1,1,1,1,1,1,1,1,2,1,
        2,1,2,5,2,58,8,2,10,2,12,2,61,9,2,1,3,1,3,1,3,5,3,66,8,3,10,3,12,
        3,69,9,3,1,3,1,3,5,3,73,8,3,10,3,12,3,76,9,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,5,4,86,8,4,10,4,12,4,89,9,4,1,4,1,4,5,4,93,8,4,10,4,
        12,4,96,9,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,104,8,4,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,118,8,7,10,7,12,7,121,9,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,5,8,130,8,8,10,8,12,8,133,9,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,161,8,9,1,10,1,10,1,10,3,10,
        166,8,10,1,10,1,10,1,11,1,11,1,11,5,11,173,8,11,10,11,12,11,176,
        9,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,3,13,185,8,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,196,8,13,10,13,12,13,199,
        9,13,1,13,0,1,26,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,2,1,0,
        21,22,1,0,23,24,213,0,31,1,0,0,0,2,37,1,0,0,0,4,54,1,0,0,0,6,62,
        1,0,0,0,8,103,1,0,0,0,10,105,1,0,0,0,12,109,1,0,0,0,14,112,1,0,0,
        0,16,124,1,0,0,0,18,160,1,0,0,0,20,162,1,0,0,0,22,169,1,0,0,0,24,
        177,1,0,0,0,26,184,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,33,1,0,
        0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,
        3,6,3,0,35,36,5,0,0,1,36,1,1,0,0,0,37,38,5,1,0,0,38,39,5,26,0,0,
        39,41,5,2,0,0,40,42,3,4,2,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,1,
        0,0,0,43,44,5,3,0,0,44,48,5,27,0,0,45,47,3,8,4,0,46,45,1,0,0,0,47,
        50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,
        0,51,52,5,4,0,0,52,53,5,27,0,0,53,3,1,0,0,0,54,59,5,26,0,0,55,56,
        5,5,0,0,56,58,5,26,0,0,57,55,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,
        59,60,1,0,0,0,60,5,1,0,0,0,61,59,1,0,0,0,62,63,5,6,0,0,63,67,5,27,
        0,0,64,66,3,8,4,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,
        1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,74,5,4,0,0,71,73,5,27,0,0,
        72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,7,1,0,
        0,0,76,74,1,0,0,0,77,78,3,10,5,0,78,79,5,27,0,0,79,104,1,0,0,0,80,
        81,3,12,6,0,81,82,5,27,0,0,82,104,1,0,0,0,83,87,3,14,7,0,84,86,5,
        27,0,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,
        104,1,0,0,0,89,87,1,0,0,0,90,94,3,16,8,0,91,93,5,27,0,0,92,91,1,
        0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,104,1,0,0,0,96,
        94,1,0,0,0,97,98,3,20,10,0,98,99,5,27,0,0,99,104,1,0,0,0,100,101,
        3,24,12,0,101,102,5,27,0,0,102,104,1,0,0,0,103,77,1,0,0,0,103,80,
        1,0,0,0,103,83,1,0,0,0,103,90,1,0,0,0,103,97,1,0,0,0,103,100,1,0,
        0,0,104,9,1,0,0,0,105,106,5,26,0,0,106,107,5,7,0,0,107,108,3,26,
        13,0,108,11,1,0,0,0,109,110,5,8,0,0,110,111,3,26,13,0,111,13,1,0,
        0,0,112,113,5,9,0,0,113,114,3,18,9,0,114,115,5,10,0,0,115,119,5,
        27,0,0,116,118,3,8,4,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,1,
        0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,119,1,0,0,0,122,123,5,
        4,0,0,123,15,1,0,0,0,124,125,5,11,0,0,125,126,3,18,9,0,126,127,5,
        12,0,0,127,131,5,27,0,0,128,130,3,8,4,0,129,128,1,0,0,0,130,133,
        1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,
        1,0,0,0,134,135,5,4,0,0,135,17,1,0,0,0,136,137,3,26,13,0,137,138,
        5,13,0,0,138,139,3,26,13,0,139,161,1,0,0,0,140,141,3,26,13,0,141,
        142,5,14,0,0,142,143,3,26,13,0,143,161,1,0,0,0,144,145,3,26,13,0,
        145,146,5,15,0,0,146,147,3,26,13,0,147,161,1,0,0,0,148,149,3,26,
        13,0,149,150,5,16,0,0,150,151,3,26,13,0,151,161,1,0,0,0,152,153,
        3,26,13,0,153,154,5,17,0,0,154,155,3,26,13,0,155,161,1,0,0,0,156,
        157,3,26,13,0,157,158,5,18,0,0,158,159,3,26,13,0,159,161,1,0,0,0,
        160,136,1,0,0,0,160,140,1,0,0,0,160,144,1,0,0,0,160,148,1,0,0,0,
        160,152,1,0,0,0,160,156,1,0,0,0,161,19,1,0,0,0,162,163,5,26,0,0,
        163,165,5,2,0,0,164,166,3,22,11,0,165,164,1,0,0,0,165,166,1,0,0,
        0,166,167,1,0,0,0,167,168,5,3,0,0,168,21,1,0,0,0,169,174,3,26,13,
        0,170,171,5,5,0,0,171,173,3,26,13,0,172,170,1,0,0,0,173,176,1,0,
        0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,23,1,0,0,0,176,174,1,0,0,
        0,177,178,5,19,0,0,178,179,3,26,13,0,179,25,1,0,0,0,180,181,6,13,
        -1,0,181,185,5,25,0,0,182,185,3,20,10,0,183,185,5,26,0,0,184,180,
        1,0,0,0,184,182,1,0,0,0,184,183,1,0,0,0,185,197,1,0,0,0,186,187,
        10,6,0,0,187,188,5,20,0,0,188,196,3,26,13,6,189,190,10,5,0,0,190,
        191,7,0,0,0,191,196,3,26,13,6,192,193,10,4,0,0,193,194,7,1,0,0,194,
        196,3,26,13,5,195,186,1,0,0,0,195,189,1,0,0,0,195,192,1,0,0,0,196,
        199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,27,1,0,0,0,199,197,
        1,0,0,0,17,31,41,48,59,67,74,87,94,103,119,131,160,165,174,184,195,
        197
    ]

class ex8Parser ( Parser ):

    grammarFileName = "ex8.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "'('", "')'", "'end'", "','", 
                     "'main'", "':='", "'write'", "'if'", "'then'", "'while'", 
                     "'do'", "'='", "'<>'", "'<='", "'>='", "'<'", "'>'", 
                     "'return'", "'^'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "ID", "NL", "WS" ]

    RULE_program = 0
    RULE_func = 1
    RULE_paramList = 2
    RULE_main = 3
    RULE_statement = 4
    RULE_assign = 5
    RULE_write = 6
    RULE_cond = 7
    RULE_while = 8
    RULE_boolexpr = 9
    RULE_funcCall = 10
    RULE_arglist = 11
    RULE_retSt = 12
    RULE_expr = 13

    ruleNames =  [ "program", "func", "paramList", "main", "statement", 
                   "assign", "write", "cond", "while", "boolexpr", "funcCall", 
                   "arglist", "retSt", "expr" ]

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
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    NUM=25
    ID=26
    NL=27
    WS=28

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

        def main(self):
            return self.getTypedRuleContext(ex8Parser.MainContext,0)


        def EOF(self):
            return self.getToken(ex8Parser.EOF, 0)

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.FuncContext)
            else:
                return self.getTypedRuleContext(ex8Parser.FuncContext,i)


        def getRuleIndex(self):
            return ex8Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ex8Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 28
                self.func()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.main()
            self.state = 35
            self.match(ex8Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ex8Parser.ID, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ex8Parser.NL)
            else:
                return self.getToken(ex8Parser.NL, i)

        def paramList(self):
            return self.getTypedRuleContext(ex8Parser.ParamListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ex8Parser.StatementContext,i)


        def getRuleIndex(self):
            return ex8Parser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ex8Parser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ex8Parser.T__0)
            self.state = 38
            self.match(ex8Parser.ID)
            self.state = 39
            self.match(ex8Parser.T__1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 40
                self.paramList()


            self.state = 43
            self.match(ex8Parser.T__2)
            self.state = 44
            self.match(ex8Parser.NL)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67635968) != 0):
                self.state = 45
                self.statement()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.match(ex8Parser.T__3)
            self.state = 52
            self.match(ex8Parser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ex8Parser.ID)
            else:
                return self.getToken(ex8Parser.ID, i)

        def getRuleIndex(self):
            return ex8Parser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = ex8Parser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ex8Parser.ID)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 55
                self.match(ex8Parser.T__4)
                self.state = 56
                self.match(ex8Parser.ID)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ex8Parser.NL)
            else:
                return self.getToken(ex8Parser.NL, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ex8Parser.StatementContext,i)


        def getRuleIndex(self):
            return ex8Parser.RULE_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = ex8Parser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ex8Parser.T__5)
            self.state = 63
            self.match(ex8Parser.NL)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67635968) != 0):
                self.state = 64
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(ex8Parser.T__3)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 71
                self.match(ex8Parser.NL)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getTypedRuleContext(ex8Parser.AssignContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ex8Parser.NL)
            else:
                return self.getToken(ex8Parser.NL, i)

        def write(self):
            return self.getTypedRuleContext(ex8Parser.WriteContext,0)


        def cond(self):
            return self.getTypedRuleContext(ex8Parser.CondContext,0)


        def while_(self):
            return self.getTypedRuleContext(ex8Parser.WhileContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(ex8Parser.FuncCallContext,0)


        def retSt(self):
            return self.getTypedRuleContext(ex8Parser.RetStContext,0)


        def getRuleIndex(self):
            return ex8Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ex8Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.assign()
                self.state = 78
                self.match(ex8Parser.NL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.write()
                self.state = 81
                self.match(ex8Parser.NL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.cond()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 84
                    self.match(ex8Parser.NL)
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.while_()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 91
                    self.match(ex8Parser.NL)
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.funcCall()
                self.state = 98
                self.match(ex8Parser.NL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 100
                self.retSt()
                self.state = 101
                self.match(ex8Parser.NL)
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
            return self.getToken(ex8Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ex8Parser.ExprContext,0)


        def getRuleIndex(self):
            return ex8Parser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ex8Parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ex8Parser.ID)
            self.state = 106
            self.match(ex8Parser.T__6)
            self.state = 107
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
            return self.getTypedRuleContext(ex8Parser.ExprContext,0)


        def getRuleIndex(self):
            return ex8Parser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = ex8Parser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ex8Parser.T__7)
            self.state = 110
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
            return self.getTypedRuleContext(ex8Parser.BoolexprContext,0)


        def NL(self):
            return self.getToken(ex8Parser.NL, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ex8Parser.StatementContext,i)


        def getRuleIndex(self):
            return ex8Parser.RULE_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = ex8Parser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(ex8Parser.T__8)
            self.state = 113
            self.boolexpr()
            self.state = 114
            self.match(ex8Parser.T__9)
            self.state = 115
            self.match(ex8Parser.NL)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67635968) != 0):
                self.state = 116
                self.statement()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(ex8Parser.T__3)
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
            return self.getTypedRuleContext(ex8Parser.BoolexprContext,0)


        def NL(self):
            return self.getToken(ex8Parser.NL, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.StatementContext)
            else:
                return self.getTypedRuleContext(ex8Parser.StatementContext,i)


        def getRuleIndex(self):
            return ex8Parser.RULE_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = ex8Parser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ex8Parser.T__10)
            self.state = 125
            self.boolexpr()
            self.state = 126
            self.match(ex8Parser.T__11)
            self.state = 127
            self.match(ex8Parser.NL)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67635968) != 0):
                self.state = 128
                self.statement()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(ex8Parser.T__3)
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
                return self.getTypedRuleContexts(ex8Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex8Parser.ExprContext,i)


        def getRuleIndex(self):
            return ex8Parser.RULE_boolexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolexpr" ):
                return visitor.visitBoolexpr(self)
            else:
                return visitor.visitChildren(self)




    def boolexpr(self):

        localctx = ex8Parser.BoolexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolexpr)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.expr(0)
                self.state = 137
                self.match(ex8Parser.T__12)
                self.state = 138
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.expr(0)
                self.state = 141
                self.match(ex8Parser.T__13)
                self.state = 142
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.expr(0)
                self.state = 145
                self.match(ex8Parser.T__14)
                self.state = 146
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(ex8Parser.T__15)
                self.state = 150
                self.expr(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 152
                self.expr(0)
                self.state = 153
                self.match(ex8Parser.T__16)
                self.state = 154
                self.expr(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.expr(0)
                self.state = 157
                self.match(ex8Parser.T__17)
                self.state = 158
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ex8Parser.ID, 0)

        def arglist(self):
            return self.getTypedRuleContext(ex8Parser.ArglistContext,0)


        def getRuleIndex(self):
            return ex8Parser.RULE_funcCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = ex8Parser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ex8Parser.ID)
            self.state = 163
            self.match(ex8Parser.T__1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25 or _la==26:
                self.state = 164
                self.arglist()


            self.state = 167
            self.match(ex8Parser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex8Parser.ExprContext,i)


        def getRuleIndex(self):
            return ex8Parser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = ex8Parser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.expr(0)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 170
                self.match(ex8Parser.T__4)
                self.state = 171
                self.expr(0)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetStContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ex8Parser.ExprContext,0)


        def getRuleIndex(self):
            return ex8Parser.RULE_retSt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetSt" ):
                return visitor.visitRetSt(self)
            else:
                return visitor.visitChildren(self)




    def retSt(self):

        localctx = ex8Parser.RetStContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_retSt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ex8Parser.T__18)
            self.state = 178
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
            return ex8Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex8Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumSub" ):
                return visitor.visitSumSub(self)
            else:
                return visitor.visitChildren(self)


    class PotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex8Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPot" ):
                return visitor.visitPot(self)
            else:
                return visitor.visitChildren(self)


    class FExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcCall(self):
            return self.getTypedRuleContext(ex8Parser.FuncCallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFExpr" ):
                return visitor.visitFExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ex8Parser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ex8Parser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class MultDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ex8Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ex8Parser.ExprContext)
            else:
                return self.getTypedRuleContext(ex8Parser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultDiv" ):
                return visitor.visitMultDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ex8Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = ex8Parser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 181
                self.match(ex8Parser.NUM)
                pass

            elif la_ == 2:
                localctx = ex8Parser.FExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.funcCall()
                pass

            elif la_ == 3:
                localctx = ex8Parser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.match(ex8Parser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 195
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = ex8Parser.PotContext(self, ex8Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 186
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 187
                        self.match(ex8Parser.T__19)
                        self.state = 188
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ex8Parser.MultDivContext(self, ex8Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 189
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 190
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ex8Parser.SumSubContext(self, ex8Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 192
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 193
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 194
                        self.expr(5)
                        pass

             
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self._predicates[13] = self.expr_sempred
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
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         





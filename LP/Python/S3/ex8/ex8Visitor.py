# Generated from ex8.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ex8Parser import ex8Parser
else:
    from ex8Parser import ex8Parser

# This class defines a complete generic visitor for a parse tree produced by ex8Parser.

class ex8Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by ex8Parser#program.
    def visitProgram(self, ctx:ex8Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#func.
    def visitFunc(self, ctx:ex8Parser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#paramList.
    def visitParamList(self, ctx:ex8Parser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#main.
    def visitMain(self, ctx:ex8Parser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#statement.
    def visitStatement(self, ctx:ex8Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#assign.
    def visitAssign(self, ctx:ex8Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#write.
    def visitWrite(self, ctx:ex8Parser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#cond.
    def visitCond(self, ctx:ex8Parser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#while.
    def visitWhile(self, ctx:ex8Parser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#boolexpr.
    def visitBoolexpr(self, ctx:ex8Parser.BoolexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#funcCall.
    def visitFuncCall(self, ctx:ex8Parser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#arglist.
    def visitArglist(self, ctx:ex8Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#retSt.
    def visitRetSt(self, ctx:ex8Parser.RetStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#SumSub.
    def visitSumSub(self, ctx:ex8Parser.SumSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#Pot.
    def visitPot(self, ctx:ex8Parser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#fExpr.
    def visitFExpr(self, ctx:ex8Parser.FExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#Num.
    def visitNum(self, ctx:ex8Parser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#Id.
    def visitId(self, ctx:ex8Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex8Parser#MultDiv.
    def visitMultDiv(self, ctx:ex8Parser.MultDivContext):
        return self.visitChildren(ctx)



del ex8Parser
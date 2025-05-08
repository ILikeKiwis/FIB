# Generated from ex4.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ex4Parser import ex4Parser
else:
    from ex4Parser import ex4Parser

# This class defines a complete generic visitor for a parse tree produced by ex4Parser.

class ex4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by ex4Parser#program.
    def visitProgram(self, ctx:ex4Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#statement.
    def visitStatement(self, ctx:ex4Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#assign.
    def visitAssign(self, ctx:ex4Parser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#write.
    def visitWrite(self, ctx:ex4Parser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#cond.
    def visitCond(self, ctx:ex4Parser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#while.
    def visitWhile(self, ctx:ex4Parser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#boolexpr.
    def visitBoolexpr(self, ctx:ex4Parser.BoolexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#SumSub.
    def visitSumSub(self, ctx:ex4Parser.SumSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#Pot.
    def visitPot(self, ctx:ex4Parser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#Num.
    def visitNum(self, ctx:ex4Parser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#Id.
    def visitId(self, ctx:ex4Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ex4Parser#MultDiv.
    def visitMultDiv(self, ctx:ex4Parser.MultDivContext):
        return self.visitChildren(ctx)



del ex4Parser
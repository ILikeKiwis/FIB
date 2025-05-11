# Generated from g.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gParser import gParser
else:
    from gParser import gParser

# This class defines a complete generic visitor for a parse tree produced by gParser.

class gVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gParser#program.
    def visitProgram(self, ctx:gParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#ExprSt.
    def visitExprSt(self, ctx:gParser.ExprStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#AssignSt.
    def visitAssignSt(self, ctx:gParser.AssignStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#assign.
    def visitAssign(self, ctx:gParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#UnitaryOp.
    def visitUnitaryOp(self, ctx:gParser.UnitaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#FilterOp.
    def visitFilterOp(self, ctx:gParser.FilterOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#List.
    def visitList(self, ctx:gParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#Id.
    def visitId(self, ctx:gParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#Prio.
    def visitPrio(self, ctx:gParser.PrioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#BinaryOp.
    def visitBinaryOp(self, ctx:gParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#flip.
    def visitFlip(self, ctx:gParser.FlipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#uop.
    def visitUop(self, ctx:gParser.UopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#numList.
    def visitNumList(self, ctx:gParser.NumListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#num.
    def visitNum(self, ctx:gParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#neg.
    def visitNeg(self, ctx:gParser.NegContext):
        return self.visitChildren(ctx)



del gParser
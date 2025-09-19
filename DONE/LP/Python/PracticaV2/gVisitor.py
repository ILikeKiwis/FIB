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


    # Visit a parse tree produced by gParser#AssignSt.
    def visitAssignSt(self, ctx:gParser.AssignStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#ExprSt.
    def visitExprSt(self, ctx:gParser.ExprStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#assign.
    def visitAssign(self, ctx:gParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#BinaryOP.
    def visitBinaryOP(self, ctx:gParser.BinaryOPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#MajorOrMinor.
    def visitMajorOrMinor(self, ctx:gParser.MajorOrMinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#IdValue.
    def visitIdValue(self, ctx:gParser.IdValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#ToMinor.
    def visitToMinor(self, ctx:gParser.ToMinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#UnitaryOP.
    def visitUnitaryOP(self, ctx:gParser.UnitaryOPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#FilterOP.
    def visitFilterOP(self, ctx:gParser.FilterOPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#List.
    def visitList(self, ctx:gParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#OnlyUnitary.
    def visitOnlyUnitary(self, ctx:gParser.OnlyUnitaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#Id.
    def visitId(self, ctx:gParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#Identity.
    def visitIdentity(self, ctx:gParser.IdentityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#Prio.
    def visitPrio(self, ctx:gParser.PrioContext):
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
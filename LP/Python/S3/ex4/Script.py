from antlr4 import *
from ex4Lexer import ex4Lexer
from ex4Parser import ex4Parser
from ex4Visitor import ex4Visitor
import sys

class EvalVisitor(ex4Visitor):

    def __init__(self):
        self.vars = {}

    def visitProgram(self, ctx):
       for stm in ctx.statement():
           self.visit(stm)
    
    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.vars[id] = value
    
    def visitWrite(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
    
    def visitCond(self, ctx):
        b = self.visit(ctx.boolexpr())
        if b:
            for stm in ctx.statement():
                self.visit(stm)

    def visitWhile(self, ctx):
        while(self.visit(ctx.boolexpr())):
            for stm in ctx.statement():
                self.visit(stm)
        
    def visitBoolexpr(self, ctx):
        [expr1, operator, expr2] = list(ctx.getChildren())
        op = operator.getText()
        value1 = self.visit(expr1)
        value2 = self.visit(expr2)
        match op:
            case '=':
                return value1 == value2
            case '<>':
                return value1 != value2
            case '<=':
                return value1 <= value2
            case '>=':
                return value1 >= value2
            case '<':
                return value1 < value2
            case '>':
                return value1 > value2
            
    def visitPot(self, ctx):
        [expr1, op, expr2] = list(ctx.getChildren())
        return self.visit(expr1) ** self.visit(expr2)
    
    def visitMultDiv(self, ctx):
        [expr1, op, expr2] = list(ctx.getChildren())
        if op.getText() == '/' :
            return self.visit(expr1) / self.visit(expr2)
        else :
            return self.visit(expr1) * self.visit(expr2)
        
    def visitSumSub(self, ctx):
        [expr1, op, expr2] = list(ctx.getChildren())
        if op.getText() == '-' :
            return self.visit(expr1) - self.visit(expr2)
        else :
            return self.visit(expr1) + self.visit(expr2)

    def visitNum(self, ctx):
        return int(ctx.NUM().getText())
    
    def visitId(self, ctx):
        id = ctx.ID().getText()
        return self.vars.get(id, 0)
        




stream = FileStream(sys.argv[1], encoding="utf-8")

lexer = ex4Lexer(stream)

token_stream = CommonTokenStream(lexer)

parser = ex4Parser(token_stream)

tree = parser.program()

visitor = EvalVisitor()
visitor.visit(tree)
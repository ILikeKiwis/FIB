from antlr4 import *
from ex8Visitor import ex8Visitor
from ex8Parser import ex8Parser

class Return(Exception):
    def __init__(self, value):
        self.value = value

class EvalVisitor(ex8Visitor):
    def __init__(self):
        #Pila de contextos 
        self.contextos = []
        #Diccionario de funciones
        self.funcs = {}
    
    def visitProgram(self, ctx):
        for f in ctx.func():
            self.visit(f)
        self.visit(ctx.main())
    
    def visitFunc(self, ctx):
        id = ctx.ID().getText()
        params = [p.getText() for p in ctx.paramList().ID()] if ctx.paramList() else []
        body = ctx.statement()
        self.funcs[id] = (params, body)

    def visitMain(self, ctx):
        self.contextos.append({})
        for st in ctx.statement():
            self.visit(st)
        self.contextos.pop()
    
    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.contextos[-1][id] = value
    
    def visitWrite(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
    
    def visitCond(self, ctx):
        if self.visit(ctx.boolexpr()):
            for st in ctx.statement():
                self.visit(st)
    
    def visitWhile(self, ctx):
        while self.visit(ctx.boolexpr()):
            for st in ctx.statement():
                self.visit(st)

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
            
    def visitFuncCall(self, ctx):
        id = ctx.ID().getText()
        if ctx.arglist():
            argValues = [self.visit(expr) for expr in ctx.arglist().expr()]
        else : 
            argValues = []
        params, body = self.funcs[id]

        contexto = dict(zip(params, argValues))
        self.contextos.append(contexto)
        
        try:
            for st in body:
                self.visit(st)
        except Return as r:
            self.contextos.pop()
            return r.value
        
        self.contextos.pop()
        

    def visitRetSt(self, ctx):
        value = self.visit(ctx.expr())
        raise Return(value)

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
    
    def visitFExpr(self, ctx):
        return self.visit(ctx.funcCall())
    
    def visitId(self, ctx):
        id = ctx.ID().getText()
        return self.contextos[-1][id]
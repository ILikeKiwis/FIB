from antlr4 import *
from gVisitor import gVisitor
import numpy as np
from functools import reduce
from operator import add, mul, sub, pow, floordiv, mod

def foldr(func, arr):
    return reduce(lambda acc, x: func(x, acc), arr[::-1])

class Evaler(gVisitor):

    def __init__(self):
        self.vars = {}

    def visitProgram(self, ctx):
        for st in ctx.statement():
            self.visit(st)

    def visitExprSt(self, ctx):
        print("   ", ctx.expr().getText())
        ret = self.visit(ctx.expr())
        print (ret)

    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = ctx.expr()
        self.vars[id] = value
    
    def visitFilterOp(self, ctx):
        print("Entro en filter op")
        expr1 = ctx.expr(0)
        expr2 = ctx.expr(1)
        n_flips = len(ctx.flip())
        flip = n_flips % 2
        if flip:
            value1 = self.visit(expr2)
            value2 = self.visit(expr1)
        else:
            value1 = self.visit(expr1)
            value2 = self.visit(expr2)
        try :
            return np.repeat(value2, value1)
        except Exception as e:
            print("lenght error")
            return [-0]

    def visitBinaryOp(self, ctx):
        expr1 = ctx.expr(0)
        expr2 = ctx.expr(1)
        op = ctx.BOP().getText()
        n_flips = len(ctx.flip())
        flip = n_flips % 2
        if flip:
            value1 = self.visit(expr2)
            value2 = self.visit(expr1)
        else:
            value1 = self.visit(expr1)
            value2 = self.visit(expr2)
        try :
            match op:
                case '+':
                    ret = value1 + value2
                case '-':
                    ret = value1 - value2
                case '*':
                    ret = value1 * value2
                case '%':
                    ret = value1 // value2
                case '^':
                    ret = value1 ** value2
                case '|':
                    ret = value2 % value1
                case ',':
                    ret = np.hstack((value1, value2))
                case '{':
                    ret = np.take(value2, value1)
                case '<':
                    ret = np.less(value1, value2)
                case '<=':
                    ret = np.less_equal(value1, value2)
                case '>':
                    ret = np.greater(value1, value2)
                case '>=':
                    ret = np.greater_equal(value1, value2)
                case '=' : 
                    ret = np.equal(value1, value2)
                case '<>':
                    ret = np.not_equal(value1, value2)
            return ret
        except Exception as e:
            print("lenght error")
            return [-0]
    
    def visitUnitaryOp(self, ctx):
        uop_ctx = ctx.uop()
        bop = uop_ctx.BOP()
        expr = ctx.expr()

        if bop:
            value = self.visit(expr)
            op = ctx.uop().getText()[-1]
            b = bop.getText()
            if op == ':':
                match b:
                    case '+':
                        ret = value + value
                    case '-':
                        ret = value - value
                    case '*':
                        ret = value * value
                    case '%':
                        ret = value // value
                    case '^':
                        ret = value ** value
                    case '|':
                        ret = value % value
                return ret
            else :
                match b:
                    case '+':
                        ret = foldr(add, value)
                    case '-':
                        ret = foldr(sub, value)
                    case '*':
                        ret = foldr(mul, value)
                    case '%':
                        ret = foldr(floordiv, value)
                    case '^':
                        ret = foldr(pow, value)
                    case '|':
                        ret = foldr(mod, value)
                return ret
        else :
            op = ctx.uop().getText()
            match op:
                case ']':
                    return self.visit(expr)
                case '#':
                    return len(self.visit(expr))
                case 'i.':
                    return np.arange(self.visit(expr))

    
    def visitList(self, ctx):
        l_ctx = ctx.numList()
        return np.array([self.visit(x) for x in l_ctx.num()])

    def visitPrio(self, ctx):
        return self.visit(ctx.expr())
    
    def visitId(self, ctx):
        value = self.vars[ctx.ID().getText()]
        return self.visit(value)
    
    def visitNum(self, ctx):
        a = -1 if ctx.neg() != None else 1
        return a*int(ctx.NUM().getText())

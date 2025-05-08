from antlr4 import *
from gVisitor import gVisitor
import numpy as np

class Evaler(gVisitor):

    def visitProgram(self, ctx):
        for st in ctx.statement():
            self.visit(st)

    def visitExprSt(self, ctx):
        print("   ", ctx.expr().getText())
        ret = self.visit(ctx.expr())
        print (ret)
    
    def visitFilterOp(self, ctx):
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
                        ret = np.add.reduce(value)
                    case '-':
                        ret = np.subtract.reduce(value)
                    case '*':
                        ret = np.multiply.reduce(value)
                    case '%':
                        ret = np.floor_divide.reduce(value)
                    case '^':
                        ret = np.power.reduce(value)
                    case '|':
                        ret = np.mod.reduce(value)
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
        return np.array([int(n.getText()) for n in l_ctx.NUM()])

    def visitPrio(self, ctx):
        return self.visit(ctx.expr())
    
    def visitNum(self, ctx):
        return int(ctx.NUM().getText())

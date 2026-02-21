from functools import reduce
from operator import add, mul, sub, pow, floordiv, mod


import numpy as np


from gVisitor import gVisitor


def foldr(func, arr):
    return reduce(lambda acc, x: func(x, acc), arr[::-1])


class Evaler(gVisitor):
    """
    Classe encarregada d'avaluar els programes en G.
    """

    # Constructora on creem el diccionari de variables (assignacions)
    def __init__(self):
        self.vars = {}

    # Tractem totes les sentencies del programa
    def visitProgram(self, ctx):
        for st in ctx.statement():
            self.visit(st)

    # Diferents tipus de sentencies
    def visitAssignSt(self, ctx):               # Regla AssignSt
        self.visit(ctx.assign())

    def visitExprSt(self, ctx):                 # Regla ExprSt
        ret = self.visit(ctx.expr())
        form = ["_"+str(abs(x)) if x < 0 else str(abs(x)) for x in ret]  # Els valors negatius es representen amb un _
        print(*form)

    def visitCom(self, ctx):                    # Regla Com
        ret = self.visit(ctx.comment())

    # Context Assign, on assignem valors a diferents IDs
    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = ctx.assign_expr()
        self.vars[id] = value

    def visitAsExpr(self, ctx):                 # Regla AsExpr
        ex1 = ctx.assign_expr(0)
        ex2 = ctx.assign_expr(1)
        res = self.visit(ex2)
        old = self.vars
        self.vars["__identity__"] = res
        ret = self.visit(ex1)
        self.vars = old
        return ret

    def visitOnlyUnitary(self, ctx):            # Regla OnlyUnitary
        uop_ctx = ctx.uop()
        bop = uop_ctx.BOP()

        if bop:
            value = self.vars["__identity__"]
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
            else:
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
                return [ret]
        else:
            op = ctx.uop().getText()
            match op:
                case '#':
                    return [len(self.vars["__identity__"])]
                case 'i.':
                    return np.arange(self.vars["__identity__"])

    # Context Expr, son les diferents expresions que podem fer servir al nostre interpret
    def visitBinaryOP(self, ctx):               # Regla BinaryOP
        expr0 = ctx.expr(0)
        expr1 = ctx.expr(1)
        op = ctx.BOP().getText()
        n_flips = len(ctx.flip())
        flip = n_flips % 2
        if flip:
            value1 = self.visit(expr1)
            value2 = self.visit(expr0)
        else:
            value1 = self.visit(expr0)
            value2 = self.visit(expr1)
        try:
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
                    ret = np.less(value1, value2) * 1
                case '<=':
                    ret = np.less_equal(value1, value2) * 1
                case '>':
                    ret = np.greater(value1, value2) * 1
                case '>=':
                    ret = np.greater_equal(value1, value2) * 1
                case '=':
                    ret = np.equal(value1, value2) * 1
                case '<>':
                    ret = np.not_equal(value1, value2) * 1
                case '@:':
                    self.vars["__identity__"] = self.visit(ctx.expr())
                    ret = self.visit(expr0)
            return ret
        except Exception:
            print("lenght error")
            return [-0]

    def visitUnitaryOP(self, ctx):              # Regla UnitaryOP
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
            else:
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
                return [ret]
        else:
            op = ctx.uop().getText()
            match op:
                case ']':
                    return self.visit(expr)
                case 'i.':
                    return np.arange(self.visit(expr))
                case '#':
                    return [len(self.visit(expr))]

    def visitIdValue(self, ctx):                # Regla IdValue
        id = ctx.ID().getText()
        try:
            expr = self.vars[id]
        except KeyError:
            print("value error: " + id)
            return [0]
        old = dict(self.vars)
        self.vars["__identity__"] = self.visit(ctx.expr())
        ret = self.visit(expr)
        self.vars = old
        return ret

    def visitPrio(self, ctx):                   # Regla Prio
        return self.visit(ctx.expr())

    def visitList(self, ctx):                   # Regla List
        l_ctx = ctx.numList()
        return np.array([self.visit(x) for x in l_ctx.num()])

    def visitFilterOP(self, ctx):               # Regla FilterOP
        expr0 = ctx.expr(0)
        expr1 = ctx.expr(1)
        n_flips = len(ctx.flip())
        flip = n_flips % 2
        if flip:
            value1 = self.visit(expr1)
            value2 = self.visit(expr0)
        else:
            value1 = self.visit(expr0)
            value2 = self.visit(expr1)
        try:
            return np.repeat(value2, value1)
        except Exception:
            print("lenght error")
            return [-0]

    def visitIdentity(self, ctx):               # Regla Identity
        try:
            return self.vars["__identity__"]
        except KeyError:
            print("Error: No hi ha sobre que aplicar la identitat")
            return [0]

    def visitId(self, ctx):                     # Regla Id
        try:
            value = self.vars[ctx.ID().getText()]
            return self.visit(value)
        except KeyError:
            print("value error: " + ctx.ID().getText())
            return [0]

    # Context numList, serveix per llegir el tipus basic de G
    def visitNum(self, ctx):
        a = -1 if ctx.NEG() is not None else 1
        return a*int(ctx.NUM().getText())

    # Context Comment, serveix per llegir els comentaris
    def visitComment(self, ctx):
        com = ctx.COMMENT().getText()
        com = com[3:]
        com = com[1:] if com[0] == " " else com
        return com

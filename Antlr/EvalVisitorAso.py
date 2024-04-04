from CalculadoraAsoVisitor import CalculadoraAsoVisitor
from CalculadoraAsoParser import CalculadoraAsoParser
import math


class EvalVisitorAso(CalculadoraAsoVisitor):
    memory = {}

    def visitAssign(self, ctx: CalculadoraAsoParser.AssignContext):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    def visitPrintExpr(self, ctx: CalculadoraAsoParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0
        
    def visitBool(self, ctx: CalculadoraAsoParser.BoolContext):
        return ctx.BOOL().getText()

    def visitInt(self, ctx: CalculadoraAsoParser.IntContext):
        return int(ctx.INT().getText())
            
    def visitId(self, ctx: CalculadoraAsoParser.IdContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return self.memory[id_]
        return 0

    def visitMulDiv(self, ctx: CalculadoraAsoParser.MulDivContext):
        left = self.visit(ctx.expr(1))
        right = self.visit(ctx.expr(0))

        if ctx.op.type == CalculadoraAsoParser.MUL:
            return left * right
        elif ctx.op.type == CalculadoraAsoParser.MOD:
            return left % right
        else:
            if right != 0:
                return left / right
            else:
                print("Error: División por cero", end=" ")
                return 0

    def visitAddSub(self, ctx: CalculadoraAsoParser.AddSubContext):
        left = self.visit(ctx.expr(1))
        right = self.visit(ctx.expr(0))

        if ctx.op.type == CalculadoraAsoParser.ADD:
            result = left + right
        else:    
            result = left - right
        return result


    def visitParens(self, ctx: CalculadoraAsoParser.ParensContext):
        return self.visit(ctx.expr())

    def visitSenFunc(self, ctx: CalculadoraAsoParser.SenFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.sin(arg)

    def visitCosFunc(self, ctx: CalculadoraAsoParser.CosFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.cos(arg)

    def visitTanFunc(self, ctx: CalculadoraAsoParser.TanFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.tan(arg)

    def visitAbs(self, ctx: CalculadoraAsoParser.AbsContext):
        value = self.visit(ctx.expr())
        return abs(value)
        
    def visitExp(self, ctx: CalculadoraAsoParser.ExpContext):
        left = self.visit(ctx.expr(1))
        right = self.visit(ctx.expr(0))
        return left ** right
        
    def visitModCoc(self, ctx: CalculadoraAsoParser.ModCocContext):
        left = self.visit(ctx.expr(1))
        right = self.visit(ctx.expr(0))

        return left % right if ctx.op.type == CalculadoraAsoParser.MOD else left // right

    def visitNegNum(self, ctx: CalculadoraAsoParser.NegNumContext):
        value = self.visit(ctx.expr())*(-1)
        return value
        
    def visitNotBool(self, ctx: CalculadoraAsoParser.NotBoolContext):
        value = self.visit(ctx.expr())
        if value == 'true':
            return "false"
        elif value == 'false':
            return "true"
        else:
            print("Error: expresión no booleana: ", end=" ")
            return None
    

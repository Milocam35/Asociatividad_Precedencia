from CalculadoraVisitor import CalculadoraVisitor
from CalculadoraParser import CalculadoraParser
import math


class EvalVisitor(CalculadoraVisitor):
    memory = {}

    def visitAssign(self, ctx: CalculadoraParser.AssignContext):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    def visitPrintExpr(self, ctx: CalculadoraParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx: CalculadoraParser.IntContext):
        return int(ctx.INT().getText())
        
    def visitBool(self, ctx: CalculadoraParser.BoolContext):
        return ctx.BOOL().getText()
            
    def visitId(self, ctx: CalculadoraParser.IdContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return self.memory[id_]
        return 0

    def visitMulDiv(self, ctx: CalculadoraParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == CalculadoraParser.MUL:
            return left * right
        elif ctx.op.type == CalculadoraParser.MOD:
            return left % right
        else:
            if right != 0:
                return left / right
            else:
                print("Error: División por cero", end=" ")
                return 0

    def visitAddSub(self, ctx: CalculadoraParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left + right if ctx.op.type == CalculadoraParser.ADD else left - right

    def visitParens(self, ctx: CalculadoraParser.ParensContext):
        return self.visit(ctx.expr())

    def visitSenFunc(self, ctx: CalculadoraParser.SenFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.sin(arg)

    def visitCosFunc(self, ctx: CalculadoraParser.CosFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.cos(arg)

    def visitTanFunc(self, ctx: CalculadoraParser.TanFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.tan(arg)

    def visitAbs(self, ctx: CalculadoraParser.AbsContext):
        value = self.visit(ctx.expr())
        return abs(value)
        
    def visitExp(self, ctx: CalculadoraParser.ExpContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right
        
    def visitModCoc(self, ctx: CalculadoraParser.ModCocContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left % right if ctx.op.type == CalculadoraParser.MOD else left // right

    def visitNegNum(self, ctx: CalculadoraParser.NegNumContext):
        value = self.visit(ctx.expr())*(-1)
        return value
        
    def visitNotBool(self, ctx: CalculadoraParser.NotBoolContext):
        value = self.visit(ctx.expr())
        if value == 'true':
            return "false"
        elif value == 'false':
            return "true"
        else:
            print("Error: expresión no booleana: ", end=" ")
            return None
    

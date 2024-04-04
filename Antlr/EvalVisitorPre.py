from CalculadoraPreVisitor import CalculadoraPreVisitor
from CalculadoraPreParser import CalculadoraPreParser
import math


class EvalVisitorPre(CalculadoraPreVisitor):
    memory = {}

    def visitAssign(self, ctx: CalculadoraPreParser.AssignContext):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    def visitPrintExpr(self, ctx: CalculadoraPreParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx: CalculadoraPreParser.IntContext):
        return int(ctx.INT().getText())
        
    def visitBool(self, ctx: CalculadoraPreParser.BoolContext):
        return ctx.BOOL().getText()
            
    def visitId(self, ctx: CalculadoraPreParser.IdContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return self.memory[id_]
        return 0

    def visitMulDiv(self, ctx: CalculadoraPreParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == CalculadoraPreParser.MUL:
            return left * right
        elif ctx.op.type == CalculadoraPreParser.MOD:
            return left % right
        else:
            if right != 0:
                return left / right
            else:
                print("Error: División por cero", end=" ")
                return 0

    def visitAddSub(self, ctx: CalculadoraPreParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left + right if ctx.op.type == CalculadoraPreParser.ADD else left - right

    def visitParens(self, ctx: CalculadoraPreParser.ParensContext):
        return self.visit(ctx.expr())

    def visitSenFunc(self, ctx: CalculadoraPreParser.SenFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.sin(arg)

    def visitCosFunc(self, ctx: CalculadoraPreParser.CosFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.cos(arg)

    def visitTanFunc(self, ctx: CalculadoraPreParser.TanFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.tan(arg)

    def visitAbs(self, ctx: CalculadoraPreParser.AbsContext):
        value = self.visit(ctx.expr())
        return abs(value)
        
    def visitExp(self, ctx: CalculadoraPreParser.ExpContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left ** right
        
    def visitModCoc(self, ctx: CalculadoraPreParser.ModCocContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        return left % right if ctx.op.type == CalculadoraPreParser.MOD else left // right

    def visitNegNum(self, ctx: CalculadoraPreParser.NegNumContext):
        value = self.visit(ctx.expr())*(-1)
        return value
        
    def visitNotBool(self, ctx: CalculadoraPreParser.NotBoolContext):
        value = self.visit(ctx.expr())
        if value == 'true':
            return "false"
        elif value == 'false':
            return "true"
        else:
            print("Error: expresión no booleana: ", end=" ")
            return None
    

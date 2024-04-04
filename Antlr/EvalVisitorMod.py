from CalculadoraModVisitor import CalculadoraModVisitor
from CalculadoraModParser import CalculadoraModParser
import math


class EvalVisitorMod(CalculadoraModVisitor):
    memory = {}

    def visitAssign(self, ctx: CalculadoraModParser.AssignContext):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    def visitPrintExpr(self, ctx: CalculadoraModParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0
        
    def visitBool(self, ctx: CalculadoraModParser.BoolContext):
        return ctx.BOOL().getText()

    def visitInt(self, ctx: CalculadoraModParser.IntContext):
        return int(ctx.INT().getText())
            
    def visitId(self, ctx: CalculadoraModParser.IdContext):
        id_ = ctx.ID().getText()
        if id_ in self.memory:
            return self.memory[id_]
        return 0

    def visitMulDiv(self, ctx: CalculadoraModParser.MulDivContext):
        left = self.visit(ctx.expr(1))
        right = self.visit(ctx.expr(0))

        if ctx.op.type == CalculadoraModParser.MUL:
            return left * right
        elif ctx.op.type == CalculadoraModParser.MOD:
            return left % right
        else:
            if right != 0:
                return left / right
            else:
                print("Error: División por cero", end=" ")
                return 0

    def visitAddSub(self, ctx: CalculadoraModParser.AddSubContext):
        left = self.visit(ctx.expr(1))
        right = self.visit(ctx.expr(0))

        return left + right if ctx.op.type == CalculadoraModParser.ADD else left - right

    def visitParens(self, ctx: CalculadoraModParser.ParensContext):
        return self.visit(ctx.expr())

    def visitSenFunc(self, ctx: CalculadoraModParser.SenFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.sin(arg)

    def visitCosFunc(self, ctx: CalculadoraModParser.CosFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.cos(arg)

    def visitTanFunc(self, ctx: CalculadoraModParser.TanFuncContext):
        arg = math.radians(self.visit(ctx.expr()))
        return math.tan(arg)

    def visitAbs(self, ctx: CalculadoraModParser.AbsContext):
        value = self.visit(ctx.expr())
        return abs(value)
        
    def visitExp(self, ctx: CalculadoraModParser.ExpContext):
        left = self.visit(ctx.expr(1))
        right = self.visit(ctx.expr(0))
        return left ** right
        
    def visitModCoc(self, ctx: CalculadoraModParser.ModCocContext):  
        left = self.visit(ctx.expr(1))
        right = self.visit(ctx.expr(0))

        return left % right if ctx.op.type == CalculadoraModParser.MOD else left // right

    def visitNegNum(self, ctx: CalculadoraModParser.NegNumContext):
        value = self.visit(ctx.expr())*(-1)
        return value
        
    def visitNotBool(self, ctx: CalculadoraModParser.NotBoolContext):
        value = self.visit(ctx.expr())
        if value == 'true':
            return "false"
        elif value == 'false':
            return "true"
        else:
            print("Error: expresión no booleana: ", end=" ")
            return None
    

# Generated from CalculadoraPre.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraPreParser import CalculadoraPreParser
else:
    from CalculadoraPreParser import CalculadoraPreParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraPreParser.

class CalculadoraPreVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraPreParser#prog.
    def visitProg(self, ctx:CalculadoraPreParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#printExpr.
    def visitPrintExpr(self, ctx:CalculadoraPreParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#assign.
    def visitAssign(self, ctx:CalculadoraPreParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#blank.
    def visitBlank(self, ctx:CalculadoraPreParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#parens.
    def visitParens(self, ctx:CalculadoraPreParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#Abs.
    def visitAbs(self, ctx:CalculadoraPreParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#bool.
    def visitBool(self, ctx:CalculadoraPreParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#AddSub.
    def visitAddSub(self, ctx:CalculadoraPreParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#MulDiv.
    def visitMulDiv(self, ctx:CalculadoraPreParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#TrigFunction.
    def visitTrigFunction(self, ctx:CalculadoraPreParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#ModCoc.
    def visitModCoc(self, ctx:CalculadoraPreParser.ModCocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#id.
    def visitId(self, ctx:CalculadoraPreParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#Exp.
    def visitExp(self, ctx:CalculadoraPreParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#int.
    def visitInt(self, ctx:CalculadoraPreParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#NegNum.
    def visitNegNum(self, ctx:CalculadoraPreParser.NegNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#NotBool.
    def visitNotBool(self, ctx:CalculadoraPreParser.NotBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#CosFunc.
    def visitCosFunc(self, ctx:CalculadoraPreParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#SenFunc.
    def visitSenFunc(self, ctx:CalculadoraPreParser.SenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraPreParser#TanFunc.
    def visitTanFunc(self, ctx:CalculadoraPreParser.TanFuncContext):
        return self.visitChildren(ctx)



del CalculadoraPreParser
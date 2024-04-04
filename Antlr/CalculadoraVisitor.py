# Generated from Calculadora.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#prog.
    def visitProg(self, ctx:CalculadoraParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#printExpr.
    def visitPrintExpr(self, ctx:CalculadoraParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#assign.
    def visitAssign(self, ctx:CalculadoraParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#blank.
    def visitBlank(self, ctx:CalculadoraParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#parens.
    def visitParens(self, ctx:CalculadoraParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Abs.
    def visitAbs(self, ctx:CalculadoraParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#bool.
    def visitBool(self, ctx:CalculadoraParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#MulDiv.
    def visitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#AddSub.
    def visitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#TrigFunction.
    def visitTrigFunction(self, ctx:CalculadoraParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#ModCoc.
    def visitModCoc(self, ctx:CalculadoraParser.ModCocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#id.
    def visitId(self, ctx:CalculadoraParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#Exp.
    def visitExp(self, ctx:CalculadoraParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#int.
    def visitInt(self, ctx:CalculadoraParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#NegNum.
    def visitNegNum(self, ctx:CalculadoraParser.NegNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#NotBool.
    def visitNotBool(self, ctx:CalculadoraParser.NotBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#CosFunc.
    def visitCosFunc(self, ctx:CalculadoraParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#SenFunc.
    def visitSenFunc(self, ctx:CalculadoraParser.SenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#TanFunc.
    def visitTanFunc(self, ctx:CalculadoraParser.TanFuncContext):
        return self.visitChildren(ctx)



del CalculadoraParser
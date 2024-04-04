# Generated from CalculadoraAso.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraAsoParser import CalculadoraAsoParser
else:
    from CalculadoraAsoParser import CalculadoraAsoParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraAsoParser.

class CalculadoraAsoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraAsoParser#prog.
    def visitProg(self, ctx:CalculadoraAsoParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#printExpr.
    def visitPrintExpr(self, ctx:CalculadoraAsoParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#assign.
    def visitAssign(self, ctx:CalculadoraAsoParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#blank.
    def visitBlank(self, ctx:CalculadoraAsoParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#parens.
    def visitParens(self, ctx:CalculadoraAsoParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#Abs.
    def visitAbs(self, ctx:CalculadoraAsoParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#bool.
    def visitBool(self, ctx:CalculadoraAsoParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#MulDiv.
    def visitMulDiv(self, ctx:CalculadoraAsoParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#AddSub.
    def visitAddSub(self, ctx:CalculadoraAsoParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#TrigFunction.
    def visitTrigFunction(self, ctx:CalculadoraAsoParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#ModCoc.
    def visitModCoc(self, ctx:CalculadoraAsoParser.ModCocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#id.
    def visitId(self, ctx:CalculadoraAsoParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#Exp.
    def visitExp(self, ctx:CalculadoraAsoParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#int.
    def visitInt(self, ctx:CalculadoraAsoParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#NegNum.
    def visitNegNum(self, ctx:CalculadoraAsoParser.NegNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#NotBool.
    def visitNotBool(self, ctx:CalculadoraAsoParser.NotBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#CosFunc.
    def visitCosFunc(self, ctx:CalculadoraAsoParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#SenFunc.
    def visitSenFunc(self, ctx:CalculadoraAsoParser.SenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraAsoParser#TanFunc.
    def visitTanFunc(self, ctx:CalculadoraAsoParser.TanFuncContext):
        return self.visitChildren(ctx)



del CalculadoraAsoParser
# Generated from CalculadoraMod.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraModParser import CalculadoraModParser
else:
    from CalculadoraModParser import CalculadoraModParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraModParser.

class CalculadoraModVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraModParser#prog.
    def visitProg(self, ctx:CalculadoraModParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#printExpr.
    def visitPrintExpr(self, ctx:CalculadoraModParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#assign.
    def visitAssign(self, ctx:CalculadoraModParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#blank.
    def visitBlank(self, ctx:CalculadoraModParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#parens.
    def visitParens(self, ctx:CalculadoraModParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#Abs.
    def visitAbs(self, ctx:CalculadoraModParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#bool.
    def visitBool(self, ctx:CalculadoraModParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#AddSub.
    def visitAddSub(self, ctx:CalculadoraModParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#MulDiv.
    def visitMulDiv(self, ctx:CalculadoraModParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#TrigFunction.
    def visitTrigFunction(self, ctx:CalculadoraModParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#ModCoc.
    def visitModCoc(self, ctx:CalculadoraModParser.ModCocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#id.
    def visitId(self, ctx:CalculadoraModParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#Exp.
    def visitExp(self, ctx:CalculadoraModParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#int.
    def visitInt(self, ctx:CalculadoraModParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#NegNum.
    def visitNegNum(self, ctx:CalculadoraModParser.NegNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#NotBool.
    def visitNotBool(self, ctx:CalculadoraModParser.NotBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#CosFunc.
    def visitCosFunc(self, ctx:CalculadoraModParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#SenFunc.
    def visitSenFunc(self, ctx:CalculadoraModParser.SenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraModParser#TanFunc.
    def visitTanFunc(self, ctx:CalculadoraModParser.TanFuncContext):
        return self.visitChildren(ctx)



del CalculadoraModParser
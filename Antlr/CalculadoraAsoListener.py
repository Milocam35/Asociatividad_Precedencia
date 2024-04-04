# Generated from CalculadoraAso.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraAsoParser import CalculadoraAsoParser
else:
    from CalculadoraAsoParser import CalculadoraAsoParser

# This class defines a complete listener for a parse tree produced by CalculadoraAsoParser.
class CalculadoraAsoListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraAsoParser#prog.
    def enterProg(self, ctx:CalculadoraAsoParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#prog.
    def exitProg(self, ctx:CalculadoraAsoParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#printExpr.
    def enterPrintExpr(self, ctx:CalculadoraAsoParser.PrintExprContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#printExpr.
    def exitPrintExpr(self, ctx:CalculadoraAsoParser.PrintExprContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#assign.
    def enterAssign(self, ctx:CalculadoraAsoParser.AssignContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#assign.
    def exitAssign(self, ctx:CalculadoraAsoParser.AssignContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#blank.
    def enterBlank(self, ctx:CalculadoraAsoParser.BlankContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#blank.
    def exitBlank(self, ctx:CalculadoraAsoParser.BlankContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#parens.
    def enterParens(self, ctx:CalculadoraAsoParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#parens.
    def exitParens(self, ctx:CalculadoraAsoParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#Abs.
    def enterAbs(self, ctx:CalculadoraAsoParser.AbsContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#Abs.
    def exitAbs(self, ctx:CalculadoraAsoParser.AbsContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#bool.
    def enterBool(self, ctx:CalculadoraAsoParser.BoolContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#bool.
    def exitBool(self, ctx:CalculadoraAsoParser.BoolContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#MulDiv.
    def enterMulDiv(self, ctx:CalculadoraAsoParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#MulDiv.
    def exitMulDiv(self, ctx:CalculadoraAsoParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraAsoParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraAsoParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#TrigFunction.
    def enterTrigFunction(self, ctx:CalculadoraAsoParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#TrigFunction.
    def exitTrigFunction(self, ctx:CalculadoraAsoParser.TrigFunctionContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#ModCoc.
    def enterModCoc(self, ctx:CalculadoraAsoParser.ModCocContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#ModCoc.
    def exitModCoc(self, ctx:CalculadoraAsoParser.ModCocContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#id.
    def enterId(self, ctx:CalculadoraAsoParser.IdContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#id.
    def exitId(self, ctx:CalculadoraAsoParser.IdContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#Exp.
    def enterExp(self, ctx:CalculadoraAsoParser.ExpContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#Exp.
    def exitExp(self, ctx:CalculadoraAsoParser.ExpContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#int.
    def enterInt(self, ctx:CalculadoraAsoParser.IntContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#int.
    def exitInt(self, ctx:CalculadoraAsoParser.IntContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#NegNum.
    def enterNegNum(self, ctx:CalculadoraAsoParser.NegNumContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#NegNum.
    def exitNegNum(self, ctx:CalculadoraAsoParser.NegNumContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#NotBool.
    def enterNotBool(self, ctx:CalculadoraAsoParser.NotBoolContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#NotBool.
    def exitNotBool(self, ctx:CalculadoraAsoParser.NotBoolContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#CosFunc.
    def enterCosFunc(self, ctx:CalculadoraAsoParser.CosFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#CosFunc.
    def exitCosFunc(self, ctx:CalculadoraAsoParser.CosFuncContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#SenFunc.
    def enterSenFunc(self, ctx:CalculadoraAsoParser.SenFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#SenFunc.
    def exitSenFunc(self, ctx:CalculadoraAsoParser.SenFuncContext):
        pass


    # Enter a parse tree produced by CalculadoraAsoParser#TanFunc.
    def enterTanFunc(self, ctx:CalculadoraAsoParser.TanFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraAsoParser#TanFunc.
    def exitTanFunc(self, ctx:CalculadoraAsoParser.TanFuncContext):
        pass



# Generated from Calculadora.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#prog.
    def enterProg(self, ctx:CalculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#prog.
    def exitProg(self, ctx:CalculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#printExpr.
    def enterPrintExpr(self, ctx:CalculadoraParser.PrintExprContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#printExpr.
    def exitPrintExpr(self, ctx:CalculadoraParser.PrintExprContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#assign.
    def enterAssign(self, ctx:CalculadoraParser.AssignContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#assign.
    def exitAssign(self, ctx:CalculadoraParser.AssignContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#blank.
    def enterBlank(self, ctx:CalculadoraParser.BlankContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#blank.
    def exitBlank(self, ctx:CalculadoraParser.BlankContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#parens.
    def enterParens(self, ctx:CalculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#parens.
    def exitParens(self, ctx:CalculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Abs.
    def enterAbs(self, ctx:CalculadoraParser.AbsContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Abs.
    def exitAbs(self, ctx:CalculadoraParser.AbsContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#bool.
    def enterBool(self, ctx:CalculadoraParser.BoolContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#bool.
    def exitBool(self, ctx:CalculadoraParser.BoolContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#MulDiv.
    def enterMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#MulDiv.
    def exitMulDiv(self, ctx:CalculadoraParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#TrigFunction.
    def enterTrigFunction(self, ctx:CalculadoraParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#TrigFunction.
    def exitTrigFunction(self, ctx:CalculadoraParser.TrigFunctionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#ModCoc.
    def enterModCoc(self, ctx:CalculadoraParser.ModCocContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#ModCoc.
    def exitModCoc(self, ctx:CalculadoraParser.ModCocContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#id.
    def enterId(self, ctx:CalculadoraParser.IdContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#id.
    def exitId(self, ctx:CalculadoraParser.IdContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#Exp.
    def enterExp(self, ctx:CalculadoraParser.ExpContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#Exp.
    def exitExp(self, ctx:CalculadoraParser.ExpContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#int.
    def enterInt(self, ctx:CalculadoraParser.IntContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#int.
    def exitInt(self, ctx:CalculadoraParser.IntContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#NegNum.
    def enterNegNum(self, ctx:CalculadoraParser.NegNumContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#NegNum.
    def exitNegNum(self, ctx:CalculadoraParser.NegNumContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#NotBool.
    def enterNotBool(self, ctx:CalculadoraParser.NotBoolContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#NotBool.
    def exitNotBool(self, ctx:CalculadoraParser.NotBoolContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#CosFunc.
    def enterCosFunc(self, ctx:CalculadoraParser.CosFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#CosFunc.
    def exitCosFunc(self, ctx:CalculadoraParser.CosFuncContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#SenFunc.
    def enterSenFunc(self, ctx:CalculadoraParser.SenFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#SenFunc.
    def exitSenFunc(self, ctx:CalculadoraParser.SenFuncContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#TanFunc.
    def enterTanFunc(self, ctx:CalculadoraParser.TanFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#TanFunc.
    def exitTanFunc(self, ctx:CalculadoraParser.TanFuncContext):
        pass



# Generated from CalculadoraPre.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculadoraPreParser import CalculadoraPreParser
else:
    from CalculadoraPreParser import CalculadoraPreParser

# This class defines a complete listener for a parse tree produced by CalculadoraPreParser.
class CalculadoraPreListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraPreParser#prog.
    def enterProg(self, ctx:CalculadoraPreParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#prog.
    def exitProg(self, ctx:CalculadoraPreParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#printExpr.
    def enterPrintExpr(self, ctx:CalculadoraPreParser.PrintExprContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#printExpr.
    def exitPrintExpr(self, ctx:CalculadoraPreParser.PrintExprContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#assign.
    def enterAssign(self, ctx:CalculadoraPreParser.AssignContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#assign.
    def exitAssign(self, ctx:CalculadoraPreParser.AssignContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#blank.
    def enterBlank(self, ctx:CalculadoraPreParser.BlankContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#blank.
    def exitBlank(self, ctx:CalculadoraPreParser.BlankContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#parens.
    def enterParens(self, ctx:CalculadoraPreParser.ParensContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#parens.
    def exitParens(self, ctx:CalculadoraPreParser.ParensContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#Abs.
    def enterAbs(self, ctx:CalculadoraPreParser.AbsContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#Abs.
    def exitAbs(self, ctx:CalculadoraPreParser.AbsContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#bool.
    def enterBool(self, ctx:CalculadoraPreParser.BoolContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#bool.
    def exitBool(self, ctx:CalculadoraPreParser.BoolContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraPreParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraPreParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#MulDiv.
    def enterMulDiv(self, ctx:CalculadoraPreParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#MulDiv.
    def exitMulDiv(self, ctx:CalculadoraPreParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#TrigFunction.
    def enterTrigFunction(self, ctx:CalculadoraPreParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#TrigFunction.
    def exitTrigFunction(self, ctx:CalculadoraPreParser.TrigFunctionContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#ModCoc.
    def enterModCoc(self, ctx:CalculadoraPreParser.ModCocContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#ModCoc.
    def exitModCoc(self, ctx:CalculadoraPreParser.ModCocContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#id.
    def enterId(self, ctx:CalculadoraPreParser.IdContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#id.
    def exitId(self, ctx:CalculadoraPreParser.IdContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#Exp.
    def enterExp(self, ctx:CalculadoraPreParser.ExpContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#Exp.
    def exitExp(self, ctx:CalculadoraPreParser.ExpContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#int.
    def enterInt(self, ctx:CalculadoraPreParser.IntContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#int.
    def exitInt(self, ctx:CalculadoraPreParser.IntContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#NegNum.
    def enterNegNum(self, ctx:CalculadoraPreParser.NegNumContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#NegNum.
    def exitNegNum(self, ctx:CalculadoraPreParser.NegNumContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#NotBool.
    def enterNotBool(self, ctx:CalculadoraPreParser.NotBoolContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#NotBool.
    def exitNotBool(self, ctx:CalculadoraPreParser.NotBoolContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#CosFunc.
    def enterCosFunc(self, ctx:CalculadoraPreParser.CosFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#CosFunc.
    def exitCosFunc(self, ctx:CalculadoraPreParser.CosFuncContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#SenFunc.
    def enterSenFunc(self, ctx:CalculadoraPreParser.SenFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#SenFunc.
    def exitSenFunc(self, ctx:CalculadoraPreParser.SenFuncContext):
        pass


    # Enter a parse tree produced by CalculadoraPreParser#TanFunc.
    def enterTanFunc(self, ctx:CalculadoraPreParser.TanFuncContext):
        pass

    # Exit a parse tree produced by CalculadoraPreParser#TanFunc.
    def exitTanFunc(self, ctx:CalculadoraPreParser.TanFuncContext):
        pass



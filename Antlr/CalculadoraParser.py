# Generated from Calculadora.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("G\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\4,\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\7\4:\n\4\f\4\16\4=\13\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5E\n\5\3\5\2\3\6\6\2\4\6\b\2\5\3\2\r\16\3")
        buf.write("\2\17\20\3\2\22\23\2R\2\13\3\2\2\2\4\30\3\2\2\2\6+\3\2")
        buf.write("\2\2\bD\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r")
        buf.write("\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\20\5\6\4\2\20")
        buf.write("\21\7\25\2\2\21\31\3\2\2\2\22\23\7\n\2\2\23\24\7\3\2\2")
        buf.write("\24\25\5\6\4\2\25\26\7\25\2\2\26\31\3\2\2\2\27\31\7\25")
        buf.write("\2\2\30\17\3\2\2\2\30\22\3\2\2\2\30\27\3\2\2\2\31\5\3")
        buf.write("\2\2\2\32\33\b\4\1\2\33,\7\13\2\2\34,\7\t\2\2\35,\7\n")
        buf.write("\2\2\36\37\7\20\2\2\37,\5\6\4\13 !\7\4\2\2!\"\5\6\4\2")
        buf.write("\"#\7\5\2\2#,\3\2\2\2$%\7\21\2\2%,\5\6\4\5&\'\7\6\2\2")
        buf.write("\'(\5\6\4\2()\7\6\2\2),\3\2\2\2*,\5\b\5\2+\32\3\2\2\2")
        buf.write("+\34\3\2\2\2+\35\3\2\2\2+\36\3\2\2\2+ \3\2\2\2+$\3\2\2")
        buf.write("\2+&\3\2\2\2+*\3\2\2\2,;\3\2\2\2-.\f\t\2\2./\7\f\2\2/")
        buf.write(":\5\6\4\n\60\61\f\b\2\2\61\62\t\2\2\2\62:\5\6\4\t\63\64")
        buf.write("\f\7\2\2\64\65\t\3\2\2\65:\5\6\4\b\66\67\f\6\2\2\678\t")
        buf.write("\4\2\28:\5\6\4\79-\3\2\2\29\60\3\2\2\29\63\3\2\2\29\66")
        buf.write("\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\7\3\2\2\2=;\3")
        buf.write("\2\2\2>?\7\7\2\2?E\5\6\4\2@A\7\b\2\2AE\5\6\4\2BC\7\24")
        buf.write("\2\2CE\5\6\4\2D>\3\2\2\2D@\3\2\2\2DB\3\2\2\2E\t\3\2\2")
        buf.write("\2\b\r\30+9;D")
        return buf.getvalue()


class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'|'", "'cos'", "'sen'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'^'", "'*'", 
                     "'/'", "'+'", "'-'", "'!'", "'%'", "'//'", "'tan'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BOOL", "ID", 
                      "INT", "EXP", "MUL", "DIV", "ADD", "SUB", "NOT", "MOD", 
                      "COC", "TAN", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_trigFunc = 3

    ruleNames =  [ "prog", "stat", "expr", "trigFunc" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    BOOL=7
    ID=8
    INT=9
    EXP=10
    MUL=11
    DIV=12
    ADD=13
    SUB=14
    NOT=15
    MOD=16
    COC=17
    TAN=18
    NEWLINE=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.StatContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.StatContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalculadoraParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalculadoraParser.T__1) | (1 << CalculadoraParser.T__3) | (1 << CalculadoraParser.T__4) | (1 << CalculadoraParser.T__5) | (1 << CalculadoraParser.BOOL) | (1 << CalculadoraParser.ID) | (1 << CalculadoraParser.INT) | (1 << CalculadoraParser.SUB) | (1 << CalculadoraParser.NOT) | (1 << CalculadoraParser.TAN) | (1 << CalculadoraParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(CalculadoraParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = CalculadoraParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CalculadoraParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(CalculadoraParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = CalculadoraParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(CalculadoraParser.ID)
                self.state = 17
                self.match(CalculadoraParser.T__0)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(CalculadoraParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = CalculadoraParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(CalculadoraParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class AbsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs" ):
                listener.enterAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs" ):
                listener.exitAbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs" ):
                return visitor.visitAbs(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(CalculadoraParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class TrigFunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def trigFunc(self):
            return self.getTypedRuleContext(CalculadoraParser.TrigFuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigFunction" ):
                listener.enterTrigFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigFunction" ):
                listener.exitTrigFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigFunction" ):
                return visitor.visitTrigFunction(self)
            else:
                return visitor.visitChildren(self)


    class ModCocContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModCoc" ):
                listener.enterModCoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModCoc" ):
                listener.exitModCoc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModCoc" ):
                return visitor.visitModCoc(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalculadoraParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class NegNumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegNum" ):
                listener.enterNegNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegNum" ):
                listener.exitNegNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegNum" ):
                return visitor.visitNegNum(self)
            else:
                return visitor.visitChildren(self)


    class NotBoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotBool" ):
                listener.enterNotBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotBool" ):
                listener.exitNotBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotBool" ):
                return visitor.visitNotBool(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculadoraParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculadoraParser.INT]:
                localctx = CalculadoraParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.match(CalculadoraParser.INT)
                pass
            elif token in [CalculadoraParser.BOOL]:
                localctx = CalculadoraParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(CalculadoraParser.BOOL)
                pass
            elif token in [CalculadoraParser.ID]:
                localctx = CalculadoraParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(CalculadoraParser.ID)
                pass
            elif token in [CalculadoraParser.SUB]:
                localctx = CalculadoraParser.NegNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(CalculadoraParser.SUB)
                self.state = 29
                self.expr(9)
                pass
            elif token in [CalculadoraParser.T__1]:
                localctx = CalculadoraParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(CalculadoraParser.T__1)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(CalculadoraParser.T__2)
                pass
            elif token in [CalculadoraParser.NOT]:
                localctx = CalculadoraParser.NotBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(CalculadoraParser.NOT)
                self.state = 35
                self.expr(3)
                pass
            elif token in [CalculadoraParser.T__3]:
                localctx = CalculadoraParser.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(CalculadoraParser.T__3)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(CalculadoraParser.T__3)
                pass
            elif token in [CalculadoraParser.T__4, CalculadoraParser.T__5, CalculadoraParser.TAN]:
                localctx = CalculadoraParser.TrigFunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.trigFunc()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CalculadoraParser.ExpContext(self, CalculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 44
                        self.match(CalculadoraParser.EXP)
                        self.state = 45
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = CalculadoraParser.MulDivContext(self, CalculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 47
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculadoraParser.MUL or _la==CalculadoraParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = CalculadoraParser.AddSubContext(self, CalculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 50
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculadoraParser.ADD or _la==CalculadoraParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = CalculadoraParser.ModCocContext(self, CalculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculadoraParser.MOD or _la==CalculadoraParser.COC):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(5)
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TrigFuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraParser.RULE_trigFunc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TanFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanFunc" ):
                listener.enterTanFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanFunc" ):
                listener.exitTanFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanFunc" ):
                return visitor.visitTanFunc(self)
            else:
                return visitor.visitChildren(self)


    class CosFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosFunc" ):
                listener.enterCosFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosFunc" ):
                listener.exitCosFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosFunc" ):
                return visitor.visitCosFunc(self)
            else:
                return visitor.visitChildren(self)


    class SenFuncContext(TrigFuncContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.TrigFuncContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSenFunc" ):
                listener.enterSenFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSenFunc" ):
                listener.exitSenFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSenFunc" ):
                return visitor.visitSenFunc(self)
            else:
                return visitor.visitChildren(self)



    def trigFunc(self):

        localctx = CalculadoraParser.TrigFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_trigFunc)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculadoraParser.T__4]:
                localctx = CalculadoraParser.CosFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(CalculadoraParser.T__4)
                self.state = 61
                self.expr(0)
                pass
            elif token in [CalculadoraParser.T__5]:
                localctx = CalculadoraParser.SenFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(CalculadoraParser.T__5)
                self.state = 63
                self.expr(0)
                pass
            elif token in [CalculadoraParser.TAN]:
                localctx = CalculadoraParser.TanFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(CalculadoraParser.TAN)
                self.state = 65
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         





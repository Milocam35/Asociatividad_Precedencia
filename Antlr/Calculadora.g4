grammar Calculadora; 
prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:	INT                         # int
    |   BOOL			    # bool 
    |   ID                          # id 
    |   '-' expr                    # NegNum
    |	'(' expr ')'                # parens
    |   expr '^' expr	            # Exp
    |	expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   expr op=('%'|'//') expr     # ModCoc
    |   '!' expr	            # NotBool
    |   '|' expr '|'		    # Abs
    |   trigFunc                    # TrigFunction
    ;

trigFunc : 'cos' expr               # CosFunc
         | 'sen' expr               # SenFunc
         | 'tan' expr		    # TanFunc
         ;

BOOL :  'true'|'false' ; 
ID  :   [a-zA-Z]+ ;   
INT :   [0-9]+ ; 
EXP :   '^' ;
MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
NOT :   '!' ;
MOD :   '%' ;
COC :   '//' ;
TAN :   'tan' ;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace

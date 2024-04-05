%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int yylex(void);
int yyerror(char* s);
int op_count = 0; 
%}

/* declare tokens */
%token NUMBER BOOL
%token OP CP
%token EXP
%token MUL DIV 
%token ADD SUB
%token ABS AND MOD
%token NOT LESS GREAT
%token EOL

%%
calclist: /* nothing: matches at beginning of input */ 
    | calclist expr EOL { 
        if ((op_count%2)==0) {
            printf("= %d\n", $2); op_count = 0;
        } else {
            printf("= %d\n", $2*(-1));op_count = 0;
        } 
        }
    | calclist EOL { /* Do nothing */ }
;

expr: 
      expr1
    | NOT expr1 {  
        if ($2 == 0 || $2 == 1) {
            $$ = !$2;
        } else {
            yyerror("Error: negación aplicada a un valor no booleano");
        } 
        }
    | SUB expr1 {$$ = $2 *-1;}
;

expr1: 
      expr2
    | expr1 ABS expr2 { $$ = $3 | $1; }
;

expr2: 
      expr3
    | expr2 AND expr3 { $$ = $3 & $1; }
;

expr3: 
      expr4
    | expr4 LESS expr4 { $$ = ($3 < $1) ? 1 : 0; }
    | expr4 GREAT expr4 { $$ = ($3 > $1) ? 1 : 0; }
;

expr4: prim
    | prim MOD prim { 
        if ($1 == 0) {
            yyerror("Error: división por cero");
            $$ = 0; // O cualquier otro valor que desees asignar
        } else {
            $$ = $3 % $1;
        }
    }
;
prim: 
      factor
    | prim ADD factor { $$ = $3 + $1; }
    | prim SUB factor { $$ = $3 - $1; op_count++;}
;

factor: 
      term1
    | factor MUL term1 { $$ = $3 * $1; }
    | term1 DIV factor { 
        if ($3 == 0) {
            yyerror("Error: división por cero");
            $$ = 0; // O cualquier otro valor que desees asignar
        } else {
            $$ = $1 / $3;
        }
    }
;

term1: term
    | term1 EXP term { $$ = pow($3, $1); }

term: 
      NUMBER
    |  BOOL
    | ABS term ABS { $$ = $2 >= 0? $2 : - $2; }
    | OP expr CP { $$ = $2; }
;

%%
int main(int argc, char **argv)
{
	yyparse();
}

int yyerror(char *s)
{
    fprintf(stderr, "error: %s\n", s);
    exit(EXIT_FAILURE); // Terminar el programa con un código de error
}

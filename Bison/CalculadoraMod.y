%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
int yylex(void);
int yyerror(char* s);
%}

/* declare tokens */
%token NUMBER BOOL
%token OP CP
%token EXP
%token MUL DIV 
%token ADD SUB
%token ABS AND MOD COC
%token NOT LESS GREAT
%token EOL

%right ADD SUB
%right MUL DIV
%right EXP


%%
calclist: /* nothing: matches at beginning of input */ 
    | calclist expr EOL { printf("= %d\n", $2); }
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
    |  SUB expr1 {$$ = $2 *-1;}
;

expr1: 
      expr2
    | expr1 ABS expr2 { $$ = $1 | $3; }
;


expr2: 
      expr3
    | expr2 AND expr3 { $$ = $1 & $3; }
;


expr3: 
      expr4
    | expr4 LESS expr4 { $$ = ($1 < $3) ? 1 : 0; }
    | expr4 GREAT expr4 { $$ = ($1 > $3) ? 1 : 0; }
;

expr4: expr5
    | expr4 EXP expr5 { $$ = pow($1, $3); }
;


expr5: expr6
    | expr5 MUL expr6 { $$ = $1 * $3; }
    | expr5 DIV expr6 { 
        if ($3 == 0) {
            yyerror("Error: división por cero");
            $$ = 0; // O cualquier otro valor que desees asignar
        } else {
            $$ = $1 / $3;
        }
    }
;


expr6: expr7
    | expr6 ADD expr7 { $$ = $1 + $3; }
    | expr6 SUB expr7 { $$ = $1 - $3; }
;



expr7: prim
    | prim MOD prim { 
        if ($3 == 0) {
            yyerror("Error: división por cero");
            $$ = 0; // O cualquier otro valor que desees asignar
        } else {
            $$ = $1 % $3;
        }
    }
    | prim COC prim { 
        if ($3 == 0) {
            yyerror("Error: división por cero");
            $$ = 0; // O cualquier otro valor que desees asignar
        } else {
            $$ = $1 / $3;
        }
    }


prim: 
      NUMBER
    | BOOL
    | ABS prim ABS { $$ = $2 >= 0? $2 : - $2; }
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


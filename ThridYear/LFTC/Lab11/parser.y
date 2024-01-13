%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token LIST;
%token DECLARE;
%token INT;
%token STR;
%token IF;
%token DISPLAY;
%token INPUT;
%token ELSE;
%token WHILE;
%token RETURN;

%token IDENTIFIER;
%token INTCONSTANT;
%token STRINGCONSTANT;

%token PLUS;
%token MINUS;
%token TIMES;
%token DIV;
%token MOD;
%token EQ;
%token BIGGER;
%token BIGGEREQ;
%token LESS;
%token LESSEQ;
%token EQQ;
%token NEQ;
%token AND;
%token OR;

%token SEMICOLON;
%token OPENBRACKET;
%token OPENPARANTHESES
%token CLOSEPARANTHESES
%token CLOSEBRACKET;
%token COMMA;

%start compound_statement 

%%
compound_statement : statement SEMICOLON {printf("compound_statement -> statement ; Program\n");}
compound_statement : statement SEMICOLON compound_statement {printf("compound_statement -> statement ; compound_statement\n");}
compound_statement : statement {printf("compound_statement -> statement\n");}
compound_statement : statement compound_statement {printf("compound_statement -> statement compound_statement\n");}
statement : assignment_statement {printf("statement -> assignment_statement\n");}
statement : if_statement {printf("statement -> if_statement\n");}
statement : while_statement {printf("statement -> while_statement\n");}
statement : declaration_statement {printf("statement -> declaration_statement\n");}
expression : expression PLUS term {printf("expression -> expression + term\n");}
expression : expression MINUS term {printf("expression -> expression - term\n");}
expression : term {printf("expression -> term\n");}
term : term TIMES factor {printf("term -> term * factor\n");}
term : term DIV factor {printf("term -> term / factor\n");}
term : term MOD factor {printf("term -> term MOD factor\n");}
term : factor {printf("term -> factor\n");}
factor : OPENPARANTHESES expression CLOSEPARANTHESES {printf("factor -> ( expression )\n");}
factor : IDENTIFIER {printf("factor -> ID\n");}
factor : INTCONSTANT {printf("factor -> INT_CONST\n");}
factor : STRINGCONSTANT {printf("factor -> STR_CONST\n");}
assignment_statement : IDENTIFIER EQ expression {printf("assignment_statement -> ID = expression\n");}
type : INT {printf("type -> INT\n");}
type : STR {printf("type -> STR\n");}
declaration_statement : DECLARE type assignment_statement {printf("declaration_statement -> declare type assignment_statement\n");}
if_statement : IF OPENPARANTHESES condition CLOSEPARANTHESES OPENBRACKET compound_statement CLOSEBRACKET {printf("if ( condition ) { compound_statement }\n");}
if_statement : IF OPENPARANTHESES condition CLOSEPARANTHESES OPENBRACKET compound_statement CLOSEBRACKET ELSE OPENBRACKET compound_statement CLOSEBRACKET {printf("if_statement -> if ( condition ) { compound_statement } else { compound_statement }\n");}
while_statement : WHILE OPENPARANTHESES condition CLOSEPARANTHESES OPENBRACKET compound_statement CLOSEBRACKET {printf("while ( condition ) { compound_statement }\n");}
relation : LESS {printf("relation -> <\n");}
relation : LESSEQ {printf("relation -> <=\n");}
relation : EQQ {printf("relation -> ==\n");}
relation : NEQ {printf("relation -> !=\n");}
relation : BIGGEREQ {printf("relation -> >=\n");}
relation : BIGGER {printf("relation -> >\n");}
condition : expression relation expression {printf("condition -> expression relation expression\n");}

%%
yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(argc>1) yyin =  fopen(argv[1],"r");
	if(!yyparse()) fprintf(stderr, "\tOK\n");
} 
%{
#include <stdio.h>
#include <string.h>
#include "y.tab.h"
int lines = 0;
%}

%option noyywrap
%option caseless

DIGIT [0-9]
NON_ZERO_DIGIT [1-9]
INT_CONSTANT [-]?{NON_ZERO_DIGIT}{DIGIT}*|0
LETTER [a-zA-Z_]
STRING_CONSTANT \"({LETTER}|{DIGIT})*\"
IDENTIFIER ({LETTER})+({LETTER}|{DIGIT})*
BAD_IDENTIFIER ({DIGIT})+({LETTER})+({LETTER})*

%%

"list" { printf("%s - reserved word\n", yytext); return LIST; }
"declare" { printf("%s - reserved word\n", yytext); return DECLARE; }
"if" { printf("%s - reserved word\n", yytext); return IF; }
"display" { printf("%s - reserved word\n", yytext); return DISPLAY; }
"input" { printf("%s - reserved word\n", yytext); return INPUT; }
"else" { printf("%s - reserved word\n", yytext); return ELSE; }
"while" { printf("%s - reserved word\n", yytext); return WHILE; }
"return" { printf("%s - reserved word\n", yytext); return RETURN; }
"int" { printf("%s - reserved word\n", yytext); return INT;}
"str" { printf("%s - reserved word\n", yytext); return STR;}

{IDENTIFIER} {printf("%s - identifier\n", yytext); return IDENTIFIER; }

{BAD_IDENTIFIER} {printf("Error at token %s at line %d\n", yytext, lines); return -1;}

{INT_CONSTANT} {printf("%s - int constant\n", yytext); return INTCONSTANT; }

{STRING_CONSTANT} {printf("%s - str constant\n", yytext); return STRINGCONSTANT; }

"+" { printf("%s - operator\n", yytext); return PLUS; }
"-" { printf("%s - operator\n", yytext); return MINUS; }
"*" { printf("%s - operator\n", yytext); return TIMES; }
"/" { printf("%s - operator\n", yytext); return DIV; }
"%" { printf("%s - operator\n", yytext); return MOD; }
"=" { printf("%s - operator\n", yytext); return EQ; }
">" { printf("%s - operator\n", yytext); return BIGGER; }
">=" { printf("%s - operator\n", yytext); return BIGGEREQ; }
"<" { printf("%s - operator\n", yytext); return LESS; }
"<=" { printf("%s - operator\n", yytext); return LESSEQ; }
"==" { printf("%s - operator\n", yytext); return EQQ; }
"!=" { printf("%s - operator\n", yytext); return NEQ; }
"&&" { printf("%s - operator\n", yytext); return AND; }
"||" { printf("%s - operator\n", yytext); return OR; }

";" { printf("%s - separator\n", yytext); return SEMICOLON; }
"(" { printf("%s - separator\n", yytext); return OPENPARANTHESES; }
")" { printf("%s - separator\n", yytext); return CLOSEPARANTHESES; }
"{" { printf("%s - separator\n", yytext); return OPENBRACKET; }
"}" { printf("%s - separator\n", yytext); return CLOSEBRACKET; }
"," { printf("%s - separator\n", yytext); return COMMA; }

[ \t]+ {}

[\n]+ {++lines;}

. {printf("Error at token %s at line %d\n", yytext, lines); return -1;}

%%
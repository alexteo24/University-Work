
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     LIST = 258,
     DECLARE = 259,
     INT = 260,
     STR = 261,
     IF = 262,
     DISPLAY = 263,
     INPUT = 264,
     ELSE = 265,
     WHILE = 266,
     RETURN = 267,
     IDENTIFIER = 268,
     INTCONSTANT = 269,
     STRINGCONSTANT = 270,
     PLUS = 271,
     MINUS = 272,
     TIMES = 273,
     DIV = 274,
     MOD = 275,
     EQ = 276,
     BIGGER = 277,
     BIGGEREQ = 278,
     LESS = 279,
     LESSEQ = 280,
     EQQ = 281,
     NEQ = 282,
     AND = 283,
     OR = 284,
     SEMICOLON = 285,
     OPENBRACKET = 286,
     OPENPARANTHESES = 287,
     CLOSEPARANTHESES = 288,
     CLOSEBRACKET = 289,
     COMMA = 290
   };
#endif
/* Tokens.  */
#define LIST 258
#define DECLARE 259
#define INT 260
#define STR 261
#define IF 262
#define DISPLAY 263
#define INPUT 264
#define ELSE 265
#define WHILE 266
#define RETURN 267
#define IDENTIFIER 268
#define INTCONSTANT 269
#define STRINGCONSTANT 270
#define PLUS 271
#define MINUS 272
#define TIMES 273
#define DIV 274
#define MOD 275
#define EQ 276
#define BIGGER 277
#define BIGGEREQ 278
#define LESS 279
#define LESSEQ 280
#define EQQ 281
#define NEQ 282
#define AND 283
#define OR 284
#define SEMICOLON 285
#define OPENBRACKET 286
#define OPENPARANTHESES 287
#define CLOSEPARANTHESES 288
#define CLOSEBRACKET 289
#define COMMA 290




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;



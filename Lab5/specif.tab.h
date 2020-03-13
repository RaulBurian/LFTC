
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
     IDENTIFIER = 258,
     CONSTANT = 259,
     FLOAT = 260,
     INT = 261,
     IF = 262,
     ELSE = 263,
     COUT = 264,
     CIN = 265,
     EXTRACT = 266,
     INSERT = 267,
     WHILE = 268,
     MAIN = 269,
     RETURN = 270,
     SEMI_COLON = 271,
     PLUS = 272,
     MINUS = 273,
     MULTIPLY = 274,
     DIVISION = 275,
     MOD = 276,
     LESS_THAN = 277,
     LESS_OR_EQUAL_THAN = 278,
     ASSIGNMENT = 279,
     GREATER_OR_EQUAL_THAN = 280,
     GREATER_THAN = 281,
     EQUAL = 282,
     AND = 283,
     OR = 284,
     NOT = 285,
     NOT_EQUAL = 286,
     LEFT_SQUARE_PARENTHESIS = 287,
     RIGHT_SQUARE_PARENTHESIS = 288,
     LEFT_ROUND_PARENTHESIS = 289,
     RIGHT_ROUND_PARENTHESIS = 290,
     LEFT_ACCOLADE = 291,
     RIGHT_ACCOLADE = 292
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;



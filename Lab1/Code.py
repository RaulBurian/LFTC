import re
from Separator import Separator
from Operator import Operator
from Keyword import Keyword


def isIdentifier(token):
    if len(token) > 8:
        return False
    if re.search("^[a-zA-Z_]*", token).group(0):
        return True

    return False


def isConstant(token):
    if re.search("[-+]?[0-9]*\.?[0-9]+", token).group(0):
        return True
    return False


class Code:
    IDENTIFIER = 0
    CONSTANT = 1
    INT = 2
    FLOAT = 3
    MAIN = 4
    CONST = 5
    IF = 6
    ELSE = 7
    WHILE = 8
    CIN = 9
    COUT = 10
    SMALL_BO = 11
    SMALL_BC = 12
    LARGE_BO = 13
    LARGE_BC = 14
    ACO_O = 15
    ACO_C = 16
    SEMI_COLON = 17
    PLUS = 18
    MINUS = 19
    MULT = 20
    DIVIDE = 21
    EQUAL = 22
    DEQUAL = 23
    SMALL = 24
    SMALL_EQUAL = 25
    BIG = 26
    BIG_EQUAL = 27
    EXTRACT = 28
    INSERT = 29
    RETURN = 30
    COMMA = 31

    @staticmethod
    def getCode(token):
        if Separator.isSeparator(token):
            if token == Separator.CLOSED_SMALL:
                return Code.SMALL_BC
            if token == Separator.OPEN_SMALL:
                return Code.SMALL_BO
            if token == Separator.CLOSED_BIG:
                return Code.LARGE_BC
            if token == Separator.OPEN_BIG:
                return Code.LARGE_BO
            if token == Separator.OPEN_ACO:
                return Code.ACO_O
            if token == Separator.CLOSED_ACO:
                return Code.ACO_C
            if token == Separator.SEMI_COLON:
                return Code.SEMI_COLON
            if token == Separator.COMMA:
                return Code.COMMA
        elif Operator.isOperator(token):
            if token == Operator.MINUS:
                return Code.MINUS
            if token == Operator.PLUS:
                return Code.PLUS
            if token == Operator.MULT:
                return Code.MULT
            if token == Operator.DIVIDE:
                return Code.DIVIDE
            if token == Operator.EQUAL:
                return Code.EQUAL
            if token == Operator.D_EQUAL:
                return Code.DEQUAL
            if token == Operator.SMALL:
                return Code.SMALL
            if token == Operator.SMALL_EQUAL:
                return Code.SMALL_EQUAL
            if token == Operator.BIG:
                return Code.BIG
            if token == Operator.BIG_EQUAL:
                return Code.BIG_EQUAL
            if token == Operator.EXTRACT:
                return Code.EXTRACT
            if token == Operator.INSERT:
                return Code.INSERT
        elif Keyword.isKeyword(token):
            if token == Keyword.RETURN:
                return Code.RETURN
            if token == Keyword.WHILE:
                return Code.WHILE
            if token == Keyword.IF:
                return Code.IF
            if token == Keyword.ELSE:
                return Code.ELSE
            if token == Keyword.INT:
                return Code.INT
            if token == Keyword.FLOAT:
                return Code.FLOAT
            if token == Keyword.COUT:
                return Code.COUT
            if token == Keyword.CIN:
                return Code.CIN
            if token == Keyword.MAIN:
                return Code.MAIN
            if token == Keyword.CONST:
                return Code.CONST
        elif isIdentifier(token):
            return Code.IDENTIFIER
        elif isConstant(token):
            return Code.CONSTANT

from Pif import Pif
import re
from SymTable import SymTableConst, SymTableIden
from Operator import *
from Separator import *
from Code import *
from Keyword import *


def isIdentifier(token):
    if len(token) > 8:
        return False
    if re.search("^[a-zA-Z_]*", token).group(0):
        return True

    return False


def isConstant(token):

    if re.search("[a-zA-Z_]+",token):
        return False

    if not re.search("[-]?[0-9]*\.?[0-9]+", token):
        return False

    if re.search("[-]?[0-9]*\.?[0-9]+", token).group(0)==token:
        return True
    return False


class Parser:

    def __init__(self):
        self.pif = Pif()
        self.symIden = SymTableIden()
        self.symConst = SymTableConst()

    def addToken(self, token):
        if Operator.isOperator(token[0]) or Separator.isSeparator(token[0]) or Keyword.isKeyword(token[0]):
            self.pif.addOther(token[0])
        elif isIdentifier(token[0]):

            if self.symIden.getPosOfIden(token[0]) == -1:
                self.symIden.addIden(token[0])
            self.pif.addIden(token[0], self.symIden)
        elif isConstant(token[0]):
            if self.symConst.getPosOfConst(token[0]) == -1:
                self.symConst.addConst(token[0])
            self.pif.addConst(token[0], self.symConst)
        else:
            raise Exception("Lexical Error " + str(token[2]) + " Token:" + str(token[0]))

    def restructurePIF(self):
        # print(self.pif.pif)
        for elem in self.pif.pif:
            # print(elem)
            if not (Operator.isOperator(elem[0]) or Separator.isSeparator(elem[0]) or Keyword.isKeyword(elem[0])):
                if isIdentifier(elem[0]):
                    # print(elem[0])
                    elem[1] = self.symIden.getPosOfIden(elem[0])
                elif isConstant(elem[0]):
                    elem[1] = self.symConst.getPosOfConst(elem[0])
            elem[0] = Code.getCode(elem[0])

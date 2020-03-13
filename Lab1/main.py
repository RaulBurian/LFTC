from Util import Parser
from Separator import *
from Operator import *


def tokenize():
    f = open('in.txt', 'r')
    c = f.read(1)
    word = ''
    line=1
    newLineToken=False
    tokens = []
    while c:
        if not Separator.isSeparator(c) and not Operator.isOperator(c):
            word += c

        else:
            if word != '':
                tokens.append((word, f.tell(),line))
                newLineToken=True
                word = ''
            if Separator.isSeparator(c) and c != Separator.SPACE and c != Separator.ENDL and c != Separator.OPEN_SMALL:
                newLineToken = True
                tokens.append((c, f.tell() + 1,line))
            if Separator.isSeparator(c) and c == Separator.OPEN_SMALL:
                pos = f.tell()
                nc = f.read(1)
                if nc == Operator.MINUS:
                    word += nc
                else:
                    f.seek(pos)
                newLineToken = True
                tokens.append((c, f.tell() + 1,line))
            if Separator.isSeparator(c) and c==Separator.ENDL:
                line+=1
                newLineToken=False

            if Operator.isOperator(c):
                if (c==Operator.PLUS or Operator.MINUS) and newLineToken==False:
                    word+=c
                if c == Operator.EQUAL:
                    pos = f.tell()
                    nc = f.read(1)
                    if nc == Operator.EQUAL:
                        newLineToken = True
                        tokens.append((Operator.D_EQUAL, f.tell(),line))

                    elif nc == Operator.MINUS or nc== Operator.PLUS:
                        word += nc
                        newLineToken = True
                        tokens.append((c, f.tell(),line))
                    else:
                        f.seek(pos)
                        newLineToken = True
                        tokens.append((c, f.tell(),line))

                elif c == Operator.SMALL:
                    pos = f.tell()
                    nc = f.read(1)
                    if nc == Operator.EQUAL:
                        newLineToken = True
                        tokens.append((Operator.SMALL_EQUAL, f.tell(),line))

                    elif nc == Operator.SMALL:
                        newLineToken = True
                        tokens.append((Operator.EXTRACT, f.tell(),line))

                    elif nc == Operator.MINUS or nc== Operator.PLUS:
                        word += nc
                        newLineToken = True
                        tokens.append((c, f.tell(),line))

                    else:
                        f.seek(pos)
                        newLineToken = True
                        tokens.append((c, f.tell(),line))

                elif c == Operator.BIG:
                    pos = f.tell()
                    nc = f.read(1)
                    if nc == Operator.EQUAL:
                        newLineToken = True
                        tokens.append((Operator.BIG_EQUAL, f.tell(),line))

                    elif nc == Operator.BIG:
                        newLineToken = True
                        tokens.append((Operator.INSERT, f.tell(),line))

                    elif nc == Operator.MINUS or nc== Operator.PLUS:
                        word += nc
                        newLineToken = True
                        tokens.append((c, f.tell(),line))

                    else:
                        f.seek(pos)
                        newLineToken = True
                        tokens.append((c, f.tell(),line))

                else:
                    newLineToken = True
                    tokens.append((c, f.tell(),line))

        c = f.read(1)

    return tokens


try:
    parser = Parser()
    for token in tokenize():
        parser.addToken(token)
    parser.restructurePIF()
    f = open('pif.out', 'w')
    for elem in parser.pif.pif:
        # f.write(str(elem[0]) + " | " + str(elem[1]) + '\n')
        f.write(str(elem[0])+" ")
    f.close()
    f = open('symIden.out', 'w')
    for elem in parser.symIden.table:
        # f.write(elem + ' | ' + str(parser.symIden.getPosOfIden(elem)) + '\n')
        f.write(elem+" ")
    f.close()
    f = open('symConst.out', 'w')
    for elem in parser.symConst.table:
        # f.write(elem + ' | ' + str(parser.symConst.getPosOfConst(elem)) + '\n')
        f.write(elem+" ")
    f.close()
except Exception as e:
    print(e)

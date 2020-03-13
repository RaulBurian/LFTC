class Keyword:
    INT = 'int'
    FLOAT = 'float'
    MAIN = 'main'
    CONST = 'const'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    CIN = 'cin'
    COUT = 'cout'
    RETURN = 'return'

    @staticmethod
    def isKeyword(c):
        if c == Keyword.INT or c == Keyword.CIN or c == Keyword.CONST or c == Keyword.COUT or c == Keyword.FLOAT \
                or c == Keyword.MAIN or c == Keyword.IF or c == Keyword.ELSE or c == Keyword.WHILE or c == Keyword.RETURN:
            return True
        return False

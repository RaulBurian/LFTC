
class Separator:

    COMMA=','
    SEMI_COLON=';'
    SPACE=' '
    OPEN_SMALL='('
    CLOSED_SMALL=')'
    OPEN_BIG='['
    CLOSED_BIG=']'
    OPEN_ACO='{'
    CLOSED_ACO='}'
    ENDL='\n'

    @staticmethod
    def isSeparator(c):
        if c==Separator.COMMA or c==Separator.SEMI_COLON or c==Separator.OPEN_SMALL or c==Separator.OPEN_BIG or c==Separator.OPEN_ACO\
                or c==Separator.CLOSED_ACO or c==Separator.CLOSED_BIG or c==Separator.CLOSED_SMALL or c==Separator.SPACE or c==Separator.ENDL:
            return True
        return False

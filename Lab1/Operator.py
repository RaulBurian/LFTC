
class Operator:

    EQUAL='='
    D_EQUAL='=='
    PLUS='+'
    MINUS='-'
    MULT='*'
    DIVIDE='/'
    SMALL='<'
    SMALL_EQUAL='<='
    BIG='>'
    BIG_EQUAL='>='
    INSERT='>>'
    EXTRACT='<<'

    @staticmethod
    def isOperator(c):
        if c==Operator.EQUAL or c==Operator.PLUS or c==Operator.MINUS or c==Operator.MULT or c==Operator.DIVIDE or c==Operator.SMALL or c==Operator.BIG \
            or c==Operator.SMALL_EQUAL or c==Operator.BIG_EQUAL or c==Operator.D_EQUAL or c==Operator.INSERT or c==Operator.EXTRACT:
            return True
        return False
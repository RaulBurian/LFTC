from Code import Code


class Pif:
    def __init__(self):
        self.pif = []

    def addIden(self, iden, st):
        pos = st.getPosOfIden(iden)
        self.pif.append([iden, pos])

    def addConst(self, const, st):
        pos = st.getPosOfConst(const)
        self.pif.append([const, pos])

    def addOther(self, other):
        self.pif.append([other, -1])

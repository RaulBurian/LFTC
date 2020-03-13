
class SymTableIden:

    def __init__(self):
        self.table=[]

    def addIden(self,iden):
        self.table.append(iden)
        self.table.sort()

    def getPosOfIden(self,iden):
        if iden not in self.table:
            return -1
        else:
            return self.table.index(iden)

class SymTableConst:
    def __init__(self):
        self.table = []

    def addConst(self,const):
        self.table.append(const)
        self.table=sorted(self.table,key=float)

    def getPosOfConst(self,const):
        if const not in self.table:
            return -1
        else:
            return self.table.index(const)

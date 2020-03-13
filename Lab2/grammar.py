

class Transition:

    def __init__(self,text):
        self.initial,self.value,self.next=text.split(';')


    def __str__(self):
        return "( "+self.initial+", "+self.value+" ) = "+self.next

class Automaton:

    def __init__(self):
        self.states=[]
        self.alphabet=[]
        self.transitions=[]
        self.initial_state=''
        self.final_states=[]


    def readAutomatonKeyboard(self):
        self.states.extend(input('Enter states:').split(','))
        self.alphabet.extend(input('Enter alphabet:').split(','))
        self.alphabet.extend([Transition(x) for x in input('Enter alphabet:').split(',')])
        self.initial_state=input('Enter initial state:')
        self.final_states.extend(input('Enter final states:').split(','))

    def readAutomatonFile(self,file):
        f=open(file,'r')
        self.states.extend(f.readline().strip('\n').split(','))
        self.alphabet.extend(f.readline().strip('\n').split(','))
        self.transitions.extend([Transition(x) for x in f.readline().strip('\n').split(',')])
        self.initial_state = f.readline().strip('\n')
        self.final_states.extend(f.readline().strip('\n').split(','))
        f.close()

    def toGrammar(self):
        g=Grammar()

        g.non_terminals.extend(self.states)
        g.terminals.extend(self.alphabet)
        g.starting_symbol=self.initial_state
        if self.initial_state in self.final_states:
            g.productions.append(Production(self.initial_state+'->epsilon'))
        for trans in self.transitions:

            if trans.next in self.final_states:
                g.productions.append(Production(trans.initial+'->'+trans.value))
            else:
                g.productions.append(Production(trans.initial + '->' + trans.value + trans.next))

        print(g)

    def __str__(self):
        return "N="+str(self.states)+'\n'+\
            'Alphabet='+str(self.alphabet)+'\n'+\
            'T='+str([str(x) for x in self.transitions])+'\n'+\
            'Q='+self.initial_state+'\n'+\
            'F='+str(self.final_states)+'\n'

class Production:

    def __init__(self,text):
        text=text.replace('->','-')
        self.lhs,self.rhs=text.split('-')

    def __str__(self):
        return self.lhs+' -> '+self.rhs

    def checkRegular(self):

        if len(self.lhs)==1 and len(self.rhs)==1 and self.rhs[0].islower():
            return True
        if len(self.lhs)==1 and len(self.rhs)==2 and self.rhs[0].islower() and self.rhs[1].isupper():
            return True

        return False

    def Sepsilon(self):
        if self.lhs=='S' and self.rhs=='epsilon':
            return True
        return False

    def epsilon(self):
        if self.rhs=='epsilon':
            return True
        return False

    def rhsS(self):
        if 'S' in self.rhs:
            return True
        return False

class Grammar:

    def __init__(self):
        self.terminals=[]
        self.non_terminals=[]
        self.productions=[]
        self.starting_symbol=''


    def readGrammarFile(self,file):
        f=open(file,"r")

        self.non_terminals.extend(f.readline().strip('\n').split(','))
        self.terminals.extend(f.readline().strip('\n').split(','))
        self.productions.extend([Production(x) for x in f.readline().strip('\n').split(',')])
        self.starting_symbol=f.readline()
        f.close()

    def readGrammarKeyboard(self):

        self.non_terminals.extend(input("Enter non_terminals:").split(','))
        self.terminals.extend(input("Enter terminals:").split(','))
        self.productions.extend([Production(x) for x in input("Enter production]:").split(',')])
        self.starting_symbol=input("Enter starting symbol:")


    def checkRegular(self):
        rhsS=0
        for prod in self.productions:
            if prod.epsilon() and not prod.Sepsilon():
                return False
            if prod.Sepsilon():
                rhsS=1
            if rhsS==1 and prod.rhsS():
                return False
            if not prod.checkRegular() and not prod.epsilon():
                return False
        return True

    def toAutomaton(self):
        a=Automaton()
        a.states.extend(self.non_terminals)
        a.states.append('K')
        a.alphabet.extend(self.terminals)
        a.initial_state=self.starting_symbol
        epsilon=False
        for prod in self.productions:
            if prod.epsilon():
                epsilon=True
            elif len(prod.rhs)==2:
                a.transitions.append(Transition(prod.lhs+';'+prod.rhs[0]+';'+prod.rhs[1]))
            else:
                a.transitions.append(Transition(prod.lhs+';'+prod.rhs+';'+'K'))
        if epsilon:
            a.final_states=['K',self.starting_symbol]
        else:
            a.final_states=['K']

        print(a)

    def __str__(self):
        return "N="+str(self.non_terminals)+'\n'+\
            'Sigma='+str(self.terminals)+'\n'+\
            'P='+str([str(x) for x in self.productions])+'\n'+\
            'S='+self.starting_symbol+'\n'
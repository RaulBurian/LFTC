
from grammar import Grammar,Automaton

def showMainMenu():

    print('1. Read Grammar from keyboard')
    print('2. Read Grammar from file')
    print('3. Read Automaton from keyboard')
    print('4. Read Automaton from file')
    print('0. Exit')


def showGrammarMenu():

    print('1. Display elements')
    print('2. Check regularity')
    print('3. Transform into automaton')
    print('0. Exit')

def showAutomatonMenu():

    print('1. Display elements')
    print('2. Transform into grammar')
    print('0. Exit')

def startGrammarAnalysis(grammar):
    done=False
    while not done:
        showGrammarMenu()
        n=int(input("Enter your command:"))
        if n==0:
            done=True
            continue
        elif n==1:
            print(grammar)
        elif n==2:
            print(grammar.checkRegular())
        elif n==3:
            automaton=grammar.toAutomaton()
            print(automaton)


def startAutomatonAnalysis(automaton):
    done=False
    while not done:
        showAutomatonMenu()
        n=int(input("Enter your command:"))
        if n==0:
            done=True
            continue
        elif n==1:
            print(automaton)
        elif n==2:
            grammar=automaton.toGrammar()
            print(grammar)




def main():

    done=False
    while not done:
        showMainMenu()
        n=int(input("Enter your command:"))
        if n==0:
            done=True
            continue
        elif n==1:
            g=Grammar()
            g.readGrammarKeyboard()
            startGrammarAnalysis(g)
        elif n==2:
            g=Grammar()
            m=input("Enter filename:")
            g.readGrammarFile(m)
            startGrammarAnalysis(g)
        elif n==3:
            a=Automaton()
            a.readAutomatonKeyboard()
            startAutomatonAnalysis(a)
        elif n==4:
            a=Automaton()
            m=input("Enter filename:")
            a.readAutomatonFile(m)
            startAutomatonAnalysis(a)



main()



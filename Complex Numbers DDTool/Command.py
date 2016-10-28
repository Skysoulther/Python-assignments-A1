availableCommands={'add':["add num"],
                   'insert': ["insert num at pos"],
                   'remove': ["remove pos","remove pos to pos"],
                   'replace': ["replace num with num"],
                   'list': ['list','list real pos to pos','list modulo sig pos'],
                   'sum': ['sum pos to pos'],
                   'product': ['product pos to pos'],
                   'filter': ['filter real','filter modulo sig pos'],
                   'undo': ['undo'],
                   'exit': ['exit']
                   }

def commandIsValid(comList):
    '''
    Checks if the command is valid
    Input: comList - a list with the words of the command
    Output: True-if the command is valid
    Exceptions:
    '''
    if validateCommand(comList):
        firstWord=comList[0]
        position=validateLength(comList)
        if position != -1:
            possibleCommand=availableCommands[firstWord][position].split()
            if validateWords(comList,possibleCommand):
                return True
            else:
                raise ValueError("The command has not a valid format!")
        else:
            raise ValueError("Check the number of words in your command!")
    else:
        raise ValueError("Command doesn't exist!")
    
def validateLength(comList):
    '''
    Checks if the number of words from the command is possible for that specific command
    Input: comList - a list with the words of the command
    Output: pos - position of our command in the list of possible commnads
    Exceptions: -
    '''
    pos=-1
    possibleCommands=availableCommands[comList[0]]
    for i in range(len(possibleCommands)):
        avaList=possibleCommands[i].split()
        if len(comList)==len(avaList):
            pos=i
            break
    return pos
    
def validateCommand(comList):
    '''
    Checks if the first word of the command is a valid command
    Input: comList - a list with the words of the command
    Output: True - command exists
            False - command doesn't exists
    Exceptions: -
    '''
    if comList[0] in availableCommands:
        return True
    else:
        return False

def isNumber(string):
    '''
    Checks if a string is written as a number
    Input: string - the given string
    Output: True - if it is a number
            False - otherwise
    Exceptions: -
    '''
    try:
        int(string)
        return True
    except ValueError:
        return False

def replaceWithSpace(string):
    '''
    Replaces the character the first 'i' and '+' and '-' in the string with spaces
    Input: string - the given string
    Output: Modifies the given string if it is possible
    Exceptions: -
    '''
    count=2
    i=0
    specialSymbols=['+','i']
    while i<len(string):
        if string[i] in specialSymbols:
            specialSymbols.remove(string[i])
            string=string[:i]+' '+string[i+1:]
        elif string[i]=='-' and count!=0:
            string=string[:i]+' '+string[i:]
            count-=1
            i+=1
        i+=1
    if 'i' in specialSymbols:
        string=string+'i'
    return string


def validateComplex(string):
    '''
    Checks if a complex number is written in the form 'a+bi'
    Input: string - the given string
    Output: True - if it has a valid form
            False - if the form is not valid
    Exceptions: TypeError when a int type is entered (int type doesn't have length)
    '''
    s=replaceWithSpace(string)
    listS=s.split()
    if len(listS)!=2:
        return False
    else:
        for i in listS:
            if not isNumber(i):
                return False
    return True

def validateWords(comList,possibleList):
    '''
    Checks if the words in a possible command are valid
    Input: comList - the list with the words of our command
           possibleList - verification list
    Output: True - if the words are valid
            False - otherwise
    Exceptions: -
    '''
    for i in range(1,len(possibleList)):
        sigList=['<','=','>']
        if possibleList[i]=='num':
            if not validateComplex(comList[i]):
                return False
        elif possibleList[i]=='pos':
            if not isNumber(comList[i]):
                return False
        elif possibleList[i]=='sig':
            if not comList[i] in sigList:
                return False
        else:
            if possibleList[i]!=comList[i]:
                return False
    return True
    
def testValidateCommand():
    '''
    test the function validateCommand
    '''
    comList1=['add','number']
    assert validateCommand(comList1)==True
    comList2=['remove','numbatrdsr','prime']
    assert validateCommand(comList2)==True
    comList3=['removes','number','prime']
    assert validateCommand(comList3)==False
    return

def testValidateLength():
    '''
    test the function validateLength
    '''
    comList1=['add','number']
    assert validateLength(comList1)==0
    comList2=['remove','numbatrdsr','prime']
    assert validateLength(comList2)==-1
    comList3=['remove','number','to','number']
    assert validateLength(comList3)==1
    return

def testIsNumber():
    '''
    test the function isNumber
    '''
    assert isNumber('123')==True
    assert isNumber('123F')==False
    assert isNumber('String')==False
    assert isNumber('-3')==True
    return

def testValidateComplex():
    '''
    test the function validateComplex
    '''
    assert validateComplex('4+3i')==True
    assert validateComplex('string')==False
    assert validateComplex('49')==False
    assert validateComplex('+3i+5')==True
    assert validateComplex('5i')==False
    assert validateComplex('0+5i')==True
    assert validateComplex('-1-3i')==True
    assert validateComplex('-2--4i')==False
    assert validateComplex('1-3i')==True
    assert validateComplex('-1+3i')==True
    return

def testValidateWords():
    '''
    test the function calidateWords
    '''
    verList1=['remove','pos','to', 'pos']
    verList2=['add','num']
    comList1=['remove', '2', 'to', '3']
    assert validateWords(comList1,verList1)==True
    comList2=['remove', '20' , 'to', 'abc']
    assert validateWords(comList2,verList1)==False
    comList3=['remove', '20' , 'at', '30']
    assert validateWords(comList3,verList1)==False
    comList4=['remove', '20' , 'to', '30.5']
    assert validateWords(comList4,verList1)==False
    comList5=['remove', '20' , 'to', '-30']
    assert validateWords(comList5,verList1)==True
    comList6=['add','1+3i']
    assert validateWords(comList6,verList2)==True
    comList7=['add','13i']
    assert validateWords(comList7,verList2)==False
    comList8=['add','13']
    assert validateWords(comList8,verList2)==False
    return

def testCommandIsValid():
    '''
    test the function commandIsValid
    '''
    try:
        commandIsValid(['remove','a','to','b'])
        ok=1
    except ValueError:
        ok=0
    assert ok == 0
    try:
        commandIsValid(['remove','5','to','2'])
        ok=1
    except ValueError:
        ok=0
    assert ok == 1
    try:
        commandIsValid(['undo'])
        ok=1
    except ValueError:
        ok=0
    assert ok == 1
    try:
        commandIsValid(['undo','ram'])
        ok=1
    except ValueError:
        ok=0
    assert ok == 0
    return 

#testValidateCommand()
#testValidateLength()
#testIsNumber()
#testValidateComplex()
#testValidateWords()
#testCommandIsValid()


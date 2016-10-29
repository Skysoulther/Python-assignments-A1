from Complex import *
from copy import deepcopy, copy

complexList=[ [7,7],[1,-1],[-3,-2],[-7,10],[0,10],[11,0],[0,0],[-7,10],[6,8],[12,0] ]
undoList=[]

def undoSave(l):
    '''
    Saves the state of the current list into a list of lists (undoList)
    Input: l - the list that should be save
    Output: Add the list to the undoList
    Exceptions: -
    '''
    undoElement=deepcopy(l)
    undoList.append(undoElement)
    return

def complexNumber(string):
    '''
    Transforms a string with the format 'a+bi' in a list which represents a complex number
    Input: string - the complex Number
    output: a list with two elements (real and imaginary part)
    Exceptions: -
    '''
    i=0
    specialSymbols=['+','i']
    while i<len(string):
        if string[i] in specialSymbols:
            specialSymbols.remove(string[i])
            string=string[:i]+' '+string[i+1:]
        elif string[i]=='-':
            string=string[:i]+' '+string[i:]
            i+=1
        i+=1
    complexL=string.split()
    return [int(complexL[0]),int(complexL[1])]

def addNumber(l,s):
    '''
    Adds a complex number to the list
    Input: l - list of complex numbers
           s - the complex number as a list
    Output: adds the element to the list
    Exceptions: -
    '''
    undoSave(complexList)
    l.append(s)
    print("A number was successfully added!")
    return

def insertNumber(l,s,index):
    '''
    Inserts number in list if the index is smaller tha the length-1 of the list and bigger than -1
    Input: l - list of complex numbers
           s - the complex number as a list
           index - the position where the number should be inserted
    Output: adds an element to the list (if it is possible)
    Exceptions: -
    '''
    if index>-1 and index<len(l)-1:
        undoSave(complexList)
        l.insert(index,s)
        print("The element was inserted!")
    else:
        print("The position is out of range")
    return

def removePosition(l,pos):
    '''
    Removes the number at the given position
    Input: l - list of complex numbers
           pos - position of element
    Output: Removes an element if possible
    Exceptions: -
    '''
    if pos>-1 and pos<len(l):
        undoSave(complexList)
        l.pop(pos)
        print("Element at position",pos,"was removed!")
    else:
        print("The position is out of range!")
    return

def removePositions(l,pos1,pos2):
    '''
    Removes the complex numbers from position1 to position2
    Input: l - list of complex numbers
           pos1 - position of the first element
           pos2 - position of the second elemnt
    Output: Removes elements from one position to another
    Exceptions: -
    '''
    if pos1<pos2:
        if pos1>-1 and pos2<len(l):
            undoSave(complexList)
            i=pos1
            while i<=pos2:
                l.pop(pos1)
                i+=1
            print("Elements from",pos1,"to",pos2,"were removed!")
        else:
            print("Positions are invalid!")
    else:
        print("First position is equal or bigger than the second position")
    return

def replaceNumber(l,num1,num2):
    '''
    Replaces all the occurrences of first number with the second number
    Input: l - list of complex numbers
           num1 - first number
           num2 - second number
    Output: Change elements from the list
    Exceptions: -
    '''
    if not num1 in l:
        print("The first number is not in the list. No change was made!")
    else:
        undoSave(complexList)
        for i in range(len(l)):
            if l[i]==num1:
                l[i]=num2
        print("The elements were replaced!")
    return

def toString(s):
    '''
    Converts a list of two elements into a string which represents a complex number
    Input: s - a short list which represents a complex number
    Output: string - the complex number as a string
    Exceptions: -
    '''
    string=str(s[0])
    if s[1]>=0:
        string+='+'
    string+=str(s[1])
    string+='i'
    return string

def listComplexList(l):
    '''
    Prints a list of complex numbers
    '''
    print('-'*30)
    for i in range(len(l)):
        print(str(i)+'.',toString(l[i]))
    print('-'*30)
    return

def listReal(l,pos1,pos2):
    '''
    Prints the real numbers in list from pos1 to pos2
    Input: l - list of complex numbers
           pos1 - start position
           pos2 - end position
    Output: Prints a list of real elememts
    Exceptions: -
    '''
    real=[]
    if pos1<pos2:
        if pos1>-1 and pos2<len(l):
            i=pos1
            while i<=pos2:
                if isReal(l[i]):
                    real.append(l[i])
                i+=1
            if len(real)==0:
                print("No real numbers between positions:",pos1,"and",pos2)
            else:
                print("The list of real numbers between positions:",pos1,"and",pos2)
                listComplexList(real)
        else:
            print("Positions are invalid!")
    else:
        print("First position is equal or bigger than the second position")
    return

def compareOperation(compare):
    '''
    Returns the value -1,0,1 depending of the elements '<','=','>'
    Input: comapre - a character
    Output: comNum - a number in {-1,0,1}
    Exceptions: -
    '''
    if compare=='=':
        return 0
    elif compare=='<':
        return -1
    elif compare=='>':
        return 1
    else:
        raise ValueError
    return
    
def listModulus(l,modul,comp):
    '''
    Prints all the numbers from the list having a certain modulus
    Input: l - list of complex numbers
           modul - modulus that should be compared
           comp - a numnber which indicates how to operate
    Output: Prints a list of complex numbers
    Exceptions: -
    '''
    mod=[]
    if comp==0:
        for i in range(len(l)):
            if complexModulus(l[i])==modul:
                mod.append(l[i])
    elif comp==-1:
        for i in range(len(l)):
            if complexModulus(l[i])<modul:
                mod.append(l[i])
    else:
       for i in range(len(l)):
            if complexModulus(l[i])>modul:
                mod.append(l[i])
    if len(mod)==0:
        print('No element from the list satisfies your condition!')
    else:
        print("The elements from the list which satisfy your condition are: ")
        listComplexList(mod)
    return

def sumNumbers(l,pos1,pos2):
    '''
    Calculates the sum of the numbers between position 1 and position 2
    Input: l - list of complex numbers
           pos1 - start position
           pos2 - end position
    Output: sumx - sum of the complex numbers if it is possible
    Exceptions: -
    '''
    sumx=[0,0]
    if pos1<pos2:
        if pos1>-1 and pos2<len(l):
            i=pos1
            while i<=pos2:
                sumx=complexSum(sumx,l[i])
                i+=1
        else:
            print("Positions are invalid!")
    else:
        print("First position is equal or bigger than the second position")
    return sumx

def productNumbers(l,pos1,pos2):
    '''
    Calculates the product of the numbers between position 1 and position 2
    Input: l - list of complex numbers
           pos1 - start position
           pos2 - end position
    Output: sumx - product of the complex numbers if it is possible
    Exceptions: -
    '''
    prod=[1,0]
    if pos1<pos2:
        if pos1>-1 and pos2<len(l):
            i=pos1
            while i<=pos2:
                prod=complexProduct(prod,l[i])
                i+=1
        else:
            print("Positions are invalid!")
    else:
        print("First position is equal or bigger than the second position")
    return prod

def filterReal(l):
    '''
    Keeps only the real numbers from the list l
    Input: l - list of complex numbers
    Output: Changes the list l so that it contains only real numbers
    Exceptions: -
    '''
    undoSave(complexList)
    i=0
    while i<len(l):
        if isReal(l[i]):
            i+=1
        else:
            l.pop(i)
    print("The list was filtered!")
    return

def filterModulus(l,modul,comp):
    '''
    Keeps only the complex numbers from the list l with a certain modulus
    Input: l - list of complex numbers
           modul - modulus that should be compared
           comp - a numnber which indicates how to operate
    Output: Changes the list l so that it contains only numbers with a certain modulus
    Exceptions: -
    '''
    undoSave(complexList)
    if comp==0:
        i=0
        while i<len(l):
            if complexModulus(l[i])==modul:
                i+=1
            else:
                l.pop(i)
    elif comp==-1:
        i=0
        while i<len(l):
            if complexModulus(l[i])<modul:
                i+=1
            else:
                l.pop(i)
    else:
        i=0
        while i<len(l):
            if complexModulus(l[i])>modul:
                i+=1
            else:
                l.pop(i)
    print("The list was filtered!")
    return



def undoRecovery(l):
    '''
    Changes the state of the list l so that it comes back to its previous state
    Input: l - a list
    Output: Changes the list l
    Exceptions: -
    '''
    if len(undoList)==0:
        print('-'*30+"\nThere is no further undo!\n"+'-'*30)
    else:
        l.clear()
        el=undoList.pop()
        l.extend(el)
        print("Successful undo!")
    return

def testFilterModulus():
    '''
    test the function filterModulus
    '''
    l1=[[3,4],[6,8],[0,10],[11,0]]
    assert len(l1)==4
    filterModulus(l1,10,0)
    assert len(l1)==2
    filterModulus(l1,10,1)
    assert len(l1)==0
    return

def testFilterReal():
    '''
    test the function filterReal
    '''
    testList=[]
    for i in complexList:
        testList.append(i)
    l1=[[1,1],[1,2]]
    assert len(l1)==2
    filterReal(l1)
    assert len(l1)==0
    assert len(testList)==10
    filterReal(testList)
    assert len(testList)==3
    return
    
def testProductNumbers():
    '''
    test the function productNumbers
    '''
    testList=[]
    for i in complexList:
        testList.append(i)
    assert productNumbers(testList,0,1)==[14,0]
    assert productNumbers(testList,0,2)==[-42,-28]
    assert productNumbers(testList,4,6)==[0,0]
    return

def testSumNumbers():
    '''
    test the function sumNumbers
    '''
    testList=[]
    for i in complexList:
        testList.append(i)
    assert sumNumbers(testList,0,1)==[8,6]
    assert sumNumbers(testList,0,2)==[5,4]
    assert sumNumbers(testList,4,6)==[11,10]
    return
    
def testCompareOperation():
    '''
    test the function compareOperation
    '''
    assert compareOperation('=')==0
    assert compareOperation('<')==-1
    assert compareOperation('>')==1
    return


def testToString():
    '''
    test the function toString
    '''
    assert toString([2,2])=="2+2i"
    assert toString([0,0])=="0+0i"
    assert toString([0,2])=="0+2i"
    assert toString([5,-3])=="5-3i"
    assert toString([-1,-1])=="-1-1i"
    return
    
def testReplaceNumber():
    '''
    test the function replaceNumber
    '''
    testList=[]
    for i in complexList:
        testList.append(i)
    assert len(testList)==10
    assert ([-7,10] in testList)==True
    replaceNumber(testList,[-7,10],[-7,-7])
    assert len(testList)==10
    assert ([-7,10] in testList)==False
    assert ([-7,-7] in testList)==True
    replaceNumber(testList,[-7,-7],[77,77])
    assert len(testList)==10
    assert ([-7,-7] in testList)==False
    assert ([77,77] in testList)==True
    assert ([2000,2000] in testList)==False
    replaceNumber(testList,[2000,2000],[250,250])
    assert len(testList)==10
    assert ([250,250] in testList)==False
    return
    
def testRemovePositions():
    testList=[]
    for i in complexList:
        testList.append(i)
    assert len(testList)==10
    removePositions(testList,1,2)
    assert len(testList)==8
    removePositions(testList,8,8)
    assert len(testList)==8
    removePositions(testList,5,4)
    assert len(testList)==8
    removePositions(testList,-1,5)
    assert len(testList)==8
    removePositions(testList,5,20)
    assert len(testList)==8
    removePositions(testList,1,3)
    assert len(testList)==5
    return

    
def testRemovePosition():
    '''
    test the function removePosition
    '''
    testList=[]
    for i in complexList:
        testList.append(i)
    assert len(testList)==10
    removePosition(testList,1)
    assert len(testList)==9
    removePosition(testList,11)
    assert len(testList)==9
    removePosition(testList,15)
    assert len(testList)==9
    removePosition(testList,-1)
    assert len(testList)==9
    removePosition(testList,8)
    assert len(testList)==8
    return

def testInsertNumber():
    '''
    test the function insertNumber
    '''
    testList=[]
    for i in complexList:
        testList.append(i)
    assert len(testList)==10
    insertNumber(testList,[1,1],1)
    assert len(testList)==11
    insertNumber(testList,[1,1],11)
    assert len(testList)==11
    insertNumber(testList,[1,1],15)
    assert len(testList)==11
    insertNumber(testList,[1,1],-1)
    assert len(testList)==11
    insertNumber(testList,[1,1],8)
    assert len(testList)==12
    return

def testComplexNumber():
    '''
    test the function complexNumber
    '''
    assert complexNumber('1+3i')==[1,3]
    assert complexNumber('1-3i')==[1,-3]
    assert complexNumber('-1-3i')==[-1,-3]
    assert complexNumber('-1+3i')==[-1,3]
    return

def testAddNumber():
    '''
    test the function addNumber
    '''
    testList=[]
    for i in complexList:
        testList.append(i)
    assert len(testList)==10
    addNumber(testList,[100,100])
    assert len(testList)==11
    addNumber(testList,[1000,1000])
    assert len(testList)==12
    return

def runAllTests():
    '''
    run all the tests
    '''
    testComplexNumber()
    testAddNumber()
    testInsertNumber()
    testRemovePosition()
    testRemovePositions()
    testReplaceNumber()
    testToString()
    testCompareOperation()
    testSumNumbers()
    testProductNumbers()
    testFilterReal()
    testFilterModulus()
    print('-'*50+'\nWELL DONE!\n'+'-'*50)


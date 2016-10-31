from Controller import *
'''
This is the menu-based UI of the Complex Numbers DDTool

The options are explained pretty clearly in the menus

NOTE! In this UI the user uses only numbers for options and values
'''

def mainMenu2():
    '''
    Generates the main menu of the app
    '''
    print("Welcome to Complex Numbers DDTool!")
    while True:
        try:
            printMenu()
            print("Please introduce your option in the following line:")
            option=input(">>> ")
            if option=='1':
                submenuAdd()
            elif option=='2':
                submenuInsert()
            elif option=='3':
                submenuRemove1()
            elif option=='4':
                submenuRemove2()
            elif option=='5':
                submenuReplace()
            elif option=='6':
                submenuList1()
            elif option=='7':
                submenuList2()
            elif option=='8':
                submenuList3()
            elif option=='9':
                submenuSum()
            elif option=='10':
                submenuProduct()
            elif option=='11':
                submenuFilter1()
            elif option=='12':
                submenuFilter2()
            elif option=='13':
                submenuUndo()
            elif option=='0':
                    print("-"*50+"\nThanks for using the app! Have a nice day!\n"+"-"*50)
                    break
            else:
                raise ValueError
                
        except ValueError:
            print("-"*50+"\nPlease enter a valid option!\n"+"-"*50)
        input("Press any key to continue...")

def printMenu():
    '''
    Prints the main menu of the app
    '''
    str="\n THE AVAILABLE OPTIONS: \n\n"
    str+=" 1 - Add complex number to the list\n"
    str+=" 2 - Insert a complex number in the list\n"
    str+=" 3 - Remove an element at a certain position\n"
    str+=" 4 - Remove multiple elements\n"
    str+=" 5 - Replace numbers with a given number\n"
    str+=" 6 - Prints the list of complex numbers\n"
    str+=" 7 - Prints the real numbers\n"
    str+=" 8 - Prints the elements with a certain modulus\n"
    str+=" 9 - Calculates the sum of complex numbers\n"
    str+=" 10 - Calculates the product of complex numbers\n"
    str+=" 11 - Keep only real numbers in the list\n"
    str+=" 12 - Kepp only elements with a certain modulus\n"
    str+=" 13 - Undo\n"
    str+=" 0 - Exit\n"
    print(str)

def readComplexNumber():
    '''
    Read a complex number
    Input: -
    Output: [s0,s1] - a list which represents the complex number
    '''
    while True:
        try:
            print('-'*50)
            s0=int(input("Enter the real part of the number: "))
            s1=int(input("Enter the imaginary part of the number: "))
            return [s0,s1]
        except ValueError:
            print('-'*50)
            print("You introduced invalid values!")

def readPosition():
    '''
    Read the position of the element
    Input: -
    Output: p1 - position in list
    '''
    while True:
        try:
            print('-'*50)
            p1=int(input("Enter the position of the element: "))
            return p1
        except ValueError:
            print('-'*50)
            print("You introduced an invalid position!")      

def readPositions():
    '''
    Read the position of the element
    Input: -
    Output: [p1,p2] - a list which contains two positions
    '''
    while True:
        try:
            print('-'*50)
            p1=int(input("Enter the start position: "))
            p2=int(input("Enter the finish position: "))
            return [p1,p2]
        except ValueError:
            print('-'*50)
            print("You introduced an invalid position!")
    
def readModulus():
    '''
    Reads a value which represents a modulus
    Input: -
    Output: mod - the value of modulus
    '''
    while True:
        try:
            print('-'*50)
            mod=int(input("Enter the value you want to compare: "))
            return mod
        except ValueError:
            print('-'*50)
            print("You introduced an invalid value!")

def printModulusMenu():
    '''
    prints a menu for comparison operators
    '''
    str='-'*50
    str+='\n 0 - If you want the elements with the same modulus'
    str+='\n 1 - If you want the elements smaller than the given modulus'
    str+='\n 2 - If you want the elements bigger than the given modulus'
    str+='\n'+'-'*50
    print(str)
    
def readOperator():
    '''
    Selects the comparison operates
    Input: -
    Output: a value which indicates the comparison operator to be used
    '''
    while True:
        try:
            printModulusMenu()
            choice=int(input("Enter your option: "))
            if choice==0:
                return 0
            elif choice==1:
                return -1
            elif choice==2:
                return 1
            else:
                raise ValueError
        except ValueError:
            print('-'*50)
            print("You introduced an invalid value!")
        
def submenuAdd():
    '''
    The menu for function 'add'
    '''
    print("\nAdd an element to the list")
    complexNr=readComplexNumber()
    print('-'*50)
    addNumber(complexList,complexNr)
    print("A number was successfully added!")

def submenuInsert():
    '''
    The menu for function 'insert'
    '''
    print("\nInsert an element in the list:")
    complexNr=readComplexNumber()
    pos=readPosition()
    print('-'*50)
    try:
        insertNumber(complexList,complexNr,pos)
        print("The element was inserted!")
    except ValueError:
        print("The position is out of range")
    
def submenuRemove1():
    '''
    The menu for function 'remove' part 1
    '''
    print("\nRemove an element:")
    pos=readPosition()
    print('-'*50)
    try:
        removePosition(complexList,pos)
        print("Element at position",pos,"was removed!")
    except valueError:
        print("The position is out of range!")

def submenuRemove2():
    '''
    The menu for function 'remove' part 2
    '''
    print("\nRemove multiple elements:")
    positions=readPositions()
    pos1=positions[0]
    pos2=positions[1]
    print('-'*50)
    try:
        removePositions(complexList,pos1,pos2)
        print("Elements from",pos1,"to",pos2,"were removed!")
    except ValueError as ve:
        print(str(ve))

def submenuReplace():
    '''
    The menu for function 'replace'
    '''
    print("\nReplace the first number with the second number:")
    print("\nFirst number")
    complexNr1=readComplexNumber()
    print('-'*50)
    print("Second number")
    complexNr2=readComplexNumber()
    print('-'*50)
    try:
        replaceNumber(complexList,complexNr1,complexNr2)
        print("The elements were replaced!")
    except ValueError as ve:
        print(str(ve))
    
def submenuList1():
    '''
    The menu for function 'list' part 1
    '''
    print("The list of complex numbers is: ")
    if len(complexList)==0:
        print("-"*30+"\nThe list is empty!\n"+"-"*30)
    else:
        listComplexList(complexList)

def submenuList2():
    '''
    The menu for function 'list' part 2
    '''
    print("\nThe positions between which you want to check the property:")
    positions=readPositions()
    pos1=positions[0]
    pos2=positions[1]
    print('-'*50)
    try:
        print("The list of real numbers between positions:",pos1,"and",pos2)
        listReal(complexList,pos1,pos2)
    except ValueError as ve:
        print(str(ve))

def submenuList3():
    '''
    The menu for function 'list' part 3
    '''
    print("\nCompare the modulus of the elements:")
    modulus=readModulus()
    op=readOperator()
    print('-'*50)
    try:
        print("The elements from the list which satisfy your condition are: ")
        listModulus(complexList,modulus,compareOperation(comList[2]))
    except ValueError as ve:
        print(str(ve))

def submenuSum():
    '''
    The menu for function 'sum'
    '''
    print("\nThe sum of the elements between two positions:")
    positions=readPositions()
    pos1=positions[0]
    pos2=positions[1]
    print('-'*50)
    try:
        sumx=sumNumbers(complexList,pos1,pos2)
        print("The sum of elements from",pos1,"to",pos2,"is:",toString(sumx))
    except ValueError as ve:
        print(str(ve))

def submenuProduct():
    '''
    The menu for function 'product'
    '''
    print("\nThe product of the elements between two positions:")
    positions=readPositions()
    pos1=positions[0]
    pos2=positions[1]
    print('-'*50)
    try:
        prod=productNumbers(complexList,pos1,pos2)
        print("The product of elements from",pos1,"to",pos2,"is:",toString(prod))
    except ValueError as ve:
        print(str(ve))

def submenuFilter1():
    '''
    The menu for function 'filter' part 1
    '''
    print("\nKeep only the real elements of the list:")
    filterReal(complexList)
    print("The list was filtered!")

def submenuFilter2():
    '''
    The menu for function 'filter' part 2
    '''
    print("\nKeep only the elements having a ceratin modulus:")
    modulus=readModulus()
    op=readOperator()
    print('-'*50)
    filterModulus(complexList,modulus,op)
    print("The list was filtered!")

def submenuUndo():
    try:
        undoRecovery(complexList)
        print("Successful undo!")
    except ValueError:
        print('-'*30+"\nThere is no further undo!\n"+'-'*30)


from Controller import *
from Command import *
'''
This is the command-based UI of the Complex Numbers DDTool

There are several commands that can be used:

1. add complex_number

    - It adds the complex_number to the list

2. insert complex_number at position

    - It inserts the complex_number at a certain position of the list

3. remove position

    - Removes the element at a position

4. remove position1 to position2

    - Removes the elementsbetween two positions

5. replace complex_number1 with complex_number1

    - Replace all the occurrences of the complex_number1 with the complex_number2

6. list

    - Show the list of elements

7. list real position1 to position2

    - Show all the real elements from the list between position1 and position2

8. list modulo </=/> number

    - Show all the elements which have a modulus smaller/equal/bigger than number

9. sum position1 to position2

    - Show the sum of the elements between positiona and position2

10. product position1 to position2

    - Show the product of the elements between positiona and position2

11. filter real

    - Keep only real numbers in the list

12. filter modulo </=/> number

    - Keep in the list only the elements having modulus smaller/equal/bigger than number

13. undo

    - undo the last operation that modified program data

14. exit

    - close the program

Examples:

    add 1+4i
    insert 1+1i at 1
    remove 1
    remove 1 to 3
    replace 1+3i with 5-3i
    list
    list real 1 to 5
    list modulo < 10
    sum 1 to 5
    product 1 to 5
    filter real
    filter modulo > 6
    undo
    exit

'''

def mainMenu1():
    '''
    Generates the main menu of the app
    '''
    print("Welcome to Complex Numbers DDTool!")
    while True:
        try:
            print("Please introduce your command in the following line:")
            command=input(">>> ")
            comList=command.split()
            if commandIsValid(comList):
                if comList[0]=='add':
                    submenuAdd(comList)
                elif comList[0]=='insert':
                    submenuInsert(comList)
                elif comList[0]=='remove':
                    submenuRemove(comList)
                elif comList[0]=='replace':
                    submenuReplace(comList)
                elif comList[0]=='list':
                    submenuList(comList)
                elif comList[0]=='sum':
                    submenuSum(comList)
                elif comList[0]=='product':
                    submenuProduct(comList)
                elif comList[0]=='filter':
                    submenuFilter(comList)
                elif comList[0]=='undo':
                    submenuUndo()
                else:
                    print("-"*50+"\nThanks for using the app! Have a nice day!\n"+"-"*50)
                    break
                
        except ValueError:
            print("-"*50+"\nThe command is invalid!\n"+"-"*50)

def submenuAdd(comList):
    '''
    The menu for function 'add'
    '''
    complexNr=complexNumber(comList[1])
    addNumber(complexList,complexNr)

def submenuInsert(comList):
    '''
    The menu for function 'insert'
    '''
    complexNr=complexNumber(comList[1])
    pos=int(comList[3])
    insertNumber(complexList,complexNr,pos)
    
def submenuRemove(comList):
    '''
    The menu for function 'remove'
    '''
    if len(comList)==2:
        pos=int(comList[1])
        removePosition(complexList,pos)
    else:
        pos1=int(comList[1])
        pos2=int(comList[3])
        removePositions(complexList,pos1,pos2)

def submenuReplace(comList):
    '''
    The menu for function 'replace'
    '''
    complexNr1=complexNumber(comList[1])
    complexNr2=complexNumber(comList[3])
    replaceNumber(complexList,complexNr1,complexNr2)
    
def submenuList(comList):
    '''
    The menu for function 'list'
    '''
    if len(comList)==1:
        print("The list of complex numbers is: ")
        if len(complexList)==0:
            print("-"*30+"\nThe list is empty!\n"+"-"*30)
        else:
            listComplexList(complexList)
    elif len(comList)==5:
        pos1=int(comList[2])
        pos2=int(comList[4])
        listReal(complexList,pos1,pos2)
    else:
        modulus=int(comList[3])
        listModulus(complexList,modulus,compareOperation(comList[2]))

def submenuSum(comList):
    '''
    The menu for function 'sum'
    '''
    pos1=int(comList[1])
    pos2=int(comList[3])
    sumx=sumNumbers(complexList,pos1,pos2)
    print("The sum of elements from",pos1,"to",pos2,"is:",toString(sumx))

def submenuProduct(comList):
    '''
    The menu for function 'product'
    '''
    pos1=int(comList[1])
    pos2=int(comList[3])
    prod=productNumbers(complexList,pos1,pos2)
    print("The product of elements from",pos1,"to",pos2,"is:",toString(prod))

def submenuFilter(comList):
    '''
    The menu for function 'filter'
    '''
    if len(comList)==2:
        filterReal(complexList)
    else:
        modulus=int(comList[3])
        filterModulus(complexList,modulus,compareOperation(comList[2]))

def submenuUndo():
    '''
    The menu for function 'undo'
    '''
    undoRecovery(complexList)


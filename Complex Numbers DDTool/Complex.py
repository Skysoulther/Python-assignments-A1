from math import sqrt

def complexModulus(s):
    '''
    Calculates the modulus of a complex number
    Input: s - a list which contains the real part and the imaginary part of the number
    Output: the modulus of the number
    Exceptions: -
    '''
    return sqrt(s[0]*s[0]+s[1]*s[1])

def complexSum(s,t):
    '''
    Calculates the sum of two complex numbers
    Input: s,t - two short lists which represent complex numbers
    Output: the sum of two complex numbers
    Exceptions: -
    '''
    return [s[0]+t[0],s[1]+t[1]]

def complexProduct(s,t):
    '''
    Calculates the product of two complex numbers
    Input: s,t - two short lists which represent complex numbers
    Output: the product of two complex numbers
    Exceptions: -
    '''
    return [s[0]*t[0]-s[1]*t[1],s[0]*t[1]+s[1]*t[0]]

def isReal(s):
    '''
    Checks if a number is real or not
    Input: s - a short list which represent a complex number
    Output: True - if the number is real
            False - otherwise
    Exceptions: -
    '''
    return s[1]==0
    
def testComplexModulus():
    '''
    test the function complexModulus
    '''
    assert complexModulus([3,4])==5
    assert complexModulus([-6,8])==10
    assert complexModulus([-6,-8])==10
    return

def testComplexSum():
    '''
    test the function complexSum
    '''
    assert complexSum([1,2],[2,3])==[3,5]
    assert complexSum([5,6],[-4,-5])==[1,1]
    assert complexSum([3,3],[7,-5])==[10,-2]
    return

def testComplexProduct():
    '''
    test the function complexProduct
    '''
    assert complexProduct([3,13],[7,17])==[-200,142]
    assert complexProduct([3,2],[3,2])==[5,12]
    assert complexProduct([0,1],[-1,-1])==[1,-1]
    return

def testIsReal():
    '''
    test the function isReal
    '''
    assert isReal([1,2])==False
    assert isReal([0,-2])==False
    assert isReal([0,0])==True
    assert isReal([99,0])==True
    return

#testComplexModulus()
#testComplexSum()
#testComplexProduct()
#testIsReal()

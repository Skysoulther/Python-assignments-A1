'''
Created on 4 Jan 2017

@author: DDL
'''
import unittest

class SortingFilter:
    '''
    class for the functions
    '''
    @staticmethod
    def gnomeSort(lista,f):
        '''
        function for implementing gnome sort on a list
        input: lista - list to be sorted
               f - function for comparing two items
        Output: the sorted list
        '''
        for pos in range(1,len(lista)):
            while pos>0 and not f(lista[pos-1],lista[pos]):
                lista[pos-1],lista[pos]=lista[pos],lista[pos-1]
                pos-=1
        return lista
    
    @staticmethod 
    def filter(lista,filt):
        '''
        function for filtering a list
        input: lista - list to be sorted
               f - function for checking an element from the list
        output: filteredList - The filtered list
        '''
        filteredList=[]
        for el in lista:
            if filt(el):
                filteredList.append(el)
        return filteredList       
    
    @staticmethod
    def comparison1(a,b):
        '''
        return True if first argument is smaller than the second
        '''
        return a<b;
    
    @staticmethod
    def comparison2(a,b):
        '''
        return True if first argument is greater than the second
        '''
        return a>b;
    
    @staticmethod
    def filter1(a):
        '''
        returns True if the argument is even
        '''
        return a%2==0
        
class TestSortingFilter(unittest.TestCase):
    '''
    test the SortingFilter class
    '''
    def setUp(self):
        '''
        set up the data for tests
        '''
        self.test1=[5,4,3,2,1]
        self.test2=[5,3,4,2,1]
        self.test3=["Ana","Paul","Vlad","Bogdan","Raul"]
    
    def testSorting(self):
        '''
        tests the sorting
        '''
        self.assertEqual(self.test1,[5,4,3,2,1])
        SortingFilter.gnomeSort(self.test1, SortingFilter.comparison1)
        self.assertEqual(self.test1,[1,2,3,4,5])
        self.assertEqual(self.test2,[5,3,4,2,1])
        SortingFilter.gnomeSort(self.test2, SortingFilter.comparison2)
        self.assertEqual(self.test2,[5,4,3,2,1])
        self.assertEqual(self.test3,["Ana","Paul","Vlad","Bogdan","Raul"])
        SortingFilter.gnomeSort(self.test3,SortingFilter.comparison1)
        self.assertEqual(self.test3,["Ana","Bogdan","Paul","Raul","Vlad"])
    
    def testFilter(self):
        '''
        test the filter
        '''
        self.assertEqual(self.test1,[5,4,3,2,1])
        filtered1=SortingFilter.filter(self.test1,SortingFilter.filter1)
        self.assertEqual(filtered1,[4,2])
        filtered2=[]
        for i in self.test3:
            filtered2.append(len(i))
        filtered2=SortingFilter.filter(filtered2,SortingFilter.filter1)
        self.assertEqual(filtered2,[4,4,6,4])
        self.assertEqual(len(filtered2),4)
        
        
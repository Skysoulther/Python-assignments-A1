'''
Created on Dec 12, 2016

@author: ddie2115
'''
import unittest
class iterableData:
    '''
    class for dealing with iterations
    '''
    def __init__(self):
        '''
        Initialize the iterator
        '''
        self.__store={}
        self.__keys=[]
    
    def __iter__(self):
        '''
        the iterator of the iteration. Returns the current element
        '''
        self.__index=-1
        return self
    
    def __next__(self):
        '''
        returns the next element from the iteration
        '''
        if self.__index<len(self.__store)-1:
            self.__index+=1
        else:
            raise StopIteration
        return self.__keys[self.__index]
    
    def __setitem__(self, key, item):
        '''
        save the 'item' in the dictionary at the given 'key'
        '''
        self.__store[key]=item
        self.__keys.append(key)
        return True

    def __getitem__(self,key):
        '''
        Returns the item with the given 'key'
        '''
        return self.__store[key]

    def __delitem__(self,item):
        '''
        Deletes the given item from the dictionary
        '''
        del self.__store[item]
        index=self.__keys.index(item)
        del self.__keys[index]
        return True
    
    def __len__(self):
        '''
        Returns the length of the iteration
        '''
        return len(self.__store)
    
    def pop(self,key):
        '''
        
        '''
        item=self.__store[key]
        del self.__store[key]
        return item


class testIterator(unittest.TestCase):
    '''
    test the class iterableDta
    '''
    def setUp(self):
        '''
        setup the data to work on
        '''
        self.data=iterableData()
    
    def testIterableData(self):
        '''
        test the iterableData class
        '''
        test=[]
        self.assertEqual(len(self.data),0)
        self.data[1]=1111
        self.data[2]="Two"
        self.assertEqual(len(self.data),2)
        for element in self.data:
            test.append(self.data[element])
        self.assertEqual(test,[1111,"Two"])
        del self.data[1]
        self.assertEqual(len(self.data),1)
        self.assertEqual(self.data[2],"Two")
        
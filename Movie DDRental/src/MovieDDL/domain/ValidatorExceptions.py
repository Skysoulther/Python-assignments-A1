'''
Created on 21 Nov 2016

@author: DDL
'''
class StoreException(Exception):
    '''
    Class for store exceptions
    '''
    def __init__(self,message):
        '''
        Creates an exception with a certain message
        '''
        self.__message=message
    
    def _getMessage(self):
        '''
        Returns the message of Exception
        '''
        return self.__message
        
    def __str__(self):
        '''
        Returns exception as string
        '''
        return self._getMessage()

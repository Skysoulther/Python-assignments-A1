'''
Created on 19 Nov 2016

@author: DDL
'''

class ControllerException(Exception):
    '''
    Class for exceptions in controller
    '''
    def __init__(self,message):
        '''
        Creates an error message
        '''
        self.__message=message
        
    def _getMessage(self):
        '''
        Returns the message of Exception
        '''
        return self.__message
    
    def __str__(self):
        '''
        Returns a message as a string
        '''
        return self._getMessage()
    
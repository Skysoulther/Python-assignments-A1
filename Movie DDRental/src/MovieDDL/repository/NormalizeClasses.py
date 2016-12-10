'''
Created on 10 Dec 2016

@author: DDL
'''
class JSONnormal:
    '''
    class to work with json files
    '''
    def __init__(self):
        '''
        initialize class JSONnormal
        '''
        self.__jsonObject={}
        
        
    def __normalize(self,element):
        '''
        turn an pobject into a list of strings
        '''
        
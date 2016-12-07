'''
Created on 6 Dec 2016

@author: DDL
'''
from MovieDDL.controller.ControllerExceptions import ControllerException

class undoController:
    '''
    Controller for undo/redo operations
    '''
    def __init__(self):
        '''
        initialize a controller
        '''
        self.__undoList=[]
        self.__redoList=[]
        self.__pos1=-1
        self.__pos2=-1
    
    def store_undo(self,operation):
        '''
        stores an operation in undoList
        '''
        length=len(self.__undoList)
        if self.__pos1<length-1:
            for i in range(self.__pos1+1,length):
                self.__undoList.pop()
        self.__pos1+=1
        self.__undoList.append(operation)
        
    def store_redo(self,operation):
        '''
        stores an operation in undoList
        '''
        length=len(self.__redoList)
        if self.__pos2<length-1:
            for i in range(self.__pos2+1,length):
                self.__redoList.pop()
        self.__pos2+=1
        self.__redoList.append(operation)  
    
    def load_undo(self):
        '''
        load an operation from undolIst
        '''
        if self.__pos1==-1:
            raise ControllerException("There is no further undo!\n")
        undo=self.__undoList[self.__pos1]
        self.__pos1-=1
        self.__pos2-=1
        return undo
    
    def load_redo(self):
        '''
        load an operation from redolIst
        '''
        if self.__pos2==len(self.__redoList)-1:
            raise ControllerException("There is no further redo!\n")
        redo=self.__redoList[self.__pos2+1]
        self.__pos2+=1
        self.__pos1+=1
        return redo
    
class Operation:
    '''
    Class for operation
    '''
    def __init__(self,name,parameters):
        '''
        initialize an operation
        '''
        self.__functions={}
        self.__name=name
        self.__parameters=parameters
    
    def get_name(self):
        '''
        get the name of the operation
        '''
        return self.__name
    
    def get_parameters(self):
        '''
        get the parameters of the operation
        '''
        return self.__parameters
    
        
        
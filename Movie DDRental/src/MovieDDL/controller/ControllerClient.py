'''
Created on 4 Nov 2016

@author: DDL
'''
from MovieDDL.controller.ControllerExceptions import ControllerException
from MovieDDL.controller.UndoController import Operation
from MovieDDL.domain.Entities import Client
class clientController():
    '''
    Contains functions which operates on clients
    '''
    def __init__(self, repoClient,validator,undo):
        '''
        Creates a controller for clients
        '''
        self._undoControl=undo
        self._repository=repoClient
        self.__validator=validator
    
    def _validateID(self,Id):
        '''
        Validates ID
        Exceptions: Controller Exception when ID is not a number
        '''
        try:
            Id=int(Id)
        except ValueError:
            raise ControllerException("The ID should be a number!\n")
        return True
    
    def add_client(self,client):
        '''
        Add a client to the repository
        Input: client -  a list which contains the values of the fields of a client
        Output: -
        Exceptions: -
        '''
        self._validateID(client[0])
        client=Client(int(client[0]),client[1])
        self.__validator.validateClient(client)
        self._repository.add_client(client)
        self._undoControl.store_undo([Operation("remove_client",[client.get_clientID()])])
        self._undoControl.store_redo([Operation("add_client",[client])])
    
    def remove_client(self, Id):
        '''
        Remove a client from the repository if it exists
        Input: Id - a natural number
        Output: -
        Exceptions: -
        '''
        self._validateID(Id)
        Id=int(Id)
        self.__validator.validateID(Id)
        client=self._repository.remove_client(Id)
        return client
    
    def get_allClients(self):
        '''
        Returns the list of clients
        '''
        return self._repository.get_all()
    
    def edit_client(self,Id,Name):
        '''
        Edits the name of the client with a certain ID
        '''
        self._validateID(Id)
        Id=int(Id)
        if self._repository.find_by_ID(Id):
            client=self._repository.return_client_Id(Id)
            self._undoControl.store_undo([Operation("edit_client",[Id,client.get_clientName()])])
            self._repository.update_client(Id,Name)
            self._undoControl.store_redo([Operation("edit_client",[Id,Name])])
        else:
            raise ControllerException("The client you want to edit can't be found!\n")
    
    def return_client_Id(self,Id):
        '''
        Returns a client with a certain Id
        '''
        self._validateID(Id)
        Id=int(Id)
        self.__validator.validateID(Id)
        return self._repository.return_client_Id(Id)
    
    def search_client(self, field, information):
        '''
        Searches all the clients with the mentioned field and information
        '''
        return self._repository.search_client(field,information)

################################################################################

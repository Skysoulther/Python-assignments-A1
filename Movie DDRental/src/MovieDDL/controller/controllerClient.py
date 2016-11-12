'''
Created on 4 Nov 2016

@author: DDL
'''

class clientController():
    '''
    Contains functions which operates on clients
    '''
    def __init__(self, repoClient):
        '''
        Creates a controller for clients
        '''
        self._repository=repoClient
    
    def _validateID(self,Id):
        '''
        Validates ID
        Exceptions: Controller Exception when ID is not a number
        '''
        try:
            Id=int(Id)
        except ValueError:
            raise ControllerException("The ID should be a number!\n")
    
    def add_client(self,client):
        '''
        Add a client to the repository
        Input: client -  a list which contains the values of the fields of a client
        Output: -
        Exceptions: -
        '''
        self._validateID(client[0])
        client[0]=int(client[0])
        self._repository.add_client(client)
    
    def remove_client(self, Id):
        '''
        Remove a client from the repository if it exists
        Input: Id - a natural number
        Output: -
        Exceptions: -
        '''
        self._validateID(Id)
        Id=int(Id)
        self._repository.remove_client(Id)
    
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
            self._repository.update_client(Id,Name)
        else:
            raise ControllerException("The client you want to edit can't be found!\n")
    
    def return_client_Id(self,Id):
        '''
        Returns a client with a certain Id
        '''
        self._validateID(Id)
        Id=int(Id)
        return self._repository.return_client_Id(Id)
    
    def search_movie(self, field, information):
        '''
        Searches all the clients with the mentioned field and information
        '''
        return self._repository.search_movie(field,information)

################################################################################

class ControllerException(Exception):
    '''
    Class for exceptions in controller
    '''
    def __init__(self,message):
        '''
        Creates an error message
        '''
        self.__message=message
    
    def __str__(self):
        '''
        Returns a message as a string
        '''
        return self.__message
    
#################################################################################
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
    
    def add_client(self,client):
        '''
        Add a client to the repository
        Input: client -  a list which contains the values of the fields of a movie
        Output: -
        Exceptions: -
        '''
        self._repository.add_client(client)
    
    def remove_client(self, Id):
        '''
        Remove a client from the repository if it exists
        Input: Id - a natural number
        Output: -
        Exceptions: -
        '''
        self._repository.remove_client(Id)
    
    def get_allClients(self):
        '''
        Returns the list of clients
        '''
        return self._repository.get_all()
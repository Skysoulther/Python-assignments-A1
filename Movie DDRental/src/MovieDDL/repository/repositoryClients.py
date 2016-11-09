'''
Created on 4 Nov 2016

@author: DDL
'''

class clientRepository:
    '''
    repository for the clients
    '''
    def __init__(self,validator,clients):
        '''
        Creates a repository for the clients
        '''
        self._clients=clients 
        self._validator=validator
    
    def find_by_ID(self,Id):
        '''
        Checks if the Id is in the list of clients
        Input: Id - a number
        Output: True if the Id exists, False otherwise
        Exceptions: -
        '''
        if Id in self._clients:
            return True
        else:
            return False
    
    def add_client(self,client):
        '''
        Adds a client in the repository
        Input: client - an object of the class Client
        Output: -
        Exceptions: -
        '''
        self._validator.validateClient(client)
        Id=int(client.get_clientID())
        if not self.find_by_ID(Id):
            self._clients[Id]=client
        else:
            raise ValueError("A client with the same ID already in the list"+"\n")
        
    def remove_client(self, Id):
        '''
        Removes a client from the repository
        Input: Id - a number
        Output: -
        Exceptions: -
        '''
        self._validator.validateID(Id)
        Id=int(Id)
        if self.find_by_ID(Id):
            self._clients.pop(Id)
        else:
            raise ValueError("There is no client with the ID: "+str(Id)+"\n")
    
    def get_all(self):
        '''
        Gets the dictionary of clients
        '''
        return self._clients
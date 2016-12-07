'''
Created on 4 Nov 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import RepositoryException

class clientRepository():
    '''
    repository for the clients
    '''
    def __init__(self):
        '''
        Creates a repository for the clients
        '''
        self.__clients={}
    
    def find_by_ID(self,Id):
        '''
        Checks if the Id is in the list of clients
        Input: Id - a number
        Output: True if the Id exists, False otherwise
        Exceptions: -
        '''
        if Id in self.__clients:
            return True
        else:
            return False
    
    def add_client(self,client):
        '''
        Adds a client in the repository
        Input: client - an object of the class Client
        Output: -
        Exceptions: RepositoryException if there is a client with the same ID
        '''
        Id=int(client.get_clientID())
        if not self.find_by_ID(Id):
            self.__clients[Id]=client
        else:
            raise RepositoryException("A client with the same ID already in the list"+"\n")
        
    def remove_client(self, Id):
        '''
        Removes a client from the repository
        Input: Id - a number
        Output: -
        Exceptions: RepositoryException id theere is no client with the ID 
        '''
        if self.find_by_ID(Id):
            return self.__clients.pop(Id)
        else:
            raise RepositoryException("There is no client with the ID: "+str(Id)+"\n")
    
    def return_client_Id(self,Id):
        '''
        Returns a client with a certain Id
        Input: Id - a number
        Output: self._clients[Id] - a client having the ID Id
        Exceptions: RepositoryException if there is no client with that Id
        '''
        if not self.find_by_ID(Id):
            raise RepositoryException("There is no movie with the ID: "+str(Id)+"\n")
        else:
            return self.__clients[Id]
    
    def update_client(self,Id,Name):
        '''
        Updates the client with a new name
        '''
        self.__clients[Id].set_clientName(Name)
    
    def get_all(self):
        '''
        Gets the dictionary of clients
        '''
        return self.__clients
    
    def search_client(self,field,information):
        '''
        Searches clients with certain properties in the repository
        Input: field - the field used for searching
               information - a partial string which is used for searching
        '''
        askedClients={}
        
        for key in self.__clients:
            client=self.__clients[key]
            fields={1:client.get_clientID,2:client.get_clientName}
            stringer=str(fields[field]()).lower()
            result=stringer.find(information.lower())
            if result!=-1:
                askedClients[client.get_clientID()]=client
                
        return askedClients
    
    
    
    
##################################################################################
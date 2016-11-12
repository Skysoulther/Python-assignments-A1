'''
Created on 4 Nov 2016

@author: DDL
'''
from MovieDDL.domain.Entities import Client

class clientRepository:
    '''
    repository for the clients
    '''
    def __init__(self,validator,clients):
        '''
        Creates a repository for the clients
        '''
        self.__clients=clients 
        self.__validator=validator
    
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
        client=Client(client[0],client[1])
        self.__validator.validateClient(client)
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
        self.__validator.validateID(Id)
        if self.find_by_ID(Id):
            self.__clients.pop(Id)
        else:
            raise RepositoryException("There is no client with the ID: "+str(Id)+"\n")
    
    def return_client_Id(self,Id):
        '''
        Returns a client with a certain Id
        Input: Id - a number
        Output: self._clients[Id] - a client having the ID Id
        Exceptions: RepositoryException if there is no client with that Id
        '''
        self.__validator.validateID(Id)
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
        if field==1:
            for key in self.__clients:
                client=self.__clients[key]
                stringer=str(client.get_clientID())
                result=stringer.find(information)
                if result!=-1:
                    askedClients[client.get_clientID()]=client
                
        elif field==2:
            for key in self.__clients:
                client=self.__clients[key]
                stringer=str(client.get_clientName()).lower()
                result=stringer.find(information.lower())
                if result!=-1:
                    askedClients[client.get_clientID()]=client
                
        
        return askedClients
    
    
################################################################################

class RepositoryException(Exception):
    '''
    Class for Repository Exceptions
    '''
    def __init__(self, message):
        '''
        Creates an error message
        '''
        self.__message=message
    
    def __str__(self):
        '''
        Returns a message as a string
        '''
        return self.__message
    
#######################################################################################

def testRepositoryClients():
    '''
    Test this repository
    '''
    from MovieDDL.domain.Validator import ClientValidator
    repoList={1:Client(1,"Client 1"),
              2:Client(2,"Client 2"),
              3:Client(3,"Client 3")}
    clientList1=[17,"Client 17"]
    clientList2=[2,"Client 56"]
    validator1=ClientValidator()
    repoTest=clientRepository(validator1,repoList)
    repoTest.add_client(clientList1)
    try:
        repoTest.add_client(clientList2)
        assert False
    except RepositoryException:
        assert True
    try:
        repoTest.remove_client(4)
        assert False
    except RepositoryException:
        assert True
    repoTest.remove_client(3)
    try:
        repoTest.return_client_Id(3)
        assert False
    except RepositoryException:
        assert True
    assert repoTest.return_client_Id(17).get_clientName()=="Client 17"
    assert repoTest.find_by_ID(2)
    assert repoTest.find_by_ID(3)==False
    assert repoTest.search_client(1, "5")=={}
    assert len(repoTest.search_client(2, "Cli"))==3
    print("well done!")

#testRepositoryClients()
'''
Created on 27 Nov 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.repository.RepositoryClients import clientRepository
from MovieDDL.domain.Entities import Client

class clientFileRepository(clientRepository):
    '''
    Hit all the walls in front of you in order to know how to avoid them the next time
    '''
    def __init__(self, fileName="clients.txt"):
        '''
        Constructor for file repository
        Input: fileName - the name of the file
        Output: -
        '''
        clientRepository.__init__(self)
        self.__fName=fileName
        self.__loadFromFile()
        
    def add_client(self, client):
        '''
        Method to add a new client
        Input: client - object of Class client
        Output: -
        '''
        clientRepository.add_client(self, client)
        self.__storeToFile()
    
    def remove_client(self, Id):
        '''
        Method to remove a client
        Input: Id - Id of the client to remove
        Output: -
        '''
        client=clientRepository.remove_client(self, Id)
        self.__storeToFile()
        return client
        
    def update_client(self, Id, Name):
        '''
        Method to edit the name of a client
        Input: Id - id of the client to edit
               Name - The new name of the client
        output: -
        '''
        clientRepository.update_client(self, Id, Name)
        self.__storeToFile()
    
    def __loadFromFile(self):
        try:
            f=open(self.__fName,"r")
            line=f.readline().strip()
            while line!="":
                attrs=line.split(";")
                client=Client(int(attrs[0]),attrs[1])
                clientRepository.add_client(self,client)
                line=f.readline().strip()
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close
    
    def __storeToFile(self):
        f=open(self.__fName, "w")
        clients=clientRepository.get_all(self)
        for key in clients:
            strf=str(clients[key].get_clientID())+";"+str(clients[key].get_clientName())+"\n"
            f.write(strf)
        f.close
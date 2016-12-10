'''
Created on 10 Dec 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.repository.RepositoryClients import clientRepository
from MovieDDL.domain.Entities import Client
import json

class clientJSONRepository(clientRepository):
    '''
    Hit all the walls in front of you in order to know how to avoid them the next time
    '''
    def __init__(self, fileName="clients.json"):
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
        f=open(self.__fName,"r")
        try:
            clients=json.load(f)
            for key in clients:
                client=self._JSONtoClient(clients[key])
                clientRepository.add_client(self, client)
        except EOFError:
            clientRepository.__movies={}
        except Exception as e:
            raise FileRepositoryException(e)
        finally:
            f.close()
    
    def __storeToFile(self):
        f=open(self.__fName, "w")
        clients={}
        self.__clients=clientRepository.get_all(self)
        for key in self.__clients:
            clients[key]=json.dumps(self.__clients[key].__dict__)
        json.dump(clients, f)
        f.close
    
    def _JSONtoClient(self,object):
        '''
        Convert JSON object to Client
        '''
        object=json.loads(object)
        name=object["_Client__name"]
        id=object["_Client__clientID"]
        return Client(id,name)
    
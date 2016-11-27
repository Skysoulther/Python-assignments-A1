'''
Created on 27 Nov 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import FileRepositoryException
from MovieDDL.domain.Entities import Client

class clientFileRepository:
    def __init__(self, fileName="clients.txt"):
        '''
        '''
        self._fName=fileName
        
    def _loadFromFile(self):
        clients={}
        try:
            f=open(self._fName,"r")
            line=f.readline().strip()
            while line!="":
                attrs=line.split(";")
                client=Client(int(attrs[0]),attrs[1])
                clients[int(attrs[0])]=client
                line=f.readline().strip()
        except IOError:
            raise FileRepositoryException()
        finally:
            f.close
            return clients
    
    def _storeToFile(self,clients):
        f=open(self._fName, "w")
        for key in clients:
            strf=str(clients[key].get_clientID())+";"+str(clients[key].get_clientName())+"\n"
            f.write(strf)
        f.close
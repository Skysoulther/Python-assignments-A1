'''
Created on 26 Nov 2016

@author: DDL
'''
import unittest
from MovieDDL.domain.Entities import Client
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.domain.Validator import ClientValidator
from MovieDDL.repository.RepositoryClients import clientRepository

class ClientsRepositoryTest(unittest.TestCase):
    '''
    Unit test-case for testing RepositoryClients module
    '''
    def setUp(self):
        '''
        the setup of data
        '''
        repoList={1:Client(1,"Client 1"),
              2:Client(2,"Client 2"),
              3:Client(3,"Client 3")}
        self.clientList1=[17,"Client 17"]
        self.clientList2=[2,"Client 56"]
        validator1=ClientValidator()
        self.repoTest=clientRepository(validator1,repoList)
        
    def testRepositoryClients(self):
        '''
        Test the repository of clients
        '''
        self.repoTest.add_client(self.clientList1)
        self.assertRaises(RepositoryException,self.repoTest.add_client,self.clientList1)
        self.assertRaises(RepositoryException,self.repoTest.add_client,self.clientList2)
        self.assertRaises(RepositoryException,self.repoTest.remove_client,4)
        self.repoTest.remove_client(3)
        self.assertRaises(RepositoryException,self.repoTest.return_client_Id,3)
        self.assertEqual(self.repoTest.return_client_Id(17).get_clientName(),"Client 17")
        self.assertTrue(self.repoTest.find_by_ID,2)
        self.assertFalse(self.repoTest.find_by_ID(3))
        self.assertEqual(self.repoTest.search_client(1, "5"),{})
        self.assertEqual(len(self.repoTest.search_client(2, "Cli")),3)
        
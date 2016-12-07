'''
Created on 26 Nov 2016

@author: DDL
'''
import unittest
from MovieDDL.domain.Entities import Client
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.repository.FileRepositoryClients import clientFileRepository

class ClientsRepositoryTest(unittest.TestCase):
    '''
    Unit test-case for testing RepositoryClients module
    '''
    def setUp(self):
        '''
        the setup of data
        '''
        self.clientList1=Client(17,"Client 17")
        self.clientList2=Client(2,"Client 56")
        self.repoTest=clientFileRepository("testClients.txt")
        
    def testRepositoryClients(self):
        '''
        Test the repository of clients
        '''
        self.repoTest.add_client(self.clientList1)
        self.assertRaises(RepositoryException,self.repoTest.add_client,self.clientList1)
        self.assertRaises(RepositoryException,self.repoTest.add_client,self.clientList2)
        self.assertRaises(RepositoryException,self.repoTest.remove_client,6)
        self.repoTest.remove_client(17)
        self.assertRaises(RepositoryException,self.repoTest.return_client_Id,17)
        self.assertEqual(self.repoTest.return_client_Id(5).get_clientName(),"Client 5")
        self.assertTrue(self.repoTest.find_by_ID,2)
        self.assertFalse(self.repoTest.find_by_ID(17))
        self.assertEqual(self.repoTest.search_client(1, "6"),{})
        self.assertEqual(len(self.repoTest.search_client(2, "Cli")),5)
        
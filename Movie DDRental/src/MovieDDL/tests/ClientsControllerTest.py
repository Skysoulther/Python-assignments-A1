'''
Created on 27 Nov 2016

@author: DDL
'''
import unittest
from MovieDDL.domain.Entities import Client
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.domain.Validator import ClientValidator
from MovieDDL.controller.ControllerExceptions import ControllerException
from MovieDDL.repository.RepositoryClients import clientRepository
from MovieDDL.controller.ControllerClient import clientController

class ClientsControllerTest(unittest.TestCase):
    '''
    Unit test-case for testing ControllerClients Module
    '''
    def setUp(self):
        '''
        the setup of data
        '''
        validator1=ClientValidator()
        repoTest=clientRepository(validator1,"testClients.txt")
        self.controlTest=clientController(repoTest)
    
    def testControllerClients(self):
        '''
        Test the controller for clients
        '''
        self.assertRaises(ControllerException,self.controlTest.add_client,["aba","Client 12"])
        self.assertEqual(len(self.controlTest.get_allClients()),5)
        self.controlTest.add_client([12,"Client 12"])
        self.assertEqual(len(self.controlTest.get_allClients()),6)
        self.assertRaises(RepositoryException,self.controlTest.add_client,[12,"Client 12"])
        self.assertRaises(ControllerException,self.controlTest.remove_client,"aba")
        self.controlTest.remove_client(12)
        self.assertEqual(len(self.controlTest.get_allClients()),5)
        self.assertRaises(ControllerException,self.controlTest.edit_client,12,"Block")
        self.assertEqual(self.controlTest.get_allClients()[5].get_clientName(),"Client 5")
        self.controlTest.edit_client(5, "The Client")
        self.assertEqual(self.controlTest.get_allClients()[5].get_clientName(),"The Client")
        self.assertEqual(self.controlTest.return_client_Id(5),self.controlTest.get_allClients()[5])
        self.assertEqual(len(self.controlTest.search_client(2, "the")),1)
        self.controlTest.edit_client(5, "Client 5")
        
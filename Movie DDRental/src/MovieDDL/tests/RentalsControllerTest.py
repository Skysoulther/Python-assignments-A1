'''
Created on 27 Nov 2016

@author: DDL
'''
import unittest
from MovieDDL.domain.Entities import *
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.domain.Validator import ClientValidator,MovieValidator,RentalValidator
from MovieDDL.controller.ControllerExceptions import ControllerException
from MovieDDL.repository.RepositoryClients import clientRepository
from MovieDDL.repository.RepositoryMovies import movieRepository
from MovieDDL.repository.RepositoryRentals import rentalRepository
from MovieDDL.controller.ControllerRental import rentalController

class MoviesControllerTest(unittest.TestCase):
    '''
    Unit test-case for testing ControllerRentals Module
    '''
    def setUp(self):
        '''
        the setup of data
        '''
        validator2=ClientValidator()
        repoTest2=clientRepository(validator2,"testClients.txt")
        validator1=MovieValidator()
        repoTest1=movieRepository(validator1,"testMovies.txt")
        validator=RentalValidator()
        repoTest=rentalRepository(validator,"testRentals.txt",repoTest1)
        self.controlTest=rentalController(repoTest1,repoTest2,repoTest)
        
    def testControllerRentals(self):
        '''
        Test the controller for rentals
        '''
        self.assertTrue(self.controlTest.checks_movie,2)
        self.assertRaises(ControllerException,self.controlTest.checks_movie,1)
        self.assertRaises(ControllerException,self.controlTest.checks_movie,-3)
        self.assertTrue(self.controlTest.checks_client(3))
        self.assertRaises(ControllerException,self.controlTest.checks_client,6)
        self.assertRaises(ControllerException,self.controlTest.checks_movie2,27)
        self.assertRaises(ControllerException,self.controlTest.checks_movie2,2)
        self.assertTrue(self.controlTest.checks_movie2,1)
        self.assertEqual(len(self.controlTest.get_allRentals()),2)
        self.controlTest.rent_movie([3,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=29,month=11,year=2016)])
        self.assertEqual(len(self.controlTest.get_allRentals()),3)
        self.assertRaises(ControllerException,self.controlTest.rent_movie, [4,1,datetime.date(day=12,month=11,year=2016),datetime.date(day=29,month=11,year=2016)])
        self.assertEqual(len(self.controlTest.get_allRentals()),3)
        self.assertRaises(RepositoryException,self.controlTest.return_rental,8,8)
        self.controlTest.return_rental(1, 1)
        self.assertEqual(len(self.controlTest.get_allRentals()),3)
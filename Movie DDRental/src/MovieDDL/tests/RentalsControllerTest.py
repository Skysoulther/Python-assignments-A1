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
        repoList={1:Rental(1,1,1,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016)),
              2:Rental(2,5,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=30,month=11,year=2016))}
        validator=RentalValidator()
        repoTest=rentalRepository(validator,repoList)
        repoList2={1:Client(1,"Client 1"),
              2:Client(2,"Client 2"),
              3:Client(3,"Client 3"),4:Client(4,"Client 4"),5:Client(5,"Client 5")}
        validator2=ClientValidator()
        repoTest2=clientRepository(validator2,repoList2)
        repoList1={1:Movie(1,"Test1","Description1","comedy"),
              2:Movie(2,"Test2","Description2","horror"),3:Movie(3,"Test3","Description3","action"),
              4:Movie(4,"Test4","Description4","action"),5:Movie(5,"Test5","Description5","adventure")}
        repoList1[1].set_availability(False)
        repoList1[5].set_availability(False)
        validator1=MovieValidator()
        repoTest1=movieRepository(validator1,repoList1)
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
        
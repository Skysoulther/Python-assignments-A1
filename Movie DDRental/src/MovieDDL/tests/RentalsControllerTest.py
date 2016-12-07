'''
Created on 27 Nov 2016

@author: DDL
'''
import unittest
import datetime
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.domain.Validator import RentalValidator
from MovieDDL.controller.ControllerExceptions import ControllerException
from MovieDDL.repository.FileRepositoryClients import clientFileRepository
from MovieDDL.repository.FileRepositoryMovies import movieFileRepository
from MovieDDL.repository.FileRepositoryRentals import rentalFileRepository
from MovieDDL.controller.ControllerRental import rentalController
from MovieDDL.controller.UndoController import undoController

class MoviesControllerTest(unittest.TestCase):
    '''
    Unit test-case for testing ControllerRentals Module
    '''
    def setUp(self):
        '''
        the setup of data
        '''
        repoTest2=clientFileRepository("testClients.txt")
        self.repoTest1=movieFileRepository("testMovies.txt")
        validator=RentalValidator()
        repoTest=rentalFileRepository(self.repoTest1,"testRentals.txt")
        undoControl=undoController()
        self.controlTest=rentalController(self.repoTest1,repoTest2,repoTest,validator,undoControl)
        
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
        self.controlTest.rent_movie([3,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=29,month=12,year=2016)])
        self.assertEqual(len(self.controlTest.get_allRentals()),3)
        self.assertRaises(ControllerException,self.controlTest.rent_movie, [4,1,datetime.date(day=12,month=11,year=2016),datetime.date(day=29,month=11,year=2016)])
        self.assertEqual(len(self.controlTest.get_allRentals()),3)
        self.assertRaises(RepositoryException,self.controlTest.return_rental,8,8)
        self.controlTest.return_rental(1, 1)
        self.assertEqual(len(self.controlTest.get_allRentals()),3)
        self.controlTest.undo()
        self.assertEqual(self.controlTest.get_allRentals()[1].get_returnedDate(),None)
        self.controlTest.undo()
        self.assertEqual(len(self.controlTest.get_allRentals()),2)
        self.controlTest.redo()
        self.assertEqual(len(self.controlTest.get_allRentals()),3)
        self.controlTest.undo()
    
    def testStatistics(self):
        '''
        Test the statistics
        '''
        self.assertEqual(len(self.controlTest.all_rentals()),2)
        listMovies=self.repoTest1.get_all()
        filter1=[listMovies[1],listMovies[5],]
        lateRentals=self.controlTest.late_rentals()
        mostRented1=self.controlTest.most_rented(1)
        mostRented2=self.controlTest.most_rented(2)
        mostActive=self.controlTest.active_clients()
        allRentals=self.controlTest.all_rentals()
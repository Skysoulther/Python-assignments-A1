'''
Created on 26 Nov 2016

@author: DDL
'''
import unittest
import datetime
from MovieDDL.domain.Entities import Rental
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.repository.FileRepositoryRentals import rentalFileRepository
from MovieDDL.repository.FileRepositoryMovies import movieFileRepository

class RentalsRepositoryTest(unittest.TestCase):
    '''
    Unit test-case for testing RepositoryRentals module
    '''
    def setUp(self):
        '''
        the setup of data
        '''
        rDate1=datetime.date(year=2016, month=10, day=30)
        dDate1=datetime.date(year=2016, month=11, day=7)
        dDate2=datetime.date(year=2015, month=10, day=10)
        self.rentalList1=Rental(17,20,21,rDate1,dDate1)
        self.rentalList2=Rental(2,22,23,rDate1,dDate2)
        repoTest1=movieFileRepository("testMovies.txt")
        self.repoTest=rentalFileRepository(repoTest1,"testRentals.txt")
        
    def testRepositoryRentals(self):
        '''
        Test the repository of rentals
        '''
        self.repoTest.add_rental(self.rentalList1)
        self.assertRaises(RepositoryException,self.repoTest.add_rental,self.rentalList1)
        self.assertRaises(RepositoryException,self.repoTest.add_rental,self.rentalList2)
        self.assertRaises(RepositoryException,self.repoTest.return_rental,4,5)
        self.assertEqual(len(self.repoTest.get_all()),3)
        self.repoTest.return_rental(5,5)
        self.assertEqual(len(self.repoTest.get_all()),3)
        self.assertTrue(self.repoTest.find_by_ID,2)
        self.assertFalse(self.repoTest.find_by_ID(6))
        self.repoTest.unreturn_rental(5,5)
        rentals=self.repoTest.get_all()
        self.assertEqual(rentals[2].get_returnedDate(),None)
        self.repoTest.remove_rental(17)
        self.assertFalse(self.repoTest.find_by_ID(17))
        self.assertEqual(len(self.repoTest.get_all()),2)
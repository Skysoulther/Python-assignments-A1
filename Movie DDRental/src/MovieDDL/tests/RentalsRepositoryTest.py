'''
Created on 26 Nov 2016

@author: DDL
'''
import unittest
import datetime
from MovieDDL.domain.ValidatorExceptions import StoreException
from MovieDDL.domain.Entities import Rental
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.domain.Validator import RentalValidator
from MovieDDL.repository.RepositoryRentals import rentalRepository

class RentalsRepositoryTest(unittest.TestCase):
    '''
    Unit test-case for testing RepositoryRentals module
    '''
    def setUp(self):
        '''
        the setup of data
        '''
        repoList={1:Rental(1,13,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016)),
              2:Rental(2,14,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=26,month=11,year=2016)),
              3:Rental(3,12,1,datetime.date(day=1,month=11,year=2016),datetime.date(day=8,month=11,year=2016))}
        rDate1=datetime.date(year=2016, month=10, day=30)
        dDate1=datetime.date(year=2016, month=11, day=7)
        dDate2=datetime.date(year=2015, month=10, day=10)
        self.rentalList1=[17,20,21,rDate1,dDate1]
        self.rentalList2=[2,22,23,rDate1,dDate2]
        validator1=RentalValidator()
        self.repoTest=rentalRepository(validator1,repoList)
        
    def testRepositoryRentals(self):
        '''
        Test the repository of rentals
        '''
        self.repoTest.add_rental(self.rentalList1)
        self.assertRaises(RepositoryException,self.repoTest.add_rental,self.rentalList1)
        self.assertRaises(StoreException,self.repoTest.add_rental,self.rentalList2)
        self.assertRaises(RepositoryException,self.repoTest.return_rental,4,5)
        self.assertEqual(len(self.repoTest.get_all()),4)
        self.repoTest.return_rental(5,13)
        self.assertEqual(len(self.repoTest.get_all()),4)
        self.assertTrue(self.repoTest.find_by_ID,2)
        self.assertFalse(self.repoTest.find_by_ID(6))
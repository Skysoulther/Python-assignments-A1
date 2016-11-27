'''
Created on 26 Nov 2016

@author: DDL
'''
import unittest
import datetime
from MovieDDL.domain.Validator import *
from MovieDDL.domain.Entities import  *

class ValidatorsTest(unittest.TestCase):
    '''
    Unit testcase fro testing Validators
    '''
    def setUp(self):
        '''
        The setup of the data
        '''
        self.movValidator=MovieValidator()
        self.movie1=Movie(1,"Good Title","Description1","horror")
        self.movie2=Movie(10000,"Bad Title sssssssssssssssssssssssssssssssssssssss", "Description2","bad genre")
        self.cliValidator=ClientValidator()
        self.client1=Client(1,"Good Client")
        self.client2=Client(10000,"Bad Client sssssssssssssssssssssssssssssssssssssss")
        self.rentValidator=RentalValidator()
        rDate1=datetime.date(year=2016, month=10, day=30)
        dDate1=datetime.date(year=2016, month=11, day=7)
        dDate2=datetime.date(year=2015, month=10, day=10)
        self.rental1=Rental(1,self.movie1.get_Id(),self.client1.get_clientID(),rDate1,dDate1)
        self.rental2=Rental(2,self.movie1.get_Id(),self.client1.get_clientID(),rDate1,dDate2)
            
    def testMovieValidator(self):
        '''
        Test the validator for movies
        '''
        self.assertTrue(self.movValidator.validateMovie,self.movie1)
        self.assertRaises(StoreException,self.movValidator.validateMovie,self.movie2)
        self.assertRaises(StoreException,self.movValidator.validateID,-2)
        self.assertTrue(self.movValidator.validateID,25)
    
    def testClientValidator(self):
        '''
        Test the validator for clients
        '''
        self.assertTrue(self.cliValidator.validateClient,self.client1)
        self.assertRaises(StoreException,self.cliValidator.validateClient,self.client2)
        self.assertRaises(StoreException,self.cliValidator.validateID,-4)
        self.assertTrue(self.cliValidator.validateID,35)
        
    def testRentalValidator(self):
        '''
        Test the validator for rentals
        '''
        self.assertTrue(self.rentValidator.validateRental,self.rental1)
        self.assertRaises(StoreException,self.rentValidator.validateRental,self.rental2)
        self.assertRaises(StoreException,self.rentValidator.validateID,-100)
        self.assertTrue(self.rentValidator.validateID,45)
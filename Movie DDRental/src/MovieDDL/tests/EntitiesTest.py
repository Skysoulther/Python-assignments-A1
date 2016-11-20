'''
Created on 21 Nov 2016

@author: DDL
'''
import unittest
from MovieDDL.domain.Entities import *

class EntitiesTest(unittest.TestCase):
    '''
    Unit TestCase for testing entities
    '''
    def setUp(self):
        self.movie=Movie(13,"A beautiful Mind","A movie about the life of John Nash","Biography")
        self.client=Client(47,"Sergiu Gherman")
        rDate=datetime.date(year=2016, month=10, day=30)
        dDate=datetime.date(year=2016, month=11, day=7)
        self.rental=Rental(1,self.movie.get_Id(),self.client.get_clientID(),rDate,dDate)
        
    def testMovieClass(self):
        '''
        Test the Movie class
        '''
        self.assertEqual(self.movie.get_Id(),13)
        self.assertEqual(self.movie.get_title(),"A beautiful Mind")
        self.assertEqual(self.movie.get_genre(),"Biography")
        self.assertEqual(self.movie.get_description(),"A movie about the life of John Nash")
        self.assertEqual(str(self.movie),"13    "+"A beautiful Mind"+" "*(52-len(self.movie.get_title()))+"Biography"+" "*6)
        self.movie.set_Id(18)
        self.assertEqual(self.movie.get_Id(),18)
        self.assertEqual(self.movie.get_title(),"A beautiful Mind")
        self.movie.set_title("The last day of summer")
        self.assertEqual(self.movie.get_title(),"The last day of summer")
        self.movie.set_description("A movie about summer")
        self.assertEqual(self.movie.get_description(),"A movie about summer")
        self.movie.set_genre("Comedy")
        self.assertEqual(self.movie.get_genre(),"Comedy")

    def testClientClass(self):
        '''
        Test the Client class
        '''
        self.assertEqual(self.client.get_clientID(),47)
        self.assertEqual(self.client.get_clientName(),"Sergiu Gherman")
        self.assertEqual(str(self.client),"47    "+"Sergiu Gherman"+" "*11)
        self.client.set_clientID(48)
        self.assertEqual(self.client.get_clientID(),48)
        self.client.set_clientName("Bobby")
        self.assertEqual(self.client.get_clientName(),"Bobby")

    def testRentalClass(self):
        '''
        Test the Rental class
        '''
        self.assertEqual(self.rental.get_rentalId(),1)
        self.assertEqual(self.rental.get_rmovieId(),13)
        self.assertEqual(self.rental.get_rclientId(),47)
        self.assertEqual(self.rental.get_rentDate(),datetime.date(year=2016,month=10,day=30))
        self.assertEqual(self.rental.get_dueDate().year,2016)
        self.assertEqual(self.rental.get_dueDate().month,11)
        self.assertEqual(self.rental.get_dueDate().day,7)
        self.assertEqual(str(self.rental),"1"+" "*6+"13"+" "*5+"47"+" "*5+str(self.rental.get_rentDate())+"  "+str(self.rental.get_dueDate())+"  "+"None")
        self.rental.set_rentalId(2)
        self.assertEqual(self.rental.get_rentalId(),2)
        self.rental.set_rmovieId(18)
        self.assertEqual(self.rental.get_rmovieId(),18)
        self.rental.set_rclientId(21)
        self.assertEqual(self.rental.get_rclientId(),21)
        self.rental.set_rentDate(15, 10, 2016)
        self.assertEqual(self.rental.get_rentDate(),datetime.date(year=2016,month=10,day=15))
        self.rental.set_dueDate(14, 11, 2016)
        self.assertEqual(self.rental.get_dueDate().day,14)
        self.rental.set_returnedDate(datetime.date(2016,5,7))
        self.assertEqual(self.rental.get_returnedDate(),datetime.date(2016,5,7))

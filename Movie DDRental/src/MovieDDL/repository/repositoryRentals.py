'''
Created on 6 Nov 2016

@author: DDL
'''
from MovieDDL.domain.Entities import Rental
import datetime

class rentalRepository:
    '''
    repository for the rented movies
    '''
    def __init__(self,Validator,rentals):
        '''
        Creates the repository of rented movies
        '''
        self.__rentals=rentals
        self.__validator=Validator
        
    def find_by_ID(self,Id):
        '''
        Checks if the Id is in the list of rentals
        Input: Id - a number
        Output: True if the Id exists, False otherwise
        Exceptions: -
        '''
        if Id in self.__rentals:
            return True
        else:
            return False
    
    def get_all(self):
        '''
        Gets the dictionary of rentals
        Output: self.__rentals - the dictionary of rentals
        '''
        return self.__rentals
        
    def add_rental(self,rental):
        '''
        Adds a rental in the repository
        Input: rental - an object of the class Rental
        Output: -
        Exceptions: RepositoryException if the ID of the rental is already used
        '''
        rental=Rental(rental[0],rental[1],rental[2],rental[3],rental[4])
        self.__validator.validateRental(rental)
        Id=int(rental.get_rentalId())
        if not self.find_by_ID(Id):
            self.__rentals[Id]=rental
        else:
            raise RepositoryException("A rental with the same ID already in the list"+"\n")
    
    def return_rental(self, Id):
        '''
        Removes a rented movie from the repository
        Input: Id - a number
        Output: -
        Exceptions: RepositoryException if there is no rental with that specific ID
        '''
        self._validator.validateID(Id)
        if self.find_by_ID(Id):
            self.__rentals[Id].set_returnedDate(datetime.date.today())
        else:
            raise RepositoryException("There is no rental with the ID: "+str(Id)+"\n")
        
#####################################################################################

class RepositoryException(Exception):
    '''
    Class for Repository Exceptions
    '''
    def __init__(self, message):
        '''
        Creates an error message
        '''
        self.__message=message
    
    def __str__(self):
        '''
        Returns a message as a string
        '''
        return self.__message
    
###############################################################################

def testRepositoryRentals():
    '''
    Test this repository
    '''
    from MovieDDL.domain.Validator import RentalValidator
    repoList={1:Rental(1,13,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=13,month=11,year=2016)),
              2:Rental(2,14,5,datetime.date(day=12,month=11,year=2016),datetime.date(day=26,month=11,year=2016)),
              3:Rental(3,12,1,datetime.date(day=1,month=11,year=2016),datetime.date(day=8,month=11,year=2016))}
    
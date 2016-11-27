'''
Created on 6 Nov 2016

@author: DDL
'''
from MovieDDL.domain.Entities import Rental
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.repository.FileRepositoryRentals import rentalFileRepository
import datetime

class rentalRepository(rentalFileRepository):
    '''
    repository for the rented movies
    '''
    def __init__(self,Validator,rentals,repoMovie):
        '''
        Creates the repository of rented movies
        '''
        rentalFileRepository.__init__(self,rentals)
        self.__rentals=self._loadFromFile()
        self.__validator=Validator
        self.__movieRepo=repoMovie
        self.__setAvailability()
    
    def __setAvailability(self):
        '''
        set the availability of the created movies
        '''
        for key in self.__rentals:
            movieId=self.__rentals[key].get_rmovieId()
            self.__movieRepo.change_availability(movieId,False)
    
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
            self._storeToFile(self.get_all())
        else:
            raise RepositoryException("A rental with the same ID already in the list"+"\n")
    
    def return_rental(self, clientId, movieId):
        '''
        Removes a rented movie from the repository
        Input: Id - a number
        Output: -
        Exceptions: RepositoryException if there is no rental with that specific ID
        '''
        for ID in self.__rentals:
            if self.__rentals[ID].get_rclientId()==clientId and self.__rentals[ID].get_rmovieId()==movieId:
                self.__rentals[ID].set_returnedDate(datetime.date.today())
                return self.__rentals[ID]
        raise RepositoryException("This client didn't rent this movie!\n")
        
#####################################################################################
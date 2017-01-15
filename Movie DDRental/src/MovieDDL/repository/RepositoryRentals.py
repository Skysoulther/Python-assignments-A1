'''
Created on 6 Nov 2016

@author: DDL
'''
from MovieDDL.repository.RepositoryExceptions import RepositoryException
from MovieDDL.repository.Iterator import iterableData
import datetime

class rentalRepository():
    '''
    repository for the rented movies
    '''
    def __init__(self,repoMovie):
        '''
        Creates the repository of rented movies
        '''
        self.__rentals=iterableData()
        self.__movieRepo=repoMovie
    
    def setAvailability(self):
        '''
        set the availability of the created movies
        '''
        for key in self.__rentals:
            if self.__rentals[key].get_returnedDate()==None:
                movieId=self.__rentals[key].get_rmovieId()
                self.__movieRepo.change_availability(movieId,False)
                
    def remove_rentals(self,Id):
        '''
        Remove all the rentals with the id of a client
        Input: Id - id of the client
        Output: -
        Exceptions: -
        '''
        removedRentals=[]
        for key in self.__rentals:
            clientId=self.__rentals[key].get_rclientId()
            if clientId==Id:
                removedRentals.append(self.__rentals[key])
        for i in range(len(removedRentals)):
            self.__rentals.pop(removedRentals[i].get_rentalId())
            self.__movieRepo.change_availability(removedRentals[i].get_rmovieId(),True)
        return removedRentals
    
    def add_rentals(self,rentals):
        '''
        Add some rentals in the repository
        Input: rentals - a list of rentals
        Output: -
        Exceptions: -
        '''
        for rental in rentals:
            Id=rental.get_rentalId()
            self.__rentals[Id]=rental
            self.__movieRepo.change_availability(rental.get_rmovieId(),False)
    
    def remove_rental(self,Id):
        '''
        Removes a rental from the repository
        Input: Id - the Id of the Rental
        Output: -
        Exceptions: RepositoryException if the ID of the rental is already used
        '''
        if self.find_by_ID(Id):
            return self.__rentals.pop(Id)
        else:
            raise RepositoryException("There is no rental with the ID: "+str(Id)+" \n")
    
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
        Id=int(rental.get_rentalId())
        if not self.find_by_ID(Id):
            self.__rentals[Id]=rental
        else:
            raise RepositoryException("A rental with the same ID already in the list"+"\n")
    
    def return_rental(self, clientId, movieId):
        '''
        Returns a rented movie from the repository
        Input: clientId - The ID of the client
               movieId - The ID of the movie
        Output: -
        Exceptions: RepositoryException if there is no rental with that specific ID
        '''
        for ID in self.__rentals:
            if self.__rentals[ID].get_rclientId()==clientId and self.__rentals[ID].get_rmovieId()==movieId:
                self.__rentals[ID].set_returnedDate(datetime.date.today())
                return self.__rentals[ID]
        raise RepositoryException("This client didn't rent this movie!\n")
    
    def unreturn_rental(self,clientId, movieId):
        '''
        Set return date to None
        Input: clientId - The ID of the client
               movieId - The ID of the movie
        Output: -
        Exceptions: RepositoryException if there is no rental with that specific ID
        '''
        for ID in self.__rentals:
            if self.__rentals[ID].get_rclientId()==clientId and self.__rentals[ID].get_rmovieId()==movieId:
                self.__rentals[ID].set_returnedDate(None)
                return self.__rentals[ID]
        raise RepositoryException("This client didn't rent this movie!\n")
        
#####################################################################################
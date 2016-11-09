'''
Created on 6 Nov 2016

@author: DDL
'''
class rentalRepository:
    '''
    repository for the rented movies
    '''
    def __init__(self,Validator,rented):
        '''
        Creates the repository of rented movies
        '''
        self._rentedMovies=rented
        self._validator=Validator
        
    def find_by_ID(self,Id):
        '''
        Checks if the Id is in the list of rented movies
        Input: Id - a number
        Output: True if the Id exists, False otherwise
        Exceptions: -
        '''
        if Id in self._rentedMovies:
            return True
        else:
            return False
        
    def add_rentedMovie(self,rental):
        '''
        Adds a rented movie in the repository
        Input: rmovie - an object of the class Rental
        Output: -
        Exceptions: -
        '''
        self._validator.validateRental(rental)
        Id=int(rental.get_rentalId())
        if not self.find_by_ID(Id):
            self._rentedMovies[Id]=rental
        else:
            raise ValueError("A rental with the same ID already in the list"+"\n")
    
    def remove_movie(self, Id):
        '''
        Removes a rented movie from the repository
        Input: Id - a number
        Output: -
        Exceptions: -
        '''
        self._validator.validateID(Id)
        Id=int(Id)
        if self.find_by_ID(Id):
            self._rentedMovies.pop(Id)
        else:
            raise ValueError("There is no movie with the ID: "+str(Id)+"\n")
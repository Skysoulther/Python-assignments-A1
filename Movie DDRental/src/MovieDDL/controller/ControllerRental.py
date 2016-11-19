'''
Created on 6 Nov 2016

@author: DDL
'''
from MovieDDL.controller.ControllerExceptions import ControllerException
class rentalController:
    '''
    Contains functions which operates on rentals
    '''
    def __init__(self,repoMovie,repoClient,repoRental):
        '''
        Creates a controller for rentals
        '''
        self._repositoryRental=repoRental
        self._repositoryMovie=repoMovie
        self._repositoryClient=repoClient
    
    def _validateID(self,Id):
        '''
        Validates ID
        Exceptions: Controller Exception when ID is not a number
        '''
        try:
            Id=int(Id)
        except ValueError:
            raise ControllerException("The ID should be a number!\n")
    
    def get_all(self):
        '''
        Returns the list of rentals
        '''
        return self._repositoryRental.get_all()
    
    def checks_movie(self,Id):
        '''
        Checks if a movie is in the list of availableMovies or not
        Input: Id - a number
        Output: -
        Exceptions: ControllerException from invalid Id or if the movie is not available
        '''
        self._validateID(Id)
        Id=int(Id)
        available=self._repositoryMovie.get_available()
        if not Id in available:
            raise ControllerException("The movie is not in the available list!\n")
        return
    
    def checks_client(self,Id):
        '''
        Checks if the client exists or not
        Input: Id - a number
        Output: -
        Exceptions: ControllerException from invalid Id or if the client can't be found
        '''
        self._validateID(Id)
        Id=int(Id)
        available=self._repositoryClient.get_all()
        if not Id in available:
            raise ControllerException("There is not client with that ID!\n")
        return
    
    def rent_movie(self,rental):
        '''
        Add a rental in the list of rentals
        Input: rental -  a list which contains the values of the fields of a rental
        Output: -
        Exceptions: Controller Exception when the Id of the rental is not valid
        '''
        self._repositoryRental.add_rental(rental)
        self._repositoryMovie.change_availability(rental[1],False)
        
####################################################################################
#################################################################################